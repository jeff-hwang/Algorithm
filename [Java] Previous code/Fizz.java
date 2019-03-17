import java.util.ArrayList;
import java.util.List;

public class Fizz {
	public static List<String> fizzBuzz(int n) {
		ArrayList<String> rst = new ArrayList<String>();

		for (int i = 1; i <= n; i++) {
			String result = "";
			if (i % 3 == 0 && i % 5 == 0) { // 15�� ��������
				result = "FizzBuzz";
			} else if (i % 3 == 0) { // 3���� ��������
				result = "Fizz";
			} else if (i % 5 == 0) { // 5�� ��������
				result = "Buzz";
			} else {
				result = "" + i;
			}
			System.out.println(result);
			rst.add(result);
		}
		
		
		return rst;

	}

	public static void main(String[] args) {
		fizzBuzz(3);
	}
}
