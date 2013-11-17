#!/usr/bin/env node
var jsdom = require('jsdom')
, fs = require('fs')
//, wkhtmltopdf = require('wkhtmltopdf');

////////////////////////////////////////////////////////////////////////////////////////////////////
// Functions

function executeOnJson(data) {
  function findQuadrant(numColumns, numRows, targetLoc) {
    if(targetLoc === undefined) {
      return 'NoTgt';
    }
    // Assumes row major order
    // Left, Right, Top, Bottom
    var colIndex = targetLoc % numColumns,
        rowIndex = targetLoc / numRows;

    var horizontal = colIndex < numColumns / 2 ? 'L' : 'R',
        vertical = rowIndex < numRows / 2 ? 'T' : 'B';
    return vertical+horizontal;
  }
  // Load the data and parse into shorter variable handles
  var colors = data.colors,
      gridGroups = data.grids,
      lengths = data.lengths,
      spacing = data.spacing;

  // Loop through 6x6 grid dimension group, etc.
  for(var g in gridGroups) {
    var gridsJSON = JSON.parse(gridGroups[g]),
        // `grids` has all variants for a given dimension
        grids = gridsJSON.grids,
        numColors = gridsJSON.numColors,
        numColumns = gridsJSON.numColumns,
        numRows = gridsJSON.numRows;
    // Each grid of the above dimension
    for(var h in grids) {
      // Group of same background field, target in different locations based on
      //   surrounding number of colors count
      var gridsSurroundVariants = grids[h];
      for(var i in gridsSurroundVariants) {
        var gridJSON = gridsSurroundVariants[i],
            adjColors = gridJSON.adjColors,
            grid = gridJSON['grid'],
            targetLoc = gridJSON['targetLoc'],
            targetPresent = gridJSON['target'],
            sizes = [10,20,30,40,50],
            spacing = 5;


        var quadrant = findQuadrant(numColumns, numRows, targetLoc);

        for(var size in sizes) {
          var fileName = 'grid_' + numColumns + 'x' + numRows + '_' + squareLen + '_id' + h + '_tgtLoc' + quadrant,
              squareLen = sizes[size],
              gridData = {'adjColors':adjColors, 'colorSet':colors, 'grid': grid, 'numColors':
                  numColors, 'numColumns': numColumns, 'numRows': numRows, 'spacing': spacing,
                  'squareLen': squareLen};
          runHeadlessBrowser(gridData, fileName);
        }
      }
    }
  }
}

function runHeadlessBrowser(gridData, fileName) {
  jsdom.env({features:{QuerySelector:true}, html:htmlStub, src:src, done:function(errors, window) {
    // Function for saving a figure
    function save_fig(selector, file_prefix){
      // Grab the element from the document
      var elem = $(selector)[0];

      // Output if the element exists
      if (elem){
        // Write to file as an SVG
        fs.writeFile(file_prefix + ".svg", elem.outerHTML, write_err);

        // Write to file as a PDF
        // wkhtmltopdf(elem.outerHTML).pipe(fs.creatReadStream(argv.outpre + ".pdf"));
      }
    }
    // Make libraries global loaded in window
    var d3 = window.d3;
    var $  = window.jQuery;

    // Create the oncoprint in the headless browser
    var el = d3.select("colorgrid");
    window.makeGrid(el, gridData);

    // Make sure all SVGs are properly defined
    d3.selectAll("svg").attr("xmlns", "http://www.w3.org/2000/svg");

    // Write the grid to file
    save_fig("svg#grid", argv.outdir + '/' + fileName);
    //save_fig("svg#colorgrid", argv.outdir + name);
  }});
}

// Function to notify user if write fails
function write_err(err){
  if (err){ console.log('Could not output result.' + err); }
}


////////////////////////////////////////////////////////////////////////////////////////////////////
// Main Content

// Validate args
var argv = require('optimist').argv;
if (!( argv.outdir && argv.json )){
    usage  = "Usage: node makeGridSvgs.js --outdir=</path/to/output> --json=</path/to/json>"
    console.log(usage);
    process.exit(1);
}

// Scripts required to make the grids
var scripts = [ "bower_components/jquery/jquery.js",
                "bower_components/d3/d3.js",
                "d3grid.js"
              ],
    htmlStub = '<!DOCTYPE html><colorgrid></colorgrid>';

var src = scripts.map(function(S){ return fs.readFileSync(S).toString(); })

var data = JSON.parse(fs.readFileSync(argv.json).toString());
executeOnJson(data);
