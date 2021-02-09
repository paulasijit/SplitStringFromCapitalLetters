'''
__author__ = "Asijit Paul"
__maintainer__ = "Asijit Paul"
__status__ = "Final"
'''
import sys
import re
def swap_string(str):
    n = ['1','2','3','4','5','6','7','8','9']
    c = 0
    if len(str) <= 1:
        return str
    for i in str:
        if i in n:
            break
        else:
            c += 1
    if c == len(str):
        return str
    arr = []
    res = ''
    for i in str:
        arr.append(i)
    arr[c], arr[c+1] = arr[c+1], arr[c]
    for i in arr:
        res += i
    res = res
    return res

arr = 'name	locIDStart	locIDEnd	startDay	startTime	endDay	endTime	tagPri2AxlesAuto	tagPri3AxlesAuto	tagPri4AxlesAuto	tagSec2AxlesAuto	tagSec3AxlesAuto	tagSec4AxlesAuto	cash2AxlesAuto	cash3AxlesAuto	cash4AxlesAuto	licPlate2AxlesAuto	licPlate3AxlesAuto	licPlate4AxlesAuto	cCard2AxlesAuto	cCard3AxlesAuto	cCard4AxlesAuto	prePaid2AxlesAuto	prePaid3AxlesAuto	prePaid4AxlesAuto	tagPri2AxlesLGV	tagPri2AxlesHGV	tagPri3AxlesTruck	tagPri4AxlesTruck	tagPri5AxlesTruck	tagPri6AxlesTruck	tagPri7AxlesTruck	tagSec2AxlesLGV	tagSec2AxlesHGV	tagSec3AxlesTruck	tagSec4AxlesTruck	tagSec5AxlesTruck	tagSec6AxlesTruck	tagSec7AxlesTruck	cash2AxlesLGV	cash2AxlesHGV	cash3AxlesTruck	cash4AxlesTruck	cash5AxlesTruck	cash6AxlesTruck	cash7AxlesTruck	licPlate2AxlesLGV	licPlate2AxlesHGV	licPlate3AxlesTruck	licPlate4AxlesTruck	licPlate5AxlesTruck	licPlate6AxlesTruck	licPlate7AxlesTruck	cCard2AxlesLGV	cCard2AxlesHGV	cCard3AxlesTruck	cCard4AxlesTruck	cCard5AxlesTruck	cCard6AxlesTruck	cCard7AxlesTruck	prePaid2AxlesLGV	prePaid2AxlesHGV	prePaid3AxlesTruck	prePaid4AxlesTruck	prePaid5AxlesTruck	prePaid6AxlesTruck	prePaid7AxlesTruck	tagPri2AxlesBus	tagPri3AxlesBus	tagPri4AxlesBus	tagSec2AxlesBus	tagSec3AxlesBus	tagSec4AxlesBus	cash2AxlesBus	cash3AxlesBus	cash4AxlesBus	licPlate2AxlesBus	licPlate3AxlesBus	licPlate4AxlesBus	cCard2AxlesBus	cCard3AxlesBus	cCard4AxlesBus	prePaid2AxlesBus	prePaid3AxlesBus	prePaid4AxlesBus	tagPri2AxlesMoto	tagSec2AxlesMoto	cash2AxlesMoto	licPlate2AxlesMoto	cCard2AxlesMoto	prePaid2AxlesMoto	tagPri2AxlesCaravanVan	tagPri3AxlesCaravanVan	tagPri4AxlesCaravanVan	tagSec2AxlesCaravanVan	tagSec3AxlesCaravanVan	tagSec4AxlesCaravanVan	cash2AxlesCaravanVan	cash3AxlesCaravanVan	cash4AxlesCaravanVan	licPlate2AxlesCaravanVan	licPlate3AxlesCaravanVan	licPlate4AxlesCaravanVan	cCard2AxlesCaravanVan	cCard3AxlesCaravanVan	cCard4AxlesCaravanVan	prePaid2AxlesCaravanVan	prePaid3AxlesCaravanVan	prePaid4AxlesCaravanVan	roadName	tagPrimary	tagSecondary	licPlatePrimary	licPlateSecondary	discountCarDetails	discountCarType	discountTruckDetails	discountTrucks	height	weight	length'.split()

count = 1
for i in arr:
    res = ''
    re_outer = re.compile(r'([^A-Z ])([A-Z])')
    re_inner = re.compile(r'(?<!^)([A-Z])([^A-Z])')
    s=re_outer.sub(r'\1 \2', re_inner.sub(r' \1\2', i)).lower()
    l = s
    for i in range(0, len(l)):
        if l[i] == " ":
            res += '_'
        else:
            res += l[i]
    count += 1
    result = swap_string(res)
    sys.stdout = open("result.txt", "a")
    print(result)
    sys.stdout.close()
