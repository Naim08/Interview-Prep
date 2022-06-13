

class Heap:
    def __init__(self, data):
        self.data = data
    
    
    def heapify(self, largest):
        
        i = 0
        l = 2 * i + 1
        r = 2 * i + 2
        while i < len(self.data) - 1 and l < len(self.data) - 1:
            
            if self.data[i] < self.data[l]:
                self.data[i], self.data[l] = self.data[l], self.data[i]
            
            if self.data[i] > self.data[r]:
                self.data[i], self.data[r] = self.data[r], self.data[i]
            print(self.data)
            l = 2 * i + 1
            r = 2 * i + 2
            i += 1
        
        print(self.data)
        
        

heap = Heap([ 12, 11, 13, 5, 6, 7] )

print(heap.heapify(2))