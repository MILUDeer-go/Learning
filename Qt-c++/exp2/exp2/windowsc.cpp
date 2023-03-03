#include "windowsc.h"
#include <QFont>
#include <windowsas.h>
#include <windowss.h>
#include <windowstgs.h>
#include <QDateTime>
#include <QDebug>

QByteArray kc,ivc;

QByteArray kctgs,ivctgs;
QByteArray KCTGS_kc,IVCTGS_kc;
QByteArray IDC_KTGS_kc,IDTGS_KTGS_kc,KCTGS_KTGS_kc,IVCTGS_KTGS_kc;

QByteArray IDC_KTGS,IDTGS_KTGS,KCTGS_KTGS,IVCTGS_KTGS;

QByteArray IDC_KV, IDV_KV, KCV_KV, IVCV_KV;
QByteArray KCV,IVCV;
WindowsC::WindowsC(QWidget *parent) : QWidget(parent)
{
    // 创建AS角色
    WindowsAS * AS = new WindowsAS;
    // 创建TGS
    WindowsTGS *TGS = new WindowsTGS;
    WindowSS *SS = new WindowSS;

    this->setGeometry(480,100,460,800);
    this->setWindowTitle("Client");
    QFont font;
    font.setPointSize(10);
    this->setFont(font);
    label1 = new QLabel("ID:",this);
    label1->setGeometry(30,30,60,30);
    label2 = new QLabel("KC:",this);
    label2->setGeometry(30,70,60,30);
    label3 = new QLabel("IVC:",this);
    label3->setGeometry(30,110,60,30);
    label4 = new QLabel("KCTGS:",this);
    label4->setGeometry(30,150,60,30);
    label5 = new QLabel("IVCTGS:",this);
    label5->setGeometry(30,190,60,30);
    label6 = new QLabel("KCV:",this);
    label6->setGeometry(30,230,60,30);
    label7 = new QLabel("IVCV:",this);
    label7->setGeometry(30,270,60,30);

    label_ID = new QLabel("Client01",this);
    label_ID->setGeometry(100,30,350,30);
    label_KC = new QLabel("未生成",this);
    label_KC->setGeometry(100,70,350,30);
    label_IVC = new QLabel("未生成",this);
    label_IVC->setGeometry(100,110,350,30);
    label_KCTGS = new QLabel("未生成",this);
    label_KCTGS->setGeometry(100,150,350,30);
    label_IVCTGS = new QLabel("未生成",this);
    label_IVCTGS->setGeometry(100,190,350,30);
    label_KCV = new QLabel("未生成",this);
    label_KCV->setGeometry(100,230,350,30);
    label_IVCV = new QLabel("未生成",this);
    label_IVCV->setGeometry(100,270,350,30);

    button1 = new QPushButton("请求TicketTGS",this);
    button1->setGeometry(30,310,140,40);
    button2 = new QPushButton("请求TicketV",this);
    button2->setGeometry(180,310,140,40);
    button3 = new QPushButton("请求服务",this);
    button3->setGeometry(330,310,90,40);

    ListWidget_log = new QListWidget(this);
    ListWidget_log->setGeometry(30,360,390,410);


    // 发送IDC和IDTGS（父窗口C向子窗口AS传值）
    connect(button1,&QPushButton::clicked,this,&WindowsC::sendIDC_INTGS_slots);
    connect(this,&WindowsC::sendIDC,AS,&WindowsAS::receive_IDC);
    connect(this,&WindowsC::sendIDTGS,AS,&WindowsAS::receive_IDTGS);


    // 接收从As发来kc和ivc
    connect(AS,&WindowsAS::sendKC,this,&WindowsC::receiveKC);
    connect(AS,&WindowsAS::sendIVC,this,&WindowsC::receiveIVC);

    // 接收从AS发来转发给TGS的KTGS和IVTGS
    connect(AS,&WindowsAS::sendKTGS,TGS,&WindowsTGS::receiveKTGS);
    connect(AS,&WindowsAS::sendIVTGS,TGS,&WindowsTGS::receiveIVTGS);


    // TGS给SS发送KV和IVV
    connect(AS,&WindowsAS::sendIVTGS,TGS,&WindowsTGS::makeKV_IVV_send_slot);
    connect(TGS,&WindowsTGS::sendKV,SS,&WindowSS::receiveKV_slots);
    connect(TGS,&WindowsTGS::sendIVV,SS,&WindowSS::receiveIVV_slots);


    // 接收密文
    connect(AS,&WindowsAS::sendencryKCTGS_KC,this,&WindowsC::receiveKCTGS_KC);
    connect(AS,&WindowsAS::sendencryIVCTGS_KC,this,&WindowsC::receiveIVCTGS_KC);
    connect(AS,&WindowsAS::sendencryIDC_KTGS_KC,this,&WindowsC::receiveIDC_KTGS_KC);
    connect(AS,&WindowsAS::sendencryIDTGS_KTGS_KC,this,&WindowsC::receiveIDTGS_KTGS_KC);
    connect(AS,&WindowsAS::sendencryKCTGS_KTGS_KC,this,&WindowsC::receiveKCTGS_KTGS_KC);
    connect(AS,&WindowsAS::sendencryIVCTGS_KTGS_KC,this,&WindowsC::receiveIVCTGS_KTGS_KC);

    // 解密KCTGS和IVCTGS
    connect(AS,&WindowsAS::sendencryIVCTGS_KTGS_KC,this,&WindowsC::decryKCTGSandIVCTGS);
    // 发送IDC,IDV和TicketTGS的密文给TGS
    connect(button2,&QPushButton::clicked,this,&WindowsC::sendIDC_IDV_TicketTGS_slot);
    connect(this,&WindowsC::sendIDC_tgs,TGS,&WindowsTGS::receiveIDC);
    connect(this,&WindowsC::sendIDV,TGS,&WindowsTGS::receiveIDV);
    connect(this,&WindowsC::sendIDC_KTGS,TGS,&WindowsTGS::receiveIDC_KTGS);
    connect(this,&WindowsC::sendIDTGS_KTGS,TGS,&WindowsTGS::receiveIDTGS_KTGS);
    connect(this,&WindowsC::sendKCTGS_KTGS,TGS,&WindowsTGS::receiveKCTGS_KTGS);
    connect(this,&WindowsC::sendIVCTGS_KTGS,TGS,&WindowsTGS::receiveIVCTGS_KTGS);

    //接收TGS发送的KCV的密文，IVCV的密文，IDC的双层密文，IDV的双层密文，KCV的双层密文，IVCV的双层密文并解密
    connect(TGS,&WindowsTGS::send_allenc_data,this,&WindowsC::receive_allenc_slots);

    // 请求ssv服务
    connect(button3,&QPushButton::clicked,this,&WindowsC::send_SSV_Service);
    connect(this,&WindowsC::send_signals_to_ss,SS,&WindowSS::receive_signal_fromC_slots);
    // 收到T
    connect(SS,&WindowSS::sendTS,this,&WindowsC::receiveTS);
    AS->show();
    TGS->show();
    SS->show();
}

