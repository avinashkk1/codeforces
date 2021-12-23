
def main():
    no_of_test_cases = int(input().strip())
    for i in range(no_of_test_cases):
        n, h = tuple(map(int, input().strip().split()))
        a = list(map(int, input().strip().split()))

        low = 0
        high = h
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            kFunc_val = mid
            for i in range(0, n - 1, 1):
                kFunc_val += min(mid, a[i + 1] - a[i])
            if kFunc_val >= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        print(ans)

def main1():
    no_of_test_cases = int(input().strip())
    for i in range(no_of_test_cases):
        n, h = tuple(map(int, input().strip().split()))
        a = list(map(int, input().strip().split()))

        def kFunc(k):
            kFunc_val = 0
            for i in range(0, n - 1, 1):
                kFunc_val += min(k, a[i + 1] - a[i])
            return k + kFunc_val



        def getMinK():
            low = 0
            high = h
            ans = 0
            while low <= high:
                mid = (low + high) // 2
                if kFunc(mid) >= h:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            return ans


        print(getMinK())

if __name__ == '__main__':
    main()