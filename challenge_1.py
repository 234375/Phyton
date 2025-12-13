#Write a program that takes a list of numbers and checks:
#If the number is even, store it in a dictionary with the key "even".
#If the number is odd, store it under the key "odd".
#Use a tuple (min, max) inside the dictionary to store the smallest and largest number for each category.
#Example Input:
#numbers = [3, 8, 5, 10, 2]
#Expected Output:
#{'even': (2, 10), 'odd': (3, 5)}

numbers = [3,8,5,20,25,33,32,10,2]
even_number = []
odd_number = []
for number in numbers:
    if number %2 ==0 :
        even_number.append(number)
    else:
        odd_number.append(number)
if even_number:
    even_num_tuple = (min(even_number),max(even_number))
else:
    (None,None) #None is a special built-in constant that represents the absence of a value or "nothing".
if odd_number:
    odd_num_tuple =(min(odd_number),max(odd_number))
else:
    (None,None)
result = {'even': even_num_tuple , 'odd': odd_num_tuple}
print(result)
    
        