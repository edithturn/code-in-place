MAX_NUMBER = 5

def main():
    for i in range(MAX_NUMBER+1):
        print(i, factorial)
def factorial(n):
    """
    Return factorial of a number
    
    >>> factorial(5)
    >>> factorial(3)
    >>> factorial(2)
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    main()
