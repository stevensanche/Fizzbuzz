'''
CIS 122 Spring 2022 Project 3-2
Author(s): Steven Sanchez-Jimenez
Credit: CIS 122 Resources, office hours
Description: FizzBuzz
'''
def fb(n):
    '''
    This code is to give values of Fizz, Buzz, and Fizzbuzz to the approprtiate
    numbers. It will automatically detect which numbers should be translated.
    as an example, you would put in a number which could be "10", and it will
    generate all numbers from 1-10
    '''
    for i in range(1, n+1):
        #This will be the conditional statement which will give the numbers their appropriate values
        if ((i%3==0) and (i%5==0)):
            print ('FizzBuzz')
        #This code above is what will determine all the numbers that are divisible by 3 and 5
        elif (i%3==0):
            print ('Fizz')
        #This code above is what will determine all the numbers that are divisible by 3
        elif (i%5==0):
            print ('Buzz')
        #This code above is what will determine all the numbers that are divisible by 5
        else:
            print (i)
    print ("Game Over!")
    #Once the game is over and it has calculated all numbers between 1 and the chose number, it will give an end statement

#This is to tell the user what they should do and give an input
x = input('Enter a positive integer to start the game')

#This is turning the input into an integer
x = int(x)

#This is to call the function fb(x)
fb(x)


