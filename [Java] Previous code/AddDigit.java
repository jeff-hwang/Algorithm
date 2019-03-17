public class AddDigit{
    public int addDigits(int num) {
        int rst = 0;
        for(int i = 0; i < (num+"").length(); i++){
               rst += Integer.parseInt((num+"").charAt(i)+"");
        }
        int result = 0;
        for(int i = 0; i < (rst+"").length(); i++){
               result += Integer.parseInt((rst+"").charAt(i)+"");
        }
        return result;
    }
}
