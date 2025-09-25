package domain;

public class Notification {
    Integer sendingLimit;
    final String name;
    Integer sendingStatus;

    public Notification(Integer sendingLimit, String name) {
        this.sendingLimit = sendingLimit;
        this.name = name;
        this.sendingStatus = 0;
    }

    public NotificationResult send(String message) {
        if (sendingStatus >= sendingLimit) {
            return new NotificationResult(false, String.format("[%s] 채널 전송 제한 초과", name));
        }
        sendingStatus++;
        return new NotificationResult(true, String.format("[%s] %s", name, message));
    }
}
