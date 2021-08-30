'''
Function - This program will open a frame of a video individually
Input - Ability to throttle the time between each frame is determinted by user

Implementation:
    A loop will open up an image from a directiory, with the number changing.

TO IMPLEMENT:
    Error catching if file is not found
    default values
    move time buffer to be consistent
    LIMIT THE IMPORT STATEMENT TKINTER

    WHAT IS LAMBDA?
'''
#ffmpeg -i "directory/filename" "directory/$filename%03d.bmp"

import os, time
from tkinter import *
from PIL import Image
from tkinter.messagebox import _show

r"/home/ubuntu/Desktop/frames/100.bmp"

# Input variables
frameQuantity = int(input("Frame Quantity: "))
startingFrame = int(input("Starting Frame: "))
buffer = float(input("Buffer Amount (seconds [floats accepted]): "))

#class frameParsing:
def pythonVideoFrameOpener(frameQuantity, startingFrame, buffer):
    for frameNumber in range(0, frameQuantity):
        print("frame: " + str(frameNumber + 1))
        img = Image.open("/home/ubuntu/help/" + frameNumberCalculator(frameNumber + startingFrame) + ".png")
        w, h = img.size

        window = Tk() #Tkinter instance
        window.title("Bad Apple!!")
        window.geometry(str(w) + "x" + str(h))

        # Canvas creation
        canvas = Canvas(window, height = h, width = w, bg = "#fff")
        canvas.pack()

        #window.after(1000, lambda : _show('Title', 'Prompting after 5 seconds')) # Message prompt
        
        # Add image to canvas
        pImg = PhotoImage(file=str("/home/ubuntu/help/" + frameNumberCalculator(frameNumber + startingFrame) + ".png"))
        canvas.create_image(w/2, h/2, image=pImg)

        window.after(int(buffer*1000), window.destroy) #milliseconds
        window.mainloop()


def videoFrameOpener(frameQuantity, startingFrame, buffer):
    for frameNumber in range(0, frameQuantity):
        frame = Image.open(r"/home/ubuntu/Desktop/frames/" + frameNumberCalculator(frameNumber + startingFrame) + r".bmp")
        frame.show()
        print("frame: " + str(frameNumber + 1))
        time.sleep(buffer)

def frameNumberCalculator(frameNumber):
    if(len(str(frameNumber)) == 1):
        return "00" + str(frameNumber)
    elif(len(str(frameNumber)) == 2):
        return "0" + str(frameNumber)
    else:
        return str(frameNumber)

#videoFrameOpener(frameQuantity, startingFrame, buffer)
pythonVideoFrameOpener(frameQuantity, startingFrame, buffer)
