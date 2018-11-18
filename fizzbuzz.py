'''This is apparently a common task asked at programming interviews:

“Write a program that prints the numbers from 1 to 100. But for multiples of three print
‘Fizz’ instead of the number and for the multiples of five print ‘Buzz’.
For numbers which are multiples of both three and five print ‘FizzBuzz’.”

'''

def fizzbuzz():
    num = range(1,101)
    for n in num:
        if n % 3 == 0 and n % 5 ==0:
            print ('FizzBuzz')
        elif n % 3 == 0:
            print ('Fizz')
        elif n % 5 == 0:
            print ('Buzz')
        else:
            print (n)
fizzbuzz()
