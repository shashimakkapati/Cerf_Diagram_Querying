vtpath=input("input vtp file path")
import math
from paraview.simple import *

paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML PolyData Reader'
combined_lines_finalvtp = XMLPolyDataReader(registrationName='combined_lines_final.vtp', FileName=[vtpath[1:-1]])
dim=int(input("enter dimension "))
# Properties modified on combined_lines_finalvtp
combined_lines_finalvtp.TimeArray = 'None'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
combined_lines_finalvtpDisplay = Show(combined_lines_finalvtp, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
combined_lines_finalvtpDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera(False, 0.9)


# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
combined_lines_finalvtpDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'Type'
typeLUT = GetColorTransferFunction('Type')

# get opacity transfer function/opacity map for 'Type'
typePWF = GetOpacityTransferFunction('Type')

# get 2D transfer function for 'Type'
typeTF2D = GetTransferFunction2D('Type')
renderView1 = GetActiveViewOrCreate('RenderView')
source = GetActiveSource()
bounds = source.GetDataInformation().GetBounds()

# Extract bounds
x_min, x_max, y_min, y_max, z_min, z_max = bounds
x_bound=x_max-x_min
y_bound=y_max-y_min
scale=[1481/x_bound,609/y_bound,1]

rgb=[]
# get color transfer function/color map for 'Type'
typeLUT.ApplyPreset('Traffic Lights Step', True)

for i in range(dim+1):
    red=i/dim
    green=4*((i/dim)-(i/dim)*(i/dim))
    blue=(dim-i)/dim
    
    rgb += [2*i/(dim+1),red, green, blue, 2*(i+1)/(dim+1), red, green,blue ]
typeLUT.RGBPoints = rgb
renderView1 = GetActiveViewOrCreate('RenderView')

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
#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels


#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
eps=0.001

# Rescale transfer function
typeLUT.RescaleTransferFunction(0.0, 2)

# Rescale transfer function
typePWF.RescaleTransferFunction(0.0, 2)

# Rescale 2D transfer function
typeTF2D.RescaleTransferFunction(0.0, 2, 0.0, 2)

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=combined_lines_finalvtp)

# Properties modified on transform1.Transform
transform1.Transform.Scale = scale

# show data in view
transform1Display = Show(transform1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
transform1Display.Representation = 'Surface'

# hide data in view
Hide(combined_lines_finalvtp, renderView1)

# show color bar/color legend
transform1Display.SetScalarBarVisibility(renderView1, True)
transform1.UpdatePipeline()
# update the view to ensure updated data information
renderView1.Update()

# Properties modified on renderView1
renderView1.UseColorPaletteForBackground = 0

# Properties modified on renderView1
renderView1.Background = [1.0, 1.0, 1.0]



# Set line width (e.g., 2.0 is thicker than default 1.0)
transform1Display.LineWidth = 2.0






# Render to apply the changes
Render()

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1481, 609)

#-----------------------------------
# saving camera placements for views





# find source
transform1 = FindSource('Transform1')

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=transform1)

# find source
combined_lines_finalvtp = FindSource('combined_lines_final.vtp')

