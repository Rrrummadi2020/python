from maths_methods import add, subtract, multiply, power, division

def simple_calculator():
    n1 = int(input('Enter first number: '))
    n2 = int(input('Enter second number: '))
    symbol = input('Enter operator (+, -, *, %, ^ or exit): ')
    match symbol:
        case '+':
            print(f'Result: {n1} + {n2} = {add(n1, n2)}')
        case '-':
            print('{} - {} = {}'.format(n1,n2,subtract(n1, n2)))
        case '*':
            print('{} * {} = {}'.format(n1,n2,multiply(n1, n2)))
        case '^':
            print('{} ** {} = {}'.format(n1,n2,power(n1, n2)))
        case '%':
            print('{} % {} = {}'.format(n1,n2,division(n1, n2)))
        case 'exit':
            print('Exiting the calculator. Goodbye!')
            return
        case _:
            print('Invalid operator')
    simple_calculator()

simple_calculator()
