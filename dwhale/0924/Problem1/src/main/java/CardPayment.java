public class CardPayment implements PaymentMethod{
    private Integer balance;

    public CardPayment(Integer balance) {
        this.balance = balance;
    }

    @Override
    public boolean pay(int amount) {
        return balance >= amount;
    }

    @Override
    public String getName() {
        return "Card";
    }
}
