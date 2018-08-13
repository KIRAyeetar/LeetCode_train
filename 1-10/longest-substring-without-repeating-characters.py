# encoding:utf-8

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtyp
    """
    word_rank = {}
    s = list(s)
    set_size = len(set(s))
    list_size = len(s)
    max_count = 0

    if set_size<= 2:
        return set_size

    for i in range(list_size):
        if word_rank.has_key(s[i]):
            rank = word_rank[s[i]]
            for key in word_rank.keys():
                if word_rank[key] <= rank:
                    word_rank.pop(key)

        word_rank[s[i]] = i
        if len(word_rank)>=max_count:
            max_count = len(word_rank)

    return max_count


def lengthOfLongestSubstring_sec(s):
    """
    :type s: str
    :rtyp
    """
    s = list(s)
    gap = len(set(s))
    if gap <= 2:
        return gap
    while gap>2:
        for i in range(len(s) - gap + 1):
            if len(set(s[i: i + gap])) == gap:
                return gap
        gap -= 1
    return 2


if __name__ == '__main__':
    print(lengthOfLongestSubstring('bwfasdasd'))