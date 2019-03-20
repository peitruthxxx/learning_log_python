sex = str(input('性別(M/F)：'))
age = int(input('年齡：'))
hei = float(input('身高(cm)：'))
wei = float(input('體重(kg)：'))
hei=hei/100
if sex=='M':
    bmi = float(wei/(hei*hei))
    bfp = float((1.2*bmi)+(0.23*age-5.4)-(10.8*1))
    print('BMI：',bmi,'\nBody Fat Percentage：',bfp)
    if age>=18 and age<40:
        if bfp<10:
            print('偏瘦')
        elif bfp>=10 and bfp<16:
            print('標準')
        elif bfp>=16 and bfp<21:
            print('偏重')
        elif bfp>=21 and bfp<26:
            print('肥胖')
        elif bfp>=26:
            print('嚴重肥胖')
    elif age>=40 and age<60:
        if bfp<11:
            print('偏瘦')
        elif bfp>=11 and bfp<17:
            print('標準')
        elif bfp>=17 and bfp<22:
            print('偏重')
        elif bfp>=22 and bfp<27:
            print('肥胖')
        elif bfp>=27:
            print('嚴重肥胖')
    elif age>=60:
        if bfp<13:
            print('偏瘦')
        elif bfp>=13 and bfp<19:
            print('標準')
        elif bfp>=19 and bfp<24:
            print('偏重')
        elif bfp>=24 and bfp<29:
            print('肥胖')
        elif bfp>=29:
            print('嚴重肥胖')
elif sex=='F':
    bmi = wei/(hei*hei)
    bfp = float((1.2*bmi)+(0.23*age-5.4)-(10.8*0))
    print('BMI：',bmi,'Body Fat Percantage：',bfp)
    if age>=18 and age<40:
        if bfp<20:
            print('偏瘦')
        elif bfp>=20 and bfp<27:
            print('標準')
        elif bfp>=27 and bfp<34:
            print('偏重')
        elif bfp>=34 and bfp<39:
            print('肥胖')
        elif bfp>=39:
            print('嚴重肥胖')
    elif age>=40 and age<60:
        if bfp<21:
            print('偏瘦')
        elif bfp>=21 and bfp<28:
            print('標準')
        elif bfp>=28 and bfp<35:
            print('偏重')
        elif bfp>=35 and bfp<40:
            print('肥胖')
        elif bfp>=40:
            print('嚴重肥胖')
    elif age>=60:
        if bfp<22:
            print('偏瘦')
        elif bfp>=22 and bfp<29:
            print('標準')
        elif bfp>=29 and bfp<36:
            print('偏重')
        elif bfp>=36 and bfp<41:
            print('肥胖')
        elif bfp>=41:
            print('嚴重肥胖')