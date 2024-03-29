from typing import List

## ASCII Characters 
CHAR_SET_SIZE = 128

def str_radix_sort(strings: List[str]) -> List[str]:
    def chr_counting_sort(ind: int) -> List[str]:
        count_list = [0] * CHAR_SET_SIZE
        for s in strings:
            count_list[ord(s[ind])] += 1

        for i in range(1, CHAR_SET_SIZE):
            count_list[i] += count_list[i - 1]

        ret = [None] * len(strings)

        for s in reversed(strings):
            count_list[ord(s[ind])] -= 1
            ret[count_list[ord(s[ind])]] = s

        return ret

    for i in reversed(range(len(strings[0]))):
        strings = chr_counting_sort(i)

    return strings
