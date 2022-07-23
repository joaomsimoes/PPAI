import os

data_path = './Dataset/'


count = 0
for path, currentDirectory, files in os.walk(data_path):
    for file in files:
        if path.split('\\')[-1] == 'NonDemented':
            os.rename(path+'\\'+file, path+f'\\0-{count}.jpg')
            count += 1
        if path.split('\\')[-1] == 'VeryMildDemented':
            os.rename(path+'\\'+file, path+f'\\1-{count}.jpg')
            count += 1
        if path.split('\\')[-1] == 'MildDemented':
            os.rename(path+'\\'+file, path+f'\\2-{count}.jpg')
            count += 1
        if path.split('\\')[-1] == 'ModerateDemented':
            os.rename(path+'\\'+file, path+f'\\3-{count}.jpg')
            count += 1
