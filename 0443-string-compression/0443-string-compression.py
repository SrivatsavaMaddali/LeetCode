class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        cnt = 1
        for i in range(len(chars)):
            if i < len(chars)-1 and chars[i + 1] == chars[i]:
                cnt += 1
            else:
                result.append(chars[i])
                if cnt > 1:
                    result.append(str(cnt))
                cnt = 1
        s="".join(result)
        result=[*s]
        chars[:len(result)] = result
        return len(result)
