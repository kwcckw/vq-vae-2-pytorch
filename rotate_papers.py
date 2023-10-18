import numpy as np
import cv2
import os
from glob import glob

paper_folder = "./paper/*/*"
paper_paths = glob(paper_folder)

for i, paper_path in enumerate(paper_paths):
    
    print("Processing image "+str(i))
    
    # read image
    image = cv2.imread(paper_path)
    
    # rotate in 3 different angles
    image_r1 = np.rot90(image,1)
    image_r2 = np.rot90(image,2)
    image_r3 = np.rot90(image,3)
    
    # get file name and their extensions
    file_name = os.path.basename(paper_path)
    file_name_ext = file_name.split(".")

    # get the folder path to write new image
    folder_path = os.path.dirname(paper_path)
    
    # write new images to disk
    cv2.imwrite(folder_path+"/"+file_name_ext[0]+"_1."+file_name_ext[1], image_r1)
    cv2.imwrite(folder_path+"/"+file_name_ext[0]+"_2."+file_name_ext[1], image_r2)
    cv2.imwrite(folder_path+"/"+file_name_ext[0]+"_3."+file_name_ext[1], image_r3)
    
 
# remove rotated images
"""
for paper_path in paper_paths:
    
    file_name = os.path.basename(paper_path)
    file_name_ext = file_name.split(".")
    
    n = 0
    for char1 in file_name_ext[0]:
        if char1 == "_":
            n += 1
    
    if n > 1:
        os.remove(paper_path)
"""