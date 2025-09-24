public class FeedbackItem extends EvaluationItem{
    private final String comment;

    public FeedbackItem(String name, int weight, String comment) {
        super(name, weight);
        this.comment = comment;
    }

    @Override
    String calculateResult() {
        return comment;
    }

    @Override
    public String toString() {
        return String.format("%s (weight=%d): 피드백=%s", name, weight, comment);
    }
}