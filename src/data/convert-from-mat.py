import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import os 

dir = '././data/raw/PLDM/test_gt/'
outDir = './data/interim/PLDM/labeled/'

def convert_data(indir = '', outdir = '', key = ''):
    for file in os.listdir(indir):
        if file != '.DS_Store':
            print('Working on file: ' + file)
            f_path = os.path.join(indir, file)
            mat = scipy.io.loadmat(f_path)
            arr = mat[key]
            arr = arr[0][0][0][0][0]
            fig = plt.figure(frameon=False, dpi=100, figsize=(3.6, 5.4))
            fig.figimage(arr, cmap='binary', xo=0, yo=0)
            plt.savefig(outDir + file.removesuffix('.mat') + '.jpg')