WindowsC::~WindowsC()
{
}
// 收到key和iv
void WindowsC::receiveKC(QByteArray data)
{
    kc = data;
    label_KC->setText(QString(kc.toHex()));
    ListWidget_log->addItem("===开始生成并分发密钥===");
    ListWidget_log->addItem("从AS收到密钥KC：" + QString(kc.toHex()));
}

void WindowsC::receiveIVC(QByteArray data)
{
    ivc = data;
    label_IVC->setText(QString(ivc.toHex()));
    ListWidget_log->addItem("从AS收到密钥IVC：" + QString(ivc.toHex()));
    ListWidget_log->addItem("===结束生成并分发密钥===");
}

// 发送IDC_INTGS
void WindowsC::sendIDC_INTGS_slots()
{
    if(QString(kc.toHex()) != NULL and QString(ivc.toHex()) !=NULL)
    {
    ListWidget_log->addItem("===开始向AS购票===");
    ListWidget_log->addItem("向AS发送IDC和ICTGS");
    emit sendIDC(label_ID->text());
    emit sendIDTGS("TGS1");
    }
}
// 发送IDC,IDV和TicketTGS的密文给TGS
void WindowsC::sendIDC_IDV_TicketTGS_slot()
{
    if(QString(IDC_KTGS.toHex()) != NULL)
    {
    ListWidget_log->addItem("===开始向TGS购票===");
    ListWidget_log->addItem("向TGS发送IDC,IDV和TicketTGS的密文");
    emit sendIDC_tgs(label_ID->text());;
    emit sendIDV("SSV");
    emit sendIDC_KTGS(IDC_KTGS);
    emit sendIDTGS_KTGS(IDTGS_KTGS);
    emit sendKCTGS_KTGS(KCTGS_KTGS);
    emit sendIVCTGS_KTGS(IVCTGS_KTGS);
    }
}

