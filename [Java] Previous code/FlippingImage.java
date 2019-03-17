
public class FlippingImage {
/*	
	static {
		int [][][] A = new int[3][7][8];
		System.out.println(A.length+""+A[0].length+""+A[1][1].length);
	}
*/	public int[][] flipAndInvertImage(int[][] A) {
		int[][] revA = new int[A.length][A[0].length];
		int[][] flipA = new int[A.length][A[0].length];
		for(int i = 0; i<A.length;i++) {
			for(int j=0; j<A[0].length;j++) {
				revA[i][A[0].length-1-j]=A[i][j];
			}
		}
		for(int i = 0; i<A.length;i++) {
			for(int j=0; j<A[0].length;j++) {
				if(revA[i][j]==1)
					flipA[i][j] =0;
				else
					flipA[i][j] =1;
			}
		}
		
		return flipA;
	}

	public static void main(String[] args) {

	}
}
