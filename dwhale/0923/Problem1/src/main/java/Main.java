public class Main {
    public static void main(String[] args) {
        EvaluationItem scoreItem = new ScoreItem("협업 능력", 50, 80);
        EvaluationItem feedbackItem = new FeedbackItem("협업 능력", 50, "팀을 잘 이끈다.");


        System.out.println(scoreItem);
        System.out.println("결과값: " + scoreItem.calculateResult());
        System.out.println(feedbackItem);
        System.out.println("결과값: " + feedbackItem.calculateResult());
    }
}