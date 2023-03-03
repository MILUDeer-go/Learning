#ifndef WINDOWSS_H
#define WINDOWSS_H

#include <QWidget>
#include <QLabel>
#include <QListWidget>

#include <openssl\sm2.h>
#include <openssl\evp.h>
#include <openssl\rand.h>

class WindowSS : public QWidget
{
    Q_OBJECT
public:
    explicit WindowSS(QWidget *parent = nullptr);
private:
    QLabel *label1;
    QLabel *label2;
    QLabel *label3;
    QLabel *label4;
    QLabel *label5;
    QLabel *label_ID;
    QLabel *label_KV;
    QLabel *label_IVV;
    QLabel *label_KCV;
    QLabel *label_IVCV;
    QListWidget *ListWidget_log;

    // 加密
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



public slots:
    // 接收TGS发送的kv，ivv
    void receiveKV_slots(QByteArray data);
    void receiveIVV_slots(QByteArray data);

    void receive_signal_fromC_slots(QByteArray data1,QByteArray data2,QByteArray data3,
                              QByteArray data4,QByteArray data5,QByteArray data6);


signals:

    void sendTS(QByteArray);
};

#endif // WINDOWSS_H
