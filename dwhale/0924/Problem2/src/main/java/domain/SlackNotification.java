package domain;

public class SlackNotification extends Notification {

    public SlackNotification(Integer sendingLimit, String name) {
        super(sendingLimit, name);
    }
}
