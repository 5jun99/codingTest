package model.exception;

public class LibraryException extends RuntimeException {
    ErrorCode errorCode;

    public LibraryException(ErrorCode errorCode) {
        this.errorCode = errorCode;
    }
}
