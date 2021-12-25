def main():
    no_of_test_cases = int(input().strip())
    for i in range(no_of_test_cases):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        ans = 0
        if sum(a) % n != 0:
            ans = 1
        print(ans)


if __name__ == '__main__':
    main()