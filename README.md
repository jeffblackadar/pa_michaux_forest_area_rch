# maryland_rch

Main repository

# Required software

+CloudCompare
+QGIS
+GoogleColab

## Process flow

https://jeffblackadar.github.io/maryland_rch/maryland_rch-lidar.html

##File work areas

There are two file works areas
+ (local drive) local PC: E:\a_new_orgs\carleton\hist5706-maryland\lidar_files
+ (Google Drive) Google Drive: 

### Download files from Google Drive to local drive
There is a constraint that only a 2gb zip file can be downloaded at one time. The .laz files are large so they have been batched into units of 50.
Download each batch.

### Local processing

The local PC has CloudCompare and QGIS installed, these are not available on Google Colab so it's necessary to moved files from Google Drive and process them on a PC and then move them back. Manual tasks but I could not find a better means to process these files using this collection of software.
On the local PC laz files will be converted to DEM using CloudCompare. CloudCompare is not installed on Google Colab so it's used on the local PC.

4 batches of 50 laz files (ex: 0-49, 50-99, 100-149, 150-199) will be downloaed into a folder that can contain 200 files (ex: laz_utm_0-199).

Create folders to hold downladed files. Example: E:\a_new_orgs\carleton\hist5706-maryland\lidar_files\reprojected\laz_utm_0-199. This can be done by running the first cell of 1_1_Maryland_download_laz_tiles_use_CloudCompare_to_convert_to_DEM

Download the files from Google Drive, unzip into directory. Example: /content/drive/MyDrive/crane_maryland/laz/laz_fema_2012_forested_utm/batch_50/laz_utm_0-49 









####



