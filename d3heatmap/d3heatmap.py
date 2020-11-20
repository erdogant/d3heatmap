"""Heatmap in d3 javascript."""
# --------------------------------------------------
# Name        : d3heatmap.py
# Author      : E.Taskesen
# Contact     : erdogant@gmail.com
# github      : https://github.com/erdogant/d3heatmap
# Licence     : See licences
# --------------------------------------------------

from clusteval import clusteval
from d3heatmap.utils.adjmat_vec import adjmat2vec
import numpy as np
import pandas as pd
import webbrowser
import tempfile
from shutil import copyfile
import os
curpath = os.path.dirname(os.path.abspath(__file__))


# %%
def heatmap(df, clust=None, path=None, title='d3heatmap', description=None, vmax=None, width=720, height=720, showfig=True, stroke='red', verbose=3):
    """Heatmap in d3 javascript.

    Parameters
    ----------
    df : pd.DataFrame()
        Input data. The index and column names are used for the row/column naming.
    clust : Numpy array
        Cluster label data. Should be in the same order as the columns and of the input dataframe
    path : String, (Default: user temp directory)
        Directory path to save the output, such as 'c://temp/index.html'
    title : String, (default: 'd3 Heatmap!')
        Title text.
    description : String, (default: 'Heatmap description')
        Description text of the heatmap.
    vmax : Bool, (default: 100).
        Range of colors starting with maximum value. Increasing this value will color the cells more discrete.
            * 1 : cells above value >1 are capped.
            * None : cells are colored based on the maximum value in the input data.
    width : int, (default: 500).
        Width of the window.
    height : int, (default: 500).
        height of the window.
    stroke : String, (default: 'red').
        Color of the recangle when hovering over a cell.
            * 'red'
            * 'black'
    showfig : Bool, (default: True)
        Open browser with heatmap.
    verbose : int [0-5], (default: 3)
        Verbosity to print the working-status. The higher the number, the more information.
            * 0: None
            * 1: Error
            * 2: Warning
            * 3: Info
            * 4: Debug
            * 5: Trace

    Example
    -------
    >>> # Load library
    >>> from d3heatmap import d3heatmap as d3
    >>> # Import example
    >>> df = d3.import_example()
    >>> # Create heatmap
    >>> paths = results = d3.heatmap(df)

    Returns
    -------
    out : dict.
        output path names.

    """
    if len(df.columns.unique())!=len(df.columns):
        if verbose>=2: print('[d3heatmap] >Warning: Input data should contain unique column names otherwise d3js randomly removes the non-unique ones.')
    if len(df.index.unique())!=len(df.index):
        if verbose>=2: print('[d3heatmap] >Warning: Input data should contain unique index names otherwise d3js randomly removes the non-unique ones.')
    if description is None:
        description = "This heatmap is created in d3js using https://github.com/erdogant/d3heatmap.\n\nA network can be represented by an adjacency matrix, where each cell ij represents an edge from vertex i to vertex j.\n\nGiven this two-dimensional representation of a graph, a natural visualization is to show the matrix! However, the effectiveness of a matrix diagram is heavily dependent on the order of rows and columns: if related nodes are placed closed to each other, it is easier to identify clusters and bridges.\nWhile path-following is harder in a matrix view than in a node-link diagram, matrices have other advantages. As networks get large and highly connected, node-link diagrams often devolve into giant hairballs of line crossings. Line crossings are impossible with matrix views. Matrix cells can also be encoded to show additional data; here color depicts clusters computed by a community-detection algorithm."

    # Rescale data
    if vmax is not None:
        df = _scale(df, vmax=vmax, make_round=False, verbose=verbose)
    # if vmin is None:
        # vmin = np.min(df.values)
    if vmax is None:
        vmax = np.max(df.values)
        if verbose>=3: print('[d3heatmap] >Set vmax: %.0g.' %(vmax))

    # Get path to files
    d3_library = os.path.abspath(os.path.join(curpath, 'd3js/d3.v2.min.js'))
    d3_script = os.path.abspath(os.path.join(curpath, 'd3js/d3heatmap.html'))

    # Check path
    filename, dirpath, path = _path_check(path, verbose)

    # Copy files to destination directory
    copyfile(d3_library, os.path.join(dirpath, os.path.basename(d3_library)))
    copyfile(d3_script, path)

    # Collect node names
    nodes = df.columns.astype(str).values

    # Convert into adj into vector
    dfvec = adjmat2vec(df)
    uinode, idx = np.unique(nodes, return_index=True)
    for node, i in zip(uinode, idx):
        dfvec['source'] = dfvec['source'].replace(node, i)
        dfvec['target'] = dfvec['target'].replace(node, i)

    # Write to disk (file is not used)
    basename, ext = os.path.splitext(filename)
    PATHNAME_TO_CSV = os.path.join(dirpath, basename + '.csv')
    dfvec.to_csv(PATHNAME_TO_CSV, index=False)

    # Cluster the nodes
    if clust is None:
        ce = clusteval()
        results = ce.fit(df.values)
        clust = results['labx']

    # Embed the Data in the HTML. Note that the embedding is an important stap te prevent security issues by the browsers.
    # Most (if not all) browser do not accept to read a file using d3.csv or so. It then requires security-by-passes, but thats not the way to go.
    # An alternative is use local-host and CORS but then the approach is not user-friendly coz setting up this, is not so straightforward.
    # It leaves us by embedding the data in the HTML. Thats what we are going to do here.

    NODE_STR = '\n{\n"nodes":\n[\n'
    for i in range(0, len(nodes)):
        NODE_STR = NODE_STR + '{"name":' + '"' + nodes[i] + '"' + ',' + '"cluster":' + str(clust[i]) + "},"
        NODE_STR = NODE_STR + '\n'
    NODE_STR = NODE_STR + '],\n'

    EDGE_STR = '"links":\n[\n'
    for i in range(0, dfvec.shape[0]):
        EDGE_STR = EDGE_STR + '{"source":' + str(dfvec.iloc[i, 0]) + ',' + '"target":' + str(dfvec.iloc[i, 1]) + ',' + '"value":' + str(dfvec.iloc[i, 2]) + '},'
        EDGE_STR = EDGE_STR + '\n'
    EDGE_STR = EDGE_STR + ']\n}'

    # Final data string
    DATA_STR = NODE_STR + EDGE_STR

    # Read the data
    # {
    #   "nodes":
    #       [
    #           {"name":"Name A","cluster":1},
    #           {"name":"Name B","cluster":2},
    #           {"name":"Name C","cluster":2},
    #           {"name":"Name D","cluster":3},
    #           ],
    #       "links":
    #       [
    #           {"source":0,"target":1,"value":1},
    #           {"source":2,"target":2,"value":1},
    #           {"source":3,"target":1,"value":1},
    #       ]
    #   }

    # Import in the file
    with open(path, 'r', encoding="utf8", errors='ignore') as file: d3graphscript = file.read()

    # Read the d3 html with script file
    d3graphscript = d3graphscript.replace('$DESCRIPTION$', str(description))
    d3graphscript = d3graphscript.replace('$TITLE$', str(title))
    d3graphscript = d3graphscript.replace('$WIDTH$', str(width))
    d3graphscript = d3graphscript.replace('$WIDTH_DROPDOWN$', str(int(width + 200)))
    d3graphscript = d3graphscript.replace('$HEIGHT$', str(height))
    d3graphscript = d3graphscript.replace('$STROKE$', str(stroke))
    d3graphscript = d3graphscript.replace('$DATA_PATH$', filename)
    d3graphscript = d3graphscript.replace('$DATA_COMES_HERE$', DATA_STR)

    # Write to file
    with open(path, 'w', encoding="utf8", errors='ignore') as file: file.write(d3graphscript)
    # Open browser with heatmap
    if showfig: webbrowser.open(path, new=1)

    # Return
    out = {}
    out['filename'] = filename
    out['dirpath'] = dirpath
    out['path'] = path
    out['csv'] = PATHNAME_TO_CSV
    return out


