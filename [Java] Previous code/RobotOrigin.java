

public class RobotOrigin {
	public boolean judgeCircle(String moves) {
		int[] point = { 0, 0 }; // x축, y축
		char moveBtn; // String charAt(index) 집어넣을 공간
		for (int i = 0; i < moves.length(); i++) {
			moveBtn = moves.charAt(i);
			switch (moveBtn) {
			case 'U': //
				point[1]++;
				break;
			case 'D':
				point[1]--;
				break;
			case 'L':
				point[0]--;
				break;
			case 'R':
				point[0]++;
				break;
			default :
				return false;
			}
		}
		if(point[0]==0&&point[1]==0)
			return true;
		return false;
	}
}
