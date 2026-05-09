class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""

        t_count, window = {}, {}

        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1

        for ch in t:
            if ch not in window:
                window[ch] = 0
        
        have, need = 0, len(t_count)

        min_len = float('inf')
        current_len = 0
        res = [-1, -1]
        left = 0

        for right in range(len(s)):
            if s[right] in window:
                window[s[right]] += 1
                if window[s[right]] == t_count[s[right]]:
                    have += 1
            
            while have == need:
                current_len = right - left + 1
                if current_len < min_len:
                    res = [left, right]
                    min_len = current_len
                if s[left] in window:
                    window[s[left]] -= 1
                    if window[s[left]] < t_count[s[left]]:
                        have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res != float('inf') else ""