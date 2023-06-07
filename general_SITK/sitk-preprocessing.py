import os
import numpy
import SimpleITK as sitk
import matplotlib.pyplot as plt
%matplotlib inline

def sitk_show(img, title=None, margin=0.05, dpi=40 ):
    nda = SimpleITK.GetArrayFromImage(img)
    spacing = img.GetSpacing()
    figsize = (1 + margin) * nda.shape[0] / dpi, (1 + margin) * nda.shape[1] / dpi
    extent = (0, nda.shape[1]*spacing[1], nda.shape[0]*spacing[0], 0)
    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_axes([margin, margin, 1 - 2*margin, 1 - 2*margin])

    plt.set_cmap("gray")
    ax.imshow(nda,extent=extent,interpolation=None)
    
    if title:
        plt.title(title)
    
    plt.show()

def readImage3d(path):
    reader = sitk.ImageFileReader()
    reader.SetImageIO("NiftiImageIO")
    reader.SetFileName(path)
    image = reader.Execute()
    return image


def getSlice(image3d, slice=len(image3d)/2):
    return(image3d[:,:,slice])


path = 'data/interrsect_005.nii.gz'
image_1_path = '/home/jbregazzi/Documents/josephine/GitHub/Brain-Scan-Example-Data/Interrsect/mini-dataset/INTERRSeCT01-019_FollowUp.nii.gz'

reader = sitk.ImageFileReader()
reader.SetImageIO("NiftiImageIO")
reader.SetFileName(image_1_path)
image = reader.Execute()

idxSlice = 24

# int labels to assign to the segmented white and gray matter.
labelWhiteMatter = 1
labelGrayMatter = 2



