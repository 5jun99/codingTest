package model;

import java.util.Map;
import model.domain.LibraryResource;
import model.domain.User;

public class RentalService {
    private final Map<String, LibraryResource> resources;
    private final Map<String, User> users;

    public RentalService(Map<String, LibraryResource> resources, Map<String, User> users) {
        this.resources = resources;
        this.users = users;
    }

    public synchronized void rentalResource(String userId, String resourceId) {

    }


    public synchronized void returnResource(String userId, String resourceId) {
    }
}
