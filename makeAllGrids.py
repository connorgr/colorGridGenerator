import json
import gridData

# last color is target
colors = ['rgb(120,106,24)','rgb(131,71,80)','rgb(23,73,95)','rgb(0,68,43)','rgb(98,63,117)']
dimensions = [6, 8, 10, 12, 14]
lengths = [10, 20, 30, 40, 50]
numVariants = 4
quadrants = ['tl', 'tr', 'br', 'bl']
spacing = 5

# makeGrid(grouped, numColors, numCols, numRows):
grid = gridData.makeGrid(False, 4, 6, 6)
grid = gridData.assignTgt(grid, 6, 6, 'tl', 4)

grids = []
for n in range(numVariants):
  for d in dimensions:
    for l in lengths:
      for q in quadrants:
        # makeGrid(grouped, numBaseColors, numCols, numRows)
        grid = gridData.makeGrid(False, len(colors)-1, d, d)
        # assignTgt(grid, numCols, numRows, quadrant, tgtColor)
        grid = gridData.assignTgt(grid, d, d, q, len(colors)-1)
        gridObj = {'grid': grid, 'length': l, 'setSize': d, 'tgtQuadrant': q, 'variant': n}
        grids.append(gridObj)

output = {'colors': colors, 'grids': grids, 'lengths': lengths, 'setSizes':dimensions, 'spacing': spacing, 'numVariants': numVariants}
with open('data/data.json', 'w') as outfile:
  json.dump(output, outfile)
