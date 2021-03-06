#!/usr/bin/python
from sys import stdin
from collections import Counter
from random import choice
import argparse
import itertools
import json
import random
import sys
import copy


def assignTgt(grid, numCols, numRows, quadrant, tgtColor):
  index = 0
  if quadrant == 'tl':
    tlRow = random.randint(1, numRows/2 - 2)
    tlCol = random.randint(1, numCols/2 - 2)
    index = tlRow*numCols + tlCol # row major index
  elif quadrant == 'tr':
    trRow = random.randint(1, numRows/2 - 2)
    trCol = random.randint(numCols/2 + 1, numCols - 2)
    index = trRow*numCols + trCol
  elif quadrant == 'br':
    brRow = random.randint(numRows/2 + 1, numRows - 2)
    brCol = random.randint(numCols/2 + 1, numCols - 2)
    index = brRow*numCols + brCol
  elif quadrant == 'bl':
    blRow = random.randint(numRows/2 + 1, numRows - 2)
    blCol = random.randint(1, numCols/2 - 2)
    index = blRow*numCols + blCol
  else:
    raise 'Invalid quadrant given. Options = tl, tr, br, bl'

  grid[index]['color'] = tgtColor
  return grid


# Returns a grid (list of {'color': INT, 'id': INT})
def makeGrid(grouped, numColors, numCols, numRows):
  if grouped == True:
    grid = orderedGrid(numColors, numCols, numRows)
    return grid
  else:
    grid = randomGrid(numColors, numCols, numRows)
    return grid

# Returns an ordered grid (list of {'color': INT, 'id': INT})
def orderedGrid(numColors, numCols, numRows):
  numElems = numRows * numCols
  grid = [None for i in range(numElems)]

  for i in range(len(grid)):
    color = -1
    if i/numRows < numRows/2:
      if i%numCols < numCols/2:
        color = 0# ul
      else:
        color = 1# ur
    else:
      if i%numCols < numCols/2:
        color = 2# ll
      else:
        color = 3# lr
    # we assign each grid cell an object with both color and an id to make each
    # element unique. Matter of convenience for javascript's .indexOf() w/ d3
    grid[i] = {'color': color, 'id': i}

  return grid

# Returns a randomly colored grid (list of {'color': INT, 'id': INT})
def randomGrid(numColors, numCols, numRows):
  def getRandomIndex(distribution, numColors):
    found = False
    while not found:
      i = random.randint(0, numColors-1)
      if distribution[i] > 0:
        return i

  numElems = numRows * numCols
  maxColors = numElems/numColors

  # color distribution counter
  colorDist = [maxColors for i in range(0,numColors)]
  colorsLeft = numElems%numColors

  # Randomly assign the number of color instances yet to be assigned to squares
  for i in range(0,colorsLeft):
    indexFound = False
    while not indexFound:
      index = random.randint(0, numColors-1)
      if colorDist[index] == maxColors:
        indexFound = True
    colorDist[index] = colorDist[index] + 1

  grid = [None for i in range(numElems)]

  for i in range(len(grid)):
    color = getRandomIndex(colorDist, numColors)
    # we assign each grid cell an object with both color and an id to make each
    # element unique. Matter of convenience for javascript's .indexOf() w/ d3
    grid[i] = {'color': color, 'id': i}
    colorDist[color] = colorDist[color] - 1

  return grid

# Generate grids
def start(grouped, numColors, numCols, numGrids, numRows):
  # Make grids, where each grid is a list of {'color':INT, 'id': INT}
  grids = [makeGrid(grouped, numColors, numCols, numRows) for i in range(numGrids)]

  # Remove any duplicates that might have arisen
  grids.sort()
  grids = list(grids for grids,_ in itertools.groupby(grids))

  # Create four target variants for each original grid, with a target for each
  #   quadrant in a given grid.
  grids = [variantGrids(grid, numColors, numCols, numRows) for grid in grids]

  # Each grid with targets in grids now has the following:
  # {'grid': list of {'color': INT, 'id': INT},
  #  'target': Boolean,
  #  'targetLoc': INT,
  #  'quadrant':String}  tl, tr, bl, br
  #
  # OR for a grid without targets
  #
  # {'grid': list of {'color': INT, 'id': INT},
  #  'target': Boolean}

  return {'listOfGridVariants': grids, 'numColors': numColors, 'numColumns':
      numCols, 'numRows': numRows }


def variantGrids(grid, numColors, numCols, numRows):
  # randInt is inclusive, hence generator weirdness
  def pickQuadrantTgts(numCols, numRows):
    # Pick upper left quadrant
    ulRow = random.randint(1, numRows/2 - 2)
    ulCol = random.randint(1, numCols/2 - 2)
    ul = ulRow*numCols + ulCol # row major index
    ulObj = {'index': ul,'quadrant':'tl'}
    # Pick upper right quadrant
    urRow = random.randint(1, numRows/2 - 2)
    urCol = random.randint(numCols/2 + 1, numCols - 2)
    ur = urRow*numCols + urCol
    urObj = {'index': ur,'quadrant':'tr'}
    # Pick lower right quadrant
    lrRow = random.randint(numRows/2 + 1, numRows - 2)
    lrCol = random.randint(numCols/2 + 1, numCols - 2)
    lr = lrRow*numCols + lrCol
    lrObj = {'index': lr,'quadrant':'br'}
    # Pick lower left quadrant
    llRow = random.randint(numRows/2 + 1, numRows - 2)
    llCol = random.randint(1, numCols/2 - 2)
    ll = llRow*numCols + llCol
    llObj = {'index': ll,'quadrant':'bl'}

    return [ulObj,urObj,lrObj,llObj]


  # Check if tgts can exist in all quadrants (targets need 1 cell edge buffer)
  if numCols < 5 or numRows < 5:
    raise 'Error: no target selection possible'

  tgts = pickQuadrantTgts(numCols, numRows)

  # Prepare a new object to contain the original grid and target variants
  newGrids = [{'grid': grid, 'target': False}]

  # Add the target grid variants to the return object
  targetColor = numColors # the last color will always be the color number
  for tgt in tgts:
    tmpGrid = copy.deepcopy(grid)
    tmpGrid[tgt['index']]['color'] = targetColor
    newGrids.append({'grid': tmpGrid, 'target': True, 'targetLoc':\
        tgt['index'], 'quadrant':tgt['quadrant']})

  return newGrids


def main(argv):
  pixelParser = argparse.ArgumentParser(description='Create a color grid!')
  pixelParser.add_argument('--grouped', type=bool, help='a bool if the colors should be grouped')
  pixelParser.add_argument('--numcolors', type=int, help='an integer for # of colors')
  pixelParser.add_argument('--numsquares', type=int, help='an integer (or two) for # of squares; 1 arg = per side (square), 2 args = rect (h,w)', nargs='+')
  pixelParser.add_argument('--numgrids', type=int, help='an integer for # of grids to make')

  args = pixelParser.parse_args()

  grouped = False
  if args.grouped:
    grouped = args.grouped

  numColors = 1
  if args.numcolors:
    numColors = args.numcolors

  numGrids = 1
  if args.numgrids:
    numGrids = args.numgrids

  numRows = 1
  numCols = 1
  if args.numsquares:
    if len(args.numsquares) == 1:
      numRows = args.numsquares[0]
      numCols = args.numsquares[0]
    else:
      numRows = args.numsquares[0]
      numCols = args.numsquares[1]

  spacing = 5 # constant for now

  results = start(grouped, numColors, numCols, numGrids, numRows)
  print json.dumps(results, sort_keys=True)


if __name__ == "__main__":
  main(sys.argv)