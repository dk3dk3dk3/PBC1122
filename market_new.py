# 函式庫

# 傳進來的爬蟲資料處理
import numpy as np
import pandas as pd

# 忽略warning messages
import warnings
warnings.filterwarnings('ignore')

# 日期資料處理
import datetime

import re
import os
os.chdir(r"C:\Users\emily\OneDrive\桌面\PBC1122")


# 匯入爬蟲結果的csv檔
data_name = r"markets_data.csv"
data = pd.read_csv(data_name)
df = data.copy()

# 日期欄位轉成datetme
df['start_date'] = pd.to_datetime(df['start_date'], format='%Y-%m-%d')
df['end_date'] = pd.to_datetime(df['end_date'], format='%Y-%m-%d')


# 搜尋日期後回傳哪幾列符合
def date_search(df, start_date, end_date=0):
    date_list = []
    
    for i in range(len(df)):
            if ((df.loc[i, 'start_date'] >= start_date and df.loc[i, 'start_date'] <= end_date)
                    or (df.loc[i, 'end_date'] >= start_date and df.loc[i, 'end_date'] <= end_date)
                    or (df.loc[i, 'start_date'] < start_date and df.loc[i, 'end_date'] > end_date)):
                date_list.append(i)
    
    return date_list
    

# 搜尋地點後回傳哪幾列符合
def location_search(df, location):
    location_list = []
    for i in range(len(df)):
        if location == df.loc[i, "location"]:
            location_list.append(i)
            
    return location_list
    

# 訊息回覆內容
def market_response(df, prompt):
    answer = []
    
    # 四種查詢：
    # 查詢 地點
    # 查詢 特定日期
    # 查詢 特定月份
    # 查詢 地點 特定日期
    
    date_list = []  # 特定日期、特定月份的查詢結果
    location_list = []  # 地點的查詢結果
    
    print(prompt)
    
    # 地點
    if len(prompt) == 3:
        location_list = location_search(df, prompt)
    
    # 特定日期
    elif re.match(r"\d{4}/\d{2}/\d{2}-\d{2}", prompt):
        
        prompt_list = prompt.split("-")
        date1 = datetime.datetime.strptime(prompt_list[0], "%Y/%m/%d")
        date2 = date1.replace(day=int(prompt_list[1]))
        date_list = date_search(df, date1, date2)
            
    # 地點 特定日期
    elif re.match(r".+ \d{4}/\d{2}/\d{2}-\d{2}", prompt): # location YYYY/MM/DD-DD
        location = prompt.split(" ")[0]
        prompt = prompt.replace(location + " ", "")
        location_list = (df, location)
        
        prompt_list = prompt.split("-")
        date1 = datetime.datetime.strptime(prompt_list[0], "%Y/%m/%d")
        date2 = date1.replace(day=int(prompt_list[1]))
        date_list = date_search(df, date1, date2)
        
    # 特定月份
    else:
        prompt_list = prompt.split("/")
        date1 = datetime.datetime(int(prompt_list[0]), int(prompt_list[1]), 1)
        
        # date2為下個月的第一天減去一天，就會是這個月的最後一天
        if date1.month == 12:  # 如果當前月份是12月，則年份需要加1
            next_month = date1.replace(year=date1.year + 1, month=1, day=1)
        else:
            next_month = date1.replace(month=date1.month + 1, day=1)

        # 設置為這個月的最後一天
        date2 = next_month - datetime.timedelta(days=1)
        date_list = date_search(df, date1, date2)
        # print(date1, date2)
        
        
    # 將結果存成list
    result_list = []
    
    if location_list == []:
        result_list = date_list.copy()
    elif date_list == []:
        result_list = location_list.copy()
    else:
        for i in date_list:
            if i in location_list:
                result_list.append(i)
            
    result_len = len(result_list)
    
    # 避免訊息太長傳不出去，每10個結果為一個字串存到list裡
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
    
    return answer


# 測試用
# text = input()
# answer = market_response(df, text)
# print(answer)