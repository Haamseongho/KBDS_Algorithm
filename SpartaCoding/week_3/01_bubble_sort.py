input = [4, 6, 2, 9, 1]


# for i in range(len(array) - 1):
#   for j in range(i + 1, len(array)):
#      if array[i] > array[j]:
#         array[i], array[j] = array[j], array[i]

def bubble_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
