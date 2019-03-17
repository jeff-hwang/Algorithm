
public class ToLowerCase {
	public static String toLowerCase(String str) {
		char[] strArray = new char[str.length()];
		for (int i = 0; i < str.length(); i++)
			if (str.charAt(i) >= 'A' && str.charAt(i) <= 'Z')
				strArray[i] = (char) (str.charAt(i) + 32);
			else
				strArray[i] = (char)str.charAt(i);

		String rst = "";
		for (int i = 0; i < str.length(); i++)
			rst += strArray[i];
		System.out.println(rst);
		return rst;
	}

	public static void main(String[] args) {
		toLowerCase("hellO");

	}
}
