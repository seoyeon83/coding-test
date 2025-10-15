import java.util.ArrayDeque;
import java.util.Deque;

public class StackExample {
    public static void main(String[] args) {
        Deque<Integer> stack = new ArrayDeque<>();

        // 요소 추가 (push)
        stack.push(10);
        stack.push(20);
        stack.push(30);

        System.out.println("현재 스택: " + stack);

        // 최상단 요소 확인 (peek)
        System.out.println("Peek: " + stack.peek()); // 30

        // 요소 꺼내기 (pop)
        int popped = stack.pop();
        System.out.println("Pop: " + popped); // 30
        System.out.println("Pop 이후 스택: " + stack);

        // 스택이 비었는지 확인 (isEmpty)
        System.out.println("스택이 비었는가? " + stack.isEmpty());
    }
}