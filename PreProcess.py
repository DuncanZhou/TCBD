#!/usr/bin/python
#-*-coding:utf-8-*-
'''@Date:18-10-13'''
'''@Time:下午10:01'''
'''@author: Duncan'''

money_dic = {'美元':7,'日元':0.06,'香港元':0.88,'欧元':8,'瑞士法郎':7,'加元':5.31,'新加坡元':5.02,'丹麦克朗':1.07,"人民币元":1}

# 数据预处理，将币种统一

def convert(x):
    if x in money_dic.keys():
        return money_dic[x]
    else:
        return x

# 转换币种
def Convert_money(df):
    df["rate"] = df["注册资本(金)币种名称"].apply(convert)
    df["注册资金(元)"] = df["注册资金"] * df["rate"]
    df.drop(columns={"注册资金","rate"},inplace=True)
    return df


