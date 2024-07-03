"""
Coastlines and borders
======================

Plotting coastlines and borders is handled by :meth:`pygmt.Figure.coast`.
"""

# %%
import pygmt

# %%
# Shorelines
# ----------
#
# Use the ``shorelines`` parameter to plot only the shorelines:

fig = pygmt.Figure()
fig.basemap(region="g", projection="W15c", frame=True)
fig.coast(shorelines=True)
fig.show()

# %%
# The shorelines are divided in 4 levels:
#
# 1. coastline
# 2. lakeshore
# 3. island-in-lake shore
# 4. lake-in-island-in-lake shore
#
# You can specify which level you want to plot by passing the level number and
# a GMT pen configuration. For example, to plot just the coastlines with 0.5p
# thickness and black lines:

fig = pygmt.Figure()
fig.basemap(region="g", projection="W15c", frame=True)
fig.coast(shorelines="1/0.5p,black")
fig.show()

# %%
# You can specify multiple levels (with their own pens) by passing a list to
# ``shorelines``:

fig = pygmt.Figure()
fig.basemap(region="g", projection="W15c", frame=True)
fig.coast(shorelines=["1/1p,black", "2/0.5p,red"])
fig.show()


# %%
# Resolutions
# -----------
#
# The coastline database comes with 5 resolutions. The resolution drops by 80%
# between levels:
#
# 1. ``"c"``: crude
# 2. ``"l"``: low (default)
# 3. ``"i"``: intermediate
# 4. ``"h"``: high
# 5. ``"f"``: full

oahu = [-158.3, -157.6, 21.2, 21.8]
fig = pygmt.Figure()
for res in ["c", "l", "i", "h", "f"]:
    fig.coast(resolution=res, shorelines="1p", region=oahu, projection="M5c")
    fig.shift_origin(xshift="5c")
fig.show()


# %%
# Land and water
# --------------
#
# Use the ``land`` and ``water`` parameters to specify a fill color for land
# and water bodies. The colors can be given by name or hex codes (like the ones
# used in HTML and CSS):

fig = pygmt.Figure()
fig.basemap(region="g", projection="W15c", frame=True)
fig.coast(land="#666666", water="skyblue")
fig.show()

# sphinx_gallery_thumbnail_number = 5

"""
Setting the region
==================

Many of the plotting methods take the ``region`` parameter, which sets the
area that will be shown in the figure. This tutorial covers the different types
of inputs that it can accept.
"""

# %%
import pygmt

# %%
# Coordinates
# -----------
#
# A string of coordinates can be passed to ``region``, in the form of
# *xmin*/*xmax*/*ymin*/*ymax*.

fig = pygmt.Figure()
fig.coast(
    # Set the x-range from 10E to 20E and the y-range to 35N to 45N
    region="10/20/35/45",
    # Set projection to Mercator, and the figure size to 15 centimeters
    projection="M15c",
    # Set the color of the land to light gray
    land="lightgray",
    # Set the color of the water to white
    water="white",
    # Display the national borders and set the pen thickness to 0.5p
    borders="1/0.5p",
    # Display the shorelines and set the pen thickness to 0.5p
    shorelines="1/0.5p",
    # Set the frame to display annotations and gridlines
    frame="ag",
)
fig.show()

# %%
# The coordinates can be passed to ``region`` as a list, in the form of
# [*xmin*, *xmax*, *ymin*, *ymax*].

