import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        Map<String, PaymentMethod> methods = new HashMap<>();

        for (int i = 0; i < N; i++) {
            String type = sc.next();
            Integer balance = sc.nextInt();

            if (type.equals("Card")) {
                methods.put("Card", new CardPayment(balance));
            } else if (type.equals("KakaoPay")) {
                methods.put("KakaoPay", new KakaoPayPayment(balance));
            } else if (type.equals("Point")) {
                methods.put("Point", new PointPayment(balance));
            }
        }

        int M = sc.nextInt();
        Map<String, Order> orders = new HashMap<>();

        for (int i = 0; i < M; i ++) {
            String orderId = sc.next();
            int amount = sc.nextInt();
            String methodName = sc.next();

            PaymentMethod paymentMethod = methods.get(methodName);

            Order order = new Order(orderId, amount, paymentMethod);

            orders.put(orderId, order);
        }

        for (Entry<String, Order> entry : orders.entrySet()) {
            Order order = entry.getValue();

            boolean success = order.processOrder();

            if (success) {
                System.out.println(order.getOrderId() + ": 결제 성공 (" + order.getPaymentMethod().getName() + ")");
            } else {
                System.out.println(order.getOrderId() + ": 결제 실패 (" + order.getPaymentMethod().getName() + ")");
            }
        }

    }
}
