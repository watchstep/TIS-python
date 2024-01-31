class BinaryHeap(object):
    def __init__(self):
        self.items = [None]
    
    def __len__(self):
        return len(self.items) - 1 # 마지막 요소의 인덱스를 가져오기 위해 -1
    
    # Up-Heap 연산
    # 반복 구조로 구현
    def _percolate_up(self): # O(logn)
        i = len(self)
        parent = i // 2
        while parent >= 0:
            # 자식 노드가 부모 노드보다 작으면, 스왑
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] = self.items[i], self.items[parent]
            i = parent
            parent = i // 2
            
    def insert(self, k): 
        self.itemsp.append(k) # 요소 가장 마지막에 삽입
        self._percolate_up() # 부모 값과 비교하면서 스왑 진행
    
    # 재귀 구조로 구현
    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx
        
        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
            
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right
        
        if smallest != idx:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
            self._percolate_down(smallest)
            
    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted
            