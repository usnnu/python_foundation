# coding:utf-8

__author__ = "sn"

"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

"""

"""
思路：

1.float()...

2.去空格，正则匹配
首位是否为+或-
数字 
^[0-9]{1,}[\.]{0,1}[0-9]{0,}$
^\.[0-9]{1,}$
科学计数
^[0-9]{1,}[\.]{0,1}[0-9]*e[0-9]+$


3.类似正则
合法的数字表达式有以下几种：
全数字
.全数字
数字.数字
数字e[+-]数字

按.和e作分割点，分别进行判断是否合规
先将两端的空格去掉，首字符是否为+-
判断是否数字，如果不是直接返回False，
遇到'.'，判断.后是否有一列数字
遇到‘e'，然后判断'e'以后是否有’+‘，’-‘
判断后续的是否是数字。
使用 if else 即可
注意边界情况；


4.抽象化，搜索发现有一种东东叫有穷状态自动机DFA
结合本案例，字符串有9种状态
0无输入或只有空格
1输入了数字
3无数字，只有dot
4有数字有dot
5e或者E输入后的状态
6输入e之后输入sign的状态
7输入e之后输入数字的状态
8有效数字输入后，输入空格


"""


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        begin, last = 0, len(s)-1
        # 去首尾空格
        while begin <= last and s[begin] == " ":
            begin += 1
        while last >= begin and s[last] == " ":
            last -= 1

        # 首位是否为+或-
        if begin < last and (s[begin] == "+" or s[begin] == "-"):
            begin += 1

        num, dot, exp = False, False, False
        # 主体校验
        while begin <= last:
            if s[begin] >= "0" and s[begin] <= "9":
                num = True
            elif s[begin] == ".":
                if dot or exp:
                    return False
                dot = True
            elif s[begin] == "e" or s[begin] == "E":
                if exp or not num:
                    return False
                exp, num = True, False
            elif s[begin] == "+" or s[begin] == "-":
                if not(s[begin-1] == "e" or s[begin-1] == "E"):
                    return False
            else:
                return False
            begin += 1
        return num
	
	
	 # 有限状态自动机
    def isNumber(self, s):
        INVALID = 0;SPACE = 1;   SIGN = 2;        DIGIT = 3;        DOT = 4;        EXPONENT = 5;

        transitionTable = [[-1, 0, 3, 1, 2, -1],  
                           [-1, 8, -1, 1, 4, 5],  
                           [-1, -1, -1, 4, -1, -1],  
                           [-1, -1, -1, 1, 2, -1],  
                           [-1, 8, -1, 4, -1, 5],  
                           [-1, -1, 6, 7, -1, -1],  
                           [-1, -1, -1, 7, -1, -1],  
                           [-1, 8, -1, 7, -1, -1],  
                           [-1, 8, -1, -1, -1, -1]]  
        state = 0; i = 0
        while i < len(s):
            inputtype = INVALID
            if s[i] == ' ':
                inputtype = SPACE
            elif s[i] == '-' or s[i] == '+':
                inputtype = SIGN
            elif s[i] in '0123456789':
                inputtype = DIGIT
            elif s[i] == '.':
                inputtype = DOT
            elif s[i] == 'e' or s[i] == 'E':
                inputtype = EXPONENT

            state = transitionTable[state][inputtype]
            if state == -1:
                return False
            else:
                i += 1
        return state == 1 or state == 4 or state == 7 or state == 8
	
	
	# 换一种方式实现DFA
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # define a DFA
        state = [
            {"space": 0, "digit": 1, "sign": 3, ".": 2},
            {"digit": 1, "space": 8, "e": 5, ".": 4},
            {"digit": 4},
            {"digit": 1, ".": 2},
            {"digit": 4, "e": 5, "space": 8},
            {"digit": 7, "sign": 6},
            {"digit": 7},
            {"digit": 7, "space": 8},
            {"space": 8}]
        currentstate = 0
        for c in s:
            if c >= "0" and c <= "9":
                c = "digit"
            elif c == " ":
                c = "space"
            elif c in ["+", "-"]:
                c = "sign"
            elif c in ["e", "E"]:
                c = "e"
            # if c == ".":
             #   c ="."

            if c not in state[currentstate].keys():
                return False
            currentstate = state[currentstate][c]
            print("cc",currentstate)
        print(currentstate)
        if currentstate  in [1, 4, 7, 8]:
            return True
        else:
            return False
	




res = Solution()
str_num = "4.7e7"
result = res.isNumber(str_num)
if result:
    print("is number.")
else:
    print("is not number.")




