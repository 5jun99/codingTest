package asis.model;

import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

public class FeedbackService {
    private final ReadWriteLock lock = new ReentrantReadWriteLock();

    public void addFeedback(Employee employee, Feedback feedback) {
        lock.writeLock().lock();
        try {
            employee.addFeedback(feedback);
        } finally {
            lock.writeLock().unlock();
        }
    }
}