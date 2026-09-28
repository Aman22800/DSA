class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        # Required frequency of each character
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        have = 0
        required = len(need)

        left = 0
        min_len = float("inf")
        min_start = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # Character requirement is now satisfied
            if ch in need and window[ch] == need[ch]:
                have += 1

            # Try to shrink the window
            while have == required:
                current_len = right - left + 1

                if current_len < min_len:
                    min_len = current_len
                    min_start = left

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[min_start:min_start + min_len]
        