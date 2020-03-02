# coding:utf-8
#Longest Substring Without Repeating Characters
"""
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
思路：
接收字符

确定start，
用dict保存已存在过的字符
如果出现已存在过的字符（该字符序列号应在start之后），求当前长度并与历史最长相比，留下大值
如果在上一条件下求长度并确定最长值，有一个问题是最后一个不重复的串无法识别
解决办法：
将长度求值部分放到else中,
同样有部分情况下不会求长度值，但在前一条件下当前子串长度不可能大于历史长度
"""



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict_used = {}
        start = 0
        maxlength = 0
        for i in range(len(s)):
            if s[i] in dict_used and dict_used[s[i]] >= start:
                start = dict_used[s[i]] + 1
            else:
                maxlength = max(maxlength, i - start + 1)

            dict_used[s[i]] = i
        return maxlength


str = "acdcedacd"
a = Solution()
print(a.lengthOfLongestSubstring(str))


		
		
		