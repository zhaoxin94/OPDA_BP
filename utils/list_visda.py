"""This original implementation is not efficient. Deprecated"""

import os

# replace visda_path to your own path
visda_path = '/home/zhao/data/DA/visda17'

p_path = os.path.join(visda_path, 'train')
dir_list = os.listdir(p_path)
print(dir_list)

class_list = ["bicycle", "bus", "car", "motorcycle", "train", "truck", "unk"]
path_source = "./source_list_pre.txt"
path_target = "./target_list_pre.txt"
write_source = open(path_source, "w")
write_target = open(path_target, "w")
for k, direc in enumerate(dir_list):
    if '.txt' not in direc:
        files = os.listdir(os.path.join(p_path, direc))
        for i, file in enumerate(files):
            if direc in class_list:
                class_name = direc
                file_name = os.path.join(p_path, direc, file)
                write_source.write('%s %s\n' %
                                   (file_name, class_list.index(class_name)))
            else:
                continue
p_path = os.path.join(visda_path, 'validation')
dir_list = os.listdir(p_path)
print(dir_list)
for k, direc in enumerate(dir_list):
    if '.txt' not in direc:
        files = os.listdir(os.path.join(p_path, direc))
        for i, file in enumerate(files):
            if direc in class_list:
                class_name = direc
            else:
                class_name = "unk"
            file_name = os.path.join(p_path, direc, file)
            write_target.write('%s %s\n' %
                               (file_name, class_list.index(class_name)))
