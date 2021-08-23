"""
DownCmip6.py
这个脚本用来下载 Cmip6 GFDL_ESM4的 zos, tos数据
"""
import os
Cmip6 = "/content/DL/Cmip6"
if os.path.isdir(Cmip6):
  pass
else:
    os.mkdir(Cmip6)
    
import wget
ini = r"https://esgdata.gfdl.noaa.gov/thredds/fileServer/gfdl_dataroot4/CMIP/" + \
      r"NOAA-GFDL/GFDL-ESM4/historical/r1i1p1f1/Omon/%s/gr/v20190726/%s_Omon_GFDL-ESM4_historical_r1i1p1f1_gr_%s-%s.nc"
#
for var in ["tos", "zos"]:
    for year in range(1850, 2019, 20):
        time1 = str(year) + str(0) + str(1)
        time2 = str(year + 19) + str(12)
        if int(time2)>201412:  #数据只到201412
            time2="201412"
        NeedUrl = ini % (var, var, time1, time2)
        #print(NeedUrl)
        fileName = "GFDL-ESM4_%s_%s-%s.nc" % (var, time1, time2)
        print(fileName)
        wget.download(NeedUrl, '/content/DL/Cmip6/' + fileName)
