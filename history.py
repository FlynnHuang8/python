import os
import sqlite3
import pandas as pd
import datetime

# 历史记录数据库文件路径
data_file = 'C:\\Users\\123\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History'

# 连接到历史记录数据库
conn = sqlite3.connect(data_file)
cursor = conn.cursor()

# 查询历史记录数据
query = "SELECT url, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 1000"
result = cursor.execute(query)

# 逐行读取历史记录，并将记录转换成DataFrame结构
history = []
for row in result:
    history.append([datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=row[1]), row[0]])
history_df = pd.DataFrame(history, columns=['datetime', 'url'])

# 转换时间格式
history_df['datetime'] = history_df['datetime'].dt.strftime('%Y-%m-%d-%H:%M:%A')
history_df.to_excel('history.xlsx', index=False)