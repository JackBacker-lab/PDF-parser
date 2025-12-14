import unittest

def int_to_rgb(color: int) -> tuple[int, int, int]:
    if not 0 <= color <= 0xFFFFFF:
        raise ValueError("color must be 0..0xFFFFFF")
    return (
        (color >> 16) & 0xFF,
        (color >> 8) & 0xFF,
        color & 0xFF,
    )

class TestIntToRgb(unittest.TestCase):
    def test_basic_colors(self):
        self.assertEqual(int_to_rgb(0x80c080), (128, 192, 128))
        self.assertEqual(int_to_rgb(0x8000), (0, 128, 0))
        self.assertEqual(int_to_rgb(0x8080), (0, 128, 128))
        self.assertEqual(int_to_rgb(0x000000), (0, 0, 0))
        self.assertEqual(int_to_rgb(0xFFFFFF), (255, 255, 255))
    
    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            int_to_rgb(-1)
        with self.assertRaises(ValueError):
            int_to_rgb(0x1000000)
        

if __name__ == "__main__":
    unittest.main()