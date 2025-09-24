package original_state.model;

import java.util.Optional;

public class Feedback {
    String evaluatorId;
    String text;
    Optional<Integer> score;
    Double calibratedScore;

    public Feedback(String evaluatorId, String text, Optional<Integer> score) {
        this.evaluatorId = evaluatorId;
        this.text = text;
        this.score = score;
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

    public Double getCalibratedScore() {
        return calibratedScore;
    }

    public void updateCalibration(double calibratedScore) {
        this.calibratedScore = calibratedScore;
    }
}