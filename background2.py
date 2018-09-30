import numpy as np
from PIL import Image
import math

def distance(x1, y1, x2, y2):

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

numRings = 50
    
imgMat = np.zeros((1080,1080,3))
    
for x in range(1080):

    print(x)
    
    for y in range(1080):
    
            sizeValue = distance(x,y, 540, 540)
            sizeValue = sizeValue / 540
            
            angle = math.atan2(540 - y, 540 - x)
            
            for i in range(numRings):
            
                rot1 = (sizeValue*(numRings-i)+(1-sizeValue)*(i))* angle
                rot2 = (sizeValue*(i)+(1-sizeValue)*(numRings-i))* angle
                
                imgMat[x,y,0] = imgMat[x,y,0] + 5.1 * math.fabs(math.sin(rot2))* math.fabs(math.sin(rot1))

                imgMat[x,y,1] = imgMat[x,y,1] + 5.1 * math.fabs(math.sin(rot2))* math.fabs(math.cos(rot1))
                
                imgMat[x,y,2] = imgMat[x,y,2] + 5.1 * math.fabs(math.cos(rot2))
                
image = Image.fromarray(imgMat.astype('uint8'), 'RGB')

image.save('spiralBackground.png')