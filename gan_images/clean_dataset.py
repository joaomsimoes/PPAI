import os
import random
import shutil

data_path = './'


count = 0
for path, currentDirectory, files in os.walk(data_path):
    for file in files:
        if path[-1] == '0':
            os.rename(path+'\\'+file, path+f'\\0-{count}.jpg')
            count += 1
        if path[-1] == '1':
            os.rename(path+'\\'+file, path+f'\\1-{count}.jpg')
            count += 1
        if path[-1] == '2':
            os.rename(path+'\\'+file, path+f'\\2-{count}.jpg')
            count += 1
        if path[-1] == '3':
            os.rename(path+'\\'+file, path+f'\\3-{count}.jpg')
            count += 1

all_files = []
for path, currentDirectory, files in os.walk(data_path):
    for file in files:
        if '.jpg' in file:
            all_files.append(path+'/'+file)

train_data = random.sample(all_files, int(len(all_files)*.8))
test_data = list(set(all_files).difference(set(train_data)))

for file in train_data:
    shutil.move(file, './train/'+file[4:])

for file in test_data:
    shutil.move(file, './test/'+file[4:])