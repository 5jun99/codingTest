package asis.model;

import java.util.Optional;

public class Feedback {
    private String evaluatorId;
    private String text;
    private Optional<Integer> score;
    private Double calibratedScore;

    public Feedback(String evaluatorId, String text, Optional<Integer> score) {
        this.evaluatorId = evaluatorId;
        this.text = text;
        this.score = score;
        this.calibratedScore = null;
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

    public void setCalibratedScore(Double calibratedScore) {
        this.calibratedScore = calibratedScore;
    }
}