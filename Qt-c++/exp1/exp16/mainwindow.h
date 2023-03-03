#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTextEdit>

#include <QAction>
#include <QMenu>
#include <QMenuBar>
#include <QToolBar>
#include <QToolButton>
#include <QStatusBar>

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    QTextEdit *TextEdit;
    QMenuBar *MenuBar;
    QMenu * filemenu;
    QMenu * editmenu;
    QMenu * helpmenu;

    QAction * open;
    QAction * save;
    QAction * create;
    QAction * save_as;
    QAction * about;
    QAction * aboutqt;
    QAction * editmenuaction;

    QToolBar * ToolBar;
    QAction * color;
    QAction * font;
    QAction * background;
    QStatusBar *StatusBar;

public slots:
    void open_slot();
    void save_slot();
    void create_slot();
    void save_as_slot();
    void colorc();
    void fontf();
    void backgroundcolor();

    void aboutme();
    void aboutQt();
    void editmenu_slots();


signals:



};
#endif // MAINWINDOW_H
