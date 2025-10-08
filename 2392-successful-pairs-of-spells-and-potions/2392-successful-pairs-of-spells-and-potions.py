class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pst = len(potions)
        result = []
        for spell_power in spells:
            required_strength = math.ceil(success / spell_power)
            if required_strength > potions[-1]:
                result.append(0)
                continue
            index = bisect.bisect_left(potions, required_strength)
            result.append(pst - index)
        return result