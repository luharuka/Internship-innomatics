def swap_case(s):
    x1=str()
    for i in range(len(s)):
        if int(s[i].islower())==1:
            x1+=(s[i].upper())
        else:
            x1+=(s[i].lower())
    return x1
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)