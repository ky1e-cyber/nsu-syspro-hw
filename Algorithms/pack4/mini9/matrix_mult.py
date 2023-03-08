from typing import List, Tuple, Optional, Iterable, Iterator

class Matrix():
    @staticmethod
    def vec_dot(v1: Iterable, v2: Iterable):
        return sum(
            map(
                lambda x: x[0] * x[1], 
                zip(v1, v2)
            )
        )

    @staticmethod
    def get_column_as_vec(matrix, column_number: int) -> Iterator:
        for row in matrix._lists:
            yield row[column_number]

    def __init__(self, from_list: List):
        width = len(from_list[0])
        for row in from_list[1::]:
            assert len(row) == width, "Lengths of the lists in matrix should be the same"
        self.dims = (len(from_list), width)
        self._lists = from_list

    def __mul__(self, other): ## -> Matrix
        pass

    def mul_classic(self, other): ## -> Matrix
        assert self.dims[1] == other.dims[0]
        
        res = [[0] * other.dims[1] for _ in range(self.dims[0])]

        for i, row in enumerate(self._lists):
            for j in range(other.dims[1]):
                res[i][j] = vec_dot(
                    row, 
                    get_column_as_vec(other, j)
                )

        return Matrix(res)

    def mul_rec(self, other): ## -> Matrix
        assert self.dims[1] == other.dims[0]
        raise NotImplementedError()
        pass

