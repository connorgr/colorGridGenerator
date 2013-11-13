import json
import makeGridJsons


# start(grouped, numColors, numCols, numGrids, numRows)
# Returns: {'grids': grids, 'numColors': numColors, 'numColumns': numCols, 'numRows': numRows }

six = makeGridJsons.start(False, 4, 6, 1, 6)
eight = makeGridJsons.start(False, 4, 8, 1, 8)
ten = makeGridJsons.start(False, 4, 10, 1, 10)
fourteen = makeGridJsons.start(False, 4, 14, 1, 14)
eighteen = makeGridJsons.start(False, 4, 12, 1, 12)

jsonSix = json.dumps(six)
jsonEight = json.dumps(eight)
jsonTen = json.dumps(ten)
jsonFourteen = json.dumps(fourteen)
jsonEighteen = json.dumps(eighteen)

# last color is target
colors = ['rgb(124,110,16)','rgb(138,70,74)','rgb(24,75,86)','rgb(27,64,41)','rgb(100,60,126)']
lengths = [10, 20, 30, 40, 50]
spacing = 5

data = {'grids': [jsonSix, jsonEight, jsonTen, jsonFourteen, jsonEighteen], 'colors': colors, 'lengths': lengths, 'spacing': spacing}

with open('data/data_6x6.json', 'w') as outfile:
  json.dump(six, outfile)
with open('data/data_8x8.json', 'w') as outfile:
  json.dump(eight, outfile)
with open('data/data_10x10.json', 'w') as outfile:
  json.dump(ten, outfile)
with open('data/data_14x14.json', 'w') as outfile:
  json.dump(fourteen, outfile)
with open('data/data_18x18.json', 'w') as outfile:
  json.dump(eighteen, outfile)
with open('data/data.json', 'w') as outfile:
  json.dump(data, outfile)