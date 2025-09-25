package service;

import domain.Notification;
import domain.NotificationResult;
import java.util.List;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.LinkedBlockingQueue;

public class NotificationDispatcher {
    private final List<Notification> notifications;
    private final BlockingQueue<String> queue = new LinkedBlockingQueue<>();
    private final ExecutorService executor;
    private boolean running = true;

    public NotificationDispatcher(List<Notification> notifications) {
        this.notifications = notifications;
        executor = Executors.newSingleThreadExecutor();
        startWorker();
    }

    private void startWorker() {
        executor.submit(() -> {
            try {
                while (running) {
                    String message = queue.take(); // 메시지 없으면 블로킹
                    for (Notification n : notifications) {
                        NotificationResult result = n.send(message);
                        System.out.println(result.getMessage());
                    }
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });
    }

    public void submitMessage(String message) {
        queue.offer(message);
    }

    public void stop() {
        running = false;
    }
}
