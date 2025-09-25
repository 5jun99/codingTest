public class PointPayment implements PaymentMethod{
    private Integer point;

    public PointPayment(Integer balance) {
        this.point = balance;
    }

    @Override
    public boolean pay(int amount) {
        return point >= amount;
    }

    @Override
    public String getName() {
        return "Point";
    }
}
