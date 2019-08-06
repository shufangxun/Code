class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # p 和 s 有空
        if len(s) == 0 and len(p) == 0:
            return True
        elif len(s) != 0 and len(p) == 0:
            return False
        elif len(s) == 0 and len(p) != 0:
            if len(p) >= 2 and p[1] == ' * ' :
                return self.isMatch(s, p[2 : ])  # 向后继续匹配
            else:
                return False
                
        ## s 和 p 都非空
        else:
            if len(p) >= 2 and p[1] == '*':
                # 匹配0个字符
                if s[0] != p[0] and p[0] != '.':
                    return self.isMatch(s, p[2 : ])
                else:
                    # 三种匹配
                    # isMatch(s, p[2 : ])  s = 'aac' p = 'b*b*b*ac'
                    # isMatch(s[1 : ], p)  s = 'aac' p = 'b*c'
                    # isMatch(s[1 : ], p[2 : ]) s = 'aac' p = 'b*ac'
                    return self.isMatch(s[1 : ], p) or self.isMatch(s[1 : ], p[2 : ]) or self.isMatch(s, p[2 : ])

            else: # 第二个不是'*'
                if s[0] == p[0] or p[0] == '.':
                    return self.isMatch(s[1 : ], p[1 : ])
                else:
                    return False