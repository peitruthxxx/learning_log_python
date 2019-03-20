choose = int(input('1.攝氏轉華氏,2.華氏轉攝氏：'))
degree = int(input('輸入溫度：'))
if choose==1:
    fah = float(degree*1.8+32)
    print('攝氏轉華氏溫度',fah)
elif choose==2:
    cel = float((degree-32)*5/9)
    print('華氏轉攝氏溫度：',cel)
else:
    print('Wrong!')