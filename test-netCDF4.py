import os
import netCDF4 as nc  #安装 低版本的pip install netCDF4-1.5.2-cp38-cp38-win32.whl
import numpy as np
import xarray as xr
import pandas as pd
# 下载的CMIP6位置
loc = "./Cmip6"

# 使用 xarray 把分散的几个文件merge起来
FileList = os.listdir(loc)  # 获取文件夹下所有文件夹和文件
Toslist = []
Zoslist = []
for FName in FileList:
    ModeName, varName = FName.split("_")[0:2]
    print(FName)
    print(ModeName, varName)
    file_path = os.path.join(loc,FName)
    if ModeName == "GFDL-ESM4":
        if varName == "tos":
            Toslist.append(nc.Dataset(file_path)["tos"])
        else:
            Zoslist.append(nc.Dataset(loc + '/' + FName)["zos"])
print(Toslist)
# 把这两个聚合在一起，形成一个大的Data array

