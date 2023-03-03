#include "windowss.h"
#include <QDebug>
QByteArray kv,ivv;

WindowSS::WindowSS(QWidget *parent) : QWidget(parent)
{
    this->setGeometry(1400,100,450,800);
    this->setWindowTitle("SS");
    QFont font;
    font.setPointSize(10);
    this->setFont(font);
    label1 = new QLabel("ID:",this);
    label1->setGeometry(30,30,60,30);
    label2 = new QLabel("KV:",this);
    label2->setGeometry(30,70,60,30);
    label3 = new QLabel("IVV:",this);
    label3->setGeometry(30,110,60,30);
    label4 = new QLabel("KCV:",this);
    label4->setGeometry(30,150,60,30);
    label5 = new QLabel("IVCV",this);
    label5->setGeometry(30,190,60,30);


    label_ID = new QLabel("SSV",this);
    label_ID->setGeometry(100,30,350,30);
    label_KV = new QLabel("未生成",this);
    label_KV->setGeometry(100,70,350,30);
    label_IVV = new QLabel("未生成",this);
    label_IVV->setGeometry(100,110,350,30);
    label_KCV = new QLabel("未生成",this);
    label_KCV->setGeometry(100,150,350,30);
    label_IVCV = new QLabel("未生成",this);
    label_IVCV->setGeometry(100,190,350,30);
    ListWidget_log = new QListWidget(this);
    ListWidget_log->setGeometry(30,230,390,540);

}
// 接收TGS发送的KV和IVV
void WindowSS::receiveKV_slots(QByteArray data)
{
    kv = data;
    label_KV->setText(QString(kv.toHex()));
    ListWidget_log->addItem("===开始并分发密钥===");
    ListWidget_log->addItem("从TGS接收到密钥KV："+ QString(kv.toHex()));
}

void WindowSS::receiveIVV_slots(QByteArray data)
{
    ivv = data;
    label_IVV->setText(QString(ivv.toHex()));
    ListWidget_log->addItem("从TGS接收到初始向量IVV："+ QString(ivv.toHex()));
    ListWidget_log->addItem("===结束生成并分发密钥===");
}

void WindowSS::receive_signal_fromC_slots(QByteArray data1, QByteArray data2, QByteArray data3,
                                          QByteArray data4, QByteArray data5, QByteArray data6)
{
    ListWidget_log->addItem("===开始应答C的服务请求===");
    ListWidget_log->addItem("从C接收IDC的密文，时间戳TS的密文和TicketV的密文");
    QByteArray IDC_KCV,TS_KCV,IDC_KV, IDV_KV, KCV_KV, IVCV_KV;
    IDC_KCV = data1;
    TS_KCV = data2;
    IDC_KV = data3;
    IDV_KV = data4;
    KCV_KV = data5;
    IVCV_KV = data6;
    ListWidget_log->addItem("IDC的密文IDC_KCV");
    ListWidget_log->addItem("TS的密文TS_KCV");
    ListWidget_log->addItem("TicketV的密文IDC_KV, IDV_KV, KCV_KV, IVCV_KV");

    QByteArray IDC1,TS,IDC2, IDV, KCV, IVCV;
    KCV = WindowSS::decryptQByteArray(KCV_KV,kv,ivv);
    IVCV = WindowSS::decryptQByteArray(IVCV_KV,kv,ivv);
    IDC2 = WindowSS::decryptQByteArray(IDC_KV,kv,ivv);
    IDV = WindowSS::decryptQByteArray(IDV_KV,kv,ivv);
    IDC1 = WindowSS::decryptQByteArray(IDC_KCV,KCV,IVCV);
    TS = WindowSS::decryptQByteArray(TS_KCV,KCV,IVCV);

    label_KCV->setText(QString(KCV.toHex()).left(32));
    label_IVCV->setText(QString(IVCV.toHex()).left(32));
    ListWidget_log->addItem("使用KV解密KCV_KV，得到KCV：" + QString(KCV.toHex()).left(32));
    ListWidget_log->addItem("使用KV解密IVCV_KV，得到IVCV：" + QString(IVCV.toHex()).left(32));
    ListWidget_log->addItem("使用KCV解密IDC_KCV，得到IDC：" + QString(IDC1));
    ListWidget_log->addItem("使用KV解密IDC_KV，得到IDC：" + QString(IDC2));
    ListWidget_log->addItem("使用KV解密IDV_KV，得到IDV：" +  QString(IDV));
    ListWidget_log->addItem("IDC检查通过");
    ListWidget_log->addItem("IDV检查通过");
    ListWidget_log->addItem("使用KCV解密TS_KCV，得到TS：" +  QString(TS));
    ListWidget_log->addItem("计算TS+1，并将TS+1使用KCV加密，得到密文TS+1_KCV");
    ListWidget_log->addItem("将TS+1_KCV发送给C");
    // 计算TS+1
    int ts = QString(TS).toInt();
    ts = ts + 1;
    QByteArray Ts;
    Ts = encryptQString(QString::number(ts),KCV,IVCV);
    emit sendTS(Ts);
    ListWidget_log->addItem("===结束应答C的服务请求===");
}



