"""
本 脚本用来 merge ersstv5数据
"""

import xarray as xr
import os
import pandas as pd
fileLoc = "/content/DL/ersstv5/"
fList = os.listdir(fileLoc)
print(fList)
# 对下载的nc文件进行合并
ncList = []
for FileName in fList:
    nc = xr.open_dataset(fileLoc + r"/" + FileName)["sst"]
    ncList.append(nc)
# 使用 concat 进行合并，不过会很慢
sst1 = xr.concat(ncList, dim="time")
# print(sst1)
print(sst1.shape)
# 画出来看看
sst1[100].plot()
plt.show()

# 统一时间格式并保存
Time = pd.date_range(start="18540101", end="20201231", freq="MS")
sst1["time"] = Time
print(sst1)

SstSave = xr.Dataset({"sst": sst1})
SstSave.to_netcdf("/content/DL/ersstMerge.nc")
