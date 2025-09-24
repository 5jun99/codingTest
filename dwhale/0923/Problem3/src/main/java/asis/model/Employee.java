package asis.model;

import java.util.ArrayList;
import java.util.List;

public class Employee {
    private String id;
    private String name;
    private List<Feedback> feedbacks = new ArrayList<>();

    public Employee(String id, String name) {
        this.id = id;
        this.name = name;
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

    public Report generateReport() {
        List<String> feedbackTexts = new ArrayList<>();
        List<Double> originalScores = new ArrayList<>();
        List<Double> calibratedScores = new ArrayList<>();

        for (Feedback feedback : feedbacks) {
            feedbackTexts.add(feedback.getText());
            if (feedback.getScore().isPresent()) {
                originalScores.add(feedback.getScore().get().doubleValue());
                calibratedScores.add(feedback.getCalibratedScore());
            }
        }

        double originalAverage = originalScores.stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
        double calibratedAverage = calibratedScores.stream().mapToDouble(Double::doubleValue).average().orElse(0.0);

        return new Report(name, originalAverage, calibratedAverage, feedbackTexts);
    }
}