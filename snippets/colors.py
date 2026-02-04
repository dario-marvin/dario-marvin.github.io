import matplotlib as mpl
import numpy as np

colormap = 'plasma'
n_colors = 8

cmap = mpl.colormaps[colormap]
colors = cmap(np.linspace(0, 1, n_colors))
cmaplist = [mpl.colors.to_hex(i) for i in colors]
print(' '.join(cmaplist)) 
