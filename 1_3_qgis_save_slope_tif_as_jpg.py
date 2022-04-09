batch_group = "0-597"
input_slope_tif_fp = "E:/a_new_orgs/carleton/pennsylvania_michaux/lidar_files/slope/slope_"+batch_group+"/"
output_slope_jpg_fp = "E:/a_new_orgs/carleton/pennsylvania_michaux/lidar_files/slope/slope_"+batch_group+"/jpgs/"

#Convert tifs to jpgs 
import gdal
import numpy as np
import gdalnumeric
import os

def tif_to_jpg(tif_file, output_file_name, output_folder):
    #print(tif_file,output_file_name, output_folder)
    ds = gdal.Open(tif_file)
    #geoTrans = srcImage.GetGeoTransform()
    band = ds.GetRasterBand(1)
    width = ds.RasterXSize
    height = ds.RasterYSize

    data = band.ReadAsArray(0, 0, width, height)
    #convert all the bad data
    data[data==-9999.0] = 0
    max_value = np.max(data)
    color_multiplier = 255/(max_value-1)
    #print(color_multiplier)
    data = data*color_multiplier
    #print(data)
    data_int = np.array(data, dtype='int')
    #print(data_int)
    #clip = ds.readasarray(ds)
    data_int = data_int.astype(gdalnumeric.numpy.uint8)
    
    print(os.path.join(output_folder,(output_file_name)))
    gdalnumeric.SaveArray(data_int, os.path.join(output_folder,(output_file_name)), format="JPEG")



if not (os.path.exists(output_slope_jpg_fp)):  
    print("Does not exist.")
    os.mkdir(output_slope_jpg_fp)
else:
    print(output_slope_jpg_fp,"Exists.")

# find all images
counter = 0
for filename in os.listdir(input_slope_tif_fp):
    # extract image id
    image_id = filename[:-4]
    ext = filename[-4:]

    if(ext ==".tif"):
        print(counter, filename)
        img_path = os.path.join(input_slope_tif_fp, filename)
        tif_to_jpg(img_path, (filename[:-4]+".jpg"), output_slope_jpg_fp)
        counter = counter + 1