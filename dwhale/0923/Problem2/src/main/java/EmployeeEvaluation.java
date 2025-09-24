public class EmployeeEvaluation {
    int totalScore;
    int count;

    public EmployeeEvaluation() {
        this.totalScore = 0;
        this.count = 0;
    }

    public synchronized void addScores(int score) {
        if (score > 100 || score < 0) {
            throw new IllegalArgumentException("점수는 0~100 인 수입니다.");
        }
        totalScore += score;
        count ++;
    }

    public synchronized double getAverage() {
        return (double) totalScore / count;
    }
}
