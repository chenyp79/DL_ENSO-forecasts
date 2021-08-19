"""
DownLersstv5.py
用来下载ersst v5的数据
"""


import wget
import os


dest_folder =  os.getcwd() + '\\ersstv5\\' #当前py目录下定义ersstv5文件夹
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)#新建ersstv5文件夹

    # construct url
for year in range(1854, 2021):
    for month in range(1, 13):
        month = str(month).zfill(2)
        url = "https://www.ncei.noaa.gov/pub/data/cmb/ersst/v5/netcdf/ersst.v5.{}{}.nc".format(year, month)
        file = wget.download(url, out=dest_folder)
        print(file)
        


  
