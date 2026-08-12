class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        visited = [[False] * cols for _ in range(rows)]

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(row, col, i):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            if visited[row][col]:
                return False

            if board[row][col] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            visited[row][col] = True

            for dr, dc in directions:
                if dfs(row + dr, col + dc, i + 1):
                    return True

            visited[row][col] = False

            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True

        return False
        