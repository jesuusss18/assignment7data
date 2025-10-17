class Patient:
    def __init__(self,name,urgency):
        self.name = name
        self.urgency = urgency



class MinHeap:
    def __init__(self):
        self.data = []


    def heapify_up(self,index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] =  self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break
    
    def heapify_down(self,index):
        size = len(self.data)
        while index < size:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left

            if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right
            
            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break 
            
    def insert(self,patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        for patient in self.data:
            print(f"{patient.name}'s urgency level is {patient.urgency} ")
    def peek(self):
        if self.data:
            return self.data[0]
    def remove_min(self):
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        
        min_value = self.data[0] 
        self.data[0] = self.data.pop() 
        self.heapify_down(0) 
        return min_value

heap = MinHeap()
heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))
heap.insert(Patient("Jesus", 0))
heap.insert(Patient("Lucia", 4))
heap.print_heap()

print("Current Queue:")
heap.print_heap()

served = heap.remove_min()
print(f"Served patient: {served.name}")  

print("Queue after removal:")
heap.print_heap()