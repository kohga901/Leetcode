using namespace std;
#include <vector>
#include <algorithm>
#include <iostream>
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        nums1.insert(nums1.end(), nums2.begin(), nums2.end());
        std::sort(nums1.begin(), nums1.end());
        int length = nums1.size();
        int index;
        if (length % 2 == 0) {
            int index_2 = length / 2;
            int index_1 = index_2 - 1;
            return (nums1.at(index_1) + nums1.at(index_2)) / 2.0;
        }
        index = length / 2;
        return nums1.at(index);
    }
};

int main() {
    Solution sol = Solution();
    vector<int> nums1 = {1, 2};
    vector<int> nums2 = {3, 4};
    cout << sol.findMedianSortedArrays(nums1, nums2) << endl;
}