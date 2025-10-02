class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        int ans = numBottles;
        int emp = numBottles;
        while (emp >= numExchange) {
            emp -= numExchange;
            numExchange++;
            ans++;
            emp++;
        }
        return ans;
    }
};