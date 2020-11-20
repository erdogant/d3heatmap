from d3heatmap import d3heatmap

from d3heatmap.utils.adjmat_vec import (
    vec2adjmat,
    adjmat2vec,
    )

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '0.1.7'

# module level doc-string
__doc__ = """
d3heatmap
=====================================================================

Description
-----------
d3heatmap is a Python package to create interactive heatmaps based on d3js.

Example
-------
>>> # Load library
>>> from d3heatmap import d3heatmap as d3
>>>
>>> # Example 1:
>>> df = d3.import_example()
>>> # Create heatmap
>>> paths = results = d3.heatmap(df)
>>>
>>> # Example 2:
>>> df = d3.import_example(size=(6,20))
>>> # Create heatmap
>>> paths = d3.matrix(df)
>>>
>>> # Example 3:
>>> # The dataframe contains more columns then rows. Adjust the size and color differently.
>>> paths = d3.matrix(df, fontsize=10, title='Hooray!', description='d3 matrix is created using https://github.com/erdogant/d3heatmap.', path='c:/temp/example/d3_matrix.html', width=600, height=300, cmap='interpolateGreens', vmin=1)
>>>

References
----------
* https://github.com/erdogant/d3heatmap
* https://d3-graph-gallery.com
* https://https://d3js.org/
"""
