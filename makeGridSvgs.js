#!/usr/bin/env node
var jsdom = require('jsdom')
, fs = require('fs')
//, wkhtmltopdf = require('wkhtmltopdf');

////////////////////////////////////////////////////////////////////////////////////////////////////
// Functions

function executeOnJson(data) {
  var colors = data.colors,
      grids = data.grids,
      lengths = data.lengths,
      numColors = colors.length,
      numVariants = data.numVariants,
      setSizes = data.setSizes,
      spacing = data.spacing;

  for(var g in grids) {
    var grid = grids[g].grid,
        length = grids[g].length,
        setSize = grids[g].setSize,
        tgtQuadrant = grids[g].tgtQuadrant,
        variant = grids[g].variant;

    var numColumns = setSize,
        numRows = setSize,
        gridData = {'colorSet':colors, 'grid': grid, 'numColors':
                  numColors, 'numColumns': numColumns, 'numRows': numRows,
                  'spacing': spacing, 'squareLen': length};

    var fileName = '';
    fileName = fileName = 'grid_' + numColumns + 'x' + numRows + '_' + length + '_' + tgtQuadrant + '_' + variant;

    runHeadlessBrowser(gridData, fileName);
    process.stdout.write('.');
  }
  console.log('\n >>> Done. Saving results to file.');
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
