import java.util.ArrayList;
import java.util.List;

public class SelfDivide {
	public static List<Integer> selfDividingNumbers(int left, int right) {
		String num = "";
		ArrayList<Integer> rst = new ArrayList<Integer>();
		int cnt = 0;
		for (int i = left; i <= right; i++) {
			num = i + "";
			for (int j = 0; j < num.length(); j++) {
				if ((int) Integer.parseInt("" + num.toCharArray()[j]) != 0) {
					if (i % (int) Integer.parseInt("" + num.toCharArray()[j]) == 0)
						cnt++;
				}
			}
			if (num.length() == cnt) {
				rst.add(Integer.parseInt(num));
			}
			cnt=0;
		}
		return rst;
	}

	public static void main(String[] args) {
		selfDividingNumbers(1, 22);

	}
}
