def Fibbonaci(n):
    if n <= 1:
        return n
    else:
        return Fibbonaci(n-1) + Fibbonaci(n-2)

def Main():
    
    # initialized to y to start program
    userChar = 'y' 
    
    # loops if userChar is y, anything else will exit program
    while userChar == 'y': 
        try:
            userNum = int(input('Enter a number to find the Fibbonaci: '))
            print('The Fibonacci of {} = {}'.format(userNum, Fibbonaci(userNum)))
            userChar = input('Do you wish to enter another number (y/n)?')
        except:
            print('Please enter an integer')
    print('Goodbye!')
    
Main()
