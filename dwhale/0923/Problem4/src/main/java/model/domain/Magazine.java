package model.domain;

public class Magazine extends LibraryResource {
    private Magazine(String id, String title) {
        super(id, title);
    }

    public static Magazine of(String id, String title) {
        return new Magazine(id, title);
    }

    @Override
    public String getResourceType() {
        return "Magazine";
    }
}
