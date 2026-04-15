class Solution {
public:
    int findMin(vector<int> &nums) {

        int start = 0;
        int end = nums.size() - 1;

        while(start < end) {
            int mid = start +(end - start)  / 2;
            if(nums[start] < nums[end]) return nums[start];
            if(nums[start] < nums[mid]) {
                start = mid;
            } else {
                end = mid;
            }
        }
        if(start == nums.size() - 1) return nums[start];
        return nums[start + 1];
      
    }
};
