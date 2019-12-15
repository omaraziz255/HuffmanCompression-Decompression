class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq


class Heap:
    def __init__(self, array):
        self.heapSize = array.__len__()
        self.minHeap = array
        for i in range((self.heapSize//2)-1, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        left_child = left(i)
        right_child = right(i)
        smallest = i
        if left_child < self.heapSize and self.minHeap[left_child].freq < self.minHeap[smallest].freq:
            smallest = left_child
        if right_child < self.heapSize and self.minHeap[right_child].freq < self.minHeap[smallest].freq:
            smallest = right_child
        if smallest != i:
            self.minHeap[i], self.minHeap[smallest] = self.minHeap[smallest], self.minHeap[i]
            self.min_heapify(smallest)


def right(i):
    return (i * 2) + 2


def left(i):
    return (i * 2) + 1


def parent(i):
    return i // 2

