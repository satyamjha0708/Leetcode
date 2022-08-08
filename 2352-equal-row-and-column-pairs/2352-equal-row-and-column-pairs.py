class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(map(tuple, grid))
        cols = Counter(map(tuple, zip(*grid)))
        print(rows, cols)
        return sum(rows[row]*cols[row] for row in rows)