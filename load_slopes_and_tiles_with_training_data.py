import os
from qgis.core import *
import qgis.utils

def check_path(fp):
    return  
    if not os.path.exists(fp):
        print("missing: ", fp)
        os.makedirs(fp)
        if not os.path.exists(fp):
            print("still missing: ", fp)
        else:
            print("made directory: ", fp)

#batch_group = "pa_northcentral_2019_b19"
#batch_group = "pa_allentown_2016"
#batch_group = "pa_3_county_south_central_2018_d18"
#batch_group = "pa_luzernecounty_2018"
#batch_group = "pa_sandy_2014"
#batch_group = "pa_south_central_b1_2017"
batch_group = "pa_south_central_b2_2017"
#batch_group = "pa_dauphin_2016"
#batch_group = "pa_westernpa_2019_d20"
#batch_group = "de_delawarevalley_hd_2015"
#batch_group ="md-pa_sandysupp_2014"

#dem_tif_fp = os.path.join("/content/drive/MyDrive/crane_pennsylvania/dem/",batch_group)
#check_path(dem_tif_fp)
slope_tif_fp = os.path.join("G:\\My Drive\\crane_pennsylvania\\slope\\",batch_group)
check_path(slope_tif_fp)
slope_tif_tiles_fp = os.path.join(slope_tif_fp,"tiles640\\")
check_path(slope_tif_tiles_fp)
slope_tif_tiles_jpgs_fp = os.path.join(slope_tif_tiles_fp,"jpgs\\")
check_path(slope_tif_tiles_jpgs_fp)
slope_tif_tiles_polys_fp = os.path.join(slope_tif_tiles_fp,"polys\\")
check_path(slope_tif_tiles_polys_fp)
prediction_fp = 'G:\\My Drive\\crane_pennsylvania\\predictions\\project_'+batch_group+'\\'
check_path(prediction_fp)
#prediction_xmls_fp = '/content/drive/MyDrive/crane_pennsylvania/predictions/project_'+batch_group+'/xmls/'
#check_path(prediction_xmls_fp)

rasters_fp = os.path.join(prediction_fp,"rasters_with_points.txt")

raster_list_file = open(rasters_fp, 'r')
#  /content/drive/MyDrive/crane_pennsylvania/slope/pa_south_central_b1_2017/tiles/USGS_one_meter_x25y441_PA_South_Central_B1_2017r00c00.tif
for filename in raster_list_file:
    
    slope_tif_tile_fp = os.path.join(slope_tif_tiles_fp, filename.strip())
    
    if slope_tif_tile_fp[-17:-15]=="B2":
        print(slope_tif_tile_fp,slope_tif_tile_fp[-17:-15])
        rlayer = iface.addRasterLayer(slope_tif_tile_fp, filename)

raster_list_file.close()    