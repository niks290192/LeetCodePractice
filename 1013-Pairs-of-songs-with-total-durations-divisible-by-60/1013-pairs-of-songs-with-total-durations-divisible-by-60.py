# 1013. Pairs of Songs With Total Durations Divisible by 60
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution:
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        mod_times = {}
        for i in time:
            mod_times[i%60] = 1 if i%60 not in mod_times.keys() else mod_times[i%60]+1
        cnt = 0
        
        for key,value in mod_times.items():
            print(key,value)
            if key == 0 or key == 30:
                cnt += int((mod_times[key]*(mod_times[key]-1))/2)
            elif key < 30 and (60-key) in mod_times.keys():
                cnt += mod_times[key] * mod_times[60-key]
             
        return cnt

