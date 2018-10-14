#!/usr/bin/python
#-*-coding:utf-8-*-
'''@Date:18-10-14'''
'''@Time:下午3:21'''
'''@author: Duncan'''

import pandas as pd
import PreProcess as prep
import Features as fea

# 处理企业基本信息
def Process1(df):
    pri_id = "企业名称"
    res = pd.DataFrame()
    res[pri_id] = df[pri_id].unique()
    # 转换币种
    df = prep.Convert_money(df)
    # 提取注册资金特征（最大值，最小值，均值，方差）
    res = pd.merge(res,fea.GetValAvg(df,pri_id,"注册资金(元)"),on=pri_id)
    res = pd.merge(res,fea.GetValMaxMin(df,pri_id,"注册资金(元)"),on=pri_id)
    res = pd.merge(res,fea.GetValVar(df,pri_id,"注册资金(元)"),on=pri_id)

    # 提取类别特征
    num_fea = ['注册资金(元)',"出资比例"]
    cat_fea = [col for col in df.columns if col != pri_id and col not in num_fea]
    for col in cat_fea:
        res = pd.merge(res,fea.GetCategroicalCount(df,pri_id,col),on=pri_id)

    # 法定代表人和首席代表标志为空统计
    res = pd.merge(res,fea.GetValNaCount(df,pri_id,"法定代表人标志","姓名"),on=pri_id)
    res = pd.merge(res,fea.GetValNaCount(df,pri_id,"首席代表标志","姓名"),on=pri_id)

    # 统计 相应职务个树
    res = pd.merge(res,fea.CatRowsToCols(df,pri_id,"职务","姓名"))

    # 提取出资比例（最大值，最小值，均值，方差）
    res = pd.merge(res,fea.GetValAvg(df,pri_id,"出资比例"),on=pri_id)
    res = pd.merge(res,fea.GetValMaxMin(df,pri_id,"出资比例"),on=pri_id)
    res = pd.merge(res,fea.GetValVar(df,pri_id,"出资比例"),on=pri_id)

    return res

basic_info = pd.read_csv("data/train/企业基本信息&高管信息&投资信息.csv")
df = Process1(basic_info)
print(df.columns)