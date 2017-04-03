package com.smartsync.error;


/**
 * @author Jack Meyer
 *
 * Service Not Found Exception which is thrown when the user that is tyring to be accessed is not found in the database.
 */
public class ServiceNotFoundException extends RuntimeException {

    /**
     * The url which the error occured
     */
    private String url;

    /**
     * The error message
     */
    private String message;

    public ServiceNotFoundException(String message, String url) {
        this.message = message;
        this.url = url;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
