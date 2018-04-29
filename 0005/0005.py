from PIL import Image
import os
import glob

IPHONE_WIDTH = 1136
IPHONE_HIGH = 640


def resize_img(img):
    im = Image.open(img)
    x,y = im.size

    filename = os.path.basename(img)

    while True:
        x = int(x/2)
        y = int(y/2)
        if x < IPHONE_WIDTH and y < IPHONE_HIGH:
            break

    try:
        os.mkdir('resize')
    except:
        pass

    resizedIm = im.resize((x,y))
    resizedIm.save('resize/'+filename)


if __name__ == '__main__':
    files = glob.glob('./image/*.jpg')

    for file in files:
        resize_img(file)

    print(os.system('tree -h'))
