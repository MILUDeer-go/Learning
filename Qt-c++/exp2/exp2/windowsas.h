#ifndef WINDOWSAS_H
#define WINDOWSAS_H

#include <QWidget>
#include <QLabel>
#include <QPushButton>
#include <QListWidget>

#include <openssl\sm2.h>
#include <openssl\evp.h>
#include <openssl\rand.h>
class WindowsAS : public QWidget
{
    Q_OBJECT
public:
    explicit WindowsAS(QWidget *parent = nullptr);
    ~WindowsAS();

private:
    QLabel *label1;
    QLabel *label2;
    QLabel *label3;
    QLabel *label4;
    QLabel *label5;
    QLabel *label_ID;
    QLabel *label_KC;
    QLabel *label_IVC;
    QLabel *label_KTGS;
    QLabel *label_IVTGS;

    QPushButton *button;
    QListWidget *ListWidget_log;

public slots:
    void button_click();
    QByteArray generateRandomKey();
    QByteArray generateRandomIV();
    QByteArray generateRandomKTGS();
    QByteArray generateRandomIVTGS();
    void ASencrytedIDC_IDTGS();

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
// 发送KC和IVC
    void sendKC_slot();
    void sendIVC_slot();
// 发送KTGS和IVTGS
    void sendKTGSandIVTGS_slot();

// 收取
    void receive_IDC(QString data);
    void receive_IDTGS(QString data);

signals:
    void sendKC(QByteArray);
    void sendIVC(QByteArray);

    void sendKTGS(QByteArray);
    void sendIVTGS(QByteArray);
    //发送密文
    void sendencryKCTGS_KC(QByteArray);
    void sendencryIVCTGS_KC(QByteArray);
    void sendencryIDC_KTGS_KC(QByteArray);
    void sendencryIDTGS_KTGS_KC(QByteArray);
    void sendencryKCTGS_KTGS_KC(QByteArray);
    void sendencryIVCTGS_KTGS_KC(QByteArray);
    void receiveIDC_IDTGS();

};




#endif // WINDOWSAS_H
