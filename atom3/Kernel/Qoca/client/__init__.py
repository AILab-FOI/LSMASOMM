import os

cwd = os.path.split(__file__)[0]
fileList = os.listdir(cwd)
for file in fileList:
  if(os.path.splitext(file)[1] == '.jar'):
    QOCAPATH = os.path.join(cwd, file)
    break
