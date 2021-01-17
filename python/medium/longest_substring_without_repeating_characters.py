



def my_slow_solution(s: str) -> int:
        # Want all combinations of substrings
        # sorted by largest -> smallest
        # eliminate any with dups
        n = len(s)
        if n in (0, 1): return n
        l, r = 0, 1
        largest = 0
        while (r <= n):
            sub = s[l:r]
            len_sub = len(sub)
            len_sub_set = len(set(sub))
            if len_sub == len_sub_set:
                if len_sub > largest:
                    largest = len_sub
                r += 1
            else:
                l += 1
        return largest



if __name__ == "__main__":

    input = "au"

    my_slow_solution(input)
