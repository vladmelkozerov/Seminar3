# Задание 1 Нахождение cуммы элементов списка с нечетными индексами
int_list = [4,5,8,1,9,2,9,7,6,1]
sum = 0
for i in range(1,len(int_list),2):
    sum+=int_list[i]
print ("Задание 1")
print (f"Cумма элементов списка {int_list} с нечетными индексами составляет { sum}")
print()
    
#Задание 2 Нахождение произведения пар чисел списка
int_list = [4,2,4,2,1,3,5]
new_list = []
print ("Задание 2")
print(f"Исходный список {int_list}")
midElement_index = len(int_list)/2
if  midElement_index != int(midElement_index):
    int_list.insert(len(int_list)//2,int_list[int(midElement_index)])
for i in range(0,len(int_list)//2):
    new_list.append(int_list[i]*int_list[len(int_list)-i-1])
print(f"Список произведений пар чисел {new_list}")
print()

#Задание 3 Нахождение разницы между наибольшей и наименьшей дробной частью элементов списка
f_list = [-4.27,5,9.04,6.07,12345.01,9.25]
print ("Задание 3")
print(f"Исходный список {f_list}")
import math
for i in range (0,len(f_list)):
     f_list[i] = abs (float (format(math.fmod(f_list[i],1.00),'.2f')))
f_list.remove(0)
print (f'разница между наибольшей ={max (f_list)} и наименьшей ={min(f_list)} дробными частями чисел списка составляет:') 
print(format (max (f_list)-min(f_list),'.2f'))
print()

#Задание 4 Преобразование десятичного числа в двоичное
r = int (input("Задание 4 Введите целое число "))
print(f"Двоичное представление числа {r}",end=":  ")
binary=[]
while r!=0:
       binary.insert(0,r%2)
       r =  r //2
for i in range(0,len(binary),1):
       print(binary[i],end=" ")
print("\n")
 

#Задание 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
r = int (input("Задание 5 Введите целое число "))
Fib=[1,0,1,1]
for i in range (4,r+2):
    Fib.append(Fib[i-2]+Fib[i-1])
for i in range (1,r):
    Fib.insert(0,Fib[1]-Fib[0])
print(f"Список чисел Фибоначчи в том числе и для отрицательных индексов:")
for i in Fib:
    print (i,end=" ")
print("\n")



 