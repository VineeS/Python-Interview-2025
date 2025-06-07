def longestPalindrome(s):
    res = ""
    resLen = 0
    for i in range(len(s)):
        # odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            print("l --> ",l,"r --> ",r,"(r - l + 1) -->",(r - l + 1),"resLen -->",resLen)
            if (r - l + 1) > resLen:
                print("r =", r)
                print("l =", l)
                print("r - l =", r - l)
                print("r - l + 1 =", r - l + 1)
                print("s[l:r+1]  --> ", s[l:r+1], "(r - l + 1) --> ",(r - l + 1))
                res = s[l:r+1]
                resLen = (r - l + 1)

            l -= 1
            r += 1

        #enven lenth
        l, r = i,i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r+1]
                resLen = (r - l + 1)

            l -= 1
            r += 1

    return res


s = "babad"
print(longestPalindrome(s))

# s1 = "xyzdabbad"
# print(longestPalindrome(s1))