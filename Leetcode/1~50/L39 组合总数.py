class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def find(sums, visit):
            for i in candidates:
                if not visit or i >= visit[-1]:
                    if sums + i == target:
                        result.append(visit + [i])
                        return
                    elif sums + i < target:
                        find(sums + i, visit + [i])
                    else:
                        return

        find(0, [])
        return result
