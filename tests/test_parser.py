import unittest

class TestIntToRgb(unittest.TestCase):
    def test_green1(self):
        self.assertEqual(int_to_rgb(0x80c080), (128, 192, 128))
    def test_green2(self):
        self.assertEqual(int_to_rgb(0x8000), (0, 128, 0))
    def test_blue(self):
        self.assertEqual(int_to_rgb(0x8080), (0, 128, 128))


def int_to_rgb(color: int) -> tuple[int, int, int]:
    return (
        (color >> 16) & 0xFF,
        (color >> 8) & 0xFF,
        color & 0xFF,
    )