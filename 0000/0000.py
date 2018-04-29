from PIL import Image, ImageDraw, ImageFont

OUTPUT_IMG_NAME = 'pic_add_num.jpg'
ORIGIN_IMG_NAME = 'origin.jpg'


def add_num(img,num):
    im = Image.open(img)
    x,y = im.size
    font = ImageFont.truetype('Royal.otf', int(x/4))
    ImageDraw.Draw(im).text((x*0.7,0),num,font=font,fill='red')
    im.save(OUTPUT_IMG_NAME)
    im.show()

if __name__ == '__main__':
    add_num(ORIGIN_IMG_NAME,'4')

