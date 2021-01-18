
def longestPalindrome(s: str) -> str:
    n = len(s)
    if n == 1:
        return s

    def check_pal(sub):
        return sub == sub[::-1]

    longest = ""
    for l in range(n):
        for r in range(n + 1):
            sub = s[l:r]
            subl = len(sub)
            if check_pal(sub):
                if subl > len(longest):
                    longest = sub
    return longest

def longestPalindrome2(s: str) -> str:

    def check_paln(sub):
        return sub == "".join(reversed(sub))

    n = len(s)
    subs = [(i, j) for i in range(n) for j in range(i + 1, n + 1)]

    def diff(key):
        return abs(key[0] - key[1])

    subs.sort(key=diff, reverse=True)

    print(subs)

    for i, j in subs:
        if check_paln(s[i:j]):
            return s[i:j]


if __name__ == "__main__":
    test = "babad"
    print(longestPalindrome2(test))
    test2 = "bb"
    print(longestPalindrome(test2))
    import  time
    s = "mwwfjysbkebpdjyabcfkgprtxpwvhglddhmvaprcvrnuxifcrjpdgnktvmggmguiiquibmtviwjsqwtchkqgxqwljouunurcdtoeygdqmijdympcamawnlzsxucbpqtuwkjfqnzvvvigifyvymfhtppqamlgjozvebygkxawcbwtouaankxsjrteeijpuzbsfsjwxejtfrancoekxgfyangvzjkdskhssdjvkvdskjtiybqgsmpxmghvvicmjxqtxdowkjhmlnfcpbtwvtmjhnzntxyfxyinmqzivxkwigkondghzmbioelmepgfttczskvqfejfiibxjcuyevvpawybcvvxtxycrfbcnpvkzryrqujqaqhoagdmofgdcbhvlwgwmsmhomknbanvntspvvhvccedzzngdywuccxrnzbtchisdwsrfdqpcwknwqvalczznilujdrlevncdsyuhnpmheukottewtkuzhookcsvctsqwwdvfjxifpfsqxpmpwospndozcdbfhselfdltmpujlnhfzjcgnbgprvopxklmlgrlbldzpnkhvhkybpgtzipzotrgzkdrqntnuaqyaplcybqyvidwcfcuxinchretgvfaepmgilbrtxgqoddzyjmmupkjqcypdpfhpkhitfegickfszermqhkwmffdizeoprmnlzbjcwfnqyvmhtdekmfhqwaftlyydirjnojbrieutjhymfpflsfemkqsoewbojwluqdckmzixwxufrdpqnwvwpbavosnvjqxqbosctttxvsbmqpnolfmapywtpfaotzmyjwnd"

    s_time = time.time()
    s_r_1 = s[::-1]
    e_time = time.time()
    print((e_time - s_time))

    s_time = time.time()
    s_r_2 = "".join(reversed(s))
    e_time = time.time()
    print((e_time - s_time))
