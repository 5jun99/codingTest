public class Order {
    private final String orderId;
    private final int amount;
    private final PaymentMethod paymentMethod;

    public Order(String orderId, int amount, PaymentMethod paymentMethod) {
        this.orderId = orderId;
        this.amount = amount;
        this.paymentMethod = paymentMethod;
    }

    public boolean processOrder() {
        return paymentMethod.pay(amount);
    }

    public String getOrderId() {
        return orderId;
    }

    public int getAmount() {
        return amount;
    }

    public PaymentMethod getPaymentMethod() {
        return paymentMethod;
    }
}
