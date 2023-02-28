import tkinter as tk

app = tk.Tk()
app.title("first tkinter windows")
# 窗口大小
app.geometry("720x560")

print("电脑的分辨率是%dx%d" % (app.winfo_screenwidth(), app.winfo_screenheight()))
app.update()
print("窗口的分辨率是%dx%d" % (app.winfo_width(), app.winfo_height()))
text = tk.Label(app, text="C语言中文网，网址：c.biancheng.net", bg="yellow", fg="red", font=('Times', 15, 'bold italic underline'))
# 将文本内容放置在主窗口内
text.pack()
app.config(background="#6fb765")
button = tk.Button(app, text="关闭", command=app.quit)
# 将按钮放置在主窗口内
button.pack(side="bottom")
app.mainloop()