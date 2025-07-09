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

renderView1 = GetActiveViewOrCreate('RenderView')
renderView1.UseColorPaletteForBackground = 0

# Properties modified on renderView1
renderView1.Background = [1.0, 1.0, 1.0]
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
cerf_final1 = tube_2dim(registrationName='Cerf_final1', Input=combined_lines_finalvtp)
cerf_final1.Function='coordsX/'+str(scale[0])
# show data in view
cerf_final1Display = Show(cerf_final1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
cerf_final1Display.Representation = 'Surface'

# hide data in view
Hide(combined_lines_finalvtp, renderView1)

# show color bar/color legend
cerf_final1Display.SetScalarBarVisibility(renderView1, True)

# show data in view
cerf_final1Display_1 = Show(OutputPort(cerf_final1, 1), renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
cerf_final1Display_1.Representation = 'Surface'

# hide data in view


# show color bar/color legend
cerf_final1Display_1.SetScalarBarVisibility(renderView1, True)

# show data in view
cerf_final1Display_2 = Show(OutputPort(cerf_final1, 2), renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
cerf_final1Display_2.Representation = 'Surface'

# hide data in view



# show color bar/color legend
cerf_final1Display_2.SetScalarBarVisibility(renderView1, True)
ColorBy(cerf_final1Display_1, ('CELLS', 'Type'))
ColorBy(cerf_final1Display_2, ('CELLS', 'Type'))
# update the view to ensure updated data information
renderView1.Update()
renderView1.AxesGrid.Visibility = 1
# Rescale 2D transfer function
typeTF2D.RescaleTransferFunction(0.0, 2, 0.0, 2)
cerf_final1.Transform.Scale = scale
renderView1.AxesGrid.XTitle = 'Time'
renderView1.AxesGrid.YTitle = 'Function Value'
renderView1.AxesGrid.XTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.YTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.XLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.YLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.DataScale = scale
typeLUT = GetColorTransferFunction('Type')

# get opacity transfer function/opacity map for 'Type'
typePWF = GetOpacityTransferFunction('Type')
RenameSource('given_vtp', combined_lines_finalvtp)
#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()
ColorBy(cerf_final1Display_1, ('CELLS', 'Type'))
ColorBy(cerf_final1Display_2, ('CELLS', 'Type'))

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1481, 609)

#-----------------------------------
# saving camera placements for views
renderView1 = GetActiveViewOrCreate('RenderView')
renderView1.InteractionMode = '2D'
renderView1.ResetCamera(True, 0.8)
#########
cerf_final1Display = GetDisplayProperties(cerf_final1, view=renderView1)

# set scalar coloring
ColorBy(cerf_final1Display, ('CELLS', 'Type'))

cerf_final1Display.LineWidth=2
cerf_final1Display_1.LineWidth=2
cerf_final1Display_2.LineWidth=2



# rescale color and/or opacity maps used to include current data range
cerf_final1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
cerf_final1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Type'
typeLUT = GetColorTransferFunction('Type')

# get opacity transfer function/opacity map for 'Type'
typePWF = GetOpacityTransferFunction('Type')

# get 2D transfer function for 'Type'
typeTF2D = GetTransferFunction2D('Type')
typeLUT.ApplyPreset('Traffic Lights Step', True)

for i in range(dim+1):
    red=i/dim
    green=4*((i/dim)-(i/dim)*(i/dim))
    blue=(dim-i)/dim
    
    rgb += [2*i/(dim+1),red, green, blue, 2*(i+1)/(dim+1), red, green,blue ]
typeLUT.RGBPoints = rgb
