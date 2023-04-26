from PIL import Image, ImageDraw, ImageFont

def generateimage():
    img = Image.open("nature.png")
    msg = 'Youre only lonely if youre not there for you.'
    d1 = ImageDraw.Draw(img)
    w, h = d1.textsize(msg, font=ImageFont.truetype("BadScript-Regular.ttf", 28))
    d1.text(((800 - w) / 2, (800 - h) / 2), msg, fill="black", font=ImageFont.truetype("BadScript-Regular.ttf", 28))
    img.show()
    img.save("natureGenerated.png")