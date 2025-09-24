package model.domain;

public class User {
    private final String id;

    private final String name;

    private User(String id, String name) {
        this.id = id;
        this.name = name;
    }

    public static User of(String id, String name) {
        return new User(id, name);
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}
