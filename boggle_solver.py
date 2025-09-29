class Boggle:
<<<<<<< HEAD
    def __init__(self, grid=None, dictionary=None):
        self.grid = grid
        self.dictionary = dictionary
        self.solution = []
        self._solved = False
        self.rows = 0
        self.cols = 0
        self.debug = False  # Toggle for internal debug logs

    def setGrid(self, grid):
        self._solved = False
        self.solution = []
        self.grid = grid

    def setDictionary(self, dictionary):
        self._solved = False
        self.solution = []
        self.dictionary = dictionary

    def getSolution(self):
        """
        Returns the sorted list of found words in uppercase. Solves if not already solved.
        """
        if not self._solved:
            self._solve()
            self._solved = True
        return self.solution

    def _solve(self):
        """
        Main solving logic: validates input, processes dictionary, performs DFS on grid.
        """
        # Basic validation
        if self.grid is None or self.dictionary is None:
            self.solution = []
            return

        if not isinstance(self.grid, list) or len(self.grid) == 0 or not all(isinstance(row, list) for row in self.grid):
            self.solution = []
            return

        self.rows = len(self.grid)
        self.cols = len(self.grid[0]) if self.rows > 0 else 0
        if self.cols == 0:
            self.solution = []
            return

        for row in self.grid:
            if len(row) != self.cols:
                self.solution = []
                return
            if not all(isinstance(cell, str) for cell in row):
                self.solution = []
                return

        # Normalize to lowercase
        processed_grid, processed_dictionary = self._convert_case_to_lower(self.grid, self.dictionary)

        # Build dictionary and prefix sets
        self.dictionary_set = set(word for word in processed_dictionary if len(word) >= 3)
        self.prefix_set = self._create_prefix_set(processed_dictionary)

        if not self.dictionary_set:
            self.solution = []
            return

        solution_set = set()

        for y in range(self.rows):
            for x in range(self.cols):
                visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
                self._find_words("", y, x, visited, solution_set, processed_grid)

        self.solution = self._format_solution(solution_set)

    def _find_words(self, current_word, y, x, visited, solution_set, grid):
        # Bounds and visited check
        if y < 0 or y >= self.rows or x < 0 or x >= self.cols or visited[y][x]:
            return

        tile = grid[y][x]
        new_word = current_word + tile.lower()  # Ensure lowercase tile

        # Prune if no words start with this prefix
        if new_word not in self.prefix_set:
            return

        visited[y][x] = True

        if len(new_word) >= 3 and new_word in self.dictionary_set:
            solution_set.add(new_word)

        # Explore all 8 directions
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dy == 0 and dx == 0:
                    continue
                self._find_words(new_word, y + dy, x + dx, visited, solution_set, grid)

        visited[y][x] = False

    def _convert_case_to_lower(self, grid, dictionary):
        """Normalize grid and dictionary to lowercase, stripping whitespace and validating."""
        lowered_grid = [[cell.lower() for cell in row] for row in grid]
        lowered_dictionary = [word.strip().lower() for word in dictionary if isinstance(word, str)]
        return lowered_grid, lowered_dictionary

    def _create_prefix_set(self, dictionary):
        """Builds a set of all valid prefixes for dictionary pruning."""
        prefix_set = set()
        for word in dictionary:
            for i in range(1, len(word) + 1):
                prefix_set.add(word[:i])
        return prefix_set

    def _format_solution(self, solution_set):
        """Formats the final output as a sorted list of uppercase words."""
        return sorted([word.upper() for word in solution_set])


def main():
    """Optional: basic debug run."""
    print("--- Boggle Solver Debug Run ---")
    grid = [["Qu", "A"], ["R", "T"]]
    dictionary = ["quart", "quit", "quar", "quartz"]
    b = Boggle(grid, dictionary)
    b.debug = True
    print("Solution:", b.getSolution())

=======
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

    def getSolution(self):
        # 1. Check input parameters are valid
        if self.grid is None or self.dictionary is None:
            return self.solutions

        # 1b. Check if grid is NxN
        N = len(self.grid)
        for row in self.grid:
            if len(row) != N:
                return self.solutions

        # Convert input data into the same case
        self.convert_case_to_lower(self.grid, self.dictionary)

        # Check if grid is valid
        if not self.is_grid_valid(self.grid):
            return self.solutions

        # Setup all data structures
        solution_set = set()
        hash_map = self.create_hash_map(self.dictionary)

        # Iterate over the NN grid - find all words that begin with grid[y][x]
        for y in range(N):
            for x in range(N):
                word = ""
                visited = [[False for _ in range(N)] for _ in range(N)]
                self.find_words(word, y, x, self.grid, visited, hash_map, solution_set)

        self.solutions = list(solution_set)
        return self.solutions

    def find_words(self, word, y, x, grid, visited, hash_map, solution_set):
        # Base Case: y and x are out of bounds or already visited
        if y < 0 or x < 0 or y >= len(grid) or x >= len(grid) or visited[y][x]:
            return

        # Append grid[y][x] to the word
        word += grid[y][x]

        # Check if the new word is a prefix for any word in the hash_map
        if word not in hash_map["prefixes"]:
            return

        # Mark as visited
        visited[y][x] = True

        # Check if it's an actual word in the dictionary
        if len(word) >= 3 and word in hash_map["words"]:
            solution_set.add(word)

        # Continue searching using the adjacent tiles
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == 0 and dx == 0:
                    continue
                self.find_words(word, y + dy, x + dx, grid, visited, hash_map, solution_set)

        # Unmark location y, x as visited
        visited[y][x] = False

    def convert_case_to_lower(self, grid, dictionary):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                self.grid[i][j] = grid[i][j].lower()

        for i in range(len(dictionary)):
            self.dictionary[i] = dictionary[i].lower()

    def is_grid_valid(self, grid):
      for row in grid:
          for cell in row:
              if not cell.isalpha():
                  return False
      return True


    def create_hash_map(self, dictionary):
        # Create hash map with words and prefixes
        words = set(dictionary)
        prefixes = set()
        for word in dictionary:
            for i in range(1, len(word) + 1):
                prefixes.add(word[:i])
        return {"words": words, "prefixes": prefixes}


def main():
    grid = [["T", "W", "Y", "R"],
            ["E", "N", "P", "H"],
            ["G", "Z", "Qu", "R"],
            ["O", "N", "T", "A"]]
    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry",
        "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet",
        "arty", "rhr", "not", "quar"
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())
>>>>>>> 87ea53ecf9f455658b908d19653744a2a715a7ac

if __name__ == "__main__":
    main()
