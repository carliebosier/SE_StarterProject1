import unittest
from boggle_solver import Boggle


class TestBoggleSolver(unittest.TestCase):

    def test_normal_grid_valid_dictionary(self):
        grid = [["T", "W", "Y", "R"],
                ["E", "N", "P", "H"],
                ["G", "Z", "Qu", "R"],
                ["O", "N", "T", "A"]]
        dictionary = ["art", "ego", "gent", "get", "net", "new", "newt",
                      "prat", "pry", "qua", "quart", "quartz", "rat", "tar",
                      "tarp", "ten", "went", "wet", "arty"]
        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()
        expected = ['ART', 'ARTY', 'GENT', 'GET', 'NET', 'NEW', 'NEWT',
                    'PRAT', 'PRY', 'QUA', 'QUART', 'QUARTZ', 'RAT', 'TAR',
                    'TARP', 'TEN', 'WENT', 'WET']
        self.assertEqual(sorted(result), sorted(expected))

    def test_empty_dictionary(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = []
        boggle = Boggle(grid, dictionary)
        self.assertEqual(boggle.getSolution(), [])

    def test_empty_grid(self):
        grid = []
        dictionary = ["ABC"]
        boggle = Boggle(grid, dictionary)
        self.assertEqual(boggle.getSolution(), [])

    def test_mismatched_row_lengths(self):
        grid = [["A", "B", "C"], ["D", "E"], ["F", "G", "H"]]
        dictionary = ["abc", "def"]
        boggle = Boggle(grid, dictionary)
        self.assertEqual(boggle.getSolution(), [])

    def test_lowercase_grid_and_mixed_case_dictionary(self):
        grid = [["a", "b"], ["c", "d"]]
        dictionary = ["ABC", "BCD", "CDA"]
        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()
        self.assertIn("ABC", result)

    def test_grid_with_Qu_tile(self):
        grid = [["Qu", "A"], ["R", "T"]]
        dictionary = ["quart", "quit", "quar"]
        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()
        self.assertIn("QUART", result)

    def test_dictionary_with_short_words(self):
        grid = [["C", "A"], ["T", "D"]]
        dictionary = ["ca", "cat", "at"]
        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()
        self.assertIn("CAT", result)
        self.assertNotIn("CA", result)  # too short
        self.assertNotIn("AT", result)  # too short

    def test_single_row_grid(self):
        grid = [["C", "A", "T", "S"]]
        dictionary = ["cats", "cat", "acts"]
        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()
        self.assertIn("CATS", result)

    def test_single_column_grid(self):
        grid = [["D"], ["O"], ["G"]]
        dictionary = ["dog", "god"]
        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()
        self.assertIn("DOG", result)

    def test_diagonal_word(self):
        grid = [["C", "A"], ["T", "S"]]
        dictionary = ["cats", "cast"]
        boggle = Boggle(grid, dictionary)
        result = boggle.getSolution()
        self.assertIn("CAST", result)


if __name__ == "__main__":
    unittest.main()
