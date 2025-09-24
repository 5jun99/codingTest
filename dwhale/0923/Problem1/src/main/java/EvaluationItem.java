public abstract class EvaluationItem {
    String name;
    int weight;

    public EvaluationItem(String name, int weight) {
        this.name = name;
        this.weight = weight;
    }

    abstract Object calculateResult();

    @Override
    public abstract String toString();
}
