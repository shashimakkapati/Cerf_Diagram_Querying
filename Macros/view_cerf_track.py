# trace generated using paraview version 5.13.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
vtpath=input("input cerf track file path ")
# get active source.
cerf_final1 = GetActiveSource()
print("Make sure you have generated a track using a file in the queries folder\n")
# set active source
SetActiveSource(cerf_final1)

# create a new 'XML PolyData Reader'
cerf_150_650_line_beta7vtp = XMLPolyDataReader(registrationName='line_query', FileName=[vtpath[1:-1]])

# find source
given_vtp = FindSource('given_vtp')
bounds = given_vtp.GetDataInformation().GetBounds()

scale=[1481/(bounds[1]-bounds[0]),609/(bounds[3]-bounds[2]),1]
# Properties modified on cerf_150_650_line_beta7vtp
cerf_150_650_line_beta7vtp.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
cerf_150_650_line_beta7vtpDisplay = Show(cerf_150_650_line_beta7vtp, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
cerf_150_650_line_beta7vtpDisplay.Representation = 'Surface'

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'Type'
typePWF = GetOpacityTransferFunction('Type')

# Rescale transfer function
typePWF.RescaleTransferFunction(0.6666666666666666, 2.0)

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=cerf_150_650_line_beta7vtp)

# set active source
SetActiveSource(cerf_final1)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=transform1.Transform)

# toggle interactive widget visibility (only when running from the GUI)


# get color transfer function/color map for 'Type'
typeLUT = GetColorTransferFunction('Type')

# get 2D transfer function for 'Type'
typeTF2D = GetTransferFunction2D('Type')

# get display properties


# set active source
SetActiveSource(transform1)

# toggle interactive widget visibility (only when running from the GUI)


# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(cerf_final1)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=transform1.Transform)

# toggle interactive widget visibility (only when running from the GUI)


# set active source
SetActiveSource(transform1)

# toggle interactive widget visibility (only when running from the GUI)


# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=transform1.Transform)

# Properties modified on transform1.Transform
transform1.Transform.Scale = scale


# show data in view
transform1Display = Show(transform1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'

# hide data in view
Hide(cerf_150_650_line_beta7vtp, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=transform1)

# Properties modified on tube1
tube1.Scalars = ['POINTS', '']
tube1.Vectors = ['POINTS', '1']
tube1.Radius = 2.0

# show data in view
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.Opacity = 0.6
# hide data in view
Hide(transform1, renderView1)

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
renderView1.CameraPosition = [740.5087491504908, 304.4990493924131, 3097.740287368718]
renderView1.CameraFocalPoint = [740.5087491504908, 304.4990493924131, 0.0]
renderView1.CameraParallelScale = 380.98211100167947


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
