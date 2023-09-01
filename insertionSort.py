import time

def insertion_sort(array,draw):

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # draw(array, ['yellow' if x == i or x == i + 1 else 'cyan' if x <= i else 'green' for x in range(len(array))])
        # time.sleep(0.8)

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

            draw(array, ['yellow' if x == j else 'red' if x <= j else 'green' for x in range(len(array))])
            time.sleep(0.1)

        array[j + 1] = key

