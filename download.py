import torch
import torchvision
import torch.nn as nn
import torchvision.transforms as transforms
import SimpleITK as sitk
import skimage.io as io
import numpy as np
from skimage.color import rgb2gray
from skimage.filters import sobel

image = io.imread("sub-strokecase0002_ses-0001_flair.nii")

print(type(image))