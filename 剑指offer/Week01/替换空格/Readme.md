**题目**  
实现一个函数，把字符串中的每个空格替换"%20"。

>假定输入字符串的长度最大是1000。
注意输出字符串的长度可能大于1000。

**算法**   
动态将数组扩大,降低空间复杂度
1. 遍历一次原数组，将数组扩充成最终长度, lenNew = lenOld + space * 2  

2. 使用两个指针，i指向原字符串的末尾，指针j指向扩充后末尾:
    -  两个指针分别从后往前遍历，如果str[i] == ' '，则指针j的位置上依次填充'0'， '2'， '%'，倒看是"%20"，同时指针向前移动３格；如果str[i] != ' '，指针j的位置上填充该字符即可，同时指针向前移动１格

3.  当两个指针位置重合时，所有空格替换完毕

**时间复杂度**  
所有字符只移动了一次，时间复杂度是O(n)