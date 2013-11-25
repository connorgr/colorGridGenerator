import json
import gridData


# start(grouped, numColors, numCols, numGrids, numRows)
# Returns: {'grids': grids, 'numColors': numColors, 'numColumns': numCols, 'numRows': numRows }

six = gridData.start(False, 4, 6, 1, 6)
eight = gridData.start(False, 4, 8, 1, 8)
ten = gridData.start(False, 4, 10, 1, 10)
twelve = gridData.start(False, 4, 12, 1, 12)
fourteen = gridData.start(False, 4, 14, 1, 14)

jsonSix = json.dumps(six)
jsonEight = json.dumps(eight)
jsonTen = json.dumps(ten)
jsonTwelve = json.dumps(twelve)
jsonFourteen = json.dumps(fourteen)

# last color is target
colors = ['rgb(120,106,24)','rgb(131,71,80)','rgb(23,73,95)','rgb(0,68,43)','rgb(98,63,117)']
yellow = ['rgb(120,106,24)','rgb(120,106,24)','rgb(120,106,24)','rgb(120,106,24)','rgb(98,63,117)']
red = ['rgb(131,71,80)','rgb(131,71,80)','rgb(131,71,80)','rgb(131,71,80)','rgb(98,63,117)']
blue = ['rgb(23,73,95)','rgb(23,73,95)','rgb(23,73,95)','rgb(23,73,95)','rgb(98,63,117)']
green = ['rgb(0,68,43)','rgb(0,68,43)','rgb(0,68,43)','rgb(0,68,43)','rgb(98,63,117)']

lengths = [10, 20, 30, 40, 50]
spacing = 5

data = {'grids': [jsonSix, jsonEight, jsonTen, jsonTwelve, jsonFourteen], 'colors': colors, 'lengths': lengths, 'spacing': spacing}

dataYellow = {'grids': [jsonSix, jsonEight, jsonTen, jsonTwelve, jsonFourteen], 'colors': yellow, 'lengths': lengths, 'spacing': spacing}
dataRed = {'grids': [jsonSix, jsonEight, jsonTen, jsonTwelve, jsonFourteen], 'colors': red, 'lengths': lengths, 'spacing': spacing}
dataBlue = {'grids': [jsonSix, jsonEight, jsonTen, jsonTwelve, jsonFourteen], 'colors': blue, 'lengths': lengths, 'spacing': spacing}
dataGreen = {'grids': [jsonSix, jsonEight, jsonTen, jsonTwelve, jsonFourteen], 'colors': green, 'lengths': lengths, 'spacing': spacing}

with open('data/data.json', 'w') as outfile:
  json.dump(data, outfile)
with open('data/dataYellow.json', 'w') as outfile:
  json.dump(dataYellow, outfile)
with open('data/dataRed.json', 'w') as outfile:
  json.dump(dataRed, outfile)
with open('data/dataBlue.json', 'w') as outfile:
  json.dump(dataBlue, outfile)
with open('data/dataGreen.json', 'w') as outfile:
  json.dump(dataGreen, outfile)