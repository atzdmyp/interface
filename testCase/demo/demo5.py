import zipfile
import glob


files = glob.glob('F:\study\python\python\*')
f = zipfile.ZipFile('../result/test.zip', 'w', zipfile.ZIP_DEFLATED)
for file in files:
    f.write(file)
f.close()
