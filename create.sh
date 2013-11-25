ulimit -n 10000
python makeAllGrids.py
echo 'makeAllGrids.py completed'


# Running makeSingleColorGrids before each SVG creator makes each color batch
#   have a randomized target location

node makeGridSvgs.js --outdir=gridsBlue --json=data/dataBlue.json
echo 'single color blue made'

node makeGridSvgs.js --outdir=gridsGreen --json=data/dataGreen.json
echo 'single color green made'

node makeGridSvgs.js --outdir=gridsRed --json=data/dataRed.json
echo 'single color red made'

node makeGridSvgs.js --outdir=gridsYellow --json=data/dataYellow.json
echo 'single color yellow made'


node makeGridSvgs.js --outdir=grouped1 --json=data/dataG1.json
echo 'group 1 made'

node makeGridSvgs.js --outdir=grouped2 --json=data/dataG2.json
echo 'group 2 made'

node makeGridSvgs.js --outdir=grouped3 --json=data/dataG3.json
echo 'group 3 made'

node makeGridSvgs.js --outdir=grouped4 --json=data/dataG4.json
echo 'group 4 made'