import random
import cv2
import numpy as np

def generate(img,length,breadth):
    centre_x = random.randint(0,length)
    centre_y = random.randint(0,breadth)
    red_ = random.randint(0,255)
    green_ = random.randint(0,255)
    blue_ = random.randint(0,255)
    major_axis = random.randint(0,length/3)
    minor_axis = random.randint(0,breadth/3)
    cv2.ellipse(img,(centre_x,centre_y),(major_axis,minor_axis),0,0,360,(red_,green_,blue_),-1)

def main():
    length = int(input("Enter the breadth of the image: "))
    breadth = int(input("Enter the height of the image: "))
    img = np.zeros((length, breadth, 3), dtype = "uint8")

    for i in range(0,500):
        generate(img,600,600)

    cv2.imshow('dark',img)

    cv2.waitKey(0) 
    cv2.destroyAllWindows() 

main()