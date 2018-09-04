# encoding:utf-8


def run():
    print(reverse(1534236469))


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    x = str(x)
    if x[0:1] == '-':
        x = -int(x[:-len(x):-1])
    else:
        x = int(x[::-1])
    if (x>2**31-1) | (x<-2**31):
        return 0
    return x


if __name__ == '__main__':
    run()