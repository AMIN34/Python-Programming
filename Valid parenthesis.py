class Solution:
    def bracket_matcher(lpar, rpar):
        br_map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        return (lpar in br_map and br_map[lpar] == rpar)

    def isValid(self, s: str) -> bool:
        i = 0
        last_idx = -1
        # null string or single char counts as invalid
        if s is None or len(s) == 1:
            return False
        
        while i < len(s) and len(s) > 0:
            if last_idx == -1:
                last_idx = i
                i += 1
                continue
            if Solution.bracket_matcher(s[last_idx], s[i]):
                # Modify the original string accordingly
                s = s[:last_idx] + s[i+1:]
                last_idx -= 1
                i = last_idx
            else:
                last_idx = i
            i += 1
        return last_idx == -1