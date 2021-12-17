def get_no_of_msgs(k, x):
    if x > k * k:
        return (2 * k - 1)
    
    no_of_msgs = 0
    tot_emotes = 0
    for i in range(1, k + 1):
        tot_emotes += i
        if tot_emotes >= x:
            no_of_msgs += i
            break
    
    if no_of_msgs != 0:
        return no_of_msgs
    
    no_of_msgs = k
    for i in range(k - 1, 0, -1):
        tot_emotes += i
        if tot_emotes >= x:
            no_of_msgs += (k - i)
            break
    
    return no_of_msgs

def bsearch(x, l, h):
    while l <= h:
        m = (l + h) // 2
        sum_of_first_m_nums = m * (m + 1) // 2
        if x == sum_of_first_m_nums:
            return m
        elif x > sum_of_first_m_nums:
            l = m + 1
        else:
            h = m - 1
    return l

def r_bsearch(x, l, h):
    sum_of_k_minus_one_nums = h * (h + 1) // 2
    orig_h = h
    
    while l <= h:        
        m = (l + h) // 2
        sum_of_first_m_nums = sum_of_k_minus_one_nums - ((orig_h - m) * (orig_h - m + 1) // 2)
        if x == sum_of_first_m_nums:
            return m
        elif x < sum_of_first_m_nums:
            h = m - 1
        else:
            l = m + 1  
    
    return l

        
def get_no_of_msgs_log_n(k, x):
    if x > k * k:
        return (2 * k - 1)
    
    sum_of_first_k = k * (k + 1) // 2
    if x <= sum_of_first_k:
        return bsearch(x, 1, k)
    no_of_msgs = k
    x -= sum_of_first_k
    no_of_msgs += r_bsearch(x, 1, k - 1)

    return no_of_msgs




def main():
    no_of_test_cases = int(input().strip())
    for i in range(no_of_test_cases):
        k, x = tuple(map(int, input().strip().split()))
        print(get_no_of_msgs_log_n(k, x))

if __name__ == '__main__':
    main()