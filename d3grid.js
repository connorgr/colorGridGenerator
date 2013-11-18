function makeGrid(container, data) {
  var colorSet = data.colorSet,
      grid = data.grid,
      numCols = data.numColumns,
      numColors = data.numColors,
      numRows = data.numRows,
      sqLen = data.squareLen,
      sqSpace = data.spacing;

  var gridFieldHeight = numRows*(sqLen+sqSpace) - sqSpace,
      gridFieldWidth = numCols*(sqLen+sqSpace) - sqSpace,
      margin = {'bottom': 5, 'left': 5, 'right': 5, 'top': 5},
      fullWidth = gridFieldWidth + margin.left + margin.right,
      fullHeight = gridFieldHeight + margin.top + margin.bottom;

  var borderColor = '#888';

  var svg = container.append('svg')
          .attr('height', fullHeight)
          .attr('id', 'grid')
          .attr('width', fullWidth)
          .style('border', '1px solid '+borderColor)
          .style('display', 'inline-block'),
      rectG = svg.append('g').attr('transform', 'translate('+margin.left+','+margin.top+')');

  rectG.selectAll('rect')
      .data(grid)
      .enter()
      .append('rect')
        .attr('height', sqLen)
        .attr('width', sqLen)
        .attr('x', function(d) {
          var moveX = (grid.indexOf(d) % numCols) * (sqLen + sqSpace);
          return moveX;
        })
        .attr('y', function(d) {
          var moveY = (parseInt(grid.indexOf(d)/numRows)) * (sqLen + sqSpace);
          return moveY;
        })
        .style('fill', function(d) {
          return colorSet[d.color];
        });

  var horizLineData = [{'x': 0, 'y': fullHeight/2}, {'x': fullWidth, 'y': fullHeight/2}],
      vertLineData = [{'x': fullWidth/2, 'y': 0}, {'x': fullWidth/2, 'y': fullHeight}];

  var lineFn = d3.svg.line()
          .x(function(d) { return d.x; })
          .y(function(d) { return d.y; })
          .interpolate('linear'),
      horizLine = svg.append('path')
          .attr('d', lineFn(horizLineData))
          .attr('stroke', borderColor)
          .attr('stroke-width', 1)
          .attr('fill', 'none'),
      vertLine = svg.append('path')
          .attr('d', lineFn(vertLineData))
          .attr('stroke', borderColor)
          .attr('stroke-width', 1)
          .attr('fill', 'none');
}
