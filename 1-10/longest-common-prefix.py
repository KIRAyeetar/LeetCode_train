# encoding:utf-8


def run():
    print(longestCommonPrefix(["aca","cba"]))
    print(longestCommonPrefix(["flower","flow","flight"]))


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 1:
        return strs[0]
    if len(strs) == 0:
        return ''    
    count = 0
    flag = 1

    for i in range(min(map(len, strs))):
        if flag == 0:
            return strs[0][0:count]
        for j in range(len(strs)-1):
            if strs[j][i] != strs[j+1][i]:
                flag = 0
                break
            else:
                if j == len(strs)-2:
                    count += 1
    return strs[0][0:count]


if __name__ == '__main__':
    run()