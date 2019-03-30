class Solution {
    public boolean repeatedSubstringPattern(String s) {
        // 매개변수 s의 길이
        int sLen = s.length();

        // 1차 반복 : n개의 문자 비교
        for (int i = 0; i < (sLen / 2); i++) {
            // sLen을 i로 나눴을 때 몫이 0 이 아니면 반복되지 않음
            if (sLen % (i + 1) != 0) {
                // continue해서 반복을 건너뜀
                continue;
            }

            // 0~i 까지의 문자열과 i+1 씩 증가하는 j~j+i 의 문자열을 비교
            int cnt = 1;
            for (int j = i + 1; j < sLen - i; j += (i + 1)) {
                if (!s.substring(0, i + 1).equals(s.substring(j, j + i + 1))) {
                    // 같지 않으면 반복문을 빠져나감
                    break;
                } else {
                    // 같으면 cnt 변수를 증가시킴
                    cnt++;
                }
            }
            // cnt 가 전체 길이를 i+1로 나눈 것과 같다면
            // true를 리턴해준다.
            if (cnt == sLen / (i + 1)) {
                return true;
            }
        }
        // 반복문을 빠져나오게 되면 반복되지않은 문자이므로
        // return false를 해준다.
        return false;
    }

    public static void main(String[] args) {

        String input = "abcabc";
        Solution s = new Solution();

        System.out.println(s.repeatedSubstringPattern(input));
    }
}