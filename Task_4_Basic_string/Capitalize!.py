def solve(s):
    string = " ".join([word.capitalize() for word in s.split(" ")])
        
    return string
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()