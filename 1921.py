class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(dist)):
            arrive = -(-dist[i]/speed[i])
            time.append(arrive)
        #time 包含了怪兽到达的时间
        time.sort()
        res = 0
        for i in range(len(dist)):
            if time[i] > i:
                res += 1
            else:
                break
        return res
