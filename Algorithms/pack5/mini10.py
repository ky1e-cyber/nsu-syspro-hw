from typing import List

def str_radix_sort(strings: List[str]) -> List[str]:
    def chr_counting_sort(ind: int) -> List[str]:
        count_list = [0] * 128
        for s in strings:
            count_list[ord(s[ind])] += 1

        for i in range(1, 128):
            count_list[i] = count_list[i - 1]

        ret = strings.copy()

        for s in reversed(strings):
            count_list[ord(s[ind])] -= 1
            ret[count_list[ord(s[ind])]] = s

        return ret

    for i in reversed(range(len(strings[0]))):
        strings = chr_counting_sort(i)

    return strings
