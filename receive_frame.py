#!/usr/bin/env python
'''
Writes out data received from websocketd on stdin as 
png frames.
'''

import time
import base64
import binascii
from sys import stdin, stdout
import StringIO
import os
import numpy as np



# From http://stackoverflow.com/a/9807138
def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'='* missing_padding
    return base64.decodestring(data)

def main():
    '''
    As each frame is received write it to a .png file
    '''

    frames = 0

    imageMat = np.zeros((810,810))

    while True:

        received_val = stdin.readline()
		
        #number = received_val[:6]
		
        #print number
		
        #received_val = received_val[6:]
        # Right pad filenames so they can be sorted
        filename =  "frames/%s.txt" % frames #+ 
		
		
        temp = StringIO.StringIO()
        
        old_file_position = temp.tell()
        #img.save(temp, format="png") #"data/measure.png")
        
        try:
                temp.write(decode_base64(received_val))
                frames += 1
                if frames % 10 == 0:
                    print("Captured %d frames ..." % frames)
                    stdout.flush()
        except binascii.Error:
                # Ignore malformed data urls
                continue
				
        temp.seek(0,os.SEEK_END)
		
        
        #statinfo = os.stat('data/measure.png')
        #number = int(statinfo.st_size[:-1])
        data = int(temp.tell())
		
        x = frames%810
        y = frames/810
		
        if(frames % 20000 == 0):
            np.save('pixels%s.npy' % frames, imageMat)
			
            imageMat[x,y] = int(data)
		
		
        #with open(filename, 'wb') as file_handle:
		#	file_handle.write("%s" % data)
            
if __name__ == '__main__':
    main()