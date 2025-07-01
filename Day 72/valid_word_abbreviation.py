class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        a, w = 0, 0  # Pointers for abbreviation and word respectively

        while a < len(abbr) and w < len(word):
            # Case 1: Current characters match directly
            if abbr[a] == word[w]:
                a += 1
                w += 1
                continue

            # Case 2: Invalid abbreviation character (not digit and not matching letter)
            if not abbr[a].isdigit() and abbr[a] != word[w]:
                return False

            # Case 3: Abbreviation cannot start with '0' (e.g., "01" is invalid)
            if abbr[a] == '0':
                return False

            # Case 4: Parse number from abbreviation to determine skip count
            skip = 0
            while a < len(abbr) and abbr[a].isdigit():
                skip = skip * 10 + (ord(abbr[a]) - ord('0'))  # Convert digit char to int
                a += 1

            w += skip  # Skip the indicated number of characters in `word`

        # Valid abbreviation only if both pointers reach the end
        return a == len(abbr) and w == len(word)
