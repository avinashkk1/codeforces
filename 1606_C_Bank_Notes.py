def main():
    no_of_test_cases = int(input().strip())
    for i in range(no_of_test_cases):
        n, k = tuple(map(int, input().strip().split()))
        a = list(map(int, input().strip().split()))
        for i in range(n):
            a[i] = pow(10, a[i])

        k += 1
        ans = 0
        for i in range(n):
            no_of_notes = k
            if i + 1 < n:
                no_of_notes = min(no_of_notes, (a[i + 1] // a[i]) - 1)
            ans += (no_of_notes * a[i])
            k -= no_of_notes
        
        print(ans)


if __name__ == '__main__':
    main()