public class ScoreItem extends EvaluationItem{
    private int score;

    public ScoreItem(String name, int weight, int score) {
        super(name, weight);
        if (score < 0 || score > 100) {
            throw new IllegalArgumentException("점수는 0에서 100 사이여야합니다");
        }
        this.score = score;
    }

    @Override
    Integer calculateResult() {
        return (score * weight) / 100;
    }

    @Override
    public String toString() {
        return String.format("%s (weight=%d): 점수=%d -> 결과%d",
                name, weight, score, (int) calculateResult());
    }
}
