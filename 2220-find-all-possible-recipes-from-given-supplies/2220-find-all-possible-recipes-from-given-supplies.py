class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = {}
        
        for r, ing_list in zip(recipes, ingredients):
            indegree[r] = len(ing_list)
            for ing in ing_list:
                graph[ing].append(r)
        
        queue = deque(supplies)
        res = []
        
        while queue:
            item = queue.popleft()
            
            if item in graph:
                for recipe in graph[item]:
                    indegree[recipe] -= 1
                    if indegree[recipe] == 0:
                        queue.append(recipe)
                        res.append(recipe)
        
        return res