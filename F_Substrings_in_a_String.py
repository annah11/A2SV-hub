import sys
import bisect

class StringProcessor:
    def __init__(self, s):
        self.s = list(s)  # Convert to list for mutation
        self.n = len(s)
        self.occurrences = {}  # Stores positions of each substring
        self.preprocess_occurrences()

    def preprocess_occurrences(self):
        """Precomputes occurrences of all substrings using a dictionary of lists."""
        for i in range(self.n):
            for j in range(i + 1, min(self.n, i + 100) + 1):  # Limit substring length to 100 for efficiency
                substr = ''.join(self.s[i:j])
                if substr not in self.occurrences:
                    self.occurrences[substr] = []
                self.occurrences[substr].append(i + 1)  # 1-based indexing

    def update_character(self, i, c):
        """Updates character at position i (1-based index) to c and updates occurrences."""
        i -= 1  # Convert to 0-based index
        if self.s[i] == c:
            return  # No change needed

        # Remove old occurrences in affected range
        for j in range(max(0, i - 100), min(self.n, i + 100)):  # Limit update range
            for k in range(j + 1, min(self.n, j + 100) + 1):
                substr = ''.join(self.s[j:k])
                if substr in self.occurrences:
                    if i + 1 in self.occurrences[substr]:  # Remove old entry
                        self.occurrences[substr].remove(i + 1)

        # Update character
        self.s[i] = c

        # Recalculate occurrences in affected range
        for j in range(max(0, i - 100), min(self.n, i + 100)):
            for k in range(j + 1, min(self.n, j + 100) + 1):
                substr = ''.join(self.s[j:k])
                if substr not in self.occurrences:
                    self.occurrences[substr] = []
                self.occurrences[substr].append(j + 1)

    def count_occurrences(self, l, r, y):
        """Counts occurrences of y in substring s[l:r] using binary search."""
        if y not in self.occurrences:
            return 0
        positions = self.occurrences[y]
        left = bisect.bisect_left(positions, l)
        right = bisect.bisect_right(positions, r)
        return right - left

# Read input
input = sys.stdin.read
data = input().split("\n")

s = data[0].strip()
q = int(data[1].strip())
processor = StringProcessor(s)

results = []
index = 2
for _ in range(q):
    query = data[index].strip().split()
    index += 1

    if query[0] == '1':
        i = int(query[1])
        c = query[2]
        processor.update_character(i, c)

    elif query[0] == '2':
        l, r, y = int(query[1]), int(query[2]), query[3]
        results.append(str(processor.count_occurrences(l, r, y)))

# Output all results
sys.stdout.write("\n".join(results) + "\n")
