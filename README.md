# d3heatmap

[![Python](https://img.shields.io/pypi/pyversions/d3heatmap)](https://img.shields.io/pypi/pyversions/d3heatmap)
[![PyPI Version](https://img.shields.io/pypi/v/d3heatmap)](https://pypi.org/project/d3heatmap/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/d3heatmap/blob/master/LICENSE)
[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)
[![Github Forks](https://img.shields.io/github/forks/erdogant/d3heatmap.svg)](https://github.com/erdogant/d3heatmap/network)
[![GitHub Open Issues](https://img.shields.io/github/issues/erdogant/d3heatmap.svg)](https://github.com/erdogant/d3heatmap/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Downloads](https://pepy.tech/badge/d3heatmap/month)](https://pepy.tech/project/d3heatmap)
[![Downloads](https://pepy.tech/badge/d3heatmap)](https://pepy.tech/project/d3heatmap)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/erdogant/d3heatmap/blob/master/notebooks/d3heatmap.ipynb)

* ``d3heatmap`` is a Python package to create interactive heatmaps based on d3js.
* The **aim** of d3heatmap is to create interactive heatmaps that can be used stand-alone and visual attractive. 
* This library does not require you any additional installation, downloads or setting paths to your systems environments. You just need python and this library. All other is taken care off. There are two main functions to create a heatmap ``matrix`` and ``heatmap`` and there are some differences between the two.

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


### Installation
* Install ``d3heatmap`` from PyPI (recommended). d3heatmap is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* It is distributed under the MIT license.

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
Please cite d3heatmap in your publications if this is useful for your research. Here is an example BibTeX entry:
```BibTeX
@misc{erdogant2020d3heatmap,
  title={d3heatmap},
  author={Erdogan Taskesen},
  year={2019},
  howpublished={\url{https://github.com/erdogant/d3heatmap}},
}
```

#### References
* https://github.com/erdogant/d3heatmap
* https://d3-graph-gallery.com
* https://https://d3js.org/
   
### Maintainer
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)
* This work is created and maintained in my free time. If you wish to buy me a <a href="https://erdogant.github.io/donate/?currency=USD&amount=5">Coffee</a> for this work, it is very appreciated.
* Contributions are welcome.
* Star it if you like it!
