def binary_search(lst, target):
    start, end = 0, len(lst)
    mid = (start + end) // 2
    while target != lst[mid] and start != end:
        if target < lst[mid]:
            end = mid
        else:
            start = mid
        mid = (start + end) // 2
    return mid

if __name__ == "__main__":
    print(binary_search([1,2,3,4,5,6,7,8,9],8))