public class Main {
    public static void main(String[] args) throws InterruptedException {
        EmployeeEvaluation evaluation = new EmployeeEvaluation();

        Runnable task = () -> {
          for(int i = 0; i< 100; i ++) {
              evaluation.addScores((int) (Math.random() * 101));
          }
        };

        Thread[] threads = new Thread[10];
        for(int i = 0; i < 10; i++) {
            threads[i] = new Thread(task);
            threads[i].start();
        }


        for (Thread thread : threads) {
            thread.join();
        }

        System.out.println(evaluation.getAverage());
    }
}
