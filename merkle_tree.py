import attr


@attr.s
class BinaryMerkleTree:
    data = attr.ib(default=None)
    _left = attr.ib(default=None, init=False)
    _right = attr.ib(default=None, init=False)
    _hash: int = attr.ib(init=False)

    @data.validator
    def sortable(self, attribute, value):
        vcls = value.__class__
        if vcls.__lt__ == object.__lt__ and vcls.__gt__ == object.__gt__:
            raise ValueError("Need comparable object for data")

    @_hash.default
    def calculate_hash(self) -> int:
        h = hash(self.data)
        if self._left:
            h += self._left.calculate_hash()
        if self._right:
            h += self._right.calculate_hash()
        return h

    def get_hash(self) -> int:
        return self._hash

    def insert(self, data):
        if not isinstance(self.data, data.__class__):
            raise ValueError("Type of data must be the same")

        if data < self.data:
            if self._left:
                self._left.insert(data)
            else:
                self._left = BinaryMerkleTree(data)
        else:
            if self._right:
                self._right.insert(data)
            else:
                self._right = BinaryMerkleTree(data)
        self._hash = self.calculate_hash()

    def print(self):
        if self._left:
            self._left.print()
        print(f"data: {self.data}, hash: {self._hash}")
        if self._right:
            self._right.print()
