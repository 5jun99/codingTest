package original_state.model;

import java.util.ArrayList;
import java.util.List;

public class Employee {
    String id;
    String name;

    List<Feedback> feedbacks = new ArrayList<>();

    public Employee(String id, String name) {
        this.id = id;
        this.name = name;
    }

    public static Employee of(String id, String name) {
        return new Employee(id, name);
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public List<Feedback> getFeedbacks() {
        return feedbacks;
    }

    public void addFeedback(Feedback feedback) {
        feedbacks.add(feedback);
    }

    public List<String> getFeedbackTexts() {
        return feedbacks.stream().map(Feedback::getText).toList();
    }
}