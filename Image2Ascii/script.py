import cv2
import sys
import os
import numpy as np

gscale2 = "@%#*+=-:._" 

image = cv2.imread(os.path.join(sys.path[0],'Mickey.jpg'))

image_grayscale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

length,breadth = image_grayscale.shape

output = np.empty([length,breadth],dtype='S1')

for i in range(length):
    for j in range(breadth):
        output[i][j] = gscale2[int(image_grayscale[i][j]//25.5)-1]


f = open(os.path.join(sys.path[0],'Output1.txt'),'w')

for rows in output:
    for items in rows:
        f.write(str(items)[2:-1])
    f.write('\n')


f.close()