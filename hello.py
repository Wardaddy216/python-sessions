import random
odd_count=0
even_count=0
for i in range(5):
        random_num=random.randint(1,10)
        if random_num%2==0:
            print("the number {} is even".format(random_num))
            even_count=even_count+1
        else:
            print("the number {} is odd".format(random_num))
            odd_count=odd_count+1
print("the total no of evencount is",even_count)
print("the total count of odd number is",odd_count)



#next program
import random
count = 0
for i in range(10):
     random_num1=random.randint(1,99)
     if random_num1>50:
          count = count + 1
          print("the number greater than 50 is",random_num1)
print("the total number greater than 50 is",count)

#next program
import random
def check_div():
    total_div=0
    num1=eval(input("enter a number you want to check"))
    for i in range(1,11):
        if num1%i==0:
            print("divisible by {}".format(i))
            total_div=total_div+1
    return(total_div)
val1=check_div()
print(val1)

#when ever you want to count  implement inside the function.
# strings
# loops
# dictionary 
# tuple
# set
# lambda function
# file handling session
# 

     



