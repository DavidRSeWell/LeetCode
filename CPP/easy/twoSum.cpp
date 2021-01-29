#include <iostream>
#include <vector>
#include <unordered_map>

using std::vector;
using std::unordered_map;

vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> h;

        int n = nums.size();

        vector<int> ret;

        for(int i = 0; i != n; ++i){

            int val = nums[i];
            int diff = target - val;
            auto search = h.find(diff);
            if (search != h.end()){
                ret.push_back(h[diff]);
                ret.push_back(i);
                return ret;
            }else{
                h.insert({val,i});
            }
        }

        return ret;

    }

int main(){
    vector<int> test1 = {2,7,11,15};
    vector<int> res1 = {0,1};

    assert(twoSum(test1,9) == res1);

    std::cout << "Passed test \n";

}