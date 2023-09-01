import time


def bubble_sort(data,draw):
    n=len(data)

    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                draw(data,['yellow' if x == j or x==j+1 else 'green' for x in range(len(data))])
                time.sleep(0.2)
    draw(data,['yellow' for x in range(len(data))])
