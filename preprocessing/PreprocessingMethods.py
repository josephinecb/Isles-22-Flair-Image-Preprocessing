import torch
import numpy as np
import torchvision
from skimage.exposure import rescale_intensity
from skimage.transform import resize


print(torch.cuda.is_available())
print(torch.cuda.device_count())

dev_idx = torch.cuda.current_device()
print(torch.cuda.get_device_name(dev_idx))

device = (
    'cuda'
    if torch.cuda.is_available()  # For Nvidia GPUS
    else 'mps'
    if torch.backends.mps.is_available()  # For AMD GPUs
    else 'cpu'  # If no GPU
)
print('Using {} device'.format(device))



# def dataLoader(path){ dataset = Dataset(images_dir=path)}

# def rotate(self, image){}