// 从AS收到密文
void WindowsC::receiveKCTGS_KC(QByteArray data)
{
    KCTGS_kc = data;
    ListWidget_log->addItem("从AS接收到KCTGS的密文KCTGS_KC");
}

void WindowsC::receiveIVCTGS_KC(QByteArray data)
{
    IVCTGS_kc = data;
    ListWidget_log->addItem("从AS接收到IVCTGS的密文IVCTGS_KC");
}

void WindowsC::receiveIDC_KTGS_KC(QByteArray data)
{
    IDC_KTGS_kc =data;
    ListWidget_log->addItem("从AS接收到IDC的密文IDC_KTGS_KC");

}

void WindowsC::receiveIDTGS_KTGS_KC(QByteArray data)
{
    IDTGS_KTGS_kc = data;
    ListWidget_log->addItem("从AS接收到IDTGS的密文IDTGS_KTGS_KC");
}

void WindowsC::receiveKCTGS_KTGS_KC(QByteArray data)
{
    KCTGS_KTGS_kc = data;
    ListWidget_log->addItem("从AS接收到KCTGS的密文KCTGS_KTGS_KC");
}

void WindowsC::receiveIVCTGS_KTGS_KC(QByteArray data)
{
    IVCTGS_KTGS_kc = data;
    ListWidget_log->addItem("从AS接收到IVCTGS的密文IVCTGS_KTGS_KC");
}




// SM4解密函数，输出为明文长度
int WindowsC::decrypt(unsigned char *ciphertext, int ciphertext_len, unsigned char *key, unsigned char *iv, unsigned char *plaintext)
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

QByteArray WindowsC::decryptQByteArray(QByteArray _ciphertext, QByteArray _key, QByteArray _iv)
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

void WindowsC::decryKCTGSandIVCTGS()
{

    kctgs = WindowsC::decryptQByteArray(KCTGS_kc,kc,ivc);
    label_KCTGS->setText(QString(kctgs.toHex()).left(32));
    ivctgs = WindowsC::decryptQByteArray(IVCTGS_kc,kc,ivc);
    label_IVCTGS->setText(QString(ivctgs.toHex()).left(32));
    ListWidget_log->addItem("解密会话密钥KCTGS");
    ListWidget_log->addItem("使用Kc解密KCTGS_KC得到KCTGS：" + QString(kctgs.toHex()).left(32));
    ListWidget_log->addItem("使用Kc解密IVCTGS_KC得到IVCTGS：" + QString(ivctgs.toHex()).left(32));

    // 解密IDC_KTGS_kc,IDTGS_KTGS_kc,KCTGS_KTGS_kc,IVCTGS_KTGS_kc

    IDC_KTGS = WindowsC::decryptQByteArray(IDC_KTGS_kc,kc,ivc);
    IDTGS_KTGS = WindowsC::decryptQByteArray(IDTGS_KTGS_kc,kc,ivc);
    KCTGS_KTGS = WindowsC::decryptQByteArray(KCTGS_KTGS_kc,kc,ivc);
    IVCTGS_KTGS = WindowsC::decryptQByteArray(IVCTGS_KTGS_kc,kc,ivc);
    ListWidget_log->addItem("解密TicketTGS的外层密文");
    ListWidget_log->addItem("使用KC解密IDC_KTGS_kc的外层密文，得到IDC_KTGS：");
    ListWidget_log->addItem("使用KC解密IDTGS_KTGS_kc外层密文，得到IDTGS_KTGS：");
    ListWidget_log->addItem("使用KC解密KCTGS_KTGS_kc外层密文，得到KCTGS_KTGS：");
    ListWidget_log->addItem("使用KC解密IVCTGS_KTGS_kc外层密文，得到IVCTGS_KTGS：");
    ListWidget_log->addItem("===结束向AS购票===");
}

