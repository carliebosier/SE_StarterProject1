class Boggle:
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
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]
    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry",
        "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went",
        "wet", "arty", "rhr", "not", "quar"
    ]
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
