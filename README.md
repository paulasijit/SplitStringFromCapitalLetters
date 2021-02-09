# SplitStringFromCapitalLetters
## Example
* INPUT
```text
name	locIDStart	locIDEnd	startDay	startTime	endDay	endTime	tagPri2AxlesAuto	tagPri3AxlesAuto	tagPri4AxlesAuto
```
* OUTPUT
```text
name
loc_id_start
loc_id_end
start_day
start_time
end_day
end_time
tag_pri_2axles_auto
tag_pri_3axles_auto
tag_pri_4axles_auto
```
## CODE
#### IMPORT LIBRARY
```python
import sys
import re
```
#### INPUT ARRAY INITIALISING
```python
arr = 'name	locIDStart	locIDEnd	startDay	startTime	endDay	endTime	tagPri2AxlesAuto	tagPri3AxlesAuto'
```
#### TO SPLIT STRING
```python
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
    # print(result)
    sys.stdout.close()
```
#### ADDITIONAL FUNCTION TO MAKE NUMBER COMES AFTER '_'
```python
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
```
