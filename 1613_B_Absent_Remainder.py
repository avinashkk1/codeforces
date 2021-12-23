from bisect import bisect_left

def printPairs(n, a):
    a.sort()
    count = 0
    breakFlag = False
    for i in range(n - 1, -1, -1):
        for j in range(i):
            index = bisect_left(a, a[i] % a[j])
            if index != n and a[index] == a[i] % a[j]:
                continue
            print(a[i], a[j])
            count += 1
            if count >= (n // 2):
                breakFlag = True
                break
        
        if breakFlag:
            break

def printPairs1(n, a):
    minEle = min(a)
    count = 0
    for i in range(n):
        if a[i] != minEle:
            print(a[i], minEle)
            count += 1
            if count >= (n // 2):
                break




def main():
    no_of_test_cases = int(input().strip())
    for i in range(no_of_test_cases):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        printPairs1(n, a)

if __name__ == '__main__':
    main()