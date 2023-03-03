#include "windowsas.h"
#include <QFont>
#include "windowsc.h"

// 全局变量
QByteArray KC;
QByteArray IVC;
QByteArray KTGS;
QByteArray IVTGS;

QByteArray KCTGS,IVCTGS;

QString IDC;
QString IDTGS;
WindowsAS::WindowsAS(QWidget *parent) : QWidget(parent)
{
    this->setGeometry(20,100,450,800);
    this->setWindowTitle("AS");
    QFont font;
    font.setPointSize(10);
    this->setFont(font);
    label1 = new QLabel("ID:",this);
    label1->setGeometry(30,30,60,30);
    label2 = new QLabel("KC:",this);
    label2->setGeometry(30,70,60,30);
    label3 = new QLabel("IVC:",this);
    label3->setGeometry(30,110,60,30);
    label4 = new QLabel("KTGS:",this);
    label4->setGeometry(30,150,60,30);
    label5 = new QLabel("IVTGS",this);
    label5->setGeometry(30,190,60,30);


    label_ID = new QLabel("AS",this);
    label_ID->setGeometry(100,30,350,30);
    label_KC = new QLabel("未生成",this);
    label_KC->setGeometry(100,70,350,30);
    label_IVC = new QLabel("未生成",this);
    label_IVC->setGeometry(100,110,350,30);
    label_KTGS = new QLabel("未生成",this);
    label_KTGS->setGeometry(100,150,350,30);
    label_IVTGS = new QLabel("未生成",this);
    label_IVTGS->setGeometry(100,190,350,30);

    button = new QPushButton("生成并分发密钥",this);
    button->setGeometry(30,220,390,40);
    connect(button,&QPushButton::clicked,this,&WindowsAS::button_click);

    // 发送KC和IVC(AS子窗口向主窗口C)
    connect(button,&QPushButton::clicked,this,&WindowsAS::sendKC_slot);
    connect(button,&QPushButton::clicked,this,&WindowsAS::sendIVC_slot);
    // 向TGS发送KTGS和IVTGS（经由C转发）
    connect(button,&QPushButton::clicked,this,&WindowsAS::sendKTGSandIVTGS_slot);

    // 开始AS加密
    connect(this,&WindowsAS::receiveIDC_IDTGS,this,&WindowsAS::ASencrytedIDC_IDTGS);



    ListWidget_log = new QListWidget(this);

    ListWidget_log->setGeometry(30,270,390,500);
}

WindowsAS::~WindowsAS()
{
}

void WindowsAS::button_click()
{
    KC =  WindowsAS::generateRandomKey();
    IVC =  WindowsAS::generateRandomIV();
    KTGS =  WindowsAS::generateRandomKTGS();
    IVTGS =  WindowsAS::generateRandomIVTGS();
    label_KC->setText(QString(KC.toHex()));
    label_IVC->setText(QString(IVC.toHex()));
    label_KTGS->setText(QString(KTGS.toHex()));
    label_IVTGS->setText(QString(IVTGS.toHex()));
    ListWidget_log->addItem("===开始生成并分发密钥===");
    ListWidget_log->addItem("生成密钥KC：" + QString(KC.toHex()));
    ListWidget_log->addItem("生成初始向量IVC：" + QString(IVC.toHex()));
    ListWidget_log->addItem("生成密钥KTGS：" + QString(KTGS.toHex()));
    ListWidget_log->addItem("生成初始向量IVTGS：" + QString(IVTGS.toHex()));
    ListWidget_log->addItem("向C发送KC、IV");
    ListWidget_log->addItem("向TGS发送KTGS，IVTGS");
    ListWidget_log->addItem("===结束生成并分发密钥===");
}
// 生成随机密钥
QByteArray WindowsAS::generateRandomKey()
{
    unsigned char key_buff[16];
    RAND_bytes(key_buff,sizeof key_buff);
    return QByteArray(reinterpret_cast<char*>(key_buff),sizeof key_buff);
}

QByteArray WindowsAS::generateRandomIV()
{
    unsigned char iv_buff[16];
    RAND_bytes(iv_buff,sizeof iv_buff);
    return QByteArray(reinterpret_cast<char*>(iv_buff),sizeof iv_buff);
}

QByteArray WindowsAS::generateRandomKTGS()
{
    unsigned char KGTS_buff[16];
    RAND_bytes(KGTS_buff,sizeof KGTS_buff);
    return QByteArray(reinterpret_cast<char*>(KGTS_buff),sizeof KGTS_buff);
}

