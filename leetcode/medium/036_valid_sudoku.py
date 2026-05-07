import collections


class Solution:
    def isValidSudoku(self, board):
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value != "." and (
                    value in rows[i]
                    or value in cols[j]
                    or value in boxes[(i // 3, j // 3)]
                ):
                    return False

                elif value != ".":
                    rows[i].add(value)
                    cols[j].add(value)
                    boxes[(i // 3, j // 3)].add(value)

        return True


def run_test(board, expected):
    result = Solution().isValidSudoku(board)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status} | expected={expected}, got={result}")


if __name__ == "__main__":
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    invalid_row = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "5"],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    invalid_box = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", "5", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    run_test(valid_board, True)
    run_test(invalid_row, False)
    run_test(invalid_box, False)
