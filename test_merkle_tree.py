from merkle_tree import BinaryMerkleTree


def test_merkle_tree():
    merkle_tree = BinaryMerkleTree("a")

    # this value changes each time
    assert merkle_tree.get_hash()
