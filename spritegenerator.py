import os 
import sys 
file_location = input("enter the file location: ")
abc=("magick montage *.png -tile 4x2 -geometry 128x128+0+0 -background transparent  function.png".format(file_location))
os.system('{}'.format(abc))
print("file genreated and saved successfully")