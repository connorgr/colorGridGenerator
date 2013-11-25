import json
import gridData


# start(grouped, numColors, numCols, numGrids, numRows)
# Returns: {'grids': grids, 'numColors': numColors, 'numColumns': numCols, 'numRows': numRows }

sixG = gridData.start(True, 4, 6, 1, 6)
eightG = gridData.start(True, 4, 8, 1, 8)
tenG = gridData.start(True, 4, 10, 1, 10)
twelveG = gridData.start(True, 4, 12, 1, 12)
fourteenG = gridData.start(True, 4, 14, 1, 14)

jsonSixG = json.dumps(sixG)
jsonEightG = json.dumps(eightG)
jsonTenG = json.dumps(tenG)
jsonTwelveG = json.dumps(twelveG)
jsonFourteenG = json.dumps(fourteenG)

# # last color is target
colors1 = ['rgb(120,106,24)','rgb(131,71,80)','rgb(23,73,95)','rgb(0,68,43)','rgb(98,63,117)']
colors2 = ['rgb(131,71,80)','rgb(120,106,24)','rgb(23,73,95)','rgb(0,68,43)','rgb(98,63,117)']
colors3 = ['rgb(131,71,80)','rgb(120,106,24)','rgb(0,68,43)','rgb(23,73,95)','rgb(98,63,117)']
colors4 = ['rgb(120,106,24)','rgb(131,71,80)','rgb(0,68,43)','rgb(23,73,95)','rgb(98,63,117)']
lengths = [10, 20, 30, 40, 50]
spacing = 5

dataG1 = {'grids': [jsonSixG, jsonEightG, jsonTenG, jsonTwelveG, jsonFourteenG], 'colors': colors1, 'lengths': lengths, 'spacing': spacing}
dataG2 = {'grids': [jsonSixG, jsonEightG, jsonTenG, jsonTwelveG, jsonFourteenG], 'colors': colors2, 'lengths': lengths, 'spacing': spacing}
dataG3 = {'grids': [jsonSixG, jsonEightG, jsonTenG, jsonTwelveG, jsonFourteenG], 'colors': colors3, 'lengths': lengths, 'spacing': spacing}
dataG4 = {'grids': [jsonSixG, jsonEightG, jsonTenG, jsonTwelveG, jsonFourteenG], 'colors': colors4, 'lengths': lengths, 'spacing': spacing}

with open('data/dataG1.json', 'w') as outfile:
  json.dump(dataG1, outfile)
with open('data/dataG2.json', 'w') as outfile:
  json.dump(dataG2, outfile)
with open('data/dataG3.json', 'w') as outfile:
  json.dump(dataG3, outfile)
with open('data/dataG4.json', 'w') as outfile:
  json.dump(dataG4, outfile)
