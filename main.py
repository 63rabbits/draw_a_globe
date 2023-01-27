import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

import matplotlib.ticker as mticker
import numpy as np

##########
# use default map

ax = plt.axes(projection=ccrs.Orthographic(central_longitude=138, central_latitude=36))
ax.add_feature(cfeature.LAND, facecolor='lightgray')
ax.coastlines(lw=1.0)

# ##########
# # use custom map
#
# fname = 'ne_50m_admin_0_countries.shp'
# ax = plt.axes(projection=ccrs.Orthographic(central_longitude=138, central_latitude=36))
# # ax = plt.axes(projection=ccrs.Orthographic(central_longitude=30, central_latitude=30))
# shape_feature = ShapelyFeature(Reader(fname).geometries(),
#                                ccrs.PlateCarree(), facecolor='lightgray', edgecolor='black', lw=0.5)
# ax.add_feature(shape_feature)

##########
# grid

xlocator = mticker.FixedLocator(np.arange(-180, 180, 20))
ylocator = mticker.FixedLocator(np.arange(-90, 90, 20))
ax.gridlines(xlocs=xlocator, ylocs=ylocator, linestyle='--', linewidth=0.5, color='black')

##########
# show map

plt.show()
