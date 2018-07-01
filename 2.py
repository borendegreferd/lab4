'''Найти сумму квадратов всех целых чисел от a до b
(значения a и b вводятся с клавиатуры).'''
a=int(input())
b=int(input())
sum=0
for i in range(a,b+1,1):
    sum=sum+i*i
print(sum)