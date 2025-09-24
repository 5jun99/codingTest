package asis.controller;

import asis.model.*;
import asis.view.EvaluationView;

import java.util.*;

public class EvaluationController {
    private EvaluationView view;
    private FeedbackService feedbackService;
    private CalibrationModule calibrationModule;

    public EvaluationController(EvaluationView view) {
        this.view = view;
        this.feedbackService = new FeedbackService();
        this.calibrationModule = new CalibrationModule();
    }

    public EvaluationController(original_state.view.EvaluationView view) {
    }

    public void run() {
        int N = view.readEmployeeCount();

        List<Employee> employees = new ArrayList<>();
        Map<String, Employee> employeeMap = new HashMap<>();

        for (int i = 0; i < N; i++) {
            Employee employee = view.readEmployee();
            employees.add(employee);
            employeeMap.put(employee.getId(), employee);
        }

        int M = view.readFeedbackCount();

        for (int i = 0; i < M; i++) {
            EvaluationView.FeedbackInput input = view.readFeedbackInput();

            Employee employee = employeeMap.get(input.getEmpId());
            if (employee != null) {
                Optional<Integer> score = (input.getScoreVal() == -1) ?
                    Optional.empty() : Optional.of(input.getScoreVal());

                Feedback feedback = new Feedback(input.getEvaluatorId(), input.getText(), score);
                feedbackService.addFeedback(employee, feedback);
            }
        }

        calibrationModule.calibrate(employees);

        for (Employee employee : employees) {
            Report report = employee.generateReport();
            view.printReport(report);
        }
    }
}