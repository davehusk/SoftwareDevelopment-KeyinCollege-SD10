public class Date {
    private int day;
    private int month;
    private int year;

    // Constructor with day, month, and year
    public Date(int day, int month, int year) {
        this.day = day;
        this.month = month;
        this.year = year;
    }

    // Getter for day
    public int getDay() {
        return day;
    }

    // Getter for month
    public int getMonth() {
        return month;
    }

    // Getter for year
    public int getYear() {
        return year;
    }

    // Setter for day
    public void setDay(int day) {
        this.day = day;
    }

    // Setter for month
    public void setMonth(int month) {
        this.month = month;
    }

    // Setter for year
    public void setYear(int year) {
        this.year = year;
    }

    // Set date method
    public void setDate(int day, int month, int year) {
        this.day = day;
        this.month = month;
        this.year = year;
    }

    // toString method to return date in "dd/mm/yyyy" format
    @Override
    public String toString() {
        return String.format("%02d/%02d/%04d", day, month, year);
    }
}
