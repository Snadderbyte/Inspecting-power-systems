import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import os 

dir = '././data/raw/PLDM/test_gt/'
outDir = './data/interim/PLDM/labeled/'

# fig = plt.figure(frameon=False, dpi=100, figsize=(3.6, 5.4))
# fig.figimage(sub_array5, cmap='binary', xo=0, yo=0)
# plt.savefig('testfile.png')

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

convert_data(dir, outDir, 'groundTruth')
# Not finished yet
# TODO: Save the plot to file in interim folder with a fixed size of 540x360 or 360x540
# Look into saving in a single fixed format to avoid problems down the line. Ask TA/Teacher