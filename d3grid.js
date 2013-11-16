function makeGrid(container, data) {
  var colorSet = data.colorSet,
      grid = data.grid,
      numCols = data.numColumns,
      numColors = data.numColors,
      numRows = data.numRows,
      sqLen = data.squareLen,
      sqSpace = data.spacing;

  var svg = container.append('svg')
          .attr('height', numRows*(sqLen+sqSpace) - sqSpace)
          .attr('id', 'grid')
          .attr('width', numCols*(sqLen+sqSpace) - sqSpace)
          .style('border', '1px solid #000')
          .style('display', 'inline-block')
          .style('padding', 10);

  svg.selectAll('rect')
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
}
