package view.dto;

public class ResourceInput {
    private final String id;
    private final String type;
    private final String title;

    public ResourceInput(String id, String type, String title) {
        this.id = id;
        this.type = type;
        this.title = title;
    }

    public String getId() {
        return id;
    }

    public String getType() {
        return type;
    }

    public String getTitle() {
        return title;
    }
}
