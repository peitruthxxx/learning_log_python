salary_per_hour_basic = int(input('基本時薪：'))
hour = float(input('工作時數：'))

if hour<40:
    salary_per_hour = int(salary_per_hour_basic*0.8)
    print('每週收入：',salary_per_hour*hour)
elif hour==40:
    salary_per_hour = salary_per_hour_basic
    print('每週收入：',salary_per_hour*hour)
elif hour>40 and hour<50:
    salary_per_hour = int(salary_per_hour_basic*1.2)
    print('每週收入：',40*salary_per_hour_basic+(hour-40)*salary_per_hour)
elif hour>50:
    salary_per_hour = int(salary_per_hour_basic*1.6)
    print('每週收入：',50*salary_per_hour_basic+(hour-50)*salary_per_hour)