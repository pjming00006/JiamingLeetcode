class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_ind = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    continue
                else:
                    if zero_ind[i][j] == 1:
                        continue
                    else:
                        print(f"current: {matrix[i][j]}, i:{i}, :{j}")
                        i1, j1 = i, j
                        while i1 - 1 >= 0:
                            if matrix[i1-1][j1] != 0:
                                matrix[i1-1][j1] = 0
                                zero_ind[i1-1][j1] = 1
                            i1 -= 1
                        i1 = i
                        while j1 - 1 >= 0:
                            if matrix[i1][j1-1] != 0:
                                matrix[i1][j1-1] = 0
                                zero_ind[i1][j1-1] = 1
                            j1 -= 1
                        j1 = j
                        while i1 + 1 < len(matrix):
                            if matrix[i1+1][j1] != 0:
                                matrix[i1+1][j1] = 0
                                zero_ind[i1+1][j1] = 1
                            i1 += 1
                        i1 = i
                        while j1 + 1 < len(matrix[i]):
                            if matrix[i1][j1+1] != 0:
                                matrix[i1][j1+1] = 0
                                zero_ind[i1][j1+1] = 1
                            j1 += 1

    def setZeroesSet(self, matrix: List[List[int]]) -> None:
        rows, cols = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in cols:
                    matrix[i][j] = 0

    def setZeroesNoAdditionalSpace(self, matrix: List[List[int]]) -> None:
        is_first_col_zero = False

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                is_first_col_zero = True
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if is_first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0