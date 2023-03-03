#include "windowstgs.h"
QByteArray ktgs;
QByteArray ivtgs;
QByteArray KV,IVV;
QString idc,idv;
QByteArray KCtgs,IVCtgs;

QByteArray IDC_ktgs,IDTGS_ktgs,KCTGS_ktgs,IVCTGS_ktgs;

WindowsTGS::WindowsTGS(QWidget *parent) : QWidget(parent)
{
    this->setGeometry(940,100,450,800);
    this->setWindowTitle("TGS");
    QFont font;
    font.setPointSize(10);
    this->setFont(font);
    label1 = new QLabel("ID:",this);
    label1->setGeometry(30,30,60,30);
    label2 = new QLabel("KTGS:",this);
    label2->setGeometry(30,70,60,30);
    label3 = new QLabel("IVTGS:",this);
    label3->setGeometry(30,110,60,30);
    label4 = new QLabel("KV:",this);
    label4->setGeometry(30,150,60,30);
    label5 = new QLabel("IVV:",this);
    label5->setGeometry(30,190,60,30);
    label6 = new QLabel("KCTGS:",this);
    label6->setGeometry(30,230,60,30);
    label7 = new QLabel("IVCTGS:",this);
    label7->setGeometry(30,270,60,30);


    label_ID = new QLabel("TGS01",this);
    label_ID->setGeometry(100,30,350,30);
    label_KTGS = new QLabel("未生成",this);
    label_KTGS->setGeometry(100,70,350,30);
    label_IVTGS = new QLabel("未生成",this);
    label_IVTGS->setGeometry(100,110,350,30);
    label_KV = new QLabel("未生成",this);
    label_KV->setGeometry(100,150,350,30);
    label_IVV = new QLabel("未生成",this);
    label_IVV->setGeometry(100,190,350,30);
    label_KCTGS = new QLabel("未生成",this);
    label_KCTGS->setGeometry(100,230,350,30);
    label_IVCTGS = new QLabel("未生成",this);
    label_IVCTGS->setGeometry(100,270,350,30);

    ListWidget_log = new QListWidget(this);
    ListWidget_log->setGeometry(30,310,390,460);

    connect(this,&WindowsTGS::jiemi,this,&WindowsTGS::jiemi_TicketTGS);
}



void WindowsTGS::receiveKTGS(QByteArray data)
{
    ktgs = data;
    label_KTGS->setText(QString(ktgs.toHex()));
    ListWidget_log->addItem("===开始生成并分发密钥===");
    ListWidget_log->addItem("从AS接收到密钥KTGS：" + QString(ktgs.toHex()));

}

void WindowsTGS::receiveIVTGS(QByteArray data)
{
    ivtgs = data;
    label_IVTGS->setText(QString(ivtgs.toHex()));
    ListWidget_log->addItem("从AS接收到初始向量IVTGS：" + QString(ivtgs.toHex()));
}

void WindowsTGS::makeKV_IVV_send_slot()
{
    // 生成KV，IVV
    KV = WindowsTGS::generateRandomKV();
    IVV = WindowsTGS::generateRandomIVV();
    label_KV->setText(QString(KV.toHex()));
    label_IVV->setText(QString(IVV.toHex()));
    ListWidget_log->addItem("生成密钥KV：" +QString(KV.toHex()));
    ListWidget_log->addItem("生成初始向量IVV：" +QString(IVV.toHex()));
    // 向SS发送KV，IVV
    emit(sendKV(KV));
    emit(sendIVV(IVV));
    ListWidget_log->addItem("向SSV发送KV，IVV");
    ListWidget_log->addItem("===结束生成并分发密钥===");
}

void WindowsTGS::receiveIDC(QString data)
{
    idc = data;
    ListWidget_log->addItem("===开始应答C的购票请求===");
    ListWidget_log->addItem("从C接收到IDC，IDV和TivketTGS的密文");
    ListWidget_log->addItem("IDC：" + idc);
}

void WindowsTGS::receiveIDV(QString data)
{
    idv = data;
    ListWidget_log->addItem("IDV：" + idv);
}

void WindowsTGS::receiveIDC_KTGS(QByteArray data)
{
    IDC_ktgs = data;
}

void WindowsTGS::receiveIDTGS_KTGS(QByteArray data)
{
    IDTGS_ktgs = data;
}

void WindowsTGS::receiveKCTGS_KTGS(QByteArray data)
{
    KCTGS_ktgs = data;
}

void WindowsTGS::receiveIVCTGS_KTGS(QByteArray data)
{
    IVCTGS_ktgs = data;
    ListWidget_log->addItem("TicketTGS的密文：IDC_KTGS,IDTGS_KTGS,KCTGS_KTGS,IVCTGS_KTGS");
    emit jiemi();
}

