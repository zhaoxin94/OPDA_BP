"""Modified by zhao xin. This implementation is more efficient \
    than the original one"""

import os

# replace visda_path to your own path
visda_path = '/home/zhao/data/DA/visda17'

# set visda training path
p_path = os.path.join(visda_path, 'train')
dir_list = os.listdir(p_path)
print(dir_list)

class_list = ["bicycle", "bus", "car", "motorcycle", "train", "truck", "unk"]
path_source = "./source_list.txt"
path_target = "./target_list.txt"
write_source = open(path_source, "w")
write_target = open(path_target, "w")

# write source items to source_list.txt
for k, direc in enumerate(dir_list):
    if '.txt' not in direc and direc in class_list:
        files = os.listdir(os.path.join(p_path, direc))
        for i, file in enumerate(files):
            class_name = direc
            file_name = os.path.join(p_path, direc, file)
            write_source.write('%s %s\n' %
                               (file_name, class_list.index(class_name)))

# set visda validation path
p_path = os.path.join(visda_path, 'validation')
dir_list = os.listdir(p_path)
print(dir_list)

# write target items to target_list.txt
for direc in dir_list:
    if '.txt' not in direc:
        if direc in class_list:
            class_name = direc
        else:
            class_name = "unk"
        files = os.listdir(os.path.join(p_path, direc))
        for i, file in enumerate(files):
            file_name = os.path.join(p_path, direc, file)
            write_target.write('%s %s\n' %
                               (file_name, class_list.index(class_name)))
