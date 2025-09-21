class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.av = {}
        self.r = SortedList()
        self.sp = {(shop, movie): price for shop, movie, price in entries}

        for shop, movie, price in entries:
            if movie not in self.av:
                self.av[movie] = SortedList()
            self.av[movie].add((price, shop))

    def search(self, movie: int) -> list[int]:
        return [shop for _, shop in self.av.get(movie, [])[:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.sp[(shop, movie)]
        self.av[movie].remove((price, shop))
        self.r.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.sp[(shop, movie)]
        self.r.remove((price, shop, movie))
        self.av[movie].add((price, shop))

    def report(self) -> list[list[int]]:
        return [[shop, movie] for _, shop, movie in self.r[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()