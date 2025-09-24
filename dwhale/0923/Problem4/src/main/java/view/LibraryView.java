package view;

import java.util.Map;
import java.util.Scanner;
import model.domain.LibraryResource;
import model.domain.User;
import view.dto.RequestInput;
import view.dto.ResourceInput;
import view.dto.UserInput;

public class LibraryView {
    private final Scanner scanner;

    public LibraryView(Scanner scanner) {
        this.scanner = scanner;
    }

    public int readResourceCount() {
        return getAnInt();
    }

    public int readUserCount() {
        return getAnInt();
    }

    public ResourceInput readBook() {
        return new ResourceInput(scanner.next(), scanner.next(), scanner.next());
    }

    public UserInput readUser() {
        return new UserInput(scanner.next(), scanner.next());
    }

    public RequestInput readRequest() {
        return new RequestInput(scanner.next(), scanner.next(), scanner.next());
    }

    private int getAnInt() {
        return scanner.nextInt();
    }

    public void printResult(Map<String, LibraryResource> libraryResourceMap, Map<String, User> userMap) {
        
    }
}
