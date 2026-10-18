# Load d3blocks
from d3heatmap import heatmap

# Initialize
d3 = heatmap()

# Load example data
df = d3.import_example('energy')

# Change cluster parameters
G = d3.heatmap(df, filepath=r'd:\temp\out.html', cluster_params={'evaluate':'dbindex',
                               'metric':'hamming',
                               'linkage':'complete',
                               'normalize': False,
                               'min_clust': 3,
                               'max_clust': 15})


# %%
# Initialize
from d3heatmap import heatmap
d3 = heatmap()

# Load example data
df = d3.import_example('bigbang')

# Plot and color on label
G = d3.heatmap(df, color=[1,1,1,2,2,2,3])
d3.node_properties

# Plot and specify the hex color
d3.heatmap(df, color=['#FFF000', '#FFF000', '#FFF000', '#000FFF' , '#000FFF', '#000FFF', '#000FFF'])
d3.node_properties

