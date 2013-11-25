import json
import gridData


# start(grouped, numColors, numCols, numGrids, numRows)
# Returns: {'grids': grids, 'numColors': numColors, 'numColumns': numCols, 'numRows': numRows }

six = gridData.start(False, 4, 6, 4, 6)
eight = gridData.start(False, 4, 8, 4, 8)
ten = gridData.start(False, 4, 10, 4, 10)
twelve = gridData.start(False, 4, 12, 4, 12)
fourteen = gridData.start(False, 4, 14, 4, 14)

jsonSix = json.dumps(six)
jsonEight = json.dumps(eight)
jsonTen = json.dumps(ten)
jsonTwelve = json.dumps(twelve)
jsonFourteen = json.dumps(fourteen)

# last color is target
colors = ['rgb(120,106,24)','rgb(131,71,80)','rgb(23,73,95)','rgb(0,68,43)','rgb(98,63,117)']
lengths = [10, 20, 30, 40, 50]
spacing = 5

data = {'grids': [jsonSix, jsonEight, jsonTen, jsonTwelve, jsonFourteen], 'colors': colors, 'lengths': lengths, 'spacing': spacing}

with open('data/data_6x6.json', 'w') as outfile:
  json.dump(six, outfile)
with open('data/data_8x8.json', 'w') as outfile:
  json.dump(eight, outfile)
with open('data/data_10x10.json', 'w') as outfile:
  json.dump(ten, outfile)
with open('data/data_12x12.json', 'w') as outfile:
  json.dump(twelve, outfile)
with open('data/data_14x14.json', 'w') as outfile:
  json.dump(fourteen, outfile)
with open('data/data.json', 'w') as outfile:
  json.dump(data, outfile)