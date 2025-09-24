package asis.model;

import java.util.*;

public class CalibrationModule {

    public void calibrate(List<Employee> employees) {
        Map<String, List<Double>> evaluatorScores = new HashMap<>();

        for (Employee employee : employees) {
            for (Feedback feedback : employee.getFeedbacks()) {
                if (feedback.getScore().isPresent()) {
                    evaluatorScores.computeIfAbsent(feedback.getEvaluatorId(), k -> new ArrayList<>())
                            .add(feedback.getScore().get().doubleValue());
                }
            }
        }

        Map<String, Double> evaluatorAverages = new HashMap<>();
        for (Map.Entry<String, List<Double>> entry : evaluatorScores.entrySet()) {
            double average = entry.getValue().stream().mapToDouble(Double::doubleValue).average().orElse(0.0);
            evaluatorAverages.put(entry.getKey(), average);
        }

        double globalAverage = evaluatorAverages.values().stream()
                .mapToDouble(Double::doubleValue)
                .average()
                .orElse(0.0);

        for (Employee employee : employees) {
            for (Feedback feedback : employee.getFeedbacks()) {
                if (feedback.getScore().isPresent()) {
                    String evaluatorId = feedback.getEvaluatorId();
                    double evaluatorAverage = evaluatorAverages.get(evaluatorId);

                    if (evaluatorAverage > globalAverage) {
                        double adjustmentRatio = globalAverage / evaluatorAverage;
                        double originalScore = feedback.getScore().get().doubleValue();
                        double adjustedScore = Math.round(originalScore * adjustmentRatio * 100.0) / 100.0;
                        feedback.setCalibratedScore(adjustedScore);
                    } else {
                        feedback.setCalibratedScore(feedback.getScore().get().doubleValue());
                    }
                }
            }
        }
    }
}