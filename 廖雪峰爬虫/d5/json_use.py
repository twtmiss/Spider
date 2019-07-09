import json

# 1.字符串和dic list转换

#字符串--------dict list
data = '[{"name":"张三","age":20},{"name":"李四","age":18}]'
list_data = json.loads(data)
print(data)
print(type(list_data))

list2 = [
    {"name":"张三","age":23},
    {"name":"李四","age":24},
    {"name":"张一","age":21},
    {"name":"张二","age":22},
    {"name":"张五","age":25},
    {"name":"张六","age":26},
    {"name":"张七","age":27},
    ]
#fp是file path
#将list2写入02new.json
fp = open('.\爬虫\廖雪峰爬虫\d5\\02new.json', 'w')
json.dump(list2, fp)
fp.close()

#读取文件
# 从02new.json读取
result = json.load(open('.\爬虫\廖雪峰爬虫\d5\\02new.json','r'))
print(result)