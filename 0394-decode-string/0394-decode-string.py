class Solution:
    def decodeString(self, s: str) -> str:
        def back(index):
            curr_str, num = "", 0
            
            while index < len(s):
                char = s[index]
                
                if char.isdigit():
                    num = num * 10 + int(char)
                elif char == '[':
                    decoded_substr, index = back(index + 1)
                    curr_str += num * decoded_substr
                    num = 0
                elif char == ']':
                    return curr_str, index
                else:
                    curr_str += char
                
                index += 1
            
            return curr_str, index
        
        return back(0)[0]
