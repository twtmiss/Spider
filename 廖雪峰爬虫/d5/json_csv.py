import json
import csv

# json中的数据转换成csv文件

# 1.分别读，创建文件
json_fp = open('.\爬虫\廖雪峰爬虫\d5\\02new.json', 'r')
csv_fp = open('.\爬虫\廖雪峰爬虫\d5\\03csv.csv', 'w', encoding="utf-8")

# 2. 提出表头，表内容
data_list = json.load(json_fp)

sheet_title = data_list[0].keys()

sheet_data = []
for str in data_list:
    sheet_data.append(str.values())
    #print(str.values())

# 3. csv写入器
writer = csv.writer(csv_fp)

# 4. 写入表头
writer.writerow(sheet_title)

# 5. 写入表内容
writer.writerows(sheet_data)

# 关闭文件
json_fp.close()
csv_fp.close()