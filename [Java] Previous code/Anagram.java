import java.util.Arrays;

public class Anagram {
	public boolean isAnagram(String s, String t) {
		
		if(s.length()!=t.length())
			return false;
		
		char[] sA = s.toCharArray();
		char[] tA = t.toCharArray();
		
		Arrays.sort(sA);
		Arrays.sort(tA);
		return Arrays.equals(sA, tA)?true:false;
	}
}
