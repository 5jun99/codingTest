package controller;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import model.RentalService;
import model.domain.Book;
import model.domain.Command;
import model.domain.LibraryResource;
import model.domain.Magazine;
import model.domain.Request;
import model.domain.User;
import model.exception.LibraryException;
import view.LibraryView;
import view.dto.RequestInput;
import view.dto.ResourceInput;
import view.dto.UserInput;

public class LibraryController {
    private final LibraryView view;

    public LibraryController(LibraryView view) {
        this.view = view;
    }

    public void run() {
        int N = view.readResourceCount();

        Map<String, LibraryResource> resourceMap = new HashMap<>();

        for (int i = 0; i < N; i++) {
            ResourceInput resourceInput = view.readBook();

            LibraryResource resource;
            if (resourceInput.getType().equalsIgnoreCase("Book")) {
                resource = Book.of(resourceInput.getId(), resourceInput.getTitle());
            } else if (resourceInput.getType().equalsIgnoreCase("Magazine")) {
                resource = Magazine.of(resourceInput.getId(), resourceInput.getTitle());
            } else {
                throw new IllegalArgumentException("지원하지 않는 자원 종류: " + resourceInput.getType());
            }
            resourceMap.put(resourceInput.getId(), resource);
        }

        int M = view.readUserCount();
        Map<String, User> userMap = new HashMap<>();

        for (int i = 0; i < M; i++) {
            UserInput userInput = view.readUser();
            User user = User.of(userInput.getId(), userInput.getName());
            userMap.put(userInput.getId(), user);
        }

        int Q = view.readUserCount();
        RentalService service = new RentalService(resourceMap, userMap);
        Map<String, Request> requests = new HashMap<>();

        for (int i = 0; i < Q; i++) {
            RequestInput requestInput = view.readRequest();
            if (requestInput.getCommand().equals("BORROW")) {
                service.rentalResource(requestInput.getUserId(), requestInput.getResourceId());
            } else if (requestInput.getCommand().equals("RETURN")) {
                service.returnResource(requestInput.getUserId(), requestInput.getResourceId());
            }
        }

        ExecutorService executor = Executors.newFixedThreadPool(10);

        for (String requestId : requests.keySet()) {
            executor.submit(() -> {
                try {
                    Request request = requests.get(requestId);
                    rentalService.rentalResource(
                            request,
                            resourceMap,
                            userMap
                    );
                    view.printResult(request);
                } catch (LibraryException e) {
                    view.printFail
                }
            });
        }

        executor.shutdown();
    }

    private String generateRequestId(Map<String, Request> requests) {
        Set<String> ids = requests.keySet();
        String maxIdString = Collections.max(ids);

        int maxIdInt = Integer.parseInt(maxIdString);

        return String.valueOf(maxIdInt + 1);
    }
}
