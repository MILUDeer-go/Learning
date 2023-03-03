#ifndef WINDOWSTGS_H
#define WINDOWSTGS_H

#include <QWidget>
#include <QLabel>
#include <QListWidget>

#include <openssl\sm2.h>
#include <openssl\evp.h>
#include <openssl\rand.h>

class WindowsTGS : public QWidget
{
    Q_OBJECT
public:
    explicit WindowsTGS(QWidget *parent = nullptr);
private:
    QLabel *label1;
    QLabel *label2;
    QLabel *label3;
    QLabel *label4;
    QLabel *label5;
    QLabel *label6;
    QLabel *label7;
    QLabel *label_ID;
    QLabel *label_KTGS;
    QLabel *label_IVTGS;
    QLabel *label_KV;
    QLabel *label_IVV;
    QLabel *label_KCTGS;
    QLabel *label_IVCTGS;

    QListWidget *ListWidget_log;

public slots:
    QByteArray generateRandomKV();
    QByteArray generateRandomIVV();

    // 接收KTGS和IVTGS
    void receiveKTGS(QByteArray data);
    void receiveIVTGS(QByteArray data);
    // 生成KV，IVV并发送给SS
    void makeKV_IVV_send_slot();

    // 接收C发来的IDC_KTGS,IDTGS_KTGS,KCTGS_KTGS,IVCTGS_KTGS
    void receiveIDC(QString data);
    void receiveIDV(QString data);
    void receiveIDC_KTGS(QByteArray data);
    void receiveIDTGS_KTGS(QByteArray data);
    void receiveKCTGS_KTGS(QByteArray data);
    void receiveIVCTGS_KTGS(QByteArray data);
    // 解密票据
    void jiemi_TicketTGS();

    int encrypt(unsigned char *plaintext, int plaintext_len, unsigned char *key,
        unsigned char *iv, unsigned char *ciphertext);
    QByteArray encryptQString(QString _plaintext, QByteArray _key, QByteArray _iv);
    QByteArray encryptQByteArray(QByteArray _plaintext, QByteArray _key, QByteArray _iv);

    // 字节数组转字符
    unsigned char* QByteArrayToUsignedChar(QByteArray ba);
    // 解密
    int decrypt(unsigned char *ciphertext, int ciphertext_len, unsigned char *key,
            unsigned char *iv, unsigned char *plaintext);
    QByteArray decryptQByteArray(QByteArray _ciphertext, QByteArray _key, QByteArray _iv);
    // 发送KC和IVC

signals:
    void sendKV(QByteArray);
    void sendIVV(QByteArray);

    void jiemi();
    // KCV的密文，IVCV的密文，IDC的双层密文，IDV的双层密文，KCV的双层密文，IVCV的双层密文发送给C
    void send_allenc_data(QByteArray,QByteArray,QByteArray,QByteArray,QByteArray,QByteArray);

};



#endif // WINDOWSTGS_H