# %%
def matrix(df, path=None, title='d3heatmap!', description='Heatmap description', width=500, height=500, fontsize=10, cmap='interpolateInferno', scale=False, vmin=None, vmax=None, showfig=True, stroke='red', verbose=3):
    """Heatmap in d3 javascript.

    Parameters
    ----------
    df : pd.DataFrame()
        Input data. The index and column names are used for the row/column naming.
    path : String, (Default: user temp directory)
        Directory path to save the output, such as 'c://temp/index.html'
    title : String, (default: 'd3 Heatmap!')
        Title text.
    description : String, (default: 'Heatmap description')
        Description text of the heatmap.
    width : int, (default: 500).
        Width of the window.
    height : int, (default: 500).
        height of the window.
    fontsize : int, (default: 10).
        Font size for the X and Y labels.
    scale : Bool, (default: True).
        Scale the values between [0-100].
    vmin : Bool, (default: 0).
        Range of colors starting with minimum value.
            * 1 : cells with value <1 are coloured white.
            * None : cells are colored based on the minimum value in the input data.
    vmax : Bool, (default: 100).
        Range of colors starting with maximum value.
            * 100 : cells above value >100 are capped.
            * None : cells are colored based on the maximum value in the input data.
    stroke : String, (default: 'red').
        Color of the recangle when hovering over a cell.
            * 'red'
            * 'black'
    showfig : Bool, (default: True)
        Open browser with heatmap.
    cmap : String, (default: 'interpolateInferno').
        The colormap scheme. This can be found at: https://github.com/d3/d3-scale-chromatic.
        Categorical:
            * 'schemeCategory10'
            * 'schemeAccent'
            * 'schemeDark2'
            * 'schemePaired'
            * 'schemePastel1'
            * 'schemePastel2'
            * 'schemeSet1'
            * 'schemeSet2'
            * 'schemeSet3'
            * 'schemeTableau10'
        Diverging:
            * 'interpolateInferno'
            * 'interpolatePRGn'
            * 'interpolatePiYG'
            * 'interpolatePuOr'
            * 'interpolateRdBu'
            * 'interpolateRdGy'
            * 'interpolateRdYlBu'
            * 'interpolateRdYlGn'
            * 'interpolateSpectral'
        Single color:
            * 'interpolateBlues'
            * 'interpolateGreens'
            * 'interpolateGreys'
            * 'interpolateOranges'
            * 'interpolatePurples'
            * 'interpolateReds'
        Sequential:
            * 'interpolateTurbo'
            * 'interpolateViridis'
            * 'interpolateInferno'
            * 'interpolateMagma'
            * 'interpolatePlasma'
            * 'interpolateCividis'
            * 'interpolateWarm'
            * 'interpolateCool'
            * 'interpolateCubehelixDefault'
            * 'interpolateBuGn'
            * 'interpolateBuPu'
            * 'interpolateGnBu'
            * 'interpolateOrRd'
            * 'interpolatePuBuGn'
            * 'interpolatePuBu'
            * 'interpolatePuRd'
            * 'interpolateRdPu'
            * 'interpolateYlGnBu'
            * 'interpolateYlGn'
            * 'interpolateYlOrBr'
            * 'interpolateYlOrRd'
        Cyclic:
            * 'interpolateRainbow'
            * 'interpolateSinebow'
    verbose : int [0-5], (default: 3)
        Verbosity to print the working-status. The higher the number, the more information.
            * 0: None
            * 1: Error
            * 2: Warning
            * 3: Info
            * 4: Debug
            * 5: Trace

    Example
    -------
    >>> # Load library
    >>> from d3heatmap import d3heatmap as d3
    >>> # Import example
    >>> df = d3.import_example(size=(6,20))
    >>> # Create heatmap
    >>> paths = d3.matrix(df)
    >>> # The dataframe contains more columns then rows. Adjust the size and color differently.
    >>> paths = d3.matrix(df, fontsize=10, title='Hooray!', description='d3 matrix is created using https://github.com/erdogant/d3heatmap.', path='c:/temp/example/d3_matrix.html', width=600, height=300, cmap='interpolateGreens', vmin=1)

    Returns
    -------
    out : dict.
        output path names.

    """
    if cmap in ['schemeCategory10', 'schemeAccent', 'schemeDark2', 'schemePaired', 'schemePastel2', 'schemePastel1', 'schemeSet1', 'schemeSet2', 'schemeSet3', 'schemeTableau10']:
        cmap_type='scaleOrdinal'
        if verbose>=3: print('[d3heatmap] >d3 cmap type is set to %s' %(cmap_type))
    else:
        cmap_type='scaleSequential'

    if len(df.columns.unique())!=len(df.columns):
        if verbose>=2: print('[d3heatmap] >Warning: Input data should contain unique column names otherwise d3js randomly removes the non-unique ones.')
    if len(df.index.unique())!=len(df.index):
        if verbose>=2: print('[d3heatmap] >Warning: Input data should contain unique index names otherwise d3js randomly removes the non-unique ones.')

    # Rescale data between 0-100
    if scale:
        df = _scale(df, verbose=verbose)
    if (not scale) and (vmin is not None) and (vmax is not None):
        if verbose>=3: print('[d3heatmap] >Data is not scaled. Tip: set vmin=None and vmax=None to range colors between min-max of your data.')
    if vmin is None:
        vmin = np.min(df.values)
    if vmax is None:
        vmax = np.max(df.values)
    if verbose>=3: print('[d3heatmap] >vmin is set to: %g' %(vmin))
    if verbose>=3: print('[d3heatmap] >vmax is set to: %g' %(vmax))

    # Get path to files
    d3_library = os.path.abspath(os.path.join(curpath, 'd3js/d3.v4.js'))
    d3_chromatic = os.path.abspath(os.path.join(curpath, 'd3js/d3.scale.chromatic.v1.min.js'))
    d3_script = os.path.abspath(os.path.join(curpath, 'd3js/d3script.html'))

    # Set fontsize for x-axis, y-axis
    fontsize_x = fontsize
    fontsize_y = fontsize

    # Check path
    filename, dirpath, path = _path_check(path, verbose)

    # Copy files to destination directory
    copyfile(d3_library, os.path.join(dirpath, os.path.basename(d3_library)))
    copyfile(d3_chromatic, os.path.join(dirpath, os.path.basename(d3_chromatic)))
    copyfile(d3_script, path)

    # Convert into adj into vector
    dfvec = adjmat2vec(df)
    dfvec = dfvec.rename(columns={'source': 'variable', 'target': 'group', 'weight': 'value'})

    # Write to disk (file is not used)
    basename, ext = os.path.splitext(filename)
    PATHNAME_TO_CSV = os.path.join(dirpath, basename + '.csv')
    dfvec.to_csv(PATHNAME_TO_CSV, index=False)

    # Embed the Data in the HTML. Note that the embedding is an important stap te prevent security issues by the browsers.
    # Most (if not all) browser do not accept to read a file using d3.csv or so. It then requires security-by-passes, but thats not the way to go.
    # An alternative is use local-host and CORS but then the approach is not user-friendly coz setting up this, is not so straightforward.
    # It leaves us by embedding the data in the HTML. Thats what we are going to do here.
    DATA_STR = ''
    for i in range(0, dfvec.shape[0]):
        newline = '{group : "' + str(dfvec['group'].iloc[i]) + '", variable : "' + str(dfvec['variable'].iloc[i]) + '", value : "' + str(dfvec['value'].iloc[i]) +'"},'
        newline = newline + '\n'
        DATA_STR = DATA_STR + newline

    # Read the data
    # var data =
    # 	[
    # 		{"group":"A", "variable":"v1", "value":"3"},
    # 		{"group":"A", "variable":"v2", "value":"5"},
    # 		{"group":"B", "variable":"v1", "value":"10"},
    # 		{"group":"B", "variable":"v2", "value":"10"}
    # 	]

    # Import in the file
    with open(path, 'r') as file: d3graphscript = file.read()

    # Read the d3 html with script file
    d3graphscript = d3graphscript.replace('$DESCRIPTION$', str(description))
    d3graphscript = d3graphscript.replace('$TITLE$', str(title))

    d3graphscript = d3graphscript.replace('$WIDTH$', str(width))
    d3graphscript = d3graphscript.replace('$HEIGHT$', str(height))

    d3graphscript = d3graphscript.replace('$VMIN$', str(vmin))
    d3graphscript = d3graphscript.replace('$VMAX$', str(vmax))

    d3graphscript = d3graphscript.replace('$FONTSIZE_X$', str(fontsize_x))
    d3graphscript = d3graphscript.replace('$FONTSIZE_Y$', str(fontsize_y))

    d3graphscript = d3graphscript.replace('$STROKE$', str(stroke))
    d3graphscript = d3graphscript.replace('$CMAP$', str(cmap))
    d3graphscript = d3graphscript.replace('$CMAP_TYPE$', str(cmap_type))

    d3graphscript = d3graphscript.replace('$DATA_PATH$', filename)
    d3graphscript = d3graphscript.replace('$DATA_COMES_HERE$', DATA_STR)

    # Write to file
    with open(path, 'w', encoding="utf8", errors='ignore') as file: file.write(d3graphscript)
    # Open browser with heatmap
    if showfig: webbrowser.open(path, new=1)
    # Return
    out = {}
    out['filename'] = filename
    out['dirpath'] = dirpath
    out['path'] = path
    out['csv'] = PATHNAME_TO_CSV
    return out


