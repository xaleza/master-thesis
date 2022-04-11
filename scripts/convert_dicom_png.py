import os
import numpy as np
import pydicom
from PIL import Image
import numpy as np
from pydicom.pixel_data_handlers.util import apply_voi_lut
import matplotlib.pyplot as plt
#%matplotlib inline
import progressbar
from time import sleep


def get_names_of_imgs_inside_folder(directory):

    names = []

    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext in [".dicom"]:
                names.append(filename)

    return names

def convert(directory):
    im = pydicom.dcmread('../data/no_findings/physionet.org/files/vindr-cxr/1.0.0/train/'+directory, force=True)
    im = im.pixel_array.astype(float)

    rescaled_image = (np.maximum(im,0)/im.max())*255 # float pixels
    final_image = np.uint8(rescaled_image) # integers pixels

    final_image = Image.fromarray(final_image)
    return final_image

def read_xray(path, voi_lut = True, fix_monochrome = True):
    dicom = pydicom.read_file(path)
    
    # VOI LUT (if available by DICOM device) is used to transform raw DICOM data to "human-friendly" view
    if voi_lut:
        data = apply_voi_lut(dicom.pixel_array, dicom)
    else:
        data = dicom.pixel_array
               
    # depending on this value, X-ray may look inverted - fix that:
    if fix_monochrome and dicom.PhotometricInterpretation == "MONOCHROME1":
        data = np.amax(data) - data
        
    data = data - np.min(data)
    data = data / np.max(data)
    data = (data * 255).astype(np.uint8)
        
    return data

names = get_names_of_imgs_inside_folder('../data/no_findings/physionet.org/files/vindr-cxr/1.0.0/train/')

bar = progressbar.ProgressBar(maxval=len(names), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
i = 0

for name in names:
    filename = '../data/no_findings/png/'+name+'.png'
    if not os.path.isfile(filename):
        i+=1
        bar.update(i)
        image = read_xray('../data/no_findings/physionet.org/files/vindr-cxr/1.0.0/train/'+name)
        #image.save('../data/aortic_enlargement/png/'+name+'.png')
        im = Image.fromarray(image)
        im.save('../data/no_findings/png/'+name+'.png')

bar.finish()