fig = pygmt.Figure()
fig.coast(
    # Set the x-range from 10E to 20E and the y-range to 35N to 45N
    region=[10, 20, 35, 45],
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()

# %%
# Instead of passing axes minima and maxima, the coordinates can be passed for
# the bottom-left and top-right corners. The string format takes the
# coordinates for the bottom-left and top-right coordinates. To specify corner
# coordinates, append **+r** at the end of the ``region`` string.

fig = pygmt.Figure()
fig.coast(
    # Set the bottom-left corner as 10E, 35N and the top-right corner as
    # 20E, 45N
    region="10/35/20/45+r",
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()


# %%
# Global regions
# --------------
#
# In addition to passing coordinates, the argument **d** can be passed to set
# the region to the entire globe. The range is 180W to 180E (-180, 180) and 90S
# to 90N (-90 to 90). With no parameters set for the projection, the figure
# defaults to be centered at the mid-point of both x- and y-axes. Using
# **d**\ , the figure is centered at (0, 0), or the intersection of the equator
# and prime meridian.

fig = pygmt.Figure()
fig.coast(
    region="d",
    projection="Cyl_stere/12c",
    land="darkgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()

# %%
# The argument **g** can be passed, which encompasses the entire globe. The
# range is 0E to 360E (0, 360) and 90S to 90N (-90 to 90). With no parameters
# set for the projection, the figure is centered at (180, 0), or the
# intersection of the equator and International Date Line.

fig = pygmt.Figure()
fig.coast(
    region="g",
    projection="Cyl_stere/12c",
    land="darkgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()


# %%
# ISO code
# --------
#
# The ``region`` can be set to include a specific area specified by the
# two-character ISO 3166-1 alpha-2 convention
# (for further information: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).

fig = pygmt.Figure()
fig.coast(
    # Set the figure region to encompass Japan with the ISO code "JP"
    region="JP",
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()

# %%
# The area encompassed by the ISO code can be expanded by appending
# **+r**\ *increment* to the ISO code. The *increment* unit is in degrees, and
# if only one value is added it expands the range of the region in all
# directions. Using **+r** expands the final region boundaries to be multiples
# of *increment* .

fig = pygmt.Figure()
fig.coast(
    # Expand the region boundaries to be multiples of 3 degrees in all
    # directions
    region="JP+r3",
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()

# %%
# Instead of expanding the range of the plot uniformly in all directions, two
# values can be passed to expand differently on each axis. The format is
# *xinc*/*yinc*.

fig = pygmt.Figure()
fig.coast(
    # Expand the region boundaries to be multiples of 3 degrees on the x-axis
    # and 5 degrees on the y-axis.
    region="JP+r3/5",
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()

# %%
# Instead of expanding the range of the plot uniformly in all directions, four
# values can be passed to expand differently in each direction.
# The format is *winc*/*einc*/*sinc*/*ninc*, which expands on the west,
# east, south, and north axes.

fig = pygmt.Figure()
fig.coast(
    # Expand the region boundaries to be multiples of 3 degrees to the west, 5
    # degrees to the east, 7 degrees to the south, and 9 degrees to the north.
    region="JP+r3/5/7/9",
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()

# %%
# The ``region`` increment can be appended with **+R**, which adds the
# increment without rounding.

fig = pygmt.Figure()
fig.coast(
    # Expand the region setting outside the range of Japan by 3 degrees in all
    # directions, without rounding to the nearest increment.
    region="JP+R3",
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()

# %%
# The ``region`` increment can be appended with **+e**, which is like **+r**
# and expands the final region boundaries to be multiples of *increment*.
# However, it ensures that the bounding box extends by at least 0.25 times the
# increment.

fig = pygmt.Figure()
fig.coast(
    # Expand the region boundaries to be multiples of 3 degrees in all
    # directions
    region="JP+e3",
    projection="M12c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)
fig.show()

"""
Plotting Earth relief
=====================

Plotting a map of Earth relief can use the data accessed by the
:func:`pygmt.datasets.load_earth_relief` function. The data can then be
plotted using the :meth:`pygmt.Figure.grdimage` method.
"""

# %%
import pygmt

# %%
# Load sample Earth relief data for the entire globe at a resolution of
# 1 arc-degree. The other available resolutions are show
# at :gmt-datasets:`earth-relief.html`.
grid = pygmt.datasets.load_earth_relief(resolution="01d")


# %%
# Create a plot
# -------------
#
# The :meth:`pygmt.Figure.grdimage` method takes the ``grid`` input to create a
# figure. It creates and applies a color palette to the figure based upon the
# z-values of the data. By default, it plots the map with the *turbo* CPT, an
# equidistant cylindrical projection, and with no frame.

fig = pygmt.Figure()
fig.grdimage(grid=grid)
fig.show()

# %%
# :meth:`pygmt.Figure.grdimage` can take the optional parameter ``projection``
# for the map. In the example below, the ``projection`` is set as ``R12c`` for
# 12 centimeter figure with a Winkel Tripel projection. For a list of available
# projections, see :gmt-docs:`cookbook/map-projections.html`.

fig = pygmt.Figure()
fig.grdimage(grid=grid, projection="R12c")
fig.show()


# %%
# Set a color map
# ---------------
#
# :meth:`pygmt.Figure.grdimage` takes the ``cmap`` parameter to set the CPT of
# the figure. Examples of common CPTs for Earth relief are shown below.
# A full list of CPTs can be found at :gmt-docs:`cookbook/cpts.html`.

# %%
# Using the *geo* CPT:

fig = pygmt.Figure()
fig.grdimage(grid=grid, projection="R12c", cmap="geo")
fig.show()

# %%
# Using the *relief* CPT:

fig = pygmt.Figure()
fig.grdimage(grid=grid, projection="R12c", cmap="relief")
fig.show()


# %%
# Add a color bar
# ---------------
#
# The :meth:`pygmt.Figure.colorbar` method displays the CPT and the associated
# Z-values of the figure, and by default uses the same CPT set by the ``cmap``
# parameter for :meth:`pygmt.Figure.grdimage`. The ``frame`` parameter for
# :meth:`pygmt.Figure.colorbar` can be used to set the axis intervals and
# labels. A list is used to pass multiple arguments to ``frame``. In the
# example below, ``a2500`` sets the axis interval to 2,500, ``x+lElevation``
# sets the x-axis label, and ``y+lm`` sets the y-axis label.

fig = pygmt.Figure()
fig.grdimage(grid=grid, projection="R12c", cmap="geo")
fig.colorbar(frame=["a2500", "x+lElevation", "y+lm"])
fig.show()

# %%
# Create a region map
# -------------------
#
# In addition to providing global data, the ``region`` parameter for
# :func:`pygmt.datasets.load_earth_relief` can be used to provide data for a
# specific area. The ``region`` parameter is required for resolutions at
# 5 arc-minutes or higher, and accepts a list (as in the example below) or a
# string. The geographic ranges are passed as *xmin*/*xmax*/*ymin*/*ymax*.
#
# The example below uses data with a 10 arc-minutes resolution, and plots it on
# a 15 centimeters figure with a Mercator projection and a CPT set to *geo*.
# ``frame="a"`` is used to add a frame to the figure.

grid = pygmt.datasets.load_earth_relief(resolution="10m", region=[-14, 30, 35, 60])
fig = pygmt.Figure()
fig.grdimage(grid=grid, projection="M15c", frame="a", cmap="geo")
fig.colorbar(frame=["a1000", "x+lElevation", "y+lm"])
fig.show()

# sphinx_gallery_thumbnail_number = 5

"""
Plotting data points
====================

GMT shines when it comes to plotting data on a map. We can use some sample data
that is packaged with GMT to try this out. PyGMT provides access to these
datasets through the :mod:`pygmt.datasets` package. If you don't have the data
files already, they are automatically downloaded and saved to a cache directory
the first time you use them (usually ``~/.gmt/cache``).
"""

# %%
import pygmt

# %%
# For example, let's load the sample dataset of tsunami generating earthquakes
# around Japan using :func:`pygmt.datasets.load_sample_data`.
# The data are loaded as a :class:`pandas.DataFrame`.

data = pygmt.datasets.load_sample_data(name="japan_quakes")

# Set the region for the plot to be slightly larger than the data bounds.
region = [
    data.longitude.min() - 1,
    data.longitude.max() + 1,
    data.latitude.min() - 1,
    data.latitude.max() + 1,
]

print(region)
print(data.head())

# %%
# We'll use the :meth:`pygmt.Figure.plot` method to plot circles on the
# earthquake epicenters.

fig = pygmt.Figure()
fig.basemap(region=region, projection="M15c", frame=True)
fig.coast(land="black", water="skyblue")
fig.plot(x=data.longitude, y=data.latitude, style="c0.3c", fill="white", pen="black")
fig.show()

# %%
# We used the style ``c0.3c`` which means "circles with a diameter of 0.3
# centimeters". The ``pen`` parameter controls the outline of the symbols and
# the ``fill`` parameter controls the fill.
#
# We can map the size of the circles to the earthquake magnitude by passing an
# array to the ``size`` parameter. Because the magnitude is on a logarithmic
# scale, it helps to show the differences by scaling the values using a power
# law.

fig = pygmt.Figure()
fig.basemap(region=region, projection="M15c", frame=True)
fig.coast(land="black", water="skyblue")
fig.plot(
    x=data.longitude,
    y=data.latitude,
    size=0.02 * (2**data.magnitude),
    style="cc",
    fill="white",
    pen="black",
)
fig.show()

# %%
# Notice that we didn't include the size in the ``style`` parameter this time,
# just the symbol ``c`` (circles) and the unit ``c`` (centimeters). So in
# this case, the size will be interpreted as being in centimeters.
#
# We can also map the colors of the markers to the depths by passing an array
# to the ``fill`` parameter and providing a colormap name (``cmap``). We can
# even use the new matplotlib colormap "viridis". Here, we first create a
# continuous colormap ranging from the minimum depth to the maximum depth of
# the earthquakes using :func:`pygmt.makecpt`, then set ``cmap=True`` in
# :meth:`pygmt.Figure.plot` to use the colormap. At the end of the plot, we
# also plot a colorbar showing the colormap used in the plot.
#

fig = pygmt.Figure()
fig.basemap(region=region, projection="M15c", frame=True)
fig.coast(land="black", water="skyblue")
pygmt.makecpt(cmap="viridis", series=[data.depth_km.min(), data.depth_km.max()])
fig.plot(
    x=data.longitude,
    y=data.latitude,
    size=0.02 * 2**data.magnitude,
    fill=data.depth_km,
    cmap=True,
    style="cc",
    pen="black",
)
fig.colorbar(frame="af+lDepth (km)")
fig.show()

# sphinx_gallery_thumbnail_number = 3