# %% Import example dataset from github.
def import_example(size=(50, 50), verbose=3):
    """Generate example dataset.

    Description
    -----------
    Generate random adjacency matrix.

    Parameters
    ----------
    verbose : int, optional
        Print progress to screen. The default is 3.
        0: None, 1: ERROR, 2: WARN, 3: INFO (default), 4: DEBUG, 5: TRACE

    Returns
    -------
    pd.DataFrame()
        Dataset containing mixed features.

    """
    df = pd.DataFrame(np.random.randint(0, 10, size=size))

    # Return
    return df


# %%
def _path_check(path, verbose):
    # Check wether path
    if path is None:
        path = os.path.join(tempfile.gettempdir(), 'index.html')
    # Check wether dir + path
    dirpath, filename = os.path.split(path)
    # if input is single file, attach the absolute path.
    if dirpath=='':
        path = os.path.join(tempfile.gettempdir(), filename)
        dirpath, filename = os.path.split(path)
    # Check before proceeding
    if not ('.html' in filename):
        raise ValueError('[d3heatmap] >path should contain the file extension: ".html" ')
    # Create dir
    if not os.path.isdir(dirpath):
        if verbose>=2: print('[d3heatmap] >Warning: Creating directory [%s]' %(dirpath))
        os.makedirs(dirpath, exist_ok=True)
    # Final
    path = os.path.abspath(path)
    dirpath, filename = os.path.split(path)
    return filename, dirpath, path


# %% Scaling
def _scale(X, vmax=100, make_round=True, verbose=3):
    """Scale data.

    Description
    -----------
    Scaling in range by X*(100/max(X))

    Parameters
    ----------
    X : array-like
        Input image data.
    verbose : int (default : 3)
        Print to screen. 0: None, 1: Error, 2: Warning, 3: Info, 4: Debug, 5: Trace.

    Returns
    -------
    df : array-like
        Scaled image.

    """
    if verbose>=3: print('[d3heatmap] >Scaling image between [min-100]')
    try:
        # Normalizing between 0-100
        # X = X - X.min()
        X = X / X.max().max()
        X = X * vmax
        if make_round:
            X = np.round(X)
    except:
        if verbose>=2: print('[d3heatmap] >Warning: Scaling not possible.')

    return X