QByteArray WindowsAS::generateRandomIVTGS()
{
    unsigned char IVTGS_buff[16];
    RAND_bytes(IVTGS_buff,sizeof IVTGS_buff);
    return QByteArray(reinterpret_cast<char*>(IVTGS_buff),sizeof IVTGS_buff);
}
//  接收到IDC和IDTGS后的一系列操作
void WindowsAS::ASencrytedIDC_IDTGS()
{
    // 生成会话密钥的Kctgs和对应的初始向量IVctgs
    KCTGS = WindowsAS::generateRandomKTGS();
    IVCTGS = WindowsAS::generateRandomIVTGS();
    ListWidget_log->addItem("生成会话密钥KCTGS："+ QString(KCTGS.toHex()));
    ListWidget_log->addItem("生成会话初始向量IVCTGS："+ QString(IVCTGS.toHex()));
    // 将KCTGS和IVCTGS使用KC加密
    QByteArray KCTGS_KC,IVCTGS_KC;
    KCTGS_KC = encryptQByteArray(KCTGS,KC,IVC);
    IVCTGS_KC = encryptQByteArray(IVCTGS,KC,IVC);
    ListWidget_log->addItem("将KCTGS使用KC加密,得到密文KCTGS_KC");
    ListWidget_log->addItem("将IVCTGS使用KC加密,得到密文IVCTGS_KC");

//    DC、IDTGS、KCTGS和IVCTGS进行双重加密，第一重使用KTGS作为密钥，第二重使用KC作为密钥。
//    IDC的双重加密密文为IDC_KTGS_KC。
//    IDTGS的双重加密密文为IDTGS_KTGS_KC。
//    KCTGS的双重加密密文为KCTGS_KTGS_KC。
//    IVCTGS的双重加密密文为IVCTGS_KTGS_KC。
    // 第一重使用KTGS作为密钥
    QByteArray IDC_KTGS,IDTGS_KTGS,KCTGS_KTGS,IVCTGS_KTGS;
    IDC_KTGS = encryptQString(IDC,KTGS,IVTGS);
    IDTGS_KTGS = encryptQString(IDTGS,KTGS,IVTGS);
    KCTGS_KTGS = encryptQByteArray(KCTGS,KTGS,IVTGS);
    IVCTGS_KTGS = encryptQByteArray(IVCTGS,KTGS,IVTGS);
    // 第二重使用KC作为密钥
    QByteArray IDC_KTGS_KC,IDTGS_KTGS_KC,KCTGS_KTGS_KC,IVCTGS_KTGS_KC;
    IDC_KTGS_KC = encryptQByteArray(IDC_KTGS,KC,IVC);
    IDTGS_KTGS_KC = encryptQByteArray(IDTGS_KTGS,KC,IVC);
    KCTGS_KTGS_KC = encryptQByteArray(KCTGS_KTGS,KC,IVC);
    IVCTGS_KTGS_KC = encryptQByteArray(IVCTGS_KTGS,KC,IVC);

    ListWidget_log->addItem("计算TicketTGS");
    ListWidget_log->addItem("将IDC首先使用KTGS加密，在使用KC加密，得到双层密文IDC_KTGS_KC");
    ListWidget_log->addItem("将IDTGS首先使用KTGS加密，在使用KC加密，得到双层密文IDTGS_KTGS_KC");
    ListWidget_log->addItem("将KCTGS首先使用KTGS加密，在使用KC加密，得到双层密文KCTGS_KTGS_KC ");
    ListWidget_log->addItem("将IVCTGS首先使用KTGS加密，在使用KC加密，得到双层密文IVCTGS_KTGS_KC");
    // 发送密文
    emit sendencryKCTGS_KC(KCTGS_KC);
    emit sendencryIVCTGS_KC(IVCTGS_KC);
    emit sendencryIDC_KTGS_KC(IDC_KTGS_KC);
    emit sendencryIDTGS_KTGS_KC(IDTGS_KTGS_KC);
    emit sendencryKCTGS_KTGS_KC(KCTGS_KTGS_KC);
    emit sendencryIVCTGS_KTGS_KC(IVCTGS_KTGS_KC);
    ListWidget_log->addItem("将KCTGS的密文，IVTGS的密文，IDC的双重密文，"
                            "IDTGS的双重密文，KCTGS的双重密文，IVCTGS的双重密文"
                            "发送到C");
}

void WindowsAS::sendKC_slot()
{
    emit(sendKC(KC));
}

void WindowsAS::sendIVC_slot()
{
    emit(sendIVC(IVC));
}

void WindowsAS::sendKTGSandIVTGS_slot()
{
    emit(sendKTGS(KTGS));
    emit(sendIVTGS(IVTGS));
}


void WindowsAS::receive_IDC(QString data)
{
    IDC = data;
    ListWidget_log->addItem("===开始应答C的购票请求===");
    ListWidget_log->addItem("从C接收到IDC和IDTGS");
    ListWidget_log->addItem("IDC：" + data);
}

void WindowsAS::receive_IDTGS(QString data)
{
    IDTGS = data;
    ListWidget_log->addItem("IDTGS：" + data);
    if(IDC != NULL and IDTGS != NULL)
    {
        // 接收到IDC和IDTGS
        emit receiveIDC_IDTGS();
    }
}



// SM4加密函数，输出为密文长度
int WindowsAS::encrypt(unsigned char *plaintext, int plaintext_len, unsigned char *key,
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

QByteArray WindowsAS::encryptQString(QString _plaintext, QByteArray _key, QByteArray _iv)
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

QByteArray WindowsAS::encryptQByteArray(QByteArray _plaintext, QByteArray _key, QByteArray _iv)
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

unsigned char *WindowsAS::QByteArrayToUsignedChar(QByteArray ba)
{
    const std::size_t count = ba.size();
    unsigned char* ucharArry = new unsigned char[count];
    memcpy(ucharArry,ba.constData(),count);
    return ucharArry;
}

// SM4解密函数，输出为明文长度
int WindowsAS::decrypt(unsigned char *ciphertext, int ciphertext_len, unsigned char *key, unsigned char *iv, unsigned char *plaintext)
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

QByteArray WindowsAS::decryptQByteArray(QByteArray _ciphertext, QByteArray _key, QByteArray _iv)
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




