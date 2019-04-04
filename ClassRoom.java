import java.util.ArrayList;
import java.util.Hashtable;
import java.util.Random;
import java.util.Scanner;

class ClassRoom {
    // 자리 정보
    static Hashtable<Integer, Student> seatInfo;
    ArrayList<Student> studentsInfo = new ArrayList<Student>();

    // 좌석 수
    int seatAmount = 30;
    private int cnt = 0;

    ClassRoom() {
        // key: 좌석번호, value : 학생정보
        this.seatInfo = new Hashtable<Integer, Student>();
    }

    // 총 자리수 설정
    public void makeSeat(int seatAmount) {
        this.seatAmount = seatAmount;
    }

    // 학생생성
    public void createStudent(int stId, String stName, String stPhoneNum) {
        // Student st = new Student(2012335079, "이윤환", "010-1234-5678");
        Student st = new Student(stId, stName, stPhoneNum);
        this.studentsInfo.add(st);
    }

    // 학번으로 학생검색
    public void searchStudent(int stId) {

        // 리스트를 하나하나 돌려본다.
        for (Student st : studentsInfo) {
            if (st.stId == stId) {
                System.out.println("--------학생 정보---------");
                System.out.println("학번 : " + st.stId);
                System.out.println("이름 : " + st.name);
                System.out.println("핸드폰 번호 : " + st.phoneNum);
                System.out.println("----------------------");
                return;
            }
        }
        System.out.println(stId + " 번의 학생이 존재하지 않음");
    }

    // 랜덤 자리 배치
    public void setRandSeat() {
        // 기존에 있던 좌석정보 초기화
        this.seatInfo = new Hashtable<Integer, Student>();

        // 1차원 배열의 좌석 번호
        ArrayList<Integer> seatNo = new ArrayList<Integer>();

        Random rd = new Random();
        int size = this.seatAmount;

        // 원본 학생 정보를 건들지 않기 위해 새로 복사하여 사용
        ArrayList<Student> studentsInfo = (ArrayList<Student>) this.studentsInfo.clone();

        // 0~총좌석-1 만큼 정수 배열을 만듬 [0,1,2,3,...,n]
        for (int i = 0; i < size; i++) {
            seatNo.add(i);
        }

        // 남은 잔여 좌석 수가 0이 될때까지 반복
        while (size != 0) {
            // 0부터 size-1 까지 랜덤하게 뽑는다.
            int index = rd.nextInt(size);
            try {
                // 좌석 정보에 index 좌석에, 배열의 첫번째 학생 정보를 집어넣음
                this.seatInfo.put(index, studentsInfo.get(0));
                // 첫 번째 학생 정보를 대입하였으므로 제거
                studentsInfo.remove(0);
            } catch (Exception e) {
                System.out.println("학생 수가 부족합니다.");
                break;
            }
            // index 째 좌석은 사용하였으므로 제거
            seatNo.remove(index);
            // 남은 좌석 사이즈 감소
            size--;
        }
        // 잔여좌석을 다썼는데 학생이 남아있으면 알림
        if (studentsInfo.size() != 0) {
            System.out.println("좌석이 부족합니다.");
        }
    }

    // 현재 좌석 정보 출력
    public void printSeatArray() {

        System.out.println("------ 좌석 정보 ------");

        // JAVA 람다 표현식임 . seatInfo 에 있는 Item 들을 하나하나 출력
        this.seatInfo.forEach((key, val) -> {
            // 한줄에 3명씩 출력하도록 함
            if (cnt % 3 == 0) {
                System.out.print("\n| " + val.name + "| ");
                cnt++;
            } else {
                System.out.print("| " + val.name + "| ");
                cnt++;
            }
        });
        System.out.println("------ 총 인원 : " + cnt + "명------");
        cnt = 0;

    }

    public static void main(String[] args) {

        int menu = 0;
        Scanner sc = new Scanner(System.in);

        ClassRoom cr = new ClassRoom();

        // 1번 총 학생 출력
        // 2번 학생 생성

        while (menu != 9) {

            System.out.println("메뉴를 선택해주세요");
            menu = sc.nextInt();
            switch (menu) {

            // 전체 학생 정보 출력
            case 1:
                System.out.println(cr.studentsInfo);
                break;

            // 학생 등록
            case 2:
                System.out.println("학번 입력 : ");
                int stNum = sc.nextInt();
                System.out.println("이름 입력 : ");
                String stName = (String) sc.next();
                System.out.println("핸드폰 번호 : ");
                String stPhone = (String) sc.next();
                cr.createStudent(stNum, stName, stPhone);
                // cr.createStudent(2012335079, "이윤환", "010-9916-3363");
                System.out.println("학생 등록 완료..");
                break;

            // 자리 섞기
            case 3:
                cr.setRandSeat();
                break;
            // 전체 좌석 배열 출력
            case 4:
                cr.printSeatArray();
                break;
            // 학번으로 학생 검색
            case 5:
                System.out.println("학생 정보 검색 입니다. 학번을 입력해주세요..");
                cr.searchStudent(sc.nextInt());
                break;
            // 프로그램 종료
            case 9:
                System.out.println("종료 ...");
                return;
            default:
                System.out.println("번호를 제대로 입력해주세요...");
                break;
            }

        }
    }
}

class Student {
    int stId;
    String name;
    String phoneNum;

    Student() {
    }

    Student(int stId, String name, String phoneNum) {
        this.stId = stId;
        this.name = name;
        this.phoneNum = phoneNum;
    }

    public void setId(int stId) {
        this.stId = stId;
    }

    public int getId() {
        return stId;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setPhoneNum(String phoneNum) {
        this.phoneNum = phoneNum;
    }

    public String getPhoneNum() {
        return phoneNum;
    }

}