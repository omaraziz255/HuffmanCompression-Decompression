from HuffmanCode.Heap import *


class Error(Exception):
    pass


class HeapUnderflow(Error):
    pass


class PriorityQueue:
    def __init__(self, array):
        self.heap = Heap(array)

    def heap_minimum(self):
        return self.heap.minHeap[0]

    def heap_extract_min(self):
        if self.heap.heapSize < 1:
            raise HeapUnderflow
        minimum = self.heap_minimum()
        self.heap.minHeap[0] = self.heap.minHeap[self.heap.heapSize - 1]
        self.heap.heapSize -= 1
        self.heap.minHeap.pop()
        self.heap.min_heapify(0)
        return minimum

    def insert(self, node):
        self.heap.heapSize += 1
        self.heap.minHeap.append(node)
        self.heap.min_heapify(self.heap.heapSize - 1)
