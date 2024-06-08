# 函式庫

# 傳進來的爬蟲資料處理
import numpy as np
import pandas as pd

# 忽略warning messages
import warnings
warnings.filterwarnings('ignore')

# 日期資料處理
import datetime

import os
os.chdir(r"C:\Users\emily\OneDrive\桌面\PBC1122")

data_name = r"markets_data.csv"
data = pd.read_csv(data_name)
df = data.copy()
# print(df)
df['start_date'] = pd.to_datetime(df['start_date'], format='%Y-%m-%d')
df['end_date'] = pd.to_datetime(df['end_date'], format='%Y-%m-%d')
# df["start_year"] = df["start_date"].dt.year


# 搜尋日期後回傳第幾列符合
def date_search(df, start_date, end_date=0):
    date_list = []
    
    # 單一日期
    if end_date == 0:
        for i in range(len(df)):
            if start_date >= df.loc[i, 'start_date'] and start_date <= df.loc[i, 'end_date']:
                date_list.append(i)
            
            
            
    else:
    
        for i in range(len(df)):
            if ((df.loc[i, 'start_date'] >= start_date and df.loc[i, 'start_date'] <= end_date)
                    or (df.loc[i, 'end_date'] >= start_date and df.loc[i, 'end_date'] <= end_date)
                    or (df.loc[i, 'start_date'] < start_date and df.loc[i, 'end_date'] > end_date)):
                date_list.append(i)
    
    return date_list
    

# 搜尋地點後回傳第幾列符合
def location_search(df, location):
    location_list = []
    for i in range(len(df)):
        if location == df.loc[i, "location"]:
            location_list.append(i)
            
    return location_list


def market_response(df, prompt):
    answer = []
    # 查詢 單一日期
    # 查詢 單一日期 地點
    # 查詢 一段期間
    # 查詢 一段期間 地點
    
    inp_list = prompt.split(" ")
    
    date_list = []
    location_list = []
    
    if "地點" in inp_list:
        inp_list.remove("地點")
        
        if "單一日期" in inp_list:
            inp_list.remove("單一日期")
            date = datetime.datetime.strptime(inp_list[0], "%Y-%m-%d")
            
            date_list = date_search(df, date)
            
            location_list = location_search(df, inp_list[1])
        elif "一段期間" in inp_list:
            inp_list.remove("一段期間")
            date1 = datetime.datetime.strptime(inp_list[0], "%Y-%m-%d")
            date2 = datetime.datetime.strptime(inp_list[1], "%Y-%m-%d")

            date_list = date_search(df, date1, date2)
            
            location_list = location_search(df, inp_list[2])
    
    
    
    else:
        if "單一日期" in inp_list:
            inp_list.remove("單一日期")
            date = datetime.datetime.strptime(inp_list[0], "%Y-%m-%d")
            date_list = date_search(df, date)
            
        elif "一段期間" in inp_list:
            inp_list.remove("一段期間")
            date1 = datetime.datetime.strptime(inp_list[0], "%Y-%m-%d")
            date2 = datetime.datetime.strptime(inp_list[1], "%Y-%m-%d")
            date_list = date_search(df, date1, date2)
    
    result_list = []
    
    if location_list == []:
        result_list = date_list.copy()
    else:
        for i in date_list:
            if i in location_list:
                result_list.append(i)
            
    result_len = len(result_list)
    
    for j in range(result_len // 10 + 1):
        answer.append("")
        
        for i in range(10 * j, 10 * j + 10):
            if i >= result_len:
                break
            answer[j] += f"{df.loc[result_list[i], 'name']}"\
                         f", 日期：{df.loc[result_list[i], 'start_date'].date()}至{df.loc[result_list[i], 'start_date'].date()}"\
                         f", 地點：{df.loc[result_list[i], 'location']}"\
                         f", 連結：{df.loc[result_list[i], 'link']}"\
                         f"\n"
    # 
                      
                      
    # print(date_list)
    # print(location_list)
    # print(result_list)
    
    return answer
    
# text = input()

# answer = market_response(df, text)

# print(answer)