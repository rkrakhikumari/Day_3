##### range 1,100 #####
for num in range(1,101):
    print(num)


##### sum of number from 1 to 100 #####
total = 0
for num in range(1,101):
    total += num
print(total)


##### largest number ######
numbers =[100,20,300,50,75]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(max_num)


##### factorial #####
num = int(input("Enter the number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial*i
print(factorial)


##### palindrome #####
string = input("Enter a value: ")
is_palindrome = True
for i in range(len(string)//2):#
    if string[i] != string[-(i+1)]:
        is_palindrome = False
        print("Not a palindrome.")
        break
if is_palindrome:
    print("palindrome")   
else:
    print("palindrome")


#### Check common number #####
list1 = [1,2,3,4,5,6]
list2 = [7,6,5,4,3,2,1]
common_element = []
for element in list1:
    if element in list2:
        common_element.append(element)
print(common_element)


#####fibonacci sequence #####
n = int(input("Enter a number: "))
fabonacci_series = [0, 1]
for i in range(2, n):
    next_term = fabonacci_series[i-1]+fabonacci_series[i-2]
    fabonacci_series.append(next_term)
print(fabonacci_series)


##### Longest string ######
strings = ("apple","mango","grapes","pomegranate")
longest_string = ""
for i in strings:
    if len(i) > len(longest_string):
        longest_string = i
print(longest_string)


##### Reverse of a string #####
string = input("Enter a string: ")
reversed_srtring = ""
for char in string:
    reversed_srtring = char + reversed_srtring
print(reversed_srtring)


##### Even and odd #####
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even number:",even_count)
print("Odd number:",odd_count)


##### Factorial ######
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 5
result = factorial(num)
print(result)



