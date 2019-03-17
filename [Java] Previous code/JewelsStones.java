
public class JewelsStones {
	public int numJewelsInStones(String J, String S) {
        int rstNum=0;
        char[] jArray = new char[J.length()];
        char[] sArray = new char[S.length()];
        
        for(int i=0; i<J.length(); i++)
            jArray[i] = J.charAt(i);
        for(int j=0; j<S.length(); j++)
            sArray[j] = S.charAt(j);
        
        for(int i = 0; i<J.length(); i++)
            for(int j = 0; j<S.length(); j++)
            	if((""+jArray[i]).equals(""+sArray[j]))
            		rstNum++;
        return rstNum;
    }
}
