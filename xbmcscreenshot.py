#!/usr/bin/python
from optparse import OptionParser
import subprocess
import os

parser = OptionParser()

parser.add_option("-i", "--input", action="store", dest="input")
parser.add_option("-o", "--output", action="store", dest="output")
parser.add_option("-n", "--screens", action="store", type="int", dest="number")

(options, args) = parser.parse_args();

input_file = options.input
output_directory = options.output
number = options.number

getlength = "midentify \"" + str(input_file) + "\" | grep ID_LENGTH"

child = subprocess.Popen(getlength, shell=True, stdout=subprocess.PIPE)

out, err = child.communicate()

duration=float(out.strip().split('=')[-1])

if number != None:
    screenshots = range(0, int(duration), int(duration / number))
else:
    screenshots = range(0, int(duration), int(duration / 5))

for dur in screenshots:
    genscreen = ["mplayer", input_file, "-frames", "1", "-vo", "png", "-nosound", "-ss", str(dur)]
    subprocess.call(genscreen);
    
    if os.path.isfile('00000001.png'):
        try:
            with open('00000001.png') as f: pass
        except IOError as e:
            print("");
        
        os.rename(f.name, input_file + "_" + str(dur) + ".png")
            
        


