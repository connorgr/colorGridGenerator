import json
import gridData

def makeGrids(colors, grouped, numVariants):
  # last color is target
  dimensions = [6, 8, 10, 12, 14]
  lengths = [10, 20, 30, 40, 50]
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
          grid = gridData.makeGrid(grouped, len(colors)-1, d, d)
          # assignTgt(grid, numCols, numRows, quadrant, tgtColor)
          grid = gridData.assignTgt(grid, d, d, q, len(colors)-1)
          gridObj = {'grid': grid, 'length': l, 'setSize': d, 'tgtQuadrant': q, 'variant': n}
          grids.append(gridObj)

  output = {'colors': colors, 'grids': grids, 'lengths': lengths, 'setSizes':dimensions, 'spacing': spacing, 'numVariants': numVariants}
  return output


colors = ['rgb(120,106,24)','rgb(131,71,80)','rgb(23,73,95)','rgb(0,68,43)','rgb(98,63,117)']
outputRand = makeGrids(colors, False, 4)


outputColor1 = ['rgb(120,106,24)','rgb(120,106,24)','rgb(120,106,24)','rgb(120,106,24)','rgb(98,63,117)']
outputYellow = makeGrids(outputColor1, False, 1)

outputColor2 = ['rgb(131,71,80)','rgb(131,71,80)','rgb(131,71,80)','rgb(131,71,80)','rgb(98,63,117)']
outputRed = makeGrids(outputColor2, False, 1)

outputColor3 = ['rgb(23,73,95)','rgb(23,73,95)','rgb(23,73,95)','rgb(23,73,95)','rgb(98,63,117)']
outputBlue = makeGrids(outputColor3, False, 1)

outputColor4 = ['rgb(0,68,43)','rgb(0,68,43)','rgb(0,68,43)','rgb(0,68,43)','rgb(98,63,117)']
outputGreen = makeGrids(outputColor4, False, 1)


colorsGroup1 = ['rgb(120,106,24)','rgb(131,71,80)','rgb(23,73,95)','rgb(0,68,43)','rgb(98,63,117)']
colorsGroup2 = ['rgb(131,71,80)','rgb(120,106,24)','rgb(23,73,95)','rgb(0,68,43)','rgb(98,63,117)']
colorsGroup3 = ['rgb(131,71,80)','rgb(120,106,24)','rgb(0,68,43)','rgb(23,73,95)','rgb(98,63,117)']
colorsGroup4 = ['rgb(120,106,24)','rgb(131,71,80)','rgb(0,68,43)','rgb(23,73,95)','rgb(98,63,117)']
outputGrouped1 = makeGrids(colorsGroup1, True, 1)
outputGrouped2 = makeGrids(colorsGroup2, True, 1)
outputGrouped3 = makeGrids(colorsGroup3, True, 1)
outputGrouped4 = makeGrids(colorsGroup4, True, 1)

with open('data/data.json', 'w') as outfile:
  json.dump(outputRand, outfile)

with open('data/dataYellow.json', 'w') as outfile:
  json.dump(outputYellow, outfile)
with open('data/dataRed.json', 'w') as outfile:
  json.dump(outputRed, outfile)
with open('data/dataBlue.json', 'w') as outfile:
  json.dump(outputBlue, outfile)
with open('data/dataGreen.json', 'w') as outfile:
  json.dump(outputGreen, outfile)

with open('data/dataGrouped1.json', 'w') as outfile:
  json.dump(outputGrouped1, outfile)
with open('data/dataGrouped2.json', 'w') as outfile:
  json.dump(outputGrouped2, outfile)
with open('data/dataGrouped3.json', 'w') as outfile:
  json.dump(outputGrouped3, outfile)
with open('data/dataGrouped4.json', 'w') as outfile:
  json.dump(outputGrouped4, outfile)