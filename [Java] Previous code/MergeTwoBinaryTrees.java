
class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode(int x) {
		val = x;
	}
}

public class MergeTwoBinaryTrees {
	public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
		if(t1==null)
			return t2;
		if(t2==null)
			return t1;
		TreeNode rstTree = new TreeNode(t1.val+t2.val);
		rstTree.left = mergeTrees(t1.left, t2.left);
		rstTree.right = mergeTrees(t1.right, t2.right);
		return rstTree;
	}
}
