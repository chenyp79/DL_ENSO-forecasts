# coding: UTF-8
import os

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
            Toslist.append(xr.open_dataset(file_path)["tos"])
        else:
            Zoslist.append(xr.open_dataset(loc + '/' + FName)["zos"])
print(Toslist)
