import java.util.ArrayList;
import java.util.List;

public class ContiguousListExample {
    public static void main(String[] args) {
        // String 타입을 저장하는 ArrayList 생성
        List<String> names = new ArrayList<>();

        // 요소 추가 (add)
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");

        // 요소 접근 (get)
        System.out.println("인덱스 1의 이름: " + names.get(1));

        // 요소 변경 (set)
        names.set(0, "Anna");

        // 요소 삭제 (remove)
        names.remove(2); // 인덱스 2의 "Charlie" 삭제

        // 리스트 순회
        System.out.print("현재 이름 목록: ");
        for (String name : names) {
            System.out.print(name + " ");
        }
        System.out.println();
        
        // 현재 크기 확인 (size)
        System.out.println("리스트 크기: " + names.size());
    }
}