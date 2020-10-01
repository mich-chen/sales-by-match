def sockMerchant(n, ar):

    # initialize a dictionary as a stack
    stack = {}
    # keep track of pair count
    pair_count = 0

    # iterate through array using n length
    for i in range(n):
        # if stack contains matching sock color integer
        if stack.get(ar[i], None):
            # pop matching sock color from stack
            stack.pop(ar[i])
            # increment pair count only when a matching pair is found
            pair_count += 1
        # if stack does not contain sock color, push integer to stack
        else:
            # adding stack as a key for dictionary stack
            stack[ar[i]] = 1

    return pair_count


if __name__ == '__main__':

    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    print(sockMerchant(n, ar))
