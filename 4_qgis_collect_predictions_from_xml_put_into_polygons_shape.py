def get_posx_posy(xoffset, px_w, rot1, yoffset, px_h, rot2,x,y):
    # supposing x and y are your pixel coordinate this 
    # is how to get the coordinate in space.
    posX = px_w * x + rot1 * y + xoffset
    posY = rot2 * x + px_h * y + yoffset

    # shift to the center of the pixel
    posX += px_w / 2.0
    posY += px_h / 2.0
    return posX,posY

def get_poly_from_geotif_with_x_y(geotif_fp,minx,miny,maxx,maxy):
    ds = gdal.Open(geotif_fp)
    # open the dataset and get the geo transform matrix

    xoffset, px_w, rot1, yoffset, rot2,px_h = ds.GetGeoTransform()

    #print("xoffset, px_w, rot1, yoffset, px_h, rot2",xoffset, px_w, rot1, yoffset, px_h, rot2)
    print("minx,miny,maxx,maxy",minx,miny,maxx,maxy)

    pos1x,pos1y = get_posx_posy(xoffset, px_w, rot1, yoffset, px_h, rot2,minx,miny)
    pos2x,pos2y = get_posx_posy(xoffset, px_w, rot1, yoffset, px_h, rot2,minx,maxy)
    pos3x,pos3y = get_posx_posy(xoffset, px_w, rot1, yoffset, px_h, rot2,maxx,maxy)
    pos4x,pos4y = get_posx_posy(xoffset, px_w, rot1, yoffset, px_h, rot2,maxx,miny)
    coords = [(pos1x,pos1y), (pos2x,pos2y), (pos3x,pos3y), (pos4x,pos4y)]

    #print("pos",pos1x,pos1y,pos2x,pos2y,pos3x,pos3y,pos4x,pos4y)
    poly = Polygon(coords)
    
    return poly 

# Looping through them repeatedly takes a long time.
# Instead, create a dictionary of files indexed by area.  Each entry holds a list of matching files
# This makes it easier to process these files by area.

import csv
from os import listdir
import os
construction_type = "charcoal_hearth_hill"
cfg_name = 'cfg20200826T2315'

#make a dict of all the areas + pan (or pas)
area_crs_dict = {}

area_crs_dict["catoctin_1"] = []

# Now that the dictionary is created, add all of the matching files as a list linked to the entry.
print("Now that the dictionary is created, add all of the matching files as a list linked to the entry.")
# This dictionary will be used below.
batch_group = '0-199'
annot_prediction_folder = os.path.join('E:\\a_new_orgs\\carleton\\hist5706-maryland\\lidar_files\\predictions\\cfg20200826T2315\\unknown\\'+batch_group+'\\')

for annot_filename in listdir(annot_prediction_folder):
    annot_area = "catoctin_1"
    print(annot_filename, annot_area)
    area_node = area_crs_dict[annot_area]
    area_node.append(annot_filename)
print(area_crs_dict)


# cell 2.2 
construction_type = "charcoal_hearth_hill"
cfg_name = 'cfg20200826T2315'
model_epoch='0016'


split_tifs_folder = 'E:\\a_new_orgs\\carleton\\hist5706-maryland\\lidar_files\\slope\\slope_'+batch_group+'\\'
# display image with masks and bounding boxes
from os import listdir


from xml.etree import ElementTree
#https://gis.stackexchange.com/questions/92207/split-a-large-geotiff-into-smaller-regions-with-python-and-gdal

import numpy
from osgeo import gdal, osr
import math
from itertools import chain
import geopandas as gpd
from shapely.geometry import Point, Polygon
import numpy as np
import gdalnumeric
import os

def put_preds_in_shp(state_area,state_area_num_crs):

    pred_polys = gpd.GeoDataFrame()
    pred_polys['geometry'] = None
    
    #pred_polys = pred_polys.crs(epsg=state_area_num_crs)
    pred_polys.crs = ("EPSG:" + str(state_area_num_crs))
    
    #pred_polys.geometry = pred_polys.geometry.crs(epsg=state_area_num_crs)
    pred_polys.geometry.crs = ("EPSG:" + str(state_area_num_crs))
    print("pred_polys.crs",pred_polys.crs, pred_polys.geometry.crs)
    
    import cv2

    #Store the results in XML    
    class_names = construction_type

    # find all images

    pa = area_crs_dict[str(state_area)]
    for annot_filename in pa:
    
        print(annot_filename)
        #process only the files for this state land area, since other areas may not match crs
        #if annot_filename.startswith(state_area_num):
        tree = ElementTree.parse(annot_prediction_folder+annot_filename)
        print(annot_prediction_folder+annot_filename)
        #print(tree)
        # get the root of the document
        root = tree.getroot()
        # extract each bounding box
    
        fn_image = root.find('./filename').text
        #object_present = root.find('./object_present').text
        fn_base = fn_image[:6]
        print(fn_base)
        box_num=0
        for obj in root.findall('./object'):
            score = obj.find('score').text
    
            box = obj.find('bndbox')
            box_num=obj.find('number').text
            box_num_pad = "00"+str(box_num)
            box_num_pad = box_num_pad[-2:]
            #boxes_correct[str(box_num)] = correct
            xmin = int(box.find('xmin').text)
            ymin = int(box.find('ymin').text)
            xmax = int(box.find('xmax').text)
            ymax = int(box.find('ymax').text)
            if(ymin>ymax):
                ytemp = ymin
                ymin = ymax
                ymax=ytemp
            if(xmin>xmax):
                xtemp = xmin
                xmin = xmax
                xmax=xtemp            
            coors = [xmin, ymin, xmax, ymax]
            print("score", score, coors)
            print(os.path.join(split_tifs_folder+(fn_base+".tif")))
            pred_poly = get_poly_from_geotif_with_x_y(os.path.join(split_tifs_folder+(fn_base+".tif")),xmin,ymin,xmax,ymax)
            new_pp_row = {'id':fn_base+box_num_pad, 'geometry':pred_poly, 'score':score}
            pred_polys = pred_polys.append(new_pp_row, ignore_index=True)
            print("pred_polys.crs",pred_polys.crs, pred_polys.geometry.crs)
            pred_polys.geometry.crs = ("EPSG:" + str(state_area_num_crs))
            print("pred_polys.crs",pred_polys.crs, pred_polys.geometry.crs)

    outfolder = os.path.join("E:\\a_new_orgs\\carleton\\hist5706-maryland\\lidar_files\\predictions\\cfg20200826T2315\\", (cfg_name+"\\"),"\\polys\\",(batch_group+"\\"))
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)
    outfp = os.path.join(outfolder,(state_area + "_predictions.shp"))
                         
# Write the data into that Shapefile
    if not pred_polys.empty:
        print("pred_polys.crs",pred_polys.crs, pred_polys.geometry.crs)
        pred_polys.to_file(outfp)
        #pred_polys.head()
        #pred_polys = pred_polys.to_crs({'init':'epsg:4326'})
        #pred_polys = pred_polys.to_crs(epsg = 4326)
        """
        crs_4326 = 4326
        pred_polys.geometry = pred_polys.geometry.to_crs(crs=crs_4326)
        pred_polys.to_crs(crs=crs_4326)
        pred_polys = pred_polys.to_crs(epsg=crs_4326)
        
        #pred_polys = pred_polys.set_crs(epsg = 4326)
        #pred_polys.head()
        outfp = os.path.join(outfolder,("4326_" + state_area + "_predictions.shp"))
        # Write the data into that Shapefile
        pred_polys.to_file(outfp)
        """
 
 put_preds_in_shp("catoctin_1",26985)