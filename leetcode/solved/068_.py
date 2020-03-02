# coding:utf-8

__author__ = "sn"

"""
68Text Justification
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

"""

"""
思路：
1。将所有列表元素放到1个字符串中处理

2.笨办法，模拟：
一层循环，读入单词
	如果总长度大于maxWidth，结果新增一行
		单词个数，总长度决定每个单词间空格数量，此处需要逻辑处理，比较繁琐
		总长度清空，继续读入
	否则继续

最后一行处理


"""


import cProfile, pstats, io

class Solution:
    def fullJustify(self, words, maxWidth):
        row = []
        row_char_length = row_length = 0
        result = []

        for word in words:
            word_length = len(word)
            if row_char_length + row_length + word_length > maxWidth:
                if row_length == 1:
                    result.append("".join(row).ljust(maxWidth))
                else:
                    i,j = (maxWidth - row_char_length)//(row_length-1), (maxWidth- row_char_length)%(row_length-1)
                    res = ""
                    for t in range(row_length):
                        if j >0:
                            res = res + row[t] + " "*(i+1)
                            j-=1
                        else:
                            res = res + row[t] + " "*i
                    result.append(res[:-i])
                row, row_length, row_char_length = [word], 1, word_length
            else:
                row.append(word)
                row_length += 1
                row_char_length += word_length
        if row_length >0:
            res = " ".join(row).ljust(maxWidth, " ")
            result.append(res)
        return result



pr = cProfile.Profile()
pr.enable()
res = Solution()
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

result = res.fullJustify(words, maxWidth)
pr.disable()
s = io.StringIO()
sortby = "cumulative"
ps = pstats.Stats(pr,stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

for i in result:
    print("'",i,"'",len(i))
    