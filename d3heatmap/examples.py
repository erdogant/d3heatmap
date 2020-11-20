# %%
import d3heatmap as d3
print(dir(d3))
print(d3.__version__)

# %%
import pandas as pd
import numpy as np
from d3heatmap import d3heatmap as d3

# %% Create heatmap with clustering

# Import example
df = d3.import_example()

# Create interactive heatmap
results = d3.heatmap(df, vmax=1)

# Create heatmap with some user-defined settings
results = d3.heatmap(df, vmax=1, path='c:/temp/example/d3_heatmap.html', title='Created in d3heatmap', description='d3 heatmap is created using https://github.com/erdogant/d3heatmap. This heatmap is a stand-alone application!', width=1000, height=1000)


# %% Create heatmap without clustering
df = d3.import_example(size=(6, 20))

# Create matrix using default settings
d3.matrix(df)

# The dataframe contains more columns then rows. Adjust the size and color differently.
d3.matrix(df, fontsize=10, title='Hooray!', description='d3 matrix is created using https://github.com/erdogant/d3heatmap.', path='c:/temp/example/d3_matrix.html', width=600, height=300, cmap='interpolateGreens', vmin=1)


# %% Plot same adjacency matrix using heatmap and matrix
df = d3.import_example()
results = d3.heatmap(df, vmax=1, title='d3heatmap with the heatmap function.')
results = d3.matrix(df, title='d3heatmap with the matrix function.', cmap='interpolateGreens')

# %% Several examples
df = pd.DataFrame(np.random.randint(0, 10, size=(7, 52)))

d3.matrix(df, fontsize=10, title='Hooray!', description='Heatmap in d3js using python!', path='d3heatmap_example_1.html', height=200, width=750, cmap='interpolateGreens')

# Change min-max range
d3.matrix(df, fontsize=10, title='Hooray!', description='Heatmap in d3js using python!', path='d3heatmap_example_2.html', height=200, width=750, cmap='interpolateGreens', vmin=8, vmax=10)

# Scaling
d3.matrix(df, fontsize=10, title='Hooray!', description='Heatmap in d3js using python!', path='d3heatmap_example_3.html', height=200, width=750, cmap='interpolateGreens', scale=True, vmin=80, vmax=100)

# Change colormap
d3.matrix(df, fontsize=10, title='Hooray!', description='Heatmap in d3js using python!', path='d3heatmap_example_4.html', height=200, width=750, cmap='interpolateGreens', scale=True)

# Set defaults
d3.matrix(df, fontsize=10, title='Hooray!', description='Heatmap in d3js using python!', path='d3heatmap_example_5.html', height=200, width=750, cmap='interpolateGreens', scale=False, vmin=None, vmax=None)

# Change stroke color
d3.matrix(df, fontsize=10, title='Hooray!', description='Heatmap in d3js using python!', path='d3heatmap_example_6.html', height=200, width=750, cmap='interpolateGreens', scale=False, stroke='black')

# Change several parameters
d3.matrix(df, fontsize=10, title='Hooray!', description='Heatmap in d3js using python!', path='d3heatmap_example_7.html', height=200, width=750, cmap='interpolateGreens', scale=False, stroke='red', vmin=None, vmax=None)

# %%