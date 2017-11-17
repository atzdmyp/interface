from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 验证码demo


# 随机字母
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1
def rndColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2
def rndColor2():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 240 * 60
width = 60 * 4
height = 60
img = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象
font = ImageFont.truetype('Arial.ttf', 36)

# 创建Draw对象
draw = ImageDraw.Draw(img)

# 填充每个像素
for i in range(width):
    for j in range(height):
        draw.point((i, j), fill=rndColor1())


# 输出文字
for i in range(4):
    draw.text((60 * i + 10, 10), rndChar(), font=font, fill=rndColor2())


# 模糊
img = img.filter(ImageFilter.BLUR)
img.save('code.jpg', 'jpeg')
