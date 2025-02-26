class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        romnums = {'I': 1,  'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(0, len(s)):
            if s[i] in "IXC":
                if i + 1 < len(s) and s[i] + s[i + 1] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                    res -= romnums[s[i]]
                else:
                    res += romnums[s[i]]
            else:
                res += romnums[s[i]]
        return res