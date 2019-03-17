
public class FairCandySwap {
    public int[] fairCandySwap(int[] A, int[] B) {
    	int rstA =0 , rstB = 0;
    	for(int x : A) {
    		rstA+=x;
    	}
    	for(int x : B) {
    		rstB+=x;
    	}
    	int lenA = A.length;
    	int lenB = B.length;
    	for(int i = 0; i < lenA; i++) {
    		for(int j = 0; j<lenB; j++) {
    			if(B[j]==A[i]+((rstB-rstA)/2)) {
    				return new int[] {A[i],B[j]};
    			}
    		}
    	}
    	throw null;
    }
}
