package view.dto;

public class UserInput {

    private final String id;
    private final String name;

    public UserInput(String id, String name) {
        this.id = id;
        this.name = name;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}
