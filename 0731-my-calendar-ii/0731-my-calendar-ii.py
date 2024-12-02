class MyCalendarTwo:
    def __init__(self):
        self.booked = [] 
        self.overlaps = []  
    def book(self, start: int, end: int) -> bool:
        
        for o_start, o_end in self.overlaps:
            if max(start, o_start) < min(end, o_end):
                return False  
       
        for b_start, b_end in self.booked:
            if max(start, b_start) < min(end, b_end):
                self.overlaps.append((max(start, b_start), min(end, b_end)))
        self.booked.append((start, end))
        return True
