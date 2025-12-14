import unittest
from pdf_parser.utils import int_to_rgb

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