
def paths(m ,n):
    if n == m : return 0
    if (n - m) <= 2: return (n - m)
    else: return paths(m + 1 ,n) + paths(m + 2 ,n)

def dp(m ,n,mem):
    if mem.get(m): return mem[m]
    result = None
    if n == m :
        result = 0
    if (n - m) <= 2:
        result =  (n - m)
    else:
        result = dp(m + 1 ,n,mem) + dp(m + 2 ,n,mem)
    mem[m] = result
    return result

def climbStairs(n: int,how="recursive") -> int:
    if how == "recursive":
        return paths(0 ,n)
    elif how == "dp":
        return dp(0,n,{})


if __name__ == "__main__":

    tests = [(3,3),(5,8),(8,34)]

    for test,ans in tests:
        print(f"Input={test}")
        output = climbStairs(test,how="recursive")
        print(f"Output={output}")
        assert output == ans

    print("Passed all tests")