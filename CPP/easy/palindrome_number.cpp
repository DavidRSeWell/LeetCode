#include <iostream>

using namespace std;

class Solution {
    public:
        bool isPalindrome(int x) {

            cout << x << "\n";
            if (x < 0 || (x % 10 == 0) ){
                return false;
            }

            int reverse = 0;
            while (reverse < x){
                reverse = reverse*10 + x % 10;
                x /= 10;
            }

            cout << reverse << "\n";

            if (x == reverse || x == (reverse / 10)){
                return true;
            }

            return false;

        }
};


int main(){

    int test1 = 121;
    Solution s;
    bool is_pal = s.isPalindrome(test1);

    cout << "You a pal?" << is_pal << "\n";
    return 0;

}