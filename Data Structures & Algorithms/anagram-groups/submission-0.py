class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringMap = {}
        for string in strs:
            freq = [0] * 26
            for char in string:
                index = ord(char) - 97
                freq[index] += 1
            similar = stringMap.get(str(freq))
            if similar is None:
                stringMap[str(freq)] = [string]
            else:
                stringMap[str(freq)].append(string)
        
        output = []
        for key in stringMap:
            output.append(stringMap[key])
        
        return output