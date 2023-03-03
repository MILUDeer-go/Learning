#include "widget.h"
#include "windowsas.h"
#include "windowsc.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
//    Widget w;
//    w.show();
//    WindowsAS w;
//    w.show();
    WindowsC v;
    v.show();
    return a.exec();
}
