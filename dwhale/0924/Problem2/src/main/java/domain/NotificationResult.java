package domain;

public class NotificationResult {
    public boolean isSuccess;
    public String message;

    public NotificationResult(boolean isSuccess, String message) {
        this.isSuccess = isSuccess;
        this.message = message;
    }

    public boolean isSuccess() {
        return isSuccess;
    }

    public String getMessage() {
        return message;
    }
}
