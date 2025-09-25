package service;

import domain.Notification;
import java.util.List;

public class NotificationService {

    private final List<Notification> notifications;

    public NotificationService(List<Notification> notifications) {
        this.notifications = notifications;
    }

    public List<String> sendToAll (String message) {
        return notifications.stream().map(notification -> notification.send(message).message).toList();
    }
}
