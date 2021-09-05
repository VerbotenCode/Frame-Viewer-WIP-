'''
Function - This program will open a frame of a video individually
Input - Ability to throttle the time between each frame is determinted by user along with the starting and quantity of frames

Implementation:
    A loop will open up an image from a directiory, with the number changing.

TO IMPLEMENT:
    Error catching:
        -if file is not found
        -invalid import
    add default values to methods
'''
#ffmpeg -i "directory/filename" "directory/$filename%03d.bmp"

import os, time
from tkinter import Tk, Canvas, PhotoImage
from PIL import Image
from tkinter.messagebox import _show

#r"/home/ubuntu/Desktop/frames/"
directory = r"/home/ubuntu/Desktop/frames/"
#directory = input("Directory (case sensitive): ")

# User input and variables pertaining to user input
class resources:
    def user_input():
        frame_quantity, starting_frame, buffer = resources.variables_input()
        user_choice = int(input("0 - Native Image Opener; 1 - Python Image Opener \n"))
        if(user_choice == 0):
            frame.frame_display(frame_quantity, starting_frame, buffer)
        elif(user_choice == 1):
            frame.pframe_display(frame_quantity + 1, starting_frame, buffer)
        else:
            print("invalid")
            resources.variables_input()

    def variables_input():
        # Input variables
        frame_quantity = int(input("Frame Quantity: "))
        starting_frame = int(input("Starting Frame: "))
        buffer = float(input("Buffer Amount (seconds [floats accepted]): "))
        return frame_quantity, starting_frame, buffer

# Frame parsing and calculations
class frame:
    def pframe_display(frame_quantity, starting_frame, buffer):
        for frame_number in range(1, frame_quantity):
            print("frame: " + str(frame_number))
            img = Image.open("/home/ubuntu/help/" + frame.frame_calculator(frame_number + starting_frame) + ".png")
            w, h = img.size

            # Window attributes
            window = Tk() #Tkinter instance
            window.title("Bad Apple!!")
            window.geometry(str(w) + "x" + str(h))

            # Canvas creation
            canvas = Canvas(window, height = h, width = w, bg = "#fff")
            canvas.pack()

            #window.after(1000, lambda : _show('Title', 'Prompting after 5 seconds')) # Message prompt
            
            # Add image to canvas
            p_img = PhotoImage(file=str("/home/ubuntu/help/" + frame.frame_calculator(frame_number + starting_frame) + ".png"))
            canvas.create_image(w/2, h/2, image=p_img)

            window.after(int(buffer*1000), window.destroy) #milliseconds
            window.mainloop()


    def frame_display(frame_quantity, starting_frame, buffer):
        for frame_number in range(0, frame_quantity):
            frame = Image.open(directory + frame.frame_calculator(frame_number + starting_frame) + r".bmp")
            frame.show()
            print("frame: " + str(frame_number + 1))
            time.sleep(buffer)

    def frame_calculator(frame_number):
        # Calculates the filename shift for ffmpeg exports
        if(len(str(frame_number)) == 1):
            return "00" + str(frame_number)
        elif(len(str(frame_number)) == 2):
            return "0" + str(frame_number)
        else:
            return str(frame_number)

# User control
resources.user_input()