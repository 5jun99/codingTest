package view.dto;

public class RequestInput {
    private final String command;
    private final String userId;
    private final String resourceId;

    public RequestInput(String command, String userId, String resourceId) {
        this.command = command;
        this.userId = userId;
        this.resourceId = resourceId;
    }

    public String getCommand() {
        return command;
    }

    public String getUserId() {
        return userId;
    }

    public String getResourceId() {
        return resourceId;
    }
}
