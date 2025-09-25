public class KakaoPayPayment implements PaymentMethod {
    private Integer kakoBalance;

    public KakaoPayPayment(Integer balance) {
        this.kakoBalance = balance;
    }

    @Override
    public boolean pay(int amount) {
        return kakoBalance >= amount;
    }

    @Override
    public String getName() {
        return "KakaoPay";
    }
}
