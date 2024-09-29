class Solution:
    def average(self, salary: List[int]) -> float:  # noqa: F821
        min_salary = min(salary)
        max_salary = max(salary)
        total_sum = sum(salary) - min_salary -max_salary
        