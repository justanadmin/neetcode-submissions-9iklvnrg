class Solution:
    def isValid(self, s: str) -> bool:
    # stack will store opening brackets
        stack = []
    
    # mapping of closing → opening brackets
        mapping = {')': '(', '}': '{', ']': '['}

    # loop through each character in string
        for each in s:
        
        # if it's an opening bracket → push to stack
            if each in '({[':
                stack.append(each)   # store it for future matching
                print("Push:", stack)

        # if it's a closing bracket → validate
            elif each in ')}]':
            
            # if stack is empty → nothing to match → invalid
                if not stack:
                    return False
            
            # check top of stack (last element)
            # stack[-1] = last pushed opening bracket
            # mapping[each] = expected opening bracket
                if stack[-1] == mapping[each]:
                    stack.pop()   # match found → remove from stack
                    print("Pop:", stack)
                else:
                    # mismatch → invalid
                    return False

    # after processing all characters
    # stack should be empty if all brackets matched
        return len(stack) == 0