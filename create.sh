ulimit -n 10000
python makeAllGrids.py
echo 'makeAllGrids.py completed'

node makeGridSvgs.js --outdir=grids --json=data/data.json
echo 'random grids made'

# Running makeSingleColorGrids before each SVG creator makes each color batch
#   have a randomized target location

python makeSingleColorGrids.py
node makeGridSvgs.js --outdir=gridsBlue --json=data/dataBlue.json
echo 'single color blue made'

python makeSingleColorGrids.py
node makeGridSvgs.js --outdir=gridsGreen --json=data/dataGreen.json
echo 'single color green made'

python makeSingleColorGrids.py
node makeGridSvgs.js --outdir=gridsRed --json=data/dataRed.json
echo 'single color red made'

python makeSingleColorGrids.py
node makeGridSvgs.js --outdir=gridsYellow --json=data/dataYellow.json
echo 'single color yellow made'

# Running makeAllGroupedGrids before each SVG creator makes each group batch
#   have a randomized target location
python makeAllGroupedGrids.py
node makeGridSvgs.js --outdir=grouped1 --json=data/dataG1.json
echo 'group 1 made'

python makeAllGroupedGrids.py
node makeGridSvgs.js --outdir=grouped2 --json=data/dataG2.json
echo 'group 2 made'

python makeAllGroupedGrids.py
node makeGridSvgs.js --outdir=grouped3 --json=data/dataG3.json
echo 'group 3 made'

python makeAllGroupedGrids.py
node makeGridSvgs.js --outdir=grouped4 --json=data/dataG4.json
echo 'group 4 made'