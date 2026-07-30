class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowFreq = {}
        colFreq = {}
        sqFreq = {}
        for i in range(0, len(board)):
            row = board[i]
            for j in range(0, len(row)):
                value = row[j]
                if value == ".":
                    continue
                k = (i // 3) * 3 + (j // 3)
                if rowFreq.get(i) is None:
                    rowFreq[i] = [value]
                else:
                    if value in rowFreq[i]:
                        print(value, i, rowFreq)
                        return False
                    rowFreq[i].append(value)
                if colFreq.get(j) is None:
                    colFreq[j] = [value]
                else:
                    if value in colFreq[j]:
                        print(value, j, colFreq)
                        return False
                    colFreq[j].append(value)
                if sqFreq.get(k) is None:
                    sqFreq[k] = [value]
                else:
                    if value in sqFreq[k]:
                        print(value, k, sqFreq)
                        return False
                    sqFreq[k].append(value)
        print(rowFreq)
        print(colFreq)
        print(sqFreq)
        return True
