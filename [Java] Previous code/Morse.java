

public class Morse {
	public static int uniqueMorseRepresentations(String[] words) {
		if (words.length == 1)
			return 1;
		String[] morseList = { ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
				"--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.." };
		String[] rst = new String[words.length];
		int[] cntEqual = { 0, 0 };
		for (int i = 0; i < words.length; i++) {
			rst[i] = "";
			for (int j = 0; j < words[i].length(); j++) {
				rst[i] += ("" + morseList[(int) (words[i].charAt(j) - 'a')]);
			}
		}
		for (int i = 0; i < rst.length - 1; i++) {
			for (int j = i + 1; j < rst.length; j++) {
				if (rst[i].equals(rst[j]))
					cntEqual[0]++;
			}
			if (cntEqual[0] != 0) {
				cntEqual[0] = 0;
				cntEqual[1]++;
			}
		}
		return cntEqual[1];
	}

	public static void main(String[] args) {
		String[] rst = { "a" };

		System.out.println(uniqueMorseRepresentations(rst));
	}
}
