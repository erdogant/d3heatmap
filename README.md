# d3heatmap

[![Python](https://img.shields.io/pypi/pyversions/d3heatmap)](https://img.shields.io/pypi/pyversions/d3heatmap)
[![Pypi](https://img.shields.io/pypi/v/d3heatmap)](https://pypi.org/project/d3heatmap/)
[![Docs](https://img.shields.io/badge/Sphinx-Docs-Green)](https://d3blocks.github.io/d3blocks/pages/html/Heatmap.html)
[![LOC](https://sloc.xyz/github/erdogant/d3heatmap/?category=code)](https://github.com/erdogant/d3heatmap/)
[![Downloads](https://static.pepy.tech/personalized-badge/d3heatmap?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20downloads/month)](https://pepy.tech/project/d3heatmap)
[![Downloads](https://static.pepy.tech/personalized-badge/d3heatmap?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/d3heatmap)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/d3heatmap/blob/master/LICENSE)
[![Forks](https://img.shields.io/github/forks/erdogant/d3heatmap.svg)](https://github.com/erdogant/d3heatmap/network)
[![Issues](https://img.shields.io/github/issues/erdogant/d3heatmap.svg)](https://github.com/erdogant/d3heatmap/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![DOI](https://zenodo.org/badge/298880904.svg)](https://zenodo.org/badge/latestdoi/298880904)
[![Medium](https://img.shields.io/badge/Medium-Blog-green)](https://towardsdatascience.com/d3blocks-the-python-library-to-create-interactive-and-standalone-d3js-charts-3dda98ce97d4)
[![Donate](https://img.shields.io/badge/Support%20this%20project-grey.svg?logo=github%20sponsors)](https://d3blocks.github.io/d3blocks/pages/html/Documentation.html)
<!---[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)-->
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->


``d3heatmap`` is a Python package to create interactive heatmaps based on d3js.
* The **aim** of d3heatmap is to create interactive heatmaps that can be used stand-alone and being visual attractive. 
* This library does not require any additional installation of javascript, or downloads or setting paths to your systems environments. You just need python and pip install this library. There are two main functions to create a heatmap and there are some differences between the two. Read below for more details. Have fun!

## This library is since 18-01-2023 fully implemented in [D3Blocks](https://d3blocks.github.io/d3blocks/pages/html/Heatmap.html). This repo will be froozen at v0.2.3. Please use heatmap in D3Blocks!

```
pip install d3blocks

# Import
from d3blocks import D3Blocks

# Initialize
d3 = D3Blocks()

# Load example data
df = d3.import_example('stormofswords')
df = d3.vec2adjmat(df['source'], df['target'], weight=df['weight'], symmetric=True)

# Plot
d3.heatmap(df)
```


### Functionalities

``d3heatmap.matrix``
 * Allows none symetric adjacency matrices.
 * Colormap can be changed.
 * No clustering.
 * round-ish elements.

``d3heatmap.heatmap``
 * Allows Clustering.
 * Colormap is fixed.
 * Advanced cluster coloring. Clusters are colored and within each cluster the color is incremental based on the value.
 * Adjacency matrix must be symetric.

# 
**Star this repo if you like it! ⭐️**
#


#### Installation
```
pip install d3heatmap
```

* Alternatively, install d3heatmap from the GitHub source:
```bash
git clone https://github.com/erdogant/d3heatmap.git
cd d3heatmap
pip install -U .
```  

#### Import d3heatmap

```python
from d3heatmap import d3heatmap as d3
```

#### Example 1: plot using the heatmap function

```python
df = d3.import_example()
# Create heatmap
paths = results = d3.heatmap(df)
```

Klik on the figure for the interactive example.
<p align="center">
  <a href="https://erdogant.github.io/docs/d3heatmap/d3heatmap.html">
     <img src="https://github.com/erdogant/d3heatmap/blob/master/docs/figs/example_1.png" width="600" />
  </a>
</p>

#### Example 2: plot using the matrix function

```python
df = d3.import_example(size=(6,20))
# Create heatmap
paths = d3.matrix(df)
```

<p align="center">
  <img src="https://github.com/erdogant/d3heatmap/blob/master/docs/figs/example_2.png" width="600" />
</p>


#### Example 3: plot using the matrix function

```python
# The dataframe contains more columns then rows. Adjust the size and color differently.
df = d3.import_example(size=(6,20))
# Create heatmap
paths = d3.matrix(df, fontsize=10, title='Hooray!', description='d3 matrix is created using https://github.com/erdogant/d3heatmap.', path='c:/temp/example/d3_matrix.html', width=600, height=300, cmap='interpolateGreens', vmin=1)
```

<p align="center">
  <img src="https://github.com/erdogant/d3heatmap/blob/master/docs/figs/example_3.png" width="600" />
</p>


#### Example 4: Matrix with parameters changed:

```python
# The dataframe contains more columns then rows. Adjust the size and color differently.
df = d3.import_example(size=(6,20))
# Create heatmap
paths = d3.matrix(df, fontsize=10, title='Hooray!', description='d3 matrix is created using https://github.com/erdogant/d3heatmap.', path='c:/temp/example/d3_matrix.html', width=600, height=300, cmap='interpolateGreens', vmin=1)
```

<p align="center">
  <img src="https://github.com/erdogant/d3heatmap/blob/master/docs/figs/example_4.png" width="600" />
</p>


#### Example 4: Comparison heatmap vs matrix:
There are quit some differences between the ``heatmap`` vs ``matrix`` functionality.

```python
df = d3.import_example()
results = d3.heatmap(df, title='d3heatmap with the heatmap function.', path='heatmap.html')
results = d3.matrix(df, title='d3heatmap with the matrix function.', cmap='interpolatePRGn', path='matrix.html', width=700, height=700)
```

<p align="center">
  <img src="https://github.com/erdogant/d3heatmap/blob/master/docs/figs/example_5.png" width="600" />
  <img src="https://github.com/erdogant/d3heatmap/blob/master/docs/figs/example_6.png" width="500" />
</p>

#### Citation
Please cite d3heatmap in your publications if this is useful for your research. See right column for citation information.

#### References
* https://github.com/erdogant/d3heatmap
* https://d3-graph-gallery.com
* https://https://d3js.org/
   
### Maintainer
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)
* This work is created and maintained in my free time. If you wish to buy me a <a href="https://erdogant.github.io/donate/?currency=USD&amount=5">Coffee</a> for this work, it is very appreciated.
* Contributions are welcome.
* Star it if you like it!
