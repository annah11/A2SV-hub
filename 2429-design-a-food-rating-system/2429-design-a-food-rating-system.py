class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        
        self.mgb ={}
        self.hager = {}
        for food,cusine,rating in zip(foods,cuisines,ratings):
            self.mgb[food] = (cusine,rating)
            if cusine not in self.hager:
                self.hager[cusine] =[]
            heapq.heappush(self.hager[cusine], (-rating, food))
            # print(self.mgb)
    def changeRating(self, food: str, newRating: int) -> None:
        cusine,_ = self.mgb[food]
        self.mgb[food] = (cusine,newRating)

        heapq.heappush(self.hager[cusine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.hager[cuisine]
        while heap:
            neg_rating, food = heap[0]
            if -neg_rating == self.mgb[food][1]:
                return food
            heapq.heappop(heap)
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)