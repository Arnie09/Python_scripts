import random
import cv2
import numpy as np

def generate(img,length,breadth):

    '''for generating semi-transaparent rectangles'''
    overlay = img.copy()
    output = img.copy()

    '''generating x and y coordinates of the centre of the ellipse'''
    centre_x = random.randint(0,length)
    centre_y = random.randint(0,breadth)

    '''generating RGB values'''
    red_ = random.randint(0,255)
    green_ = random.randint(0,255)
    blue_ = random.randint(0,255)

    '''generating the size of the ellipse'''
    major_axis = random.randint(0,length//3)
    minor_axis = random.randint(0,breadth//3)

    angle = random.randint(0,360)

    '''drawing the ellipse'''
    cv2.ellipse(overlay,(centre_x,centre_y),(major_axis,minor_axis),angle,0,360,(red_,green_,blue_),-1)
    
    '''applying transaprency to the drawn ellipse'''
    cv2.addWeighted(overlay,0.5,output,0.5,0,img)

def main():
    '''input from the user of length and breadth of the image'''
    length = int(input("Enter the breadth of the image: "))
    breadth = int(input("Enter the height of the image: "))

    '''creating an emoty image'''
    img = np.zeros((length, breadth, 3), dtype = "uint8")

    '''creating 500 ellipses in the canvas'''
    for i in range(0,500):
        generate(img,length,breadth)

    '''displaying the image'''
    cv2.imshow('light',img)
    
    '''waiting for the image to be displayed'''
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 

main()
