# Takes in two grids directories and unions them.
import os
import sys

if len(sys.argv) != 3:
  print 'Proper input: python doubleGrids <<grids1Dir>> <<grids2Dir>'
  sys.exit()

cwd = os.getcwd()
gridDirs = [cwd + '/' + sys.argv[1], cwd + '/' + sys.argv[2]]

outDir = cwd + '/doubleGrids/'

if not os.path.exists(outDir):
  os.makedirs(outDir)

print 'Lengths of directories that are being merged:'

numGridsFirst = 0
numGridsSecond = 0
names = []
for f in os.listdir(gridDirs[0]):
  if '.svg' not in f: continue
  os.rename(gridDirs[0] + f, outDir + f)
  numGridsFirst = numGridsFirst + 1
  names.append(f)

for f in os.listdir(gridDirs[1]):
  if '.svg' not in f: continue
  tkns = f.split('_')
  variant = int(tkns[-1].replace('.svg', '')) + 4
  newTkn = str(variant) + '.svg'
  newName = f.replace(tkns[-1], newTkn)
  os.rename(gridDirs[1] + f, outDir + newName)
  print outDir + newName
  numGridsSecond = numGridsSecond + 1
  if newName in names:
    print 'error:', newName

print 'Lengths of directories that are being merged:'
print numGridsFirst, numGridsSecond
print 'Out directory: ' + outDir
print 'In directories: ' + gridDirs[0] + ', ' + gridDirs[1]
print 'Num files in outdir: ' + str(len(os.listdir(outDir)))
print '----'