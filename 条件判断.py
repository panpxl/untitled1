age = int(input('请输入你的年龄：'))

if age >= 18:
    print('your age is', age)
    print('你已经成年了，恭喜！')
elif age >= 6:
    print('teenager')
else:
    print('你还没成年')

height = 1.75
weight = 80.5
bmi = weight / (height * height)
if bmi < 18.5:
    print('过轻')
elif bmi > 18.5 and bmi < 25:
    print('正常')
elif bmi > 25 and bmi < 28:
    print('过重')
elif bmi > 28 and bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
