import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import os 

dir = '././data/raw/PLDM/test_gt/'

for file in os.listdir(dir):
    f = os.path.join(dir, file)
    if os.path.isfile(f):
        mat = scipy.io.loadmat(f)

# Not finished yet
# TODO: Save the plot to file in interim folder with a fixed size of 540x360 or 360x540
# Look into saving in a single fixed format to avoid problems down the line. Ask TA/Teacher