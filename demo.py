
def sorting(lst : list[int])-> list:
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst

lst = [1,2,3,4,5,6,7]

def buble_sort(lst: list[int]) -> list:
    size = len(lst)
    sorted = True
    for i in range(size):
        for j in range((size-i)-1):
            if lst[j] > lst[j+1]:
                # print(lst[i] ,">", lst[j+1])
                lst[j], lst[j+1] = lst[j+1], lst[j]
                sorted = False
        print(lst)
        if sorted:
            print("list is sorted")
            break
    # return lst
    
lst.sort(reverse=True)
print(lst)

# print("----")
# print(buble_sort(lst))
new_lst = [330, 302, 202]

lst.extend(new_lst)
print(lst)