class Solution {
public:
    int getSum(int n) {
        int res = n;
        (n>0) && (res += getSum(n-1));//利用短路运算终止递归
        return res;
    }
};