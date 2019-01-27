import unittest


def largest_loss(pricesList):
    if len(pricesList) <= 1:
        return 0

    max_value = max(pricesList)
    last_max_index = max(i for i, v in enumerate(pricesList) if v == max_value)
    if last_max_index == 0:
        return 0

    min_value = min(pricesList[:last_max_index])
    return max_value - min_value


class TestLargestLoss(unittest.TestCase):

    def test_empty(self):
        loss = largest_loss([])
        self.assertEqual(0, loss)

    def test_one(self):
        loss = largest_loss([1])
        self.assertEqual(0, loss)

    def test_zero_one(self):
        loss = largest_loss([0,1])
        self.assertEqual(1, loss)

    def test_one_zero(self):
        loss = largest_loss(([1,0]))
        self.assertEqual(0, loss)

    def test_one_one(self):
        loss = largest_loss([1,1])
        self.assertEqual(0, loss)

    def test_one_zero_one(self):
        loss = largest_loss([1,0,1])
        self.assertEqual(1, loss)


if __name__ == '__main__':
    unittest.main()