#include "mainwindow.h"

#include <QFileDialog>
#include <QMessageBox>
#include <QTextStream>
#include <QColorDialog>
#include <QFontDialog>

int Flag_isOpen = 0;       //标记：判断是否打开或创建了一个文件
int Flag_IsNew = 1;        //标记：如果新建了文件就为1，初始值为0
QString Last_FileName;     //最后一次保存的文件的名字

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    this->setGeometry(400,300,800,500);
    this->setWindowTitle("文本编辑器");

    TextEdit = new QTextEdit(this);

    QString str = "1. On no account can we + V ~~~ （我们绝对不能...）"
                  "例句：On no account can we ignore the value of knowledge."
                  "2. Nothing is + ~~~ er than to + V Nothing is + more + 形容词 + than to + V"
                  "Nothing is more important than to receive education.";
    TextEdit->setText(str);
    this->setCentralWidget(TextEdit);
    QFont f;
    f.setPointSize(10);
    TextEdit->setFont(f);

    MenuBar = new QMenuBar(this);
    this->setMenuBar(MenuBar);
    filemenu = new QMenu("文件");
    editmenu = new QMenu("编辑");
    helpmenu = new QMenu("帮助");

    MenuBar->addMenu(filemenu);
    MenuBar->addMenu(editmenu);
    MenuBar->addMenu(helpmenu);

    // 设置操作
    create = new QAction("&新建");
    create->setShortcut(tr("ctrl+k"));
    open = new QAction("&打开");
    open->setShortcut(tr("ctrl+o"));
    save = new QAction("&保存");
    save->setShortcut(tr("ctrl+s"));
    save_as = new QAction("另存为");

    about = new QAction("关于作者");
    aboutqt = new QAction("关于应用");

    editmenuaction = new QAction("点这试试");


    filemenu->addAction(create);
    filemenu->addAction(open);
    filemenu->addAction(save);
    filemenu->addAction(save_as);

    editmenu->addAction(editmenuaction);

    helpmenu->addAction(about);
    helpmenu->addAction(aboutqt);

    connect(open,&QAction::triggered,this,&MainWindow::open_slot);
    connect(create,&QAction::triggered,this,&MainWindow::create_slot);
    connect(save,&QAction::triggered,this,&MainWindow::save_slot);
    connect(save_as,&QAction::triggered,this,&MainWindow::save_as_slot);
    connect(about,&QAction::triggered,this,&MainWindow::aboutme);
    connect(aboutqt,&QAction::triggered,this,&MainWindow::aboutQt);
    connect(editmenuaction,&QAction::triggered,this,&MainWindow::editmenu_slots);

    //toolbar
    ToolBar = new QToolBar(this);
    color = new QAction("颜色");
    font= new QAction("字体");
    background= new QAction("背景");
    ToolBar->addAction(color);
    ToolBar->addAction(font);
    ToolBar->addAction(background);
    this->addToolBar(ToolBar);

    connect(color,&QAction::triggered,this,&MainWindow::colorc);
    connect(font,&QAction::triggered,this,&MainWindow::fontf);
    connect(background,&QAction::triggered,this,&MainWindow::backgroundcolor);

    //StatusBar
    StatusBar = new QStatusBar();
    this->setStatusBar(StatusBar);
    StatusBar->showMessage("这是状态栏");
}

MainWindow::~MainWindow()
{
}

void MainWindow::open_slot()
{
    QString  res = QFileDialog::getOpenFileName(this,"选择文件",NULL,"文本(*.txt);;全部(*.*)");
    QFile file(res);
    if(!file.open(QFile::ReadOnly)){
            QMessageBox msg;
            msg.setText("文件不存在");
            msg.show();
        }
    else{
        TextEdit->setText(file.readAll());
        Flag_isOpen = 1;
        Flag_IsNew = 0;
        Last_FileName = res;
        QFileInfo fileInfo = QFileInfo(res);
        //文件名
        QString filename = fileInfo.fileName();
        this->setWindowTitle(filename);

        StatusBar->showMessage("打开文件" + filename);
    }

}

