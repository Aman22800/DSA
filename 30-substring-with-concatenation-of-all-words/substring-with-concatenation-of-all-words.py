class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        # All words have the same length
        word_len = len(words[0])

        # Store required frequency of each word
        need = {}
        for word in words:
            need[word] = need.get(word, 0) + 1

        ans = []

        # Try every possible starting offset within a word
        # Example: word_len = 3 → offsets 0, 1, 2
        for offset in range(word_len):

            left = offset
            right = offset

            # Frequency of words in the current window
            window = {}

            # Number of words currently in the window
            count = 0

            # Move right one complete word at a time
            while right + word_len <= len(s):

                # Extract the next word
                word = s[right:right + word_len]
                right += word_len

                # If word is not required, reset the window
                if word not in need:
                    window = {}
                    left = right
                    count = 0
                    continue

                # Add the word to the current window
                window[word] = window.get(word, 0) + 1
                count += 1

                # If we have too many copies of this word,
                # remove words from the left until the frequency is valid
                while window[word] > need[word]:
                    left_word = s[left:left + word_len]
                    window[left_word] -= 1
                    left += word_len
                    count -= 1

                # If we have exactly the required number of words,
                # the current window is a valid concatenation
                if count == len(words):
                    ans.append(left)

        return ans