#!/usr/bin/python
#-*-coding:utf-8-*-
'''@Date:18-10-13'''
'''@Time:下午10:01'''
'''@author: Duncan'''
import pandas as pd

# 聚合统计 类别特征列相应数量
def GetCategroicalCount(df,pri_id,col):
    temp = df.groupby(pri_id)[col].count().reset_index().rename(columns={col:"%s_count" % col})
    return temp

# 聚合统计 数值列均值
def GetValAvg(df,pri_id,col):
    temp = df.groupby(pri_id)[col].mean().reset_index().rename(columns={col:"%s_avg" % col})
    return temp

# 聚合统计 数值列方差
def GetValVar(df,pri_id,col):
    temp = df.groupby(pri_id)[col].var().reset_index().rename(columns={col:"%s_var" % col})
    return temp

# 聚合统计 数值列最大值和最小值
def GetValMaxMin(df,pri_id,col):
    temp1 = df.groupby(pri_id)[col].max().reset_index().rename(columns={col:"%s_max" % col})
    temp2 = df.groupby(pri_id)[col].min().reset_index().rename(columns={col:"%s_min" % col})
    temp = pd.merge(temp1,temp2,on=pri_id)
    return temp

# 某列为空统计
def GetValNaCount(df,pri_id,col,other_col):
    temp = df[df[col].isna()]
    temp = temp.groupby(pri_id)[other_col].count().reset_index().rename(columns={other_col:"%s_Nacount" % col})
    return temp

# 特征列转化（行转列）
def CatRowsToCols(df,pri_id,col,other_col):
    temp = df.groupby([pri_id,col])[other_col].count().reset_index().rename(columns={other_col:"count"})
    temp = pd.DataFrame(temp.pivot_table(index=pri_id,columns=col,values="count").reset_index())
    return temp

