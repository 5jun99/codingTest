package original_state.model;

import java.util.List;
import original_state.view.EvaluationView.ReportOutput;

public class ReportService {

    public ReportOutput createReport(Employee employee) {
        List<Feedback> feedbacks = employee.getFeedbacks();
        double originalAverage = feedbacks.stream().filter(feedback -> feedback.score.isPresent())
                .mapToInt(feedback -> feedback.getScore().get()).average().orElse(0);
        double calibratedAverage = feedbacks.stream().filter(feedback -> feedback.score.isPresent())
                .mapToDouble(Feedback::getCalibratedScore).average().orElse(0);

        return ReportOutput.of(employee.getName(), originalAverage, calibratedAverage, employee.getFeedbackTexts());
    }
}
