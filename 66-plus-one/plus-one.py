class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        string = "".join(map(str,digits))
        
        sum = int(string) + 1

        string = str(sum)

        return list((map(int,string)))