package model.domain;

public class Book extends LibraryResource {
    private Book(String id, String title) {
        super(id, title);
    }

    public static Book of(String id, String title) {
        return new Book(id, title);
    }

    @Override
    public String getResourceType() {
        return "Book";
    }
}
