
input_dem_fp = "E:/a_new_orgs/carleton/hist5706-maryland/lidar_files/reprojected/laz_utm_0-49/dem_tifs/"
output_slope_fp = "E:/a_new_orgs/carleton/hist5706-maryland/lidar_files/slope/"

import time
import os
#process .laz files one at a time
for root, dirs, files in os.walk(input_dem_fp, topdown=False):
   for name in files:      
      print(name)
      name_ext = name[-4:].lower()
      if(name_ext==".tif"):
          dem_in_path = os.path.join(input_dem_fp, name)
          slope_out_path = os.path.join(output_slope_fp, ("slope_"+ name))
          
          params = { 'CRS' : QgsCoordinateReferenceSystem('EPSG:26918'), 'INPUT' : dem_in_path}
          result = processing.run("gdal:assignprojection", params)
          result_layer = result['OUTPUT']
    
          params = { 'AS_PERCENT' : False, 'BAND' : 1, 'COMPUTE_EDGES' : False, 'EXTRA' : '', 'INPUT' : dem_in_path, 'OPTIONS' : '', 'OUTPUT' : slope_out_path, 'SCALE' : 1, 'ZEVENBERGEN' : False }
          result = processing.run("gdal:slope", params)
          result_layer_slope = result['OUTPUT']
          time.sleep(4)
    
          
