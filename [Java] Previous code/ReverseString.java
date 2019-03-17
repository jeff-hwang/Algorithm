
public class ReverseString {
	public static String reverseString(String s) {
		char[] ch = s.toCharArray();
		int leng = s.length();
		char[] rst = new char[leng];
		int cnt = 0;
		for (int i = leng - 1; i >= 0; i--) {
			rst[cnt] = ch[i];
			cnt++;
		}
		return new String(rst);
	}

	public static void main(String[] args) {
		System.out.println(reverseString("hello"));
	}
}
