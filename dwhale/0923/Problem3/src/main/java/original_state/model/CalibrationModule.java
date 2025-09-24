package original_state.model;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.stream.Collectors;

public class CalibrationModule {

    public void calibrate(Map<String, Employee> employeeMap) {
        Map<String, List<Integer>> evaluatorScores = new HashMap<>();

        for (Entry<String, Employee> entry : employeeMap.entrySet()) {
            Employee employee = entry.getValue();
            for (Feedback feedback : employee.getFeedbacks()) {
                if (feedback.getScore().isPresent()) {
                    evaluatorScores.computeIfAbsent(feedback.getEvaluatorId(), k -> new ArrayList<>())
                            .add(feedback.getScore().get());
                }
            }
        }

        Map<String, Double> evaluatorAverages = evaluatorScores.entrySet().stream()
                .collect(Collectors.toMap(
                        Entry::getKey,
                        entry -> entry.getValue().stream().mapToInt(Integer::intValue).average().orElse(0)
                ));

        double totalAverage = evaluatorAverages.values().stream().mapToDouble(v -> v).average().orElse(0);

        for (Entry<String, Employee> entry : employeeMap.entrySet()) {
            Employee employee = entry.getValue();
            for (Feedback feedback : employee.getFeedbacks()) {
                if (feedback.score.isEmpty()) {
                    continue;
                }

                Integer feedbackScore = feedback.score.get();
                Double evaluatorAverage = evaluatorAverages.get(feedback.evaluatorId);

                if (evaluatorAverage > totalAverage) {
                    double calibrationRatio = totalAverage / evaluatorAverage;
                    double calibratedScore = feedbackScore * calibrationRatio;
                    feedback.updateCalibration(calibratedScore);
                } else {
                    feedback.updateCalibration(feedbackScore.doubleValue());
                }
            }
        }
    }
}