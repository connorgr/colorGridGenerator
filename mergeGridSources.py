import os
################################################################################
# DIRECTORY NAMES

# Random grids
gridsRand = 'gridsRand'

# Grouped grids
gridsG1 = 'gridsG1'
gridsG2 = 'gridsG2'
gridsG3 = 'gridsG3'
gridsG4 = 'gridsG4'

# Single color grids
gridsBlue = 'gridsBlue'
gridsGreen = 'gridsGreen'
gridsRed = 'gridsRed'
gridsYellow = 'gridsYellow'

dirs = [gridsRand, gridsG1, gridsG2, gridsG3, gridsG4, gridsBlue, gridsGreen,\
    gridsRed, gridsYellow]

################################################################################
# SCRIPT

if not os.path.exists('grids'):
  os.makedirs('grids')

for d in dirs:
  files = os.listdir(d + '/')
  for f in files:
    if '.svg' not in f: continue
    newName = f.replace('grid_', '')
    os.rename(d + '/' + f, 'grids/' + d + '_' + newName)
