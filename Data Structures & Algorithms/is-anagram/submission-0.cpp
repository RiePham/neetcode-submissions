class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        int idx_s = 0;
        int idx_t = 0;
        while (idx_s < s.size() && idx_t < t.size()) {
            if (s[idx_s] != t[idx_t]) {
                return false;
            }

            idx_s++;
            idx_t++;
        }

        return (idx_s == idx_t);
    }
};
