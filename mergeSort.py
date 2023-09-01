import time

def merge_sort(array,draw):
    merge_sort_algo(array,0,len(array)-1,draw)

def merge_sort_algo(array, l, r, draw):
    if l < r:
        mid = (l + r) // 2
        merge_sort_algo(array, l, mid,draw)
        merge_sort_algo(array, mid + 1, r,draw)
        merge(array,l,mid,r,draw)

def merge(array,l,mid,r,draw):
    draw(array, color(len(array), l, mid, r))
    time.sleep(0.2)

    leftpart = array[l:mid+1]
    rightpart = array[mid+1:r+1]

    left_idx=right_idx=0

    for arr_idx in range(l,r+1):
        if left_idx < len(leftpart) and right_idx < len(rightpart):
            if leftpart[left_idx] <= rightpart[right_idx]:
                array[arr_idx] = leftpart[left_idx]
                left_idx+=1
            else:
                array[arr_idx]= rightpart[right_idx]
                right_idx+=1
        elif left_idx < len(leftpart):
            array[arr_idx] = leftpart[left_idx]
            left_idx+=1

        else:
            array[arr_idx] = rightpart[right_idx]
            right_idx += 1

    draw(array, ['green' if l <= x <= r else 'white' for x in range(len(array))])
    time.sleep(0.2)


def color(arrayLen, l, mid, r):
    colorArray = []

    for i in range(arrayLen):
        if l <= i <= r:
            if l <= i <= mid:
                colorArray.append('yellow')
            else:
                colorArray.append('purple')
        else:
            colorArray.append('white')

    return colorArray
