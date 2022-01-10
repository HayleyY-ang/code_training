class Solution:
    def minValueofh(self, n, m, line, array):
        from collections import defaultdict
        dic = defaultdict(list)
        for a, b in array:
            dic[a].append(b)
            dic[b].append(a)
        for i in range(m, 0, -1):
            if not self.check(i, line, dic):
                continue
            else:
                return self.check(i, line, dic)
        return -1
    def check(self, i, line, dic):
        leaf = []
        father = {}
        k = 1
        for f, s in dic.items():
            if len(s) == 1:
                leaf.append(f)
            else:
                father[f] = len(s)
                flag = max(line) + 1
            while flag > 0:
                for f, s in dic.items():
                    if line[f-1] >= flag:
                        if f in leaf:
                            k += 1
                        else:
                            k += father[f]
                    else:
                        continue
                if i == k:
                    return flag
                flag -= 1
            return 0
if __name__ == "__main__":
     
    [n, m] = list(map(int, input().split()))
    line = list(map(int, input().split()))
    array = []
    for _ in range(n-1):
        lists = list(map(int, input().split()))
        array.append(lists)
    s = Solution()
    ans = s.minValueofh(n, m, line, array)
    print(ans)