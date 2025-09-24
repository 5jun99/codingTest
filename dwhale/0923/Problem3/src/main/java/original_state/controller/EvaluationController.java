package original_state.controller;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import original_state.model.CalibrationModule;
import original_state.model.Employee;
import original_state.model.Feedback;
import original_state.model.FeedbackService;
import original_state.model.ReportService;
import original_state.view.EvaluationView;
import original_state.view.EvaluationView.EmployeeInput;
import original_state.view.EvaluationView.FeedbackInput;
import original_state.view.EvaluationView.ReportOutput;

public class EvaluationController {
    private final EvaluationView view;
    private final FeedbackService feedbackService;
    private final ReportService reportService;
    private final CalibrationModule calibrationModule;

    public EvaluationController(EvaluationView view, FeedbackService feedbackService, ReportService reportService,
                                CalibrationModule calibrationModule) {
        this.view = view;
        this.feedbackService = feedbackService;
        this.reportService = reportService;
        this.calibrationModule = calibrationModule;
    }

    public void run() {

        int N = view.readEmployeeCount();

        Map<String, Employee> employeeMap = readEmployees(N);

        int M = view.readFeedbackCount();

        readFeedBacks(M, employeeMap);

        calibrationModule.calibrate(employeeMap);

        for (Entry<String, Employee> entry : employeeMap.entrySet()) {
            ReportOutput reportOutput = reportService.createReport(entry.getValue());
            view.printReport(reportOutput);
        }
    }

    private Map<String, Employee> readEmployees(int N) {
        Map<String, Employee> employeeMap = new HashMap<>();

        for (int i = 0; i < N; i++) {
            EmployeeInput employeeInput = view.readEmployee();
            String id = employeeInput.getId();
            String name = employeeInput.getName();

            Employee employee = Employee.of(id, name);

            employeeMap.put(id, employee);
        }
        return employeeMap;
    }

    private void readFeedBacks(int M, Map<String, Employee> employeeMap) {
        for (int i = 0; i < M; i++) {
            FeedbackInput feedbackInput = view.readFeedback();
            Employee employee = employeeMap.get(feedbackInput.getEmployeeId());
            Feedback feedback = new Feedback(feedbackInput.getEvaluatorId(), feedbackInput.getText(),
                    feedbackInput.getScore());
            feedbackService.addFeedback(employee, feedback);
        }
    }
}