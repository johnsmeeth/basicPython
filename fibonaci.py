__author__ = 'thanhnguyen'
# define function to caculate fibonaci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print a, ", ",
        #print(a, ", ", end="")
        a, b = b, a + b

n = raw_input('Enter limit of fibonaci series: ') or 1000
#n = input('Enter limit: ') or 1000
fib(n)
