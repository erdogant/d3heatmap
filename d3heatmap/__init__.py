from d3blocks.d3blocks import D3Blocks

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '1.0.1'

# module level doc-string
__doc__ = """
heatmap
=====================================================================

Description
-----------
heatmap is a Python package to create interactive heatmaps based on d3js.
The heatmap allows interactive clustering where the cluster coloring can be customized.
Clusters are colored and within each cluster the color is incremental based on the value. Adjacency matrix must be symetric.

Example
-------
# Load d3heatmap
# from d3heatmap import heatmap
#
# Initialize
# d3 = heatmap()
#
# Load example data
# df = d3.import_example('stormofswords')  # 'energy'
#
# Plot
# d3.heatmap(df)
#

References
----------
https://github.com/d3blocks/d3blocks

"""

def heatmap(*args, **kwargs):
    """Factory that returns a D3Blocks instance.

    Usage:
        from d3heatmap import heatmap
        d3 = heatmap()
    """
    return D3Blocks(*args, **kwargs)


# Exported symbols
__all__ = ['heatmap']
