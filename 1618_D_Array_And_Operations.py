import math

def main():
    no_of_test_cases = int(input().strip())
    for i in range(no_of_test_cases):
        n, k = tuple(map(int, input().strip().split()))
        a = list(map(int, input().strip().split()))
        a.sort()
        sum = 0
        for i in range(n - 2 * k):
            sum += a[i]
        j = n - k
        i = n - 2 * k
        while j < n:
            sum += math.floor(a[i] / a[j])
            i += 1
            j += 1
            
        print(sum)


if __name__ == '__main__':
    main()