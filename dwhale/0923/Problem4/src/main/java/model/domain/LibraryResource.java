package model.domain;

public abstract class LibraryResource {
    protected String id;
    protected String title;
    protected Boolean isBorrowed;

    public LibraryResource(String id, String title) {
        this.id = id;
        this.title = title;
        this.isBorrowed = Boolean.FALSE;
    }

    public abstract String getResourceType();

    public Boolean getBorrowed() {
        return isBorrowed;
    }

    public void updateStatus(Boolean aTrue) {
        this.isBorrowed = aTrue;
    }
}
