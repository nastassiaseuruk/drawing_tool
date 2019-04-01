import unittest
import os
from drawing_tool import drawing_tool


class DrawTootTest(unittest.TestCase):

    def tearDown(self):
        os.remove(f"test_output.txt")

    def test_drawing_tool(self):
        drawing_tool("input.txt", "test_output.txt")
        with open("output.txt", "r") as f:
            expected_output = f.read()
        with open("test_output.txt", "r") as f:
            produced_output = f.read()
        self.assertEquals(expected_output, produced_output)
