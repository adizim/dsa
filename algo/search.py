def binary_search(lst, x):
    s, e = 0, len(lst) - 1 
    while s <= e:
        mid = (s + e) // 2
        if x == lst[mid]:
            return mid
        elif x < lst[mid]:
            e = mid - 1
        else:
            s = mid + 1
    return -1

def binary_search_recursive(lst, x):
    return binary_search_helper(lst, x, 0, len(lst) - 1)

def binary_search_helper(lst, x, s, e):
    if s > e:
        return -1
    
    mid = (s + e) // 2
    if x == lst[mid]:
        return mid
    elif x < lst[mid]:
        return binary_search_helper(lst, x, s, mid - 1)
    return binary_search_helper(lst, x, mid + 1, e)

if __name__ == "__main__":
    print(binary_search_recursive([1,2,3,4,5,6],5))