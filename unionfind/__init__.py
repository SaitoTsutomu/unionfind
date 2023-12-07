# see pyproject.toml
__version__ = "0.1.1"
__author__ = "Saito Tsutomu <tsutomu7@hotmail.co.jp>"
from typing import Optional


class unionfind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i: int, j: int) -> None:
        i = self.find(i)
        j = self.find(j)
        if i != j:
            self.parent[i] = j

    def issame(self, i: int, j: int) -> bool:
        return self.find(i) == self.find(j)

    def groups(self) -> list[list[int]]:
        r = range(len(self.parent))
        return [[j for j in r if self.issame(j, i)] for i in r if i == self.parent[i]]

    @staticmethod
    def isconnected(ll: list[list[bool]], u: Optional["unionfind"] = None) -> bool:
        nw, nh = len(ll), len(ll[0])
        rw, rh = range(nw), range(nh)
        if not u:
            u = unionfind(nw * nh)
        f = -1
        for i in rw:
            for j in rh:
                if not ll[i][j]:
                    continue
                if f < 0:
                    f = i + j * nw
                if j > 0 and ll[i][j] == ll[i][j - 1]:
                    u.unite(i + j * nw, i + j * nw - nw)
                if i > 0 and ll[i][j] == ll[i - 1][j]:
                    u.unite(i + j * nw, i + j * nw - 1)
        return f >= 0 and all([u.issame(f, i + j * nw) for i in rw for j in rh if ll[i][j]])

    @staticmethod
    def isconnectedlist(nw: int, nh: int, lst: list[tuple[int, int]]) -> bool:
        ll = [[False] * nw for j in range(nh)]
        for i, j in lst:
            ll[i][j] = True
        return unionfind.isconnected(ll)
