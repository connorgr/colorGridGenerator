colorGridGenerator
==================

This project creates randomly colored grids as SVGs. For each grid it also generates variations that feature a 
uniquely colored target square. The number of variants is less than or equal to the number of colors that could
surround any given non-edge square.

You can specify:
* Square size
* Colors
* Number of columns
* Number of rows

# Installation
For convenience, we rely on `bower` and `npm`. After cloning the repo, just run `bower install` and `npm install`. That's it!

# Generating your color grids
The pipeline consists of two stages:
1. Creating JSON grid information files for each grid: `python makeAllGrids.py`
2. Creating the SVG files based on the JSON information: `node makeGridSvgs.js --outdir=grids --json=data/data.json`
