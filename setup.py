def cal():
    def adding(x, y):
        print(float(x) + float(y))

    def subtraction(x, y):
        print(float(x) - float(y))

    def multiply(x, y):
        print(float(x) * float(y))

    def divide(x, y):
        print(float(x) // float(y))
    print('Do you want to add?(+) or subtract?(-) or multiply?(*) or divide(/)')
    answer = input('')
    if answer == '+':
        try:
            x = float(input('First number! '))
            y = float(input('Second number! '))
        except Exception as e:
            print(f'ERROR: {e}')
            return
        adding(x, y)
    if answer == '-':
        try:
            x = float(input('First number! '))
            y = float(input('Second number! '))
        except Exception as e:
            print(f'ERROR: {e}')
            return
        subtraction(x, y)
    if answer == '*':
        try:
            x = float(input('First number! '))
            y = float(input('Second number! '))
        except Exception as e:
            print(f'ERROR: {e}')
            return
        multiply(x, y)
    if answer == '/':
        try:
            x = float(input('First number! '))
            y = float(input('Second number! '))
        except Exception as e:
            print(f'ERROR: {e}')
            return
        divide(x, y)

if __name__ == '__main__':
    cal()
