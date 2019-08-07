class Solution(object):

    def longestSubstringWithoutDuplication(self, s: str) -> int:
        # 可抛弃字符串的索引尾值 - 字符串索引值，该索引值以及之前的字符都属于重复字符串中的一部分，不再在计算中涉及
        ignore_str_index_end = -1
        dic = {}        # 任意字符最后出现在索引的位置 - {字符: 字符索引值}
        max_length = 0  # 最长字符串长度

        for i, c in enumerate(s):
            # 如果字典中已经存在字符c，则字符c重复
            # 如果字符索引值大于ignore_str_index_end，则字符c在需处理的范围内（补充说明请参考备注一）
            if c in dic and dic[c] > ignore_str_index_end:
                # 先更新可抛弃字符串的索引尾值为字符c上一次的索引值
                ignore_str_index_end = dic[c]
                # 再更新字符c的索引值
                dic[c] = i
            # 否则，
            else:
                # 更新字符最近的索引位置
                dic[c] = i
                # 更新最大长度
                max_length = max(i - ignore_str_index_end, max_length)

        return max_length
