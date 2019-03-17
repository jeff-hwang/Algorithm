
public class SumArray {
	int[] numResult = new int[2];

	public int[] twoSum(int[] nums, int target) {
		int i = 0;
		int j = 0;

		for (i = 0; i < nums.length - 1; i++)
			for (j = i + 1; j < nums.length; j++)
				if (nums[i] + nums[j] == target) {
					numResult[0] = i;
					numResult[1] = j;
					return numResult;
				}
		return numResult;
	}

	public static void main(String[] args) {
		int[] nums = { 2, 7, 11, 13 };
		SumArray s2 = new SumArray();
		s2.twoSum(nums, 15);
		for (int i = 0; i < s2.numResult.length; i++)
			System.out.println(s2.numResult[i]);
	}
}
