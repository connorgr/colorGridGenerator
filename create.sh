ulimit -n 10000

python makeAllGrids.py
echo 'makeAllGrids.py completed'

node makeGridSvgs.js --outdir=gridsRand --json=data/data.json
echo 'randomized made'

node makeGridSvgs.js --outdir=gridsBlue --json=data/dataBlue.json
echo 'single color blue made'

node makeGridSvgs.js --outdir=gridsGreen --json=data/dataGreen.json
echo 'single color green made'

node makeGridSvgs.js --outdir=gridsRed --json=data/dataRed.json
echo 'single color red made'

node makeGridSvgs.js --outdir=gridsYellow --json=data/dataYellow.json
echo 'single color yellow made'


node makeGridSvgs.js --outdir=gridsG1 --json=data/dataGrouped1.json
echo 'group 1 made'

node makeGridSvgs.js --outdir=gridsG2 --json=data/dataGrouped2.json
echo 'group 2 made'

node makeGridSvgs.js --outdir=gridsG3 --json=data/dataGrouped3.json
echo 'group 3 made'

node makeGridSvgs.js --outdir=gridsG4 --json=data/dataGrouped4.json
echo 'group 4 made'

python mergeGridSources.py
