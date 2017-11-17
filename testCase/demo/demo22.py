from tkinter import *
from tkinter.filedialog import askdirectory
import qrcode


def callback():
    """
    select directory
    :return:
    """
    global path
    path.set(askdirectory())

root = Tk(className="生成二维码")
path = StringVar()

Label(root, text="URL:").grid(row=0)
e = Entry(root, width=25)
e.grid(row=0, column=1, padx=10, pady=5)
Label(root, text="图片保存路径：").grid(row=1)
e2 = Entry(root, textvariable=path, width=25)
e2.grid(row=1, column=1)
Button(root, text="选择", command=callback).grid(row=1, column=2, padx=10, pady=5)


def show():
    """
    生成二维码图片并设置尺寸大小，容错度
    :return:
    """
    url = e.get()
    path1 = e2.get()+"img.png"
    print(path1)
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(str(path1))

    e.delete(0, END)
    Label(root, text="二维码已保存到：%s" % path1, width=25).grid(row=3, column=0, columnspan=2)
# e.index(0, "默认文本...")


Button(root, text="生成专属二维码", width=15, command=show).grid(row=2, column=0, sticky=W, padx=15, pady=5)
Button(root, text="退出", width=10, command=root.quit).grid(row=2, column=2, sticky=E, padx=10, pady=5)

mainloop()