void WindowsC::receive_allenc_slots(QByteArray data1, QByteArray data2, QByteArray data3,
                                    QByteArray data4, QByteArray data5, QByteArray data6)
{
    QByteArray KCV_KCTGS,IVCV_KCTGS;
    QByteArray IDC_KV_KCTGS, IDV_KV_KCTGS, KCV_KV_KCTGS, IVCV_KV_KCTGS;
    KCV_KCTGS = data1;
    IVCV_KCTGS = data2;

    IDC_KV_KCTGS = data3;
    IDV_KV_KCTGS = data4;
    KCV_KV_KCTGS = data5;
    IVCV_KV_KCTGS = data6;
    ListWidget_log->addItem("从TGS接收到密文KCV_KCTGS");
    ListWidget_log->addItem("从TGS接收到密文IVCV_KCTGS");
    ListWidget_log->addItem("从TGS接收到密文IDC_KV_KCTGS");
    ListWidget_log->addItem("从TGS接收到密文IDV_KV_KCTGS");
    ListWidget_log->addItem("从TGS接收到密文KCV_KV_KCTGS");
    ListWidget_log->addItem("从TGS接收到密文IVCV_KV_KCTGS");

    // 使用KCTGS解密KCV_KCTGS、IVCV_KCTGS，得到会话密钥KCV和对应的IVCV

    KCV = decryptQByteArray(KCV_KCTGS,kctgs,ivctgs);
    IVCV =decryptQByteArray(IVCV_KCTGS,kctgs,ivctgs);
    label_KCV->setText(QString(KCV.toHex()).left(32));
    label_IVCV->setText(QString(IVCV.toHex()).left(32));
    ListWidget_log->addItem("解密会话密钥KCV");
    ListWidget_log->addItem("使用KCTGS解密KCV_KCTGS，得到KCV：" + QString(KCV.toHex()).left(32));
    ListWidget_log->addItem("使用KCTGS解密IVCV_KCTGS，得到IVCV：" + QString(IVCV.toHex()).left(32));
    // 解密TicketV的外层密文

    IDC_KV = decryptQByteArray(IDC_KV_KCTGS,kctgs,ivctgs);
    IDV_KV =decryptQByteArray(IDV_KV_KCTGS,kctgs,ivctgs);
    KCV_KV = decryptQByteArray(KCV_KV_KCTGS,kctgs,ivctgs);
    IVCV_KV =decryptQByteArray(IVCV_KV_KCTGS,kctgs,ivctgs);
    ListWidget_log->addItem("解密TicketV的外层密文");
    ListWidget_log->addItem("使用KCTGS解密IDC_KV_KCTGS，得到IDC_KV");
    ListWidget_log->addItem("使用KCTGS解密IDV_KV_KCTGS，得到IDV_KV");
    ListWidget_log->addItem("使用KCTGS解密KCV_KV_KCTGS，得到KCV_KV");
    ListWidget_log->addItem("使用KCTGS解密IVCV_KV_KCTGS，得到IVCV_KV");
    ListWidget_log->addItem("===结束向TGS购票===");
}


void WindowsC::send_SSV_Service()
{
    if(label_KCV->text()!=NULL)
    {
    ListWidget_log->addItem("===开始向SSV请求服务===");
    QDateTime time = QDateTime::currentDateTime();   //获取当前时间
    int TS = time.toTime_t();   //将当前时间转为时间戳
    ListWidget_log->addItem("生成时间戳:" + QString::number(TS));
    // 将IDC和TS使用KCV加密
    QByteArray IDC_KCV,TS_KCV;
    IDC_KCV = encryptQString("Client01",KCV,IVCV);
    TS_KCV = encryptQString(QString::number(TS),KCV,IVCV);
    ListWidget_log->addItem("将IDC和TS使用KCV加密");
    emit send_signals_to_ss(IDC_KCV,TS_KCV,IDC_KV,
                            IDV_KV,KCV_KV,IVCV_KV);
    ListWidget_log->addItem("向SSV发送IDC的密文，时间戳TS的密文和TicketV的密文");

    }
}

void WindowsC::receiveTS(QByteArray data)
{
    ListWidget_log->addItem("从SSV接收到TS+1的密文TS+1_KCV");
    QByteArray t;
    t = decryptQByteArray(data,KCV,IVCV);
    ListWidget_log->addItem("使用KCV解密TS+1_KCV，得到TS+1：" + QString(t));
    ListWidget_log->addItem("TS+1验证通过，开始使用服务SSV");
    ListWidget_log->addItem("===结束向SSV请求服务===");
}



// SM4加密函数，输出为密文长度
int WindowsC::encrypt(unsigned char *plaintext, int plaintext_len, unsigned char *key,
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

QByteArray WindowsC::encryptQString(QString _plaintext, QByteArray _key, QByteArray _iv)
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

QByteArray WindowsC::encryptQByteArray(QByteArray _plaintext, QByteArray _key, QByteArray _iv)
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

unsigned char *WindowsC::QByteArrayToUsignedChar(QByteArray ba)
{
    const std::size_t count = ba.size();
    unsigned char* ucharArry = new unsigned char[count];
    memcpy(ucharArry,ba.constData(),count);
    return ucharArry;
}
