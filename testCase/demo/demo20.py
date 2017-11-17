import qrcode
from PIL import Image


# 生成二维码图片
def qrimg():
    """
    生成一个二维码图片
    :return:
    """
    img = qrcode.make("www.baidu.com")
    img.save("F:\python_pictures\qrimg1.png")


def qrimg2():
    """
    生成二维码图片并设置尺寸大小，容错度
    :return:
    """
    url = "www.baidu.com"
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=2
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()

    img.save("F:\python_pictures\qrimg2.png")


def qrimg3():
    """
    生成二维码图片并插入logo图片
    :return:
    """
    url = "www.baidu.com"
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert("RGBA")
    logo = Image.open(r"E:\其他\桌面壁纸\XiongBen\logo1.png")
    img_w, img_h = img.size
    size_w = int(img_w/4)
    size_h = int(img_h/4)
    logo_w, logo_h = logo.size
    # 设置logo的大小
    if logo_w > size_w:
        logo_w = size_w
    if logo_h > size_h:
        logo_h = size_h
    logo = logo.resize((logo_w, logo_h), Image.ANTIALIAS)
    # 调整logo在二维码中的位置
    w = int((img_w-logo_w)/2)
    h = int((img_h-logo_h)/2)
    img.paste(logo, (w, h))
    img.save("F:\python_pictures\qrimg3.png")


if __name__ == "__main__":
    qrimg3()
