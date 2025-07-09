
#!/usr/bin/env python3

from main import buildPalindrome

# Test cases from the problem
test_input = """10
ottloictodtdtloloollllyocidyiodttoacoctcdcidcdttyoiilocltacdlydaailaiylcttilld
jevgfsuujwrunvgvgwpfbknkruvwzgxxgksmexqvxbghfffseuugxkwexhzfbpu
qquhuwqhdswxxrxuzzfhkplwunfagppcoildagktgdarveusjuqfistulgbglwmfgzrnyxryetwzhlnfewczmnoozlqatugmd
jwgzcfabbkoxyjxkatjmpprswkdkobdagwdwxsufeesrvncbszcepigpbzuzoootorzfskcwbqorvw
dczatfarqdkelalxzxillkfdvpfpxabqlngdscrentzamztvvcvrtcm
bqlizijdwtuyfrxolsysxlfebpolcmqsppmrfkyunydtmwbexsngxhwvroandfqjamzkpttslildlrkjoyrpxugiceahgiakev
kfnfolpcfblpncetyhtrwxkbosccskxbuvcrosavnpxzoeoyyghbbqkflslfkqbbhgyyjj
qrxpxnloeozxpnvasorcvubxksccsobkxwrthytecnplbfcplofx
mlfcpidlqrvngnvttaifcbopnwezesomkxhaiafmvkbjaisyr
btultpnxbcrmornqumatserhieqggrivouwfnbnghdfall
pb
kkb
rfq
xzj
zlc
zdw
s
k
w
d"""

expected_output = """-1
oozlzoo
lxsysxl
folpcfblpncetyhtrwxkbosccskxbuvcrosavnpxzoeoyyghbbqkflslfkqbbhgyyoeozxpnvasorcvubxksccsobkxwrthytecnplbfcplof
rvngnvr
bkkb
-1
zlz
-1
-1"""

def run_test():
    lines = test_input.strip().split('\n')
    t = int(lines[0])
    
    results = []
    for i in range(t):
        a = lines[1 + i * 2]
        b = lines[2 + i * 2]
        result = buildPalindrome(a, b)
        results.append(result)
        print(f"Test {i+1}: a='{a[:10]}...' b='{b[:10]}...' → {result}")
    
    print("\nActual output:")
    for result in results:
        print(result)
    
    print("\nExpected output:")
    print(expected_output)
    
    # Compare results
    expected_lines = expected_output.strip().split('\n')
    print(f"\nComparison:")
    for i, (actual, expected) in enumerate(zip(results, expected_lines)):
        status = "✓" if actual == expected else "✗"
        print(f"Test {i+1}: {status} {actual} (expected: {expected})")

if __name__ == "__main__":
    run_test()
