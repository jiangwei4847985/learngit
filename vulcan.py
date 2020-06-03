
# 小明身高练习程序
bmi = 80.5/pow(1.75,2)
if bmi >32:
    print ('严重肥胖')
elif 28 < bmi <=32:
    print('肥胖')
elif 25 < bmi <=28:
    print ('过重')
elif 18.5 < bmi <=25:
    print ('正常')
elif bmi <=18.5:
    print ('过轻')

## for 循环练习

name = ['陈钢','李青青','李卡卡']
for name in name:
    print(name)

sum = 0
for x in range(101):
    sum = sum + x
print (sum)

## 练习2 请利用循环依次对list中的每个名字打印出Hello, xxx!：

name = ['Hello','xxx!']
for name in name:
    print (name)
print ('利用循环依次对list中的每个名字打印出Hello, xxx!')

## break 练习  输出1~100，到58时终止

a = 1
while a <= 100:
    if a >58:
        break
    print (a)
    a = a + 1
print ('END')
print('输出1~100，到58时终止')

## continue 练习  符合条件时跳过并进入下一个循环 比如 输入输出1~100中的奇数

b=1 
while b <= 100:
    b = b + 1
    if b % 2 ==0:
        continue
    print (b)
print ("END")
print('输入输出1~100中的奇数')

## 循环练习 ：求100以内奇数的和

c = 1
for z in range(100):
    if(z%2)==1:
        c=c+z
print (c)
print ('循环练习，求100以内奇数的和')
