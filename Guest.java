package model;

import java.sql.Timestamp;
import java.util.Date;
import java.util.List;

/**
 * Model class representing a Guest in the hotel system
 * Guests are special users with role = 'GUEST' but have additional properties
 */
public class Guest {
    private int id;
    private String username;
    private String fullName;
    private String email;
    private String phone;
    private boolean status;
    private Timestamp createdAt;
    private Timestamp updatedAt;
    private String notes;
    
    // Guest-specific statistics
    private int totalBookings;
    private int completedBookings;
    private double totalSpent;
    private Date lastVisit;
    private String loyaltyStatus;
    private double avgNights;
    
    // Related data
    private List<Reservation> bookingHistory;
    
    // Constructors
    public Guest() {
        this.status = true;
        this.totalBookings = 0;
        this.completedBookings = 0;
        this.totalSpent = 0.0;
        this.avgNights = 0.0;
    }
    
    public Guest(String fullName, String email, String phone) {
        this();
        this.fullName = fullName;
        this.email = email;
        this.phone = phone;
    }
    
    // Getters and Setters
    public int getId() {
        return id;
    }
    
    public void setId(int id) {
        this.id = id;
    }
    
    public String getUsername() {
        return username;
    }
    
    public void setUsername(String username) {
        this.username = username;
    }
    
    public String getFullName() {
        return fullName;
    }
    
    public void setFullName(String fullName) {
        this.fullName = fullName;
    }
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    public String getPhone() {
        return phone;
    }
    
    public void setPhone(String phone) {
        this.phone = phone;
    }
    
    public boolean isStatus() {
        return status;
    }
    
    public void setStatus(boolean status) {
        this.status = status;
    }
    
    public Timestamp getCreatedAt() {
        return createdAt;
    }
    
    public void setCreatedAt(Timestamp createdAt) {
        this.createdAt = createdAt;
    }
    
    public Timestamp getUpdatedAt() {
        return updatedAt;
    }
    
    public void setUpdatedAt(Timestamp updatedAt) {
        this.updatedAt = updatedAt;
    }
    
    public String getNotes() {
        return notes;
    }
    
    public void setNotes(String notes) {
        this.notes = notes;
    }
    
    public int getTotalBookings() {
        return totalBookings;
    }
    
    public void setTotalBookings(int totalBookings) {
        this.totalBookings = totalBookings;
    }
    
    public int getCompletedBookings() {
        return completedBookings;
    }
    
    public void setCompletedBookings(int completedBookings) {
        this.completedBookings = completedBookings;
    }
    
    public double getTotalSpent() {
        return totalSpent;
    }
    
    public void setTotalSpent(double totalSpent) {
        this.totalSpent = totalSpent;
    }
    
    public Date getLastVisit() {
        return lastVisit;
    }
    
    public void setLastVisit(Date lastVisit) {
        this.lastVisit = lastVisit;
    }
    
    public String getLoyaltyStatus() {
        return loyaltyStatus;
    }
    
    public void setLoyaltyStatus(String loyaltyStatus) {
        this.loyaltyStatus = loyaltyStatus;
    }
    
    public double getAvgNights() {
        return avgNights;
    }
    
    public void setAvgNights(double avgNights) {
        this.avgNights = avgNights;
    }
    
    public List<Reservation> getBookingHistory() {
        return bookingHistory;
    }
    
    public void setBookingHistory(List<Reservation> bookingHistory) {
        this.bookingHistory = bookingHistory;
    }
    
    // Helper methods
    public String getInitial() {
        if (fullName != null && !fullName.isEmpty()) {
            return fullName.substring(0, 1).toUpperCase();
        }
        return "G";
    }
    
    public String getLoyaltyBadgeClass() {
        if (loyaltyStatus == null) return "badge-secondary";
        switch (loyaltyStatus.toLowerCase()) {
            case "vip": return "badge-danger";
            case "gold": return "badge-warning";
            case "silver": return "badge-info";
            case "bronze": return "badge-secondary";
            default: return "badge-secondary";
        }
    }
    
    public boolean isVIP() {
        return "VIP".equalsIgnoreCase(loyaltyStatus);
    }
    
    public String getFormattedAvgNights() {
        return String.format("%.1f", avgNights);
    }
    
    
    // Convert User to Guest (for migration purposes)
    public static Guest fromUser(User user) {
        Guest guest = new Guest();
        guest.setId(user.getId());
        guest.setUsername(user.getUsername());
        guest.setFullName(user.getFullName());
        guest.setEmail(user.getEmail());
        guest.setPhone(user.getPhone());
        guest.setStatus(user.isStatus());
        guest.setCreatedAt(user.getCreatedAt());
        guest.setUpdatedAt(user.getUpdatedAt());
        guest.setTotalBookings(user.getTotalBookings());
        return guest;
    }
    
    @Override
    public String toString() {
        return "Guest{" +
                "id=" + id +
                ", fullName='" + fullName + '\'' +
                ", email='" + email + '\'' +
                ", phone='" + phone + '\'' +
                ", status=" + status +
                ", totalBookings=" + totalBookings +
                ", completedBookings=" + completedBookings +
                ", totalSpent=" + totalSpent +
                ", lastVisit=" + lastVisit +
                ", loyaltyStatus='" + loyaltyStatus + '\'' +
                ", avgNights=" + avgNights +
                '}';
    }
}