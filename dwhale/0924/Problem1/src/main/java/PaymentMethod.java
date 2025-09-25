public interface PaymentMethod {
    boolean pay(int amount);
    String getName();
}
