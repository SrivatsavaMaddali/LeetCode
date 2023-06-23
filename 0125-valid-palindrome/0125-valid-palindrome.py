class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        print(s)
        st=[]
        for x in s:
            if x.isalnum():
                st.append(x)
        rev=st[::-1]
        print(st)
        print(rev)
        if st==rev:
            return True
        else:
            return False
                