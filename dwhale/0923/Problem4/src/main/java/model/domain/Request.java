package model.domain;

public class Request {
    private final Command command;
    private final String userId;
    private final String resourceId;

    private Request(Command command, String userId, String resourceId) {
        this.command = command;
        this.userId = userId;
        this.resourceId = resourceId;
    }

    public static Request of(Command command, String userId, String bookId) {
        return new Request(command, userId, bookId);
    }

    public Command getCommand() {
        return command;
    }

    public String getUserId() {
        return userId;
    }

    public String getResourceId() {
        return resourceId;
    }
}

