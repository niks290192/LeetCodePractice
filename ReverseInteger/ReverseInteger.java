
class ReverseInteger {
    public static void main(String[] args) {
        System.out.println(reverse(1234));
    }


    /*
    Complexity Analysis:-
    Time Complexity: log10(x). There are roughly log10(x) digits in x.

    Space Complexity: O(1)

    */

    public static int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE/10 || (rev == Integer.MAX_VALUE / 10 && pop > 7)) {
                return 0;
            }

            if (rev < Integer.MIN_VALUE/10 || (rev == Integer.MIN_VALUE / 10 && pop < -8)) {
                return 0;
            }
            rev = rev * 10 + pop;
        }
        return rev;
    }
}