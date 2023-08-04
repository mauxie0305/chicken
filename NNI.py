import numpy as np
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import os
import math
import csv

def cal_NNI(det, width, height):
    #print(width1, height1)
    NNI = 0
    det = det.values.tolist()
    area = width*height
    num = len(det)
    if num < 2:
        print("error")
    else:
        nbrs = NearestNeighbors(n_neighbors=2).fit(det)
        dist, index = nbrs.kneighbors(det)
        d_obs = sum(dist)[1]/float(num)
        d_exp = 0.5/math.sqrt(num/float(area))
        NNI = d_obs/d_exp

    return NNI

width = 1920
height = 1080
folder = "bbox_7120_230512_230614"
result_dir = f'../AgroONE/{folder}/bbox/'
labels_path = np.array([])
for root, dirs, files in os.walk(result_dir):
    for name in files:
        p = os.path.join(root, name)
        labels_path = np.append(labels_path, p)

NNI = []
file_name = []
for i in range(len(labels_path)):
    basename = os.path.splitext(os.path.basename(labels_path[i]))[0]
    df = pd.read_csv(labels_path[i], delimiter='\s+', header=None, names=['center_x_r', 'center_y_r', 'w_r', 'h_r'])
    
    df = df[['center_x_r', 'center_y_r']]
#     df = pd.concat([labels_df, df], ignore_index=True)
    # df['center_x_r'] *= width
    # df['center_y_r'] *= height
    df.columns = ['c_x', 'c_y']
    nni = cal_NNI(df, width, height)
    if nni == 0:
        continue
    file_name.append(basename)
    NNI.append(nni)
    

min_NNI = min(NNI)
max_NNI = max(NNI)

print(f'max = {max_NNI}, min = {min_NNI}')
# Test
# df = pd.read_csv(labels_path[0], delimiter='\s+', header=None, names=['center_x_r', 'center_y_r', 'w_r', 'h_r'])
# df = df[['center_x_r', 'center_y_r']]
# #     df = pd.concat([labels_df, df], ignore_index=True)
# # df['center_x_r'] *= width
# # df['center_y_r'] *= height
# df.columns = ['c_x', 'c_y']
# NNI.append(cal_NNI(df, width, height))

# print(NNI[0:5])

output_file = 'NNI.csv'
    
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['file name', 'NNI'])
    writer.writerows(zip(file_name, NNI)) 