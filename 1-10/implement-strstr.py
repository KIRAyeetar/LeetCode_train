# encoding:utf-8


def run():
    print(strStr('123', '23'))
    print(strStr('123', '4'))
    print(strStr('123', ''))


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle not in haystack:
        return -1
    if needle == '':
        return 0
    else:
        return haystack.index(needle)


if __name__ == '__main__':
    run()