# Properties modified on calculator1
calculator1.AttributeType = 'Point Data'
calculator1.Function = 'coordsX/'+str(scale[0])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
calculator1Display = Show(calculator1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'

# hide data in view
Hide(transform1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'Result'
resultLUT = GetColorTransferFunction('Result')

# get opacity transfer function/opacity map for 'Result'
resultPWF = GetOpacityTransferFunction('Result')

# get 2D transfer function for 'Result'
resultTF2D = GetTransferFunction2D('Result')

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=calculator1)

# show data in view
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(threshold1Display, ('CELLS', 'Type'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(resultLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
threshold1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)
threshold1.UpdatePipeline()
# get color transfer function/color map for 'Type'
typeLUT = GetColorTransferFunction('Type')

# get opacity transfer function/opacity map for 'Type'
typePWF = GetOpacityTransferFunction('Type')
RenameSource('Time_Range', threshold1)
Hide(threshold1, renderView1)
# get 2D transfer function for 'Type'
typeTF2D = GetTransferFunction2D('Type')
for i in range(max(dim,3)):
    threshold1 = Threshold(registrationName='Threshold'+chr((ord('x')+i)%123), Input=threshold1)
    

    # Properties modified on threshold2
    threshold1.Scalars = ['CELLS', chr(ord('x')+i)+'coordinates']

    # show data in view
    threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties
    threshold1Display.Representation = 'Surface'

    # hide data in view
    

    # show color bar/color legend
    threshold1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # set scalar coloring
    ColorBy(threshold1Display, ('CELLS', 'Type'))
    threshold1.UpdatePipeline()

    # Hide the scalar bar for this color map if no visible data is colored by it
    HideScalarBarIfNotNeeded(resultLUT, renderView1)

    # rescale color and/or opacity maps used to include current data range
    threshold1Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    threshold1Display.SetScalarBarVisibility(renderView1, True)
    Hide(threshold1, renderView1)


# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=threshold1)
eps=0.001
# Properties modified on threshold2
threshold2.Scalars = ['CELLS', 'Type']
threshold2.LowerThreshold = 2/(dim+1) 
threshold2.UpperThreshold = 2/(dim+1) 
# show data in view
threshold2Display = Show(threshold2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'

# hide data in view
Hide(threshold1, renderView1)

# show color bar/color legend
threshold2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(threshold2Display, ('CELLS', 'Type'))
threshold2.UpdatePipeline()
# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(resultLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
threshold2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
threshold2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(threshold1)
for i in range(2,dim+1):
    threshold=Threshold(registrationName='Threshold'+str(i), Input=threshold1)

    threshold.Scalars = ['CELLS', 'Type']
    threshold.LowerThreshold = 2*i/(dim+1)
    threshold.UpperThreshold =  2*i/(dim+1)
    threshold.UpdatePipeline()

    # show data in view
    thresholdDisplay = Show(threshold, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties
    thresholdDisplay.Representation = 'Surface'

    # hide data in view
    
    # show color bar/color legend
    thresholdDisplay.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # set scalar coloring
    ColorBy(thresholdDisplay, ('CELLS', 'Type'))

    # Hide the scalar bar for this color map if no visible data is colored by it
    HideScalarBarIfNotNeeded(resultLUT, renderView1)

    # rescale color and/or opacity maps used to include current data range
    thresholdDisplay.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    thresholdDisplay.SetScalarBarVisibility(renderView1, True)

    # set active source
    SetActiveSource(threshold1)
    RenameSource('Saddle'+str(i-1), threshold)
  

# create a new 'Threshold'
threshold4 = Threshold(registrationName='Threshold4', Input=threshold1)

# Properties modified on threshold4
threshold4.Scalars = ['CELLS', 'Type']
threshold4.LowerThreshold = 2
threshold4.UpperThreshold = 2

# show data in view
threshold4Display = Show(threshold4, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold4Display.Representation = 'Surface'

# hide data in view
Hide(threshold1, renderView1)

# show color bar/color legend
threshold4Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(threshold4Display, ('CELLS', 'Type'))
threshold4.UpdatePipeline()
# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(resultLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
threshold4Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
threshold4Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(threshold1)

# create a new 'Threshold'




# set active source
SetActiveSource(transform1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=transform1.Transform)

# get display properties
transform1Display = GetDisplayProperties(transform1, view=renderView1)

# rename source object
RenameSource('Scale_Data', transform1)

# set active source
SetActiveSource(calculator1)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=transform1.Transform)

# set active source
SetActiveSource(threshold1)

# rename source object


# set active source
SetActiveSource(threshold2)

# hide data in view
Hide(threshold4, renderView1)

# hide data in view
Hide(threshold2, renderView1)

# hide data in view


# set active source


# set active source
SetActiveSource(threshold4)

# set active source
SetActiveSource(threshold4)

# show data in view
threshold4Display = Show(threshold4, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
threshold4Display.SetScalarBarVisibility(renderView1, True)

RenameProxy(threshold4, 'sources', 'Maximum')

# rename source object
RenameSource('Maximum', threshold4)

# hide data in view
Hide(threshold4, renderView1)



# show data in view

# set active source
SetActiveSource(threshold2)

RenameProxy(threshold2, 'sources', 'Minimum')

# rename source object
RenameSource('Minimum', threshold2)

# set active source
SetActiveSource(threshold2)

# show data in view
threshold2Display = Show(threshold2, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
threshold2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(threshold4)

# show data in view
threshold4Display = Show(threshold4, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
threshold4Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(threshold1)


# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.XTitle = 'Time'
renderView1.AxesGrid.YTitle = 'Function Value'
renderView1.AxesGrid.XTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.YTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.XLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.YLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.DataScale = scale
SetActiveSource(threshold1)
time_Range = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
time_RangeDisplay = GetDisplayProperties(time_Range, view=renderView1)

# rescale color and/or opacity maps used to exactly fit the current data range
time_RangeDisplay.RescaleTransferFunctionToDataRange(False, True)

# get color transfer function/color map for 'Type'
typeLUT = GetColorTransferFunction('Type')

# get opacity transfer function/opacity map for 'Type'
typePWF = GetOpacityTransferFunction('Type')

# get 2D transfer function for 'Type'
typeTF2D = GetTransferFunction2D('Type')
RenameSource('given_vtp', combined_lines_finalvtp)
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
renderView1 = GetActiveViewOrCreate('RenderView')
renderView1.InteractionMode = '2D'
renderView1.ResetCamera(True, 0.8)
