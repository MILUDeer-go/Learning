#ifndef WINDOWSC_H
#define WINDOWSC_H

#include <QWidget>
#include <QLabel>
#include <QPushButton>
#include <QListWidget>

#include <openssl\sm2.h>
#include <openssl\evp.h>
#include <openssl\rand.h>

class WindowsC : public QWidget
{
    Q_OBJECT
public:
    explicit WindowsC(QWidget *parent = nullptr);
    ~WindowsC();

private:
    QLabel *label1;
    QLabel *label2;
    QLabel *label3;
    QLabel *label4;
    QLabel *label5;
    QLabel *label6;
    QLabel *label7;
    QLabel *label_ID;
    QLabel *label_KC;
    QLabel *label_IVC;
    QLabel *label_KCTGS;
    QLabel *label_IVCTGS;
    QLabel *label_KCV;
    QLabel *label_IVCV;

    QPushButton *button1;
    QPushButton *button2;
    QPushButton *button3;
    QListWidget *ListWidget_log;

public slots:
    void receiveKC(QByteArray data);
    void receiveIVC(QByteArray data);


    // 发送IDC和IDTGS给AS
    void sendIDC_INTGS_slots();
    // 发送IDC,IDV和TicketTGS的密文给TGS
    void sendIDC_IDV_TicketTGS_slot();

    // 收到密文
    void receiveKCTGS_KC(QByteArray data);
    void receiveIVCTGS_KC(QByteArray data);
    void receiveIDC_KTGS_KC(QByteArray data);
    void receiveIDTGS_KTGS_KC(QByteArray data);
    void receiveKCTGS_KTGS_KC(QByteArray data);
    void receiveIVCTGS_KTGS_KC(QByteArray data);

    // 请求SSV服务
    void send_SSV_Service();

    // 接收TS
    void receiveTS(QByteArray data);

    // 字节数组转字符
    unsigned char* QByteArrayToUsignedChar(QByteArray ba);
    // 解密
    int decrypt(unsigned char *ciphertext, int ciphertext_len, unsigned char *key,
         unsigned char *iv, unsigned char *plaintext);

    QByteArray decryptQByteArray(QByteArray _ciphertext, QByteArray _key, QByteArray _iv);


     // 解密会话密钥及KC加密的信息
    void decryKCTGSandIVCTGS();
     // 接收TGS发送的KCV的密文，IVCV的密文，IDC的双层密文，IDV的双层密文，KCV的双层密文，IVCV的双层密文
    void receive_allenc_slots(QByteArray data1,QByteArray data2,QByteArray data3,
                              QByteArray data4,QByteArray data5,QByteArray data6);

    int encrypt(unsigned char *plaintext, int plaintext_len, unsigned char *key,
        unsigned char *iv, unsigned char *ciphertext);
    QByteArray encryptQByteArray(QByteArray _plaintext, QByteArray _key, QByteArray _iv);
    QByteArray encryptQString(QString _plaintext, QByteArray _key, QByteArray _iv);


signals:
    void sendIDC(QString);
    void sendIDTGS(QString);
    void sendIDC_tgs(QString);

    void sendIDV(QString);
    void sendIDC_KTGS(QByteArray);
    void sendIDTGS_KTGS(QByteArray);
    void sendKCTGS_KTGS(QByteArray);
    void sendIVCTGS_KTGS(QByteArray);

    void send_signals_to_ss(QByteArray,QByteArray,QByteArray,
                            QByteArray,QByteArray,QByteArray);


};

#endif // WINDOWSC_H