void MainWindow::save_slot()
{
    if(Flag_IsNew)                  //如果新文件标记位为1，则弹出保存文件对话框
        {
        return save_as_slot();
        }
    else                        //否则，新文件标记位是0，代表是旧文件，默认直接保存覆盖源文件
        {
            if(Flag_isOpen)         //判断是否创建或打开了一个文件
            {
                QFile file(Last_FileName);
                if(!file.open(QIODevice::WriteOnly | QIODevice::Text))
                {
                    QMessageBox::warning(this,tr("警告"),tr("打开文件失败"));
                    return;
                }
                else
                {
                    QTextStream textStream(&file);
                    QString str = TextEdit->toPlainText();
                    textStream<<str;
                    file.close();
                    StatusBar->showMessage(Last_FileName + "内容保存成功");
                }
            }
            else
            {
                QMessageBox::warning(this,tr("警告"),tr("请先创建或者打开文件"));
                return;
            }
        }
}

void MainWindow::create_slot()
{
     TextEdit->clear();              //清除原先文件内容
     Flag_IsNew = 1;                 //新文件标记位设为1
     Flag_isOpen = 1;
     this->setWindowTitle("未命名.*");
     StatusBar->showMessage("新建文件");
}

void MainWindow::save_as_slot()
{
    QString curPath=QDir::currentPath();//获取系统当前目录
    QString dlgTitle="另存为一个文件"; //对话框标题
    QString filter="文本文件(*.txt);;所有文件(*.*);;文档(*.doc)"; //文件过滤器
    QString aFileName=QFileDialog::getSaveFileName(this,dlgTitle,curPath,filter);
    if (aFileName.isEmpty())
    {
        QMessageBox msg;
        msg.setText("内容为空！");
        msg.show();
    }
    QFile aFile(aFileName);
       //aFile.setFileName(aFileName);
    if (!aFile.open(QIODevice::WriteOnly | QIODevice::Text))
    {
        QMessageBox msg;
        msg.setText("文件写入失败！");
        msg.show();
    }
    else{
    QString str=TextEdit->toPlainText();//整个内容作为字符串
    QByteArray  strBytes=str.toUtf8();//转换为字节数组
    //QByteArray  strBytes=str.toLocal8Bit();
    aFile.write(strBytes,strBytes.length());  //写入文件
    }
    aFile.close();
    StatusBar->showMessage("文件另存为"+ aFileName);
}

void MainWindow::colorc()
{
    QColor color1;
    color1 = QColorDialog::getColor("",this,"请选择颜色");
    TextEdit->setTextColor(color1);
    StatusBar->showMessage("字体颜色已被修改");
}

void MainWindow::fontf()
{
    QFont f;
    bool ok;
    f = QFontDialog::getFont(&ok, QFont("Helvetica [Cronyx]", 10), this);
    TextEdit->setFont(f);
    StatusBar->showMessage("字体已被修改");
}

void MainWindow::backgroundcolor()
{
    QColor color;
    color = QColorDialog::getColor(Qt::white,this,"请选择颜色");

    QPalette pal = TextEdit->palette();
    // 设置画刷，填充背景颜色
    pal.setBrush(QPalette::Base, color);
    // 取消继承父类的背景样式
    TextEdit->setAutoFillBackground(true);
    // QTextEdit设置调色板，即填充了背景图片
    TextEdit->setPalette(pal);
    StatusBar->showMessage("背景颜色已被修改");
}

void MainWindow::aboutme()
{
     QMessageBox::about(this,"关于","本程序由miludeer采用Qt编写，敬请指正！");
}

void MainWindow::aboutQt()
{
    QMessageBox::aboutQt(this);
}

void MainWindow::editmenu_slots()
{
    QMessageBox::about(this,"编辑按钮","编辑按钮无用呦！");
}

