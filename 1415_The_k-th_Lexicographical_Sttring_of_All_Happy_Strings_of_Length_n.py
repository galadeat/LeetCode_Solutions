class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']
        res: List[str] = []

        def invalid_path(path: List[str]) -> bool:
            for i in range(0, len(path) - 1):
                if path[i] == path[i + 1]:
                    return True
            return False

        def dfs(start_index: int, path: List[str]) -> None:
            if invalid_path(path):
                return
            if start_index == n:
                res.append("".join(path))
                return
            for letter in "abc":
                path.append(letter)
                dfs(start_index + 1, path)
                path.pop()

        dfs(0, [])
        return res[k - 1] if k - 1 < len(res) else ""