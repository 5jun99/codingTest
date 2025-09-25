package domain;

public class SmsNotification extends Notification {
    public SmsNotification(Integer sendingLimit, String name) {
        super(sendingLimit, name);
    }
}
