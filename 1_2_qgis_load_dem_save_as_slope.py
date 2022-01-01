# Run after CloudCompare has created DEMs
# Check the directories. They must be changed manually for each batch of 200

"""
This program uses QGIS Process Algorithms. These Process Algorithms are like macros that allow QGIS tasks to be run from Python.
For example a slope tif can be created from the menu Raster | Analysis | Slope
But it can also be run as a process.

## Algorithm ID
Each process has a name.  To see the name of the process, open the Processing Toolbox, locate the process, hover over it with a mouse to see the tooltip.
For example, the Slope process is listed in the Processing Toolbox as GDAL | Raster Analysis | Slope with an Algorithm ID of 'gdal:slope'
The Algorithm ID is needed to run the process result = processing.run("gdal:slope", params)

## Process

### Set crs = EPSG:26918

### Create slope tif
"""
batch_group = "1000-1599"
input_dem_fp = "E:/a_new_orgs/carleton/hist5706-maryland/lidar_files/reprojected/laz_utm_"+batch_group+"/dem_tifs/"
output_slope_fp = "E:/a_new_orgs/carleton/hist5706-maryland/lidar_files/slope/slope_"+batch_group+"/"

import time
import os
#process .laz files one at a time
for root, dirs, files in os.walk(input_dem_fp, topdown=False):
   for name in files:      
      print(name)
      name_ext = name[-4:].lower()
      if(name_ext==".tif"):
          dem_in_path = os.path.join(input_dem_fp, name)
          slope_out_path = os.path.join(output_slope_fp, ("slope_"+ name[:name.find("_utm")+4]+".tif"))
          
          params = { 'CRS' : QgsCoordinateReferenceSystem('EPSG:26918'), 'INPUT' : dem_in_path}
          result = processing.run("gdal:assignprojection", params)
          result_layer = result['OUTPUT']
    
          params = { 'AS_PERCENT' : False, 'BAND' : 1, 'COMPUTE_EDGES' : False, 'EXTRA' : '', 'INPUT' : dem_in_path, 'OPTIONS' : '', 'OUTPUT' : slope_out_path, 'SCALE' : 1, 'ZEVENBERGEN' : False }
          result = processing.run("gdal:slope", params)
          result_layer_slope = result['OUTPUT']   
    
          
