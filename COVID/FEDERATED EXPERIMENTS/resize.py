import PIL
from PIL import Image
import os, sys

path = "TrainSet/"
dirs = os.listdir( path )

# new folder path
path_resized = 'Resized_Trainset' #the path where to save resized images

# create new folder
if not os.path.exists(path_resized):
    os.makedirs(path_resized)

# new folder path
test_path_resized = 'Resized_Testset' #the path where to save resized images

# create new folder
if not os.path.exists(test_path_resized):
    os.makedirs(test_path_resized)

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = PIL.Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((256,256), Image.ANTIALIAS)
            imResize.save('{}{}{}'.format(path_resized,'/',os.path.split(item)[1]))
resize()
path = "TestSet/"
dirs = os.listdir( path )
path_resized = test_path_resized
resize()

