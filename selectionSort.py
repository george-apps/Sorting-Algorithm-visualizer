import time


def selection_sort(array,draw):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            draw(array, ['yellow' if a == min_index or a == i else 'green' if a <= i else 'cyan' for a in range(len(array))])
            time.sleep(0.1)

            if array[min_index] > array[j]:
                # draw(array, ['red' if a == min_index or a == j else 'green' if a <= i else 'cyan' for a in range(len(array))])
                # time.sleep(0.2)
                min_index = j

        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

            # draw(array, ['orange' if a == min_index or a == i else 'green' if a <= i else 'cyan' for a in range(len(array))])
            # time.sleep(0.2)