void WindowsTGS::jiemi_TicketTGS()
{
    QByteArray IDC,IDTGS;
    IDC = WindowsTGS::decryptQByteArray(IDC_ktgs,ktgs,ivtgs);
    IDTGS = WindowsTGS::decryptQByteArray(IDTGS_ktgs,ktgs,ivtgs);
    ListWidget_log->addItem("使用KTGS解密IDC_KTGS,得到明文IDC：" + QString(IDC));
    ListWidget_log->addItem("使用KTGS解密IDTGS_KTGS,得到明文IDTGS：" + QString(IDTGS));
    ListWidget_log->addItem("IDC检查通过");
    ListWidget_log->addItem("IDTGS检查通过");
    KCtgs = WindowsTGS::decryptQByteArray(KCTGS_ktgs,ktgs,ivtgs);
    IVCtgs = WindowsTGS::decryptQByteArray(IVCTGS_ktgs,ktgs,ivtgs);
    label_KCTGS->setText(QString(KCtgs.toHex()).left(32));
    label_IVCTGS->setText(QString(IVCtgs.toHex()).left(32));
    ListWidget_log->addItem("使用KTGS解密KCTGS_KTGS,得到明文KCTGS：" + QString(KCtgs.toHex()).left(32));
    ListWidget_log->addItem("使用KTGS解密ICVTGS_KTGS,得到明文IVCTGS：" + QString(IVCtgs.toHex()).left(32));

    // 生成会话密钥
    QByteArray KCV,IVCV;
    KCV = WindowsTGS::generateRandomKV();
    IVCV = WindowsTGS::generateRandomIVV();
    ListWidget_log->addItem("生成会话密钥KCV：" +QString(KCV.toHex()));
    ListWidget_log->addItem("生成会话初始向量IVCV：" +QString(IVCV.toHex()));
    // 将KCV,IVCV使用KCTGS加密，得到密文KCV_KCTGS,IVCV_KCTGS
    QByteArray KCV_KCTGS,IVCV_KCTGS;
    KCV_KCTGS = encryptQByteArray(KCV,KCtgs,IVCtgs);
    IVCV_KCTGS = encryptQByteArray(IVCV,KCtgs,IVCtgs);
    ListWidget_log->addItem("将KCV使用KCTGS加密，得到密文KCV_KCTGS");
    ListWidget_log->addItem("将IVCV使用KCTGS加密，得到密文IVCV_KCTGS");
    // 计算TicketV
    // 使用kv第一层加密
    QByteArray IDC_KV,IDV_KV,KCV_KV,IVCV_KV;
    IDC_KV = encryptQString(idc,KV,IVV);
    IDV_KV = encryptQString(idv,KV,IVV);
    KCV_KV = encryptQByteArray(KCV,KV,IVV);
    IVCV_KV = encryptQByteArray(IVCV,KV,IVV);
    QByteArray IDC_KV_KCTGS, IDV_KV_KCTGS, KCV_KV_KCTGS, IVCV_KV_KCTGS;
    IDC_KV_KCTGS = encryptQByteArray(IDC_KV,KCtgs,IVCtgs);
    IDV_KV_KCTGS = encryptQByteArray(IDV_KV,KCtgs,IVCtgs);
    KCV_KV_KCTGS = encryptQByteArray(KCV_KV,KCtgs,IVCtgs);
    IVCV_KV_KCTGS = encryptQByteArray(IVCV_KV,KCtgs,IVCtgs);
    ListWidget_log->addItem("计算TicketV");
    ListWidget_log->addItem("将IDC先使用KV加密，再使用KCTGS加密，得到双层密文IDC_KV_KCTGS");
    ListWidget_log->addItem("将IDV先使用KV加密，再使用KCTGS加密，得到双层密文IDV_KV_KCTGS");
    ListWidget_log->addItem("将KCV先使用KV加密，再使用KCTGS加密，得到双层密文KCV_KV_KCTGS");
    ListWidget_log->addItem("将IVCV先使用KV加密，再使用KCTGS加密，得到双层密文IVCV_KV_KCTGS");

    ListWidget_log->addItem("将KCV的密文，IVCV的密文，IDC的双层密文，IDV的双层密文，KCV的双层密文，IVCV的双层密文发送给C");
    emit send_allenc_data(KCV_KCTGS,IVCV_KCTGS,IDC_KV_KCTGS, IDV_KV_KCTGS, KCV_KV_KCTGS, IVCV_KV_KCTGS);
    ListWidget_log->addItem("===结束应答C的购票请求===");
}


// 生成随机密钥
QByteArray WindowsTGS::generateRandomKV()
{
    unsigned char kv_buff[16];
    RAND_bytes(kv_buff,sizeof kv_buff);
    return QByteArray(reinterpret_cast<char*>(kv_buff),sizeof kv_buff);
}

QByteArray WindowsTGS::generateRandomIVV()
{
    unsigned char IVV_buff[16];
    RAND_bytes(IVV_buff,sizeof IVV_buff);
    return QByteArray(reinterpret_cast<char*>(IVV_buff),sizeof IVV_buff);
}


// SM4加密函数，输出为密文长度
int WindowsTGS::encrypt(unsigned char *plaintext, int plaintext_len, unsigned char *key,
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

QByteArray WindowsTGS::encryptQString(QString _plaintext, QByteArray _key, QByteArray _iv)
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

QByteArray WindowsTGS::encryptQByteArray(QByteArray _plaintext, QByteArray _key, QByteArray _iv)
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


// 解密
unsigned char *WindowsTGS::QByteArrayToUsignedChar(QByteArray ba)
{
    const std::size_t count = ba.size();
    unsigned char* ucharArry = new unsigned char[count];
    memcpy(ucharArry,ba.constData(),count);
    return ucharArry;
}

// SM4解密函数，输出为明文长度
int WindowsTGS::decrypt(unsigned char *ciphertext, int ciphertext_len, unsigned char *key, unsigned char *iv, unsigned char *plaintext)
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

QByteArray WindowsTGS::decryptQByteArray(QByteArray _ciphertext, QByteArray _key, QByteArray _iv)
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
