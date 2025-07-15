# trace generated using paraview version 5.13.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# set active source

print("Make Sure you have generated the birth and death points using the file in queries folder\n")
path=input(r"enter birth or death vtp file")
# create a new 'XML PolyData Reader'
cerf_150_650_DEATHfinal_beta6vtp = XMLPolyDataReader(registrationName='vtp_file', FileName=[path[1:-1]])

# find source


# find source
given_vtp = FindSource('given_vtp')

# Properties modified on cerf_150_650_DEATHfinal_beta6vtp
cerf_150_650_DEATHfinal_beta6vtp.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
cerf_150_650_DEATHfinal_beta6vtpDisplay = Show(cerf_150_650_DEATHfinal_beta6vtp, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
cerf_150_650_DEATHfinal_beta6vtpDisplay.Representation = 'Surface'

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'Type'
typePWF = GetOpacityTransferFunction('Type')

# Rescale transfer function
typePWF.RescaleTransferFunction(0.6666666666666666, 2.0)

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=cerf_150_650_DEATHfinal_beta6vtp)

# set active source




# toggle interactive widget visibility (only when running from the GUI)


# get color transfer function/color map for 'Type'
typeLUT = GetColorTransferFunction('Type')

# get 2D transfer function for 'Type'
typeTF2D = GetTransferFunction2D('Type')

# get display properties


# set active source
SetActiveSource(transform1)



# toggle interactive widget visibility (only when running from the GUI)


# set active source
SetActiveSource(transform1)

# toggle interactive widget visibility (only when running from the GUI)
source = cerf_150_650_DEATHfinal_beta6vtp
bounds = source.GetDataInformation().GetBounds()

# Extract bounds
x_min, x_max, y_min, y_max, z_min, z_max = bounds

x_bound=x_max-x_min
y_bound=y_max-y_min
scale=[1481/x_bound,609/y_bound,1]

# Properties modified on transform1.Transform
transform1.Transform.Scale = scale

# show data in view
transform1Display = Show(transform1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'

# hide data in view
Hide(cerf_150_650_DEATHfinal_beta6vtp, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints1 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints1', Input=transform1)

# Properties modified on tTKIcospheresFromPoints1
tTKIcospheresFromPoints1.Radius = 2.0

# show data in view
tTKIcospheresFromPoints1Display = Show(tTKIcospheresFromPoints1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKIcospheresFromPoints1Display.Representation = 'Surface'

# update the view to ensure updated data information
renderView1.Update()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1481, 609)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.ResetCamera(True, 0.8)

##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------
