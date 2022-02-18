# -*- coding: UTF8 -*-
import os
import shutil
size = 0
scannet_dir = "/home/dongshuwei/3Ddetection/scannet/scans"
ids = os.listdir(scannet_dir)
dir_id = []
file_name = []
dist_dile = "/home/dongshuwei/3Ddetection/scannet_vis"
for id in ids:
    the_dir_id = os.path.join(scannet_dir, id)
    the_file_name = id+"_vh_clean_2.ply"
    the_dir_id = os.path.join(the_dir_id, the_file_name)
    if os.path.isfile(the_dir_id):
        print("the dir the_dir_id: {} is a correct file".format(the_dir_id))
        dir_id.append(the_dir_id)
        size = size + os.path.getsize(the_dir_id)
        dist_file = os.path.join(dist_dile, the_file_name)
        shutil.copyfile(the_dir_id, dist_file)
print(dir_id)
print(size/1024/1024)



