from PIL import Image, ImageDraw, ImageFont
import glob
import os
from time import sleep


def imgNumbering(imageList):
    
    print("\n\n-------Generating Images w/ Number on Centre-------\n\n")

    sleep(2)

    folderName = "Result"

     # getting current working directory
    current_directory = os.getcwd()
    path = os.path.join(current_directory, folderName)

    # creating a new folder for storing the results
    try : 
        os.mkdir(path)
    except:
        pass

    font_size = 40
    font = ImageFont.truetype("arial.ttf", font_size)

    # iterating through the List of image names
    for i, imagePath in enumerate(imageList):

        img = Image.open(imagePath)
        text = str(i+1)
        
        #creating an object of draw()
        draw = ImageDraw.Draw(img)

        #obtaining the width and height of the input text
        w, h = draw.textsize(text,font=font)
        h += int(h*0.21)

        #finding the centre coodinates
        coodinates=((img.width-w)/2),(img.height-h)/2

        #adding text to the image
        draw.text(coodinates,text=text, fill='black', font=font)

        #saving the image
        img.save("{}//Img-with-number{:03}.jpg".format(folderName,i+1))
        print("\tImage {:03} Done!".format(i+1))
        
    sleep(2)
    print("""\n\nImages will be available at "{}"\n
---------Task-Completed---------\n\n""".format(path))


if __name__ == "__main__":
    img_list=[]

#     creating list of image path
    imagePathList = glob.glob('Data/*.jpg')
    imgNumbering(imagePathList)


