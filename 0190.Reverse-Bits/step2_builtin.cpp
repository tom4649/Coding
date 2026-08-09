#include <cstdint>

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        return __builtin_bitreverse32(n);
    }
};
