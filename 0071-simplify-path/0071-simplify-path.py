# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         lis=[]
#         result="/"
#         lis=path.split("/")
#         cnt=0
#         lis.pop(0)
#         lis1=[]
#         for x in lis:
#             if x!="":
#                 lis1.append(x)
#         lis1.append("")
#         print(lis1)
#         lis=lis1
#         i=0
#         while lis[i]!="":
#             if i<len(lis) and lis[i]==".":
#                 lis.pop(i)
#                 i=i-1
#             elif i<len(lis) and lis[i]=="..":
#                 lis.pop(i)
#                 i=i-1
#                 if i>0:
#                     lis.pop(i)
#                     i=i-1
#                 elif i==0:
#                     lis.pop(i)
#             print(lis)
#             i+=1
#         lis.pop(len(lis)-1)
#         print(lis)
#         for x in lis:
#             result+=x+"/"
#         final=result
#         if len(final)==1:
#             return final
#         else:
#             return final[0:len(final)-1]
            
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for token in path.split('/'):
            if token == '..':
                if stack:
                    stack.pop()
            elif token and token != '.':
                stack.append(token)
        return '/' + '/'.join(stack)
