class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if n%2==1:
            return False
        st=[]
        for ch in list(s):
            # opening brackets
            if ch == '{' or ch== '[' or ch== '(':
                st.append(ch)
            #closing brackets
            else:
                if len(st)==0:   #agar opening bracket se nhi s start hui yaani append nhi hoga and st is emopty therefore return flase , instantly
                    return False
                top = st.pop()
                if ch==']' and top!='[' :
                    return False
                elif ch==')' and top!='(' :
                    return False
                elif ch=='}' and top!='{' :
                    return False
        return len(st)==0

        
        

        