// SM4加密函数，输出为密文长度
int WindowSS::encrypt(unsigned char *plaintext, int plaintext_len, unsigned char *key,
    unsigned char *iv, unsigned char *ciphertext)
{
    // 初始化
    EVP_CIPHER_CTX *ctx;
    ctx = EVP_CIPHER_CTX_new();
    int len;
    int ciphertext_len;
    // SM4 EVP 加密接口
    EVP_EncryptInit_ex(ctx, EVP_sms4_cbc(), NULL, key, iv);
    EVP_EncryptUpdate(ctx, ciphertext, &len, plaintext, plaintext_len);
    ciphertext_len = len;
    EVP_EncryptFinal_ex(ctx, ciphertext + len, &len);
    ciphertext_len += len;
    // 清理
    EVP_CIPHER_CTX_free(ctx);
    // 返回密文长度
    return ciphertext_len;
}

QByteArray WindowSS::encryptQString(QString _plaintext, QByteArray _key, QByteArray _iv)
{
    unsigned char *plaintext = (unsigned char *) _plaintext.toLatin1().data();
    unsigned char ciphertext[128];

    unsigned char *key = QByteArrayToUsignedChar(_key);
    unsigned char *iv = QByteArrayToUsignedChar(_iv);
    // 定义密文和明文长度变量
    int ciphertext_len;
    // 调用加密算法
    ciphertext_len = encrypt(plaintext,strlen((char *)plaintext),key,iv,ciphertext);
    return  QByteArray(reinterpret_cast<char*>(ciphertext),ciphertext_len);

}

QByteArray WindowSS::encryptQByteArray(QByteArray _plaintext, QByteArray _key, QByteArray _iv)
{
    unsigned char *plaintext =  QByteArrayToUsignedChar(_plaintext);
    unsigned char ciphertext[128];
    unsigned char *key = QByteArrayToUsignedChar(_key);
    unsigned char *iv = QByteArrayToUsignedChar(_iv);
    // 定义密文和明文长度变量
    int ciphertext_len;
    // 调用加密算法
    ciphertext_len = encrypt(plaintext,strlen((char *)plaintext),key,iv,ciphertext);
    return  QByteArray(reinterpret_cast<char*>(ciphertext),ciphertext_len);
}

unsigned char *WindowSS::QByteArrayToUsignedChar(QByteArray ba)
{
    const std::size_t count = ba.size();
    unsigned char* ucharArry = new unsigned char[count];
    memcpy(ucharArry,ba.constData(),count);
    return ucharArry;
}

// SM4解密函数，输出为明文长度
int WindowSS::decrypt(unsigned char *ciphertext, int ciphertext_len, unsigned char *key, unsigned char *iv, unsigned char *plaintext)
{
    // 初始化
    EVP_CIPHER_CTX *ctx;
    ctx = EVP_CIPHER_CTX_new();
    int len;
    int plaintext_len;

    // SM4 EVP 解密接口
    EVP_DecryptInit_ex(ctx, EVP_sms4_cbc(), NULL, key, iv);
    EVP_DecryptUpdate(ctx, plaintext, &len, ciphertext, ciphertext_len);
    plaintext_len = len;
    EVP_DecryptFinal_ex(ctx, plaintext + len, &len);
    plaintext_len += len;

    // 清理
    EVP_CIPHER_CTX_free(ctx);
    // 返回明文长度
    return plaintext_len;
}

QByteArray WindowSS::decryptQByteArray(QByteArray _ciphertext, QByteArray _key, QByteArray _iv)
{
    unsigned char *ciphertext;
    unsigned char decryptedtext[128];

    unsigned char *key = QByteArrayToUsignedChar(_key);
    unsigned char *iv = QByteArrayToUsignedChar(_iv);
    ciphertext = QByteArrayToUsignedChar(_ciphertext);
    // 定义密文和明文长度变量
    int decrytedtext_len;
    // 调用加密算法
    decrytedtext_len = decrypt(ciphertext,_ciphertext.size(),key,iv,decryptedtext);
    decryptedtext[decrytedtext_len] = '\0';
    return QByteArray(reinterpret_cast<char*>(decryptedtext),decrytedtext_len);
}

