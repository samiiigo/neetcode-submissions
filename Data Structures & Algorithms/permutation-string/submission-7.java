class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n1 = s1.length();
        int n2 = s2.length();
        if (n1 > n2) {return false;}

        char[] s1char = s1.toCharArray();
        Arrays.sort(s1char);
        for (int i = 0; i <= n2-n1; i++) {
            String sub = s2.substring(i, i+n1);
            char[] s2sub = sub.toCharArray();
            Arrays.sort(s2sub);
            if (Arrays.equals(s1char, s2sub)) {
                return true;
            } 
        }
        return false;
    }
}
