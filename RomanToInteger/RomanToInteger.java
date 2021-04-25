import java.util.HashMap;
public class RomanToInteger {
    
    public static void main(String[] args) {
        System.out.println(romanToInt("MCMXCII"));
    }

    public static int romanToInt(String s) {
        HashMap<Character, Integer> d = new HashMap<>();
        d.put('I', 1);
        d.put('V', 5);
        d.put('X', 10);
        d.put('L', 50);
        d.put('C', 100);
        d.put('D', 500);
        d.put('M', 1000);
        
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i > 0 && d.get(s.charAt(i)) > d.get(s.charAt(i - 1))) {
                ans -= 2 * d.get(s.charAt(i - 1));
            }
            ans += d.get(s.charAt(i));
        }

        return ans;
    }
}