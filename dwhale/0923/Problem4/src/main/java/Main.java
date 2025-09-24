import controller.LibraryController;
import java.util.Scanner;
import view.LibraryView;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        LibraryView libraryView = new LibraryView(scanner);

        LibraryController libraryController = new LibraryController(libraryView);

        libraryController.run();
    }
}
