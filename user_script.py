"""
Complete the script.
"""
#fig02_01.py
"""comparing integers using if statements and comparision operators."""
print('enter two integers, and i will tell you  the relationship they satisfy. ')

# read first integer
number1 = int(input('Enter first integer: '))

# read second integer
number2 = int(input('Enter second integer: '))

if number1 == number2:
    print(number1, 'is equal to', number2)

if number1 != number2:
    print(number1, 'is not equal to', number2)

if number1 < number2:
    print(number1, 'is less than', number2)

if number1 > number2:
    print(number1, 'is greater than', number2)

if number1 <= number2:
    print(number1, 'is less than or equal to', number2)

if number1 >= number2:
    print(number1, 'is greater than or equal to', number2)

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################

#Answers from interactive mode

number1 = int(input('Enter first integer: '))
Enter first integer: 10

In [19]: number2 = int(input('Enter second integer: '))
Enter second integer: 15

In [20]: number1 == number2
Out[20]: False

In [21]: number1 != number2
Out[21]: True

In [22]: number1 < number2
Out[22]: True

In [23]: number1 > number2
Out[23]: False

In [24]: number1 <= number2
Out[24]: True

In [25]: number1 >= number2
Out[25]: False


