# encoding:utf-8


def run():
    print(lengthOfLastWord('1231232 13  '))


def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.rstrip()
    count = 0
    for i in range(len(s)):
        if s[-i - 1] == ' ':
            break
        else:
            count += 1
    return count


if __name__ == '__main__':
    run()