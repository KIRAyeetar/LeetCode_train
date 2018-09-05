# encoding:utf-8


def run():
    print(longestValidParentheses(")))(()())("))
    print(longestValidParentheses_plus(")))(()())("))



def longestValidParentheses_plus(s):
    """
    :type s: str
    :rtype: int
    """
    match = 0
    stack = []
    stack.append(-1)
    for i in range(len(s)):
        if s[i] == ')':
            stack.pop()
            if stack == []:
                stack.append(i)
            else:
                match = max(match, i - stack[-1])
        else:
            stack.append(i)
    return match


def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    flag = '()'
    flag_ = '*'
    for i in range(len(s)//2):
        if flag in s:
            s = s.replace(flag, flag_)
        flag = '('+flag_+')'
        flag_ = flag_+'*'

    max_count = 0
    flag_ = '*'
    for i in range(len(s)):
        if flag_ in s:
            max_count = i+1
        else:
            return max_count*2
        flag_ += '*'
    return max_count*2


if __name__ == '__main__':
    run()