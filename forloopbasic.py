# # Basic
nums = range(1,50)
print(list(nums))
print(list(map(str, nums)))

# Multiples of Five
for i in range(5, 1000, 5):
    print(i)

#Counting, the Dojo Way
def counting_dojo():
    for i in range (1,101,1):
        if i % 5 == 0:
            print ('Coding')
        if i % 10 == 0:
            print ('Dojo')
            
counting_dojo()

#Whoa. That Sucker's Huge
min = 0
max = 500000
Oddtotal = 0

for number in range(min, max +1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from {0} to {1} = {2}".format(min, max, Oddtotal))

#Countdown by Fours
def count_down_four():
    number = 2018
    while number > 0:
        print (number)
        number = number - 4
        
count_down_four()

#Flexible Counter
def flex_countdown(low, high, mult):
    for i in range (low, high):
        if i % mult == 0:
            print (i)
            
flex_countdown(2, 9, 3)