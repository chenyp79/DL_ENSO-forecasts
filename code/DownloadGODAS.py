"""
DownloadGODAS.py
这个脚本用来下载GODAS SSH数据
"""
import wget
import os
dest_folder =  os.getcwd() + '\\GODAS\\' #当前py目录下定义GODAS文件夹
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)#新建GODAS文件夹
    
ini = "ftp://ftp2.psl.noaa.gov/Datasets/godas/sshg.%s.nc"
for year in range(1980, 2020):
    file = wget.download(ini % year, dest_folder +"%sSSH.nc" % year)
    print(file)


