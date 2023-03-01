import numpy as np
import matplotlib.pyplot as plt
import scipy.io
from os.path import dirname, join as pjoin

mat = scipy.io.loadmat('././data/raw/PLDM/test_gt/4')

print(mat)