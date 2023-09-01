import time


def partition(array, low, high,draw):
    pivot = array[high]

    i = low - 1

    draw(array,color(len(array),low,high,i,i))
    time.sleep(0.1)

    for j in range(low, high):
        if array[j] <= pivot:
            draw(array, color(len(array), low, high, i, j,True))
            time.sleep(0.1)

            i += 1
            (array[i], array[j]) = (array[j], array[i])

        draw(array, color(len(array), low, high, i, j))
        time.sleep(0.1)

    draw(array, color(len(array), low, high, i, high,True))
    time.sleep(0.1)
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quick_sort(array, low, high,draw):
    if low < high:
        pi = partition(array, low, high,draw)

        quick_sort(array, low, pi - 1,draw)

        quick_sort(array, pi + 1, high,draw)


def color(arrayLen,low,high,border,currIdx,iSwapping=False):

    colorArray=[]
    for i in range(arrayLen):
        if low <= i <= high:
            colorArray.append("gray")
        else:
            colorArray.append("white")

        if i == high:
            colorArray[i] = 'orange'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if iSwapping:
            if i == border or i == currIdx:
                colorArray[i] = 'purple'

    return colorArray
