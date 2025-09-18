class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.sira = SortedSet()
        self.yene_sira = {}
        self.kedami = {}
        for user_id, task_id,priority in tasks:
            self.add(user_id, task_id, priority)
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.sira.add((priority, taskId, userId))
        self.yene_sira[taskId] = userId
        self.kedami[taskId] = priority
    def edit(self, taskId: int, newPriority: int) -> None:
        user = self.yene_sira[taskId]
        self.rmv(taskId)
        self.add(user, taskId, newPriority)        
    def rmv(self, taskId: int) -> None:
        user = self.yene_sira[taskId]        
        priority = self.kedami[taskId]
        self.sira.remove((priority, taskId, user))
        del self.yene_sira[taskId]
        del self.kedami[taskId]
    def execTop(self) -> int:
        if not self.sira:
            return -1
        _, task_id, user_id = self.sira[-1]
        self.rmv(task_id)
        return user_id



# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()