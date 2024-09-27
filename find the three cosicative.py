class Solution:
    def sumOfThree(self, num: int) -> List[int]:  # noqa: F821
        if (num-3)%3 == 0:
          
            x = (num-3)//3

            return [x,x+1,x+2]
        else:
            return []
        