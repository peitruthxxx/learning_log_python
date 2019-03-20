"""
給初始值、key的名稱要有意義
因為他是一個資料結構
"""
a = {
    'dogs': 9, 
    'cats':5
    }

print(a['dogs'])

a['pigs'] = 10
print(a['pigs'])

print(a.get('pig',"not exist")) #用get取value，如果沒有該key不會當機，只回傳空值和“not exist”

print(a.items()) #通常會用for迴圈取用

for key, value in a.items():
    print(key, value)

b = {'food': 'rice'}