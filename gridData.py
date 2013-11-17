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


def makeGrid(grouped, numColors, numCols, numRows):
  if grouped == True:
    return orderedGrid(numColors, numCols, numRows)
  else:
    return randomGrid(numColors, numCols, numRows)


def orderedGrid(numColors, numCols, numRows):
  return None


def variantGrids(grid, numColors, numCols, numRows):
  # Determines if the cell index is a valid target (i.e., not an edge cell for
  #   each quadrant of the color grid)
  def isTgtCandidate(cellId):
    colIndex = cellId % numCols
    rowIndex = cellId / numRows
    # check frame edges
    if colIndex == 0 or colIndex == numCols-1 or rowIndex == 0 or rowIndex ==\
        numRows-1:
      return False
    # check quadrant edges
    if colIndex == numCols/2-1 or colIndex == numCols/2 or rowIndex ==\
        numRows/2-1 or rowIndex == numRows/2:
      return False
    return True

  # we need to find locations that have 1 - numColors neighboring colors, then
  #   add a target in a randomly selected location in the set of possibilities
  colorSets = dict()
  for cell in grid:
    valid = isTgtCandidate(cell['id'])
    if valid:
      nc = cell['numColors']
      if nc in colorSets:
        colorSets[nc].append(cell['id'])
      else:
        colorSets[nc] = [cell['id']]

  # Randomly select a cell location for each numColor set
  # Construct a list of grids with targets as well as original stimuli without
  newGrids = [{'grid': grid, 'target': False}]

  # numColors can be used as shorthand for color scale index for target color
  targetColor = numColors

  # Remove the edges from variant consideration
  # colorSets.pop(None)

  # Populate newGrids with randomly selected locations for targets, such that
  #   there exists one target per number of adjacent dell color categories
  for k,v in colorSets.iteritems():
    tmpGrid = copy.deepcopy(grid)
    randIndex = choice(v)

    tmpGrid[randIndex]['color'] = targetColor
    numAdjColors = tmpGrid[randIndex]['numColors']
    newGrids.append({'adjColors': numAdjColors, 'grid': tmpGrid, 'target':
        True, 'targetLoc': randIndex})

  return newGrids


def randomGrid(numColors, numCols, numRows):
  def calcNeighborColors(cell, grid, numRows, numCols):
    i = cell['id']
    colIndex = i % numCols
    rowIndex = i / numRows

    neighbors = []

    # left and right neighbors
    if not colIndex == 0: # if cell column isn't left-most
      neighbors.append(grid[i-1])
    if not colIndex == numCols - 1: # if cell isn't right-most
      neighbors.append(grid[i+1])

    # top and bottom neighbors
    if not rowIndex == 0: # if row isn't top-most
      neighbors.append(grid[i - numCols]) # get above neighbor
    if not rowIndex == numRows - 1: #if cell isn't bottom-most
      neighbors.append(grid[i + numCols])

    # diagonal neighbors
    if not rowIndex == 0:
      if not colIndex == 0:
        neighbors.append(grid[i - numCols - 1])
      if not colIndex == numCols - 1:
        neighbors.append(grid[i - numCols + 1])
    if not rowIndex == numRows - 1:
      if not colIndex == 0:
        neighbors.append(grid[i + numCols - 1])
      if not colIndex == numCols - 1:
        neighbors.append(grid[i + numCols + 1])

    colors = [c['color'] for c in neighbors]
    colorCounts = Counter(colors)
    numColors = len(colorCounts)

    # Make all edge cells have numColors = None to make them invalid, but still
    #   add neighbors just in case we want that information in the future
    if not colIndex == 0 and not colIndex == numCols - 1 and not rowIndex == 0 \
        and not rowIndex == numRows - 1:
      cell['numColors'] = numColors
      cell['neighbors'] = [c['id'] for c in neighbors]
    else:
      cell['numColors'] = None
      cell['neighbors'] = [c['id'] for c in neighbors]

    return cell

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

  grid = [calcNeighborColors(cell, grid, numRows, numCols) for cell in grid]

  return grid


def start(grouped, numColors, numCols, numGrids, numRows):
  grids = [makeGrid(grouped, numColors, numCols, numRows) for i in range(numGrids)]

  # Get rid of duplicate grids
  grids.sort()
  grids = list(grids for grids,_ in itertools.groupby(grids))
  grids = [variantGrids(grid, numColors, numCols, numRows) for grid in grids]

  return {'grids': grids, 'numColors': numColors, 'numColumns':
      numCols, 'numRows': numRows }


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