import domain.EmailNotification;
import domain.Notification;
import domain.SlackNotification;
import domain.SmsNotification;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import service.NotificationDispatcher;
import service.NotificationService;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        List<Notification> notifications = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String name = sc.next();

            switch (name) {
                case "Email" -> notifications.add(new EmailNotification(100, "EMAIL"));
                case "Slack" -> notifications.add(new SlackNotification(50, "SLACK"));
                case "Sms" -> notifications.add(new SmsNotification(10, "SMS"));
            }
        }

        NotificationDispatcher dispatcher = new NotificationDispatcher(notifications);

        int M = sc.nextInt(); // 메시지 개수
        List<String> messages = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            messages.add(sc.next());
        }

        // === 동시에 여러 submit 요청 보내기 ===
        ExecutorService producerPool = Executors.newFixedThreadPool(5); // 5개의 생산자 스레드
        for (String msg : messages) {
            producerPool.submit(() -> dispatcher.submitMessage(msg));
        }

        while (true) {
            producerPool.submit(() -> dispatcher.submitMessage(sc.next()));
        }
    }
}
