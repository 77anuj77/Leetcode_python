class Solution(object):
    def mySqrt(self, x):

        if x == 0 or x == 1:
            return x

        low = 1
        high = x

        while low <= high:
            mid = (low + high) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                low = mid + 1

            else:
                high = mid - 1

        return high

        '''
Time complexity: O(log x)
Space complexity: O(1)

START

Take the number x

If x is 0 or 1
    return x

Set left = 1
Set right = x

While left is smaller than or equal to right

    Find the middle number
        mid = middle of left and right

    If mid × mid equals x
        return mid

    If mid × mid is smaller than x
        Move to the right side
        left = mid + 1

    Otherwise
        Move to the left side
        right = mid - 1

When the search ends
    return right

END

        '''
       