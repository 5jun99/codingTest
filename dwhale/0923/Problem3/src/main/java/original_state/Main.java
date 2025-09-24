package original_state;

import java.util.Scanner;
import original_state.controller.EvaluationController;
import original_state.model.CalibrationModule;
import original_state.model.FeedbackService;
import original_state.model.ReportService;
import original_state.view.EvaluationView;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        EvaluationView view = new EvaluationView(sc);
        FeedbackService feedbackService = new FeedbackService();
        ReportService reportService = new ReportService();
        CalibrationModule calibrationModule = new CalibrationModule();

        EvaluationController controller = new EvaluationController(view, feedbackService, reportService,
                calibrationModule);
        controller.run();
    }
}