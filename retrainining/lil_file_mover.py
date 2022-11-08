import os
from qgis.core import *
import qgis.utils
import shutil
import qgis.PyQt


def check_path(fp):
    return  
    if not os.path.exists(fp):
        print("missing: ", fp)
        # os.makedirs(fp)
        if not os.path.exists(fp):
            print("still missing: ", fp)
        else:
            print("made directory: ", fp)

"""
# done 7 Nov 2022
batch_group = "pa_south_central_b1_2017"

subject_files = ["USGS_one_meter_x37y454_PA_South_Central_B1_2017.tif",
"USGS_one_meter_x38y454_PA_South_Central_B1_2017.tif",
"USGS_one_meter_x38y453_PA_South_Central_B1_2017.tif",
"USGS_one_meter_x38y455_PA_South_Central_B1_2017.tif",
"USGS_one_meter_x26y444_PA_South_Central_B1_2017.tif",
"USGS_one_meter_x27y445_PA_South_Central_B1_2017.tif"]

subject_files = ["USGS_one_meter_x38y456_PA_South_Central_B1_2017.tif"]
"""

"""
batch_group = "pa_south_central_b2_2017"
subject_files = ["USGS_one_meter_x35y454_PA_South_Central_B2_2017.tif"]
"""


"""
batch_group = "pa_northcentral_2019_b19"
subject_files = ["USGS_1M_18_x43y451_PA_Northcentral_2019_B19.tif",
"USGS_1M_18_x43y452_PA_Northcentral_2019_B19.tif",
"USGS_1M_18_x44y452_PA_Northcentral_2019_B19.tif"]
"""

batch_group = "pa_3_county_south_central_2018_d18"
subject_files = ["USGS_1M_18_x42y446_PA_3_County_South_Central_2018_D18.tif",
"USGS_1M_18_x43y446_PA_3_County_South_Central_2018_D18.tif",
"USGS_1M_18_x43y445_PA_3_County_South_Central_2018_D18.tif"]


project_fp = "G:\\My Drive\\crane_pennsylvania\\pa_michaux_forest_area_rch\\qgis_retraining_project\\"
dem_dest_fp = os.path.join(project_fp,"dem\\")
dem_dest_fp = os.path.join(dem_dest_fp,(batch_group+"\\"))
check_path(dem_dest_fp)

slope_dest_fp = os.path.join(project_fp,"slope\\")
slope_dest_fp = os.path.join(slope_dest_fp,(batch_group+"\\"))
check_path(slope_dest_fp)

tile_grid_dest_fp = os.path.join(project_fp,"tile_grid\\")
tile_grid_dest_fp = os.path.join(tile_grid_dest_fp,(batch_group+"\\"))
check_path(tile_grid_dest_fp)
mySymbol1 = QgsFillSymbol.createSimple({'color':'255,0,0,0',
    'color_border':'#009900',
    'width_border':'0.3'})


for subject_file in subject_files:
    print(subject_file)
    dem_dest_filep = os.path.join(dem_dest_fp, subject_file)
    # shutil.copyfile(dem_source_filep, dem_dest_filep)
    rlayer = iface.addRasterLayer(dem_dest_filep, ("dem_"+subject_file))

    slope_dest_filep = os.path.join(slope_dest_fp, subject_file)
    # shutil.copyfile(slope_source_filep, slope_dest_filep)
    rlayer = iface.addRasterLayer(slope_dest_filep, ("slope_"+subject_file))

    tile_grid_dest_filep = os.path.join(tile_grid_dest_fp,(subject_file[:-4]+"r15c15_tile_poly"))
    print(tile_grid_dest_filep+".shp")
    vlayer = iface.addVectorLayer(tile_grid_dest_filep+".shp", ("tile_grid_"+subject_file[:-4]),"ogr")
    myRenderer  = vlayer.renderer()

    myRenderer.setSymbol(mySymbol1)
    vlayer.triggerRepaint()