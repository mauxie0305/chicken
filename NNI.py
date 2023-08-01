import numpy as np
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import os
import math
from sort import *

def cal_NNI(det, width, height):
    #print(width1, height1)
    det = det.values.tolist()
    area = width*height
    num = len(det)
    nbrs = NearestNeighbors(n_neighbors=2).fit(det)
    dist, index = nbrs.kneighbors(det)
    d_obs = sum(dist)[1]/float(num)
    d_exp = 0.5/math.sqrt(num/float(area))
    NNI = d_obs/d_exp

    return NNI


result_dir = "./yolov7/runs/detect/test2/labels/"
labels_path = np.array([])
for root, dirs, files in os.walk(result_dir):
    for name in files:
        p = os.path.join(root, name)
        labels_path = np.append(labels_path, p)
        
NNI = []
for i in range(len(labels_path)):
    df = pd.read_csv(labels_path[i], delimiter='\s+', header=None, names=['cls', 'center_x_r', 'center_y_r', 'w_r', 'h_r'])
    
    df = df[['center_x_r', 'center_y_r']]
#     df = pd.concat([labels_df, df], ignore_index=True)
    df['center_x_r'] *= 1920
    df['center_y_r'] *= 1080
    df.columns = ['c_x', 'c_y']
    NNI.append(cal_NNI(df, 1920, 1080))
print(NNI)
    
    