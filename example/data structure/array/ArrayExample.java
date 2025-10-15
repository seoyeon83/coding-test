public class ArrayExample {
    public static void main(String[] args) {
        int[] numbers = new int[5];

        numbers[0] = 10;
        numbers[1] = 20;

        String[] fruits = {"Apple", "Banana", "Orange"};

        System.out.println("첫 번째 숫자: " + numbers[0]);
        System.out.println("두 번째 과일: " + fruits[1]);

        System.out.println();

        System.out.println("모든 과일: ");
        for (String f:fruits) {
            System.out.print(f + " ");
        }
        System.out.println("\n");
        
        System.out.println("모든 숫자: ");
        for (int n:numbers) {
            System.out.print(n + " ");
        }
        System.out.println("\n");
    }
}