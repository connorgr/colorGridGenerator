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
        grid = gridData.assignTgt(grid, d, d, q, len(colors))
        gridObj = {'grid': grid, 'length': l, 'setSize': d, 'tgtQuadrant': q, 'variant': n}
        grids.append(gridObj)

output = {'colors': colors, 'grids': grids, 'lengths': lengths, 'setSizes':dimensions, 'spacing': spacing, 'numVariants': numVariants}
with open('data/data.json', 'w') as outfile:
  json.dump(output, outfile)


# start(grouped, numColors, numCols, numGrids, numRows)
# Returns: {'grids': grids, 'numColors': numColors, 'numColumns': numCols, 'numRows': numRows }

# six = [gridData.start(False, 4, 6, 1, 6) for i in range(len(lengths))]
# eight = [gridData.start(False, 4, 8, 0, 8) for i in range(len(lengths))]
# ten = [gridData.start(False, 4, 10, 0, 10) for i in range(len(lengths))]
# twelve = [gridData.start(False, 4, 12, 0, 12) for i in range(len(lengths))]
# fourteen = [gridData.start(False, 4, 14, 0, 14) for i in range(len(lengths))]

# jsonSix = json.dumps(six)
# jsonEight = json.dumps(eight)
# jsonTen = json.dumps(ten)
# jsonTwelve = json.dumps(twelve)
# jsonFourteen = json.dumps(fourteen)


# data = {'gridGroupSetSize': [jsonSix, jsonEight, jsonTen, jsonTwelve, jsonFourteen], 'colors': colors, 'lengths': lengths, 'spacing': spacing}

# with open('data/data_6x6.json', 'w') as outfile:
#   json.dump(six, outfile)
# with open('data/data_8x8.json', 'w') as outfile:
#   json.dump(eight, outfile)
# with open('data/data_10x10.json', 'w') as outfile:
#   json.dump(ten, outfile)
# with open('data/data_12x12.json', 'w') as outfile:
#   json.dump(twelve, outfile)
# with open('data/data_14x14.json', 'w') as outfile:
#   json.dump(fourteen, outfile)
# with open('data/data.json', 'w') as outfile:
#   json.dump(data, outfile)
