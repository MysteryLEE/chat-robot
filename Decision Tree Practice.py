#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import math
# outlook : sunny=0 overcast=1 rain=2
# humidity: high=0 normal=1
# wind: weak=0 strong=1
# play: no=0 yes=1
datas = [[0,0,0],[0,0,1],[1,0,0],[2,0,0],[2,1,0],[2,1,1],[1,1,1]
         ,[0,0,0],[0,1,0],[2,1,0],[0,1,1],[1,0,1],[1,1,0],[2,0,1]]
results = [0,0,1,1,1,0,1,0,1,1,1,1,1,0]
test = [2,0,1]

# First:
print('第一次分裂')
info = [0,0,0]
for j in [0,1,2]:
    total = 0
    if j==0:
        sum = [0,0,0]
        res = [[0,0],[0,0],[0,0]]
        arr = [0,1,2]
    else:
        sum = [0, 0]
        res = [[0, 0], [0, 0]]
        arr = [0, 1]
    for index in range(len(datas)):
        total += 1
        sum[datas[index][j]] += 1
        res[datas[index][j]][results[index]] += 1
    if j==0:
        print('按照outlook分类：'),
    if j==1:
        print('按照humidity分类：'),
    if j==2:
        print('按照wind分类：'),
    print(res)
    for i in arr:
        if sum[i] != 0:
            if res[i][0] != 0 and res[i][1] != 0:
                info[j] += (-res[i][0] * math.log(float(res[i][0]) / float(sum[i]),2))/total
                info[j] += (-res[i][1] * math.log(float(res[i][1]) / float(sum[i]),2))/total
    print('Info(D) = '),
    print(info[j])

print('\n第一次按照outlook分裂Info(D)最小\n')

# Second:
print('第二次分裂')
info = [0,0,0]
for j in [1,2]:
    total = 0
    sum = [0, 0]
    res = [[0, 0], [0, 0]]
    arr = [0, 1]
    for index in range(len(datas)):
        if datas[index][0] == 2:
            total += 1
            sum[datas[index][j]] += 1
            res[datas[index][j]][results[index]] += 1
    if j==1:
        print('按照humidity分类：'),
    if j==2:
        print('按照wind分类：'),
    print(res)
    for i in arr:
        if sum[i] != 0:
            if res[i][0] != 0 and res[i][1] != 0:
                info[j] += (-res[i][0] * math.log(float(res[i][0]) / float(sum[i]),2))/total
                info[j] += (-res[i][1] * math.log(float(res[i][1]) / float(sum[i]),2))/total
    print('Info(D) = '),
    print(info[j])

print('\n第二次按照wind分裂Info(D)最小，此时Info(D)已经为0\n')
print('故D15为(Rain,Weak) 结果为Yes')