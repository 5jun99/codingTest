package asis.model;

import java.util.List;

public class Report {
    private String employeeName;
    private double originalAverage;
    private double calibratedAverage;
    private List<String> feedbackTexts;

    public Report(String employeeName, double originalAverage, double calibratedAverage, List<String> feedbackTexts) {
        this.employeeName = employeeName;
        this.originalAverage = originalAverage;
        this.calibratedAverage = calibratedAverage;
        this.feedbackTexts = feedbackTexts;
    }

    public String getEmployeeName() {
        return employeeName;
    }

    public double getOriginalAverage() {
        return originalAverage;
    }

    public double getCalibratedAverage() {
        return calibratedAverage;
    }

    public List<String> getFeedbackTexts() {
        return feedbackTexts;
    }
}