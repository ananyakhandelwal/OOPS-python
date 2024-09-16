def power(x, n):
    pow = 1

    for i in range(n):
        pow = pow * x

    return pow

if __name__ == '__main__':

    x = int(input("enter the base number: "))
    n = int(input("enter power: "))

    print(power(x, n))
