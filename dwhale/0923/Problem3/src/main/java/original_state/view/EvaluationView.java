package original_state.view;

import java.util.List;
import java.util.Optional;
import java.util.Scanner;

public class EvaluationView {
    private final Scanner scanner;

    public EvaluationView(Scanner scanner) {
        this.scanner = scanner;
    }

    public int readEmployeeCount() {
        return getAnInt();
    }

    public int readFeedbackCount() {
        return getAnInt();
    }

    public EmployeeInput readEmployee() {
        String id = scanner.next();
        String name = scanner.next();

        return new EmployeeInput(id, name);
    }

    private int getAnInt() {
        return scanner.nextInt();
    }

    public FeedbackInput readFeedback() {
        String empId = scanner.next();
        String evaluatorId = scanner.next();
        String text = scanner.next();
        int scoreVal = scanner.nextInt();

        return new FeedbackInput(empId, evaluatorId, text, scoreVal);
    }

    public void printReport(ReportOutput reportOutput) {
        System.out.println("[" + reportOutput.getEmployeeName() + "]");
        System.out.printf("원본 평균: %.2f%n", reportOutput.getOriginalAverage());
        System.out.printf("조정 평균: %.2f%n", reportOutput.getCalibratedAverage());
        System.out.println("피드백: " + String.join(", ", reportOutput.getFeedbackTexts()));
    }

    public static class EmployeeInput{
        String id;
        String name;

        public String getId() {
            return id;
        }

        public String getName() {
            return name;
        }

        public EmployeeInput(String id, String name) {
            this.id = id;
            this.name = name;
        }
    }

    public static class FeedbackInput{
        String employeeId;
        String evaluatorId;
        String text;
        Optional<Integer> score;


        public String getEmployeeId() {
            return employeeId;
        }

        public String getEvaluatorId() {
            return evaluatorId;
        }

        public String getText() {
            return text;
        }

        public Optional<Integer> getScore() {
            return score;
        }


        public FeedbackInput(String employeeId, String evaluatorId, String text, Integer score) {
            this.employeeId = employeeId;
            this.evaluatorId = evaluatorId;
            this.text = text;
            this.score = (score == -1) ? Optional.empty() : Optional.of(score);
        }
    }

    public static class ReportOutput {
        private final String employeeName;
        private final double originalAverage;
        private final double calibratedAverage;
        private final List<String> feedbackTexts;

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

        public ReportOutput(String employeeName, double originalAverage, double calibratedAverage,
                            List<String> feedbackTexts) {
            this.employeeName = employeeName;
            this.originalAverage = originalAverage;
            this.calibratedAverage = calibratedAverage;
            this.feedbackTexts = feedbackTexts;
        }

        public static ReportOutput of(String employeeName, double originalAverage, double calibratedAverage, List<String> feedbackTexts) {
            return new ReportOutput(employeeName, originalAverage, calibratedAverage, feedbackTexts);
        }
    }
}
