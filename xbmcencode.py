#!/usr/bin/python
from optparse import OptionParser
import subprocess

parser = OptionParser()

parser.add_option("-i", "--input", action="store", dest="input")
parser.add_option("-o", "--output", action="store", dest="output")
parser.add_option("-q", "--crf", action="store", type="int", dest="quality")
parser.add_option("-s", "--size", action="store", dest="size")
parser.add_option("-a", "--audiotrack", action="store", dest="atrack")

(options, args) = parser.parse_args();

print "input:\t" + options.input
print "output:\t" + options.output
print "qual:\t" + str(options.quality)
print "size:\t" + str(options.size)
print "audio:\t" + str(options.atrack)

input_file = options.input
output_file = options.output

if (options.quality != None):
    quality = str(options.quality)
else: # Default quality
    quality = "16"

# Default size
size_x = 1920
size_y = 1080

# Default anamporphic
anamorphic = "--strict-anamorphic"

# Parse size
if (options.size == "720p"):
    size_x = 1280
    size_y = 720
    anamorphic = "--loose-anamorphic"
elif (options.size == "1080p"):
    size_x = 1920
    size_y = 1080
elif (options.size != None):
    size_x = options.size.split('x')[0]
    size_y = options.size.split('x')[1]

args = ["HandBrakeCLI", "-i", input_file, "-o", output_file, "-e", "x264", "-q", quality, "-a", str(options.atrack), "-E", "copy", "-x", "level=4.1:ref=4", "-X", str(size_x), "-Y", str(size_y), str(anamorphic), "-N", "eng"]

subprocess.call(args)


