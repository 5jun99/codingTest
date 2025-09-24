package asis.view;

import asis.model.Employee;
import asis.model.Report;

import java.util.Scanner;

public class EvaluationView {
    private Scanner scanner;

    public EvaluationView(Scanner scanner) {
        this.scanner = scanner;
    }

    public int readEmployeeCount() {
        return scanner.nextInt();
    }

    public Employee readEmployee() {
        String id = scanner.next();
        String name = scanner.next();
        return new Employee(id, name);
    }

    public int readFeedbackCount() {
        return scanner.nextInt();
    }

    public FeedbackInput readFeedbackInput() {
        String empId = scanner.next();
        String evaluatorId = scanner.next();
        String text = scanner.next();
        int scoreVal = scanner.nextInt();
        return new FeedbackInput(empId, evaluatorId, text, scoreVal);
    }

    public void printReport(Report report) {
        System.out.println("[" + report.getEmployeeName() + "]");
        System.out.printf("원본 평균: %.2f%n", report.getOriginalAverage());
        System.out.printf("조정 평균: %.2f%n", report.getCalibratedAverage());
        System.out.println("피드백: " + String.join(", ", report.getFeedbackTexts()));
    }

    public static class FeedbackInput {
        private String empId;
        private String evaluatorId;
        private String text;
        private int scoreVal;

        public FeedbackInput(String empId, String evaluatorId, String text, int scoreVal) {
            this.empId = empId;
            this.evaluatorId = evaluatorId;
            this.text = text;
            this.scoreVal = scoreVal;
        }

        public String getEmpId() { return empId; }
        public String getEvaluatorId() { return evaluatorId; }
        public String getText() { return text; }
        public int getScoreVal() { return scoreVal; }
    }
}