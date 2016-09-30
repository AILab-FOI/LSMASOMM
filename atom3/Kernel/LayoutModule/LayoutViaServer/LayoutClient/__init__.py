import os

cwd = os.path.split(__file__)[0]
fileList = os.listdir(cwd)
for file in fileList:
  if(os.path.splitext(file)[0] == 'LayoutServerProject'):
    SERVER_PATH = os.path.join(cwd, file)
    break
