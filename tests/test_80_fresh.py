#!/usr/bin/env python3
"""
Fresh 80 Test Cases for Code Smell Detection
Categories: GodClass, DataClass, Clean, LongMethod, FeatureEnvy
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import predict_smell_extended as ps
from datetime import datetime

# Test cases with balanced distribution
TEST_CASES = [
    # ==================== GodClass (16 cases) ====================
    {
        'id': 1,
        'expected': 'GodClass',
        'description': 'Monolithic dashboard controller',
        'code': '''
public class DashboardController {
    private UserService userService;
    private OrderService orderService;
    private ProductService productService;
    private ReportGenerator reportGenerator;
    private NotificationService notificationService;
    private AnalyticsEngine analytics;
    private CacheManager cacheManager;
    
    public void loadDashboard() { loadUsers(); loadOrders(); loadProducts(); generateReports(); sendNotifications(); }
    public void loadUsers() { }
    public void loadOrders() { }
    public void loadProducts() { }
    public void generateReports() { }
    public void sendNotifications() { }
    public void updateCache() { }
    public void trackAnalytics() { }
    public void exportData() { }
    public void importData() { }
    public void validateData() { }
    public void cleanupData() { }
    public void archiveOldData() { }
    public void syncWithRemote() { }
    public void handleErrors() { }
    public void logActivity() { }
    public void processScheduledTasks() { }
    public void managePermissions() { }
}'''
    },
    {
        'id': 2,
        'expected': 'GodClass',
        'description': 'Comprehensive payment gateway',
        'code': '''
public class PaymentGateway {
    private CreditCardProcessor creditCardProcessor;
    private PayPalService paypalService;
    private StripeConnector stripeConnector;
    private FraudDetector fraudDetector;
    private TransactionLogger transactionLogger;
    private EmailNotifier emailNotifier;
    private RefundManager refundManager;
    
    public void processCreditCard(Payment p) { }
    public void processPayPal(Payment p) { }
    public void processStripe(Payment p) { }
    public void detectFraud(Payment p) { }
    public void logTransaction(Payment p) { }
    public void sendReceipt(Payment p) { }
    public void processRefund(Payment p) { }
    public void validateCard(Card c) { }
    public void encryptData(String data) { }
    public void decryptData(String data) { }
    public void storePayment(Payment p) { }
    public void retrievePayment(String id) { }
    public void cancelPayment(String id) { }
    public void reconcileTransactions() { }
    public void generateFinancialReport() { }
}'''
    },
    {
        'id': 3,
        'expected': 'GodClass',
        'description': 'Content management system core',
        'code': '''
public class CMSCore {
    private ArticleRepository articleRepo;
    private MediaManager mediaManager;
    private UserManager userManager;
    private CommentModerator commentModerator;
    private SEOOptimizer seoOptimizer;
    private CacheService cacheService;
    
    public void createArticle(Article a) { }
    public void updateArticle(Article a) { }
    public void deleteArticle(String id) { }
    public void publishArticle(String id) { }
    public void uploadMedia(File f) { }
    public void deleteMedia(String id) { }
    public void manageUsers() { }
    public void moderateComments() { }
    public void optimizeSEO() { }
    public void clearCache() { }
    public void backupContent() { }
    public void restoreContent() { }
    public void exportContent() { }
    public void importContent() { }
    public void generateSitemap() { }
    public void handleSearch(String query) { }
}'''
    },
    {
        'id': 4,
        'expected': 'GodClass',
        'description': 'Warehouse management system',
        'code': '''
public class WarehouseManager {
    private InventoryTracker inventoryTracker;
    private ShipmentCoordinator shipmentCoordinator;
    private SupplierManager supplierManager;
    private QualityControl qualityControl;
    private StaffScheduler staffScheduler;
    private ReportBuilder reportBuilder;
    
    public void receiveShipment(Shipment s) { }
    public void processOutbound(Order o) { }
    public void updateInventory() { }
    public void orderFromSupplier(Product p) { }
    public void performQualityCheck(Product p) { }
    public void scheduleStaff() { }
    public void generateInventoryReport() { }
    public void trackLocation(Product p) { }
    public void handleReturns(Return r) { }
    public void optimizeStorage() { }
    public void managePicking() { }
    public void managePacking() { }
    public void scanBarcode(String code) { }
    public void updateDatabase() { }
    public void sendAlerts() { }
}'''
    },
    {
        'id': 5,
        'expected': 'GodClass',
        'description': 'Travel booking platform',
        'code': '''
public class TravelBookingPlatform {
    private FlightService flightService;
    private HotelService hotelService;
    private CarRentalService carService;
    private PaymentProcessor paymentProcessor;
    private CustomerSupport customerSupport;
    private LoyaltyProgram loyaltyProgram;
    
    public void searchFlights(SearchCriteria c) { }
    public void bookFlight(Flight f) { }
    public void searchHotels(String location) { }
    public void bookHotel(Hotel h) { }
    public void rentCar(Car c) { }
    public void processPayment(Payment p) { }
    public void cancelBooking(String id) { }
    public void modifyBooking(String id) { }
    public void sendConfirmation(Booking b) { }
    public void handleSupport(Ticket t) { }
    public void awardPoints(Customer c) { }
    public void redeemPoints(Customer c) { }
    public void generateItinerary(Booking b) { }
    public void checkInOnline(String bookingId) { }
    public void sendReminder(Booking b) { }
}'''
    },
    {
        'id': 6,
        'expected': 'GodClass',
        'description': 'Gaming platform controller',
        'code': '''
public class GamePlatformController {
    private PlayerManager playerManager;
    private GameSessionManager sessionManager;
    private LeaderboardManager leaderboardManager;
    private ChatService chatService;
    private StoreManager storeManager;
    private AchievementTracker achievementTracker;
    
    public void registerPlayer(Player p) { }
    public void loginPlayer(String username, String password) { }
    public void startGameSession(Game g) { }
    public void endGameSession(String sessionId) { }
    public void updateLeaderboard(Score s) { }
    public void sendChatMessage(Message m) { }
    public void purchaseItem(Item i) { }
    public void unlockAchievement(Achievement a) { }
    public void saveProgress(GameState state) { }
    public void loadProgress(String playerId) { }
    public void matchPlayers() { }
    public void handleDisconnect(Player p) { }
    public void banPlayer(String playerId) { }
    public void processRefund(Transaction t) { }
    public void updateStats(Player p) { }
}'''
    },
    {
        'id': 7,
        'expected': 'GodClass',
        'description': 'Healthcare system coordinator',
        'code': '''
public class HealthcareSystemCoordinator {
    private PatientRegistry patientRegistry;
    private AppointmentScheduler appointmentScheduler;
    private MedicalRecords medicalRecords;
    private BillingSystem billingSystem;
    private PharmacyConnector pharmacyConnector;
    private InsuranceVerifier insuranceVerifier;
    
    public void registerPatient(Patient p) { }
    public void scheduleAppointment(Appointment a) { }
    public void cancelAppointment(String id) { }
    public void updateMedicalRecord(Record r) { }
    public void generateBill(Visit v) { }
    public void processBilling(Bill b) { }
    public void prescribeMedication(Prescription p) { }
    public void verifyInsurance(Patient p) { }
    public void sendReminder(Appointment a) { }
    public void generateReport(String patientId) { }
    public void transferPatient(Patient p, String facility) { }
    public void admitPatient(Patient p) { }
    public void dischargePatient(String patientId) { }
    public void orderLabTest(LabOrder o) { }
    public void retrieveLabResults(String orderId) { }
}'''
    },
    {
        'id': 8,
        'expected': 'GodClass',
        'description': 'Smart home automation hub',
        'code': '''
public class SmartHomeHub {
    private LightingController lightingController;
    private ThermostatManager thermostatManager;
    private SecuritySystem securitySystem;
    private ApplianceConnector applianceConnector;
    private EnergyMonitor energyMonitor;
    private VoiceAssistant voiceAssistant;
    
    public void controlLights(String room, boolean on) { }
    public void setTemperature(int temp) { }
    public void armSecurity() { }
    public void disarmSecurity() { }
    public void startAppliance(String appliance) { }
    public void stopAppliance(String appliance) { }
    public void monitorEnergy() { }
    public void optimizeEnergy() { }
    public void processVoiceCommand(String command) { }
    public void createAutomation(Rule rule) { }
    public void executeAutomation(String ruleId) { }
    public void sendAlert(Alert a) { }
    public void checkDeviceStatus() { }
    public void updateFirmware() { }
    public void generateUsageReport() { }
}'''
    },
    {
        'id': 9,
        'expected': 'GodClass',
        'description': 'Educational platform manager',
        'code': '''
public class EducationalPlatform {
    private CourseManager courseManager;
    private StudentEnrollment studentEnrollment;
    private AssignmentTracker assignmentTracker;
    private GradingSystem gradingSystem;
    private ForumModerator forumModerator;
    private CertificateGenerator certificateGenerator;
    
    public void createCourse(Course c) { }
    public void updateCourse(Course c) { }
    public void enrollStudent(Student s, String courseId) { }
    public void unenrollStudent(String studentId, String courseId) { }
    public void submitAssignment(Assignment a) { }
    public void gradeAssignment(String assignmentId, Grade g) { }
    public void postForum(ForumPost p) { }
    public void moderateForum(String postId) { }
    public void generateCertificate(String studentId, String courseId) { }
    public void trackProgress(String studentId) { }
    public void sendNotification(Notification n) { }
    public void scheduleExam(Exam e) { }
    public void conductExam(String examId) { }
    public void publishGrades(String courseId) { }
    public void generateTranscript(String studentId) { }
}'''
    },
    {
        'id': 10,
        'expected': 'GodClass',
        'description': 'Manufacturing execution system',
        'code': '''
public class ManufacturingExecutionSystem {
    private ProductionScheduler productionScheduler;
    private QualityAssurance qualityAssurance;
    private InventoryController inventoryController;
    private MaintenanceManager maintenanceManager;
    private SupplyChainConnector supplyChainConnector;
    private ComplianceChecker complianceChecker;
    
    public void scheduleProdution(ProductionOrder o) { }
    public void startProduction(String orderId) { }
    public void stopProduction(String orderId) { }
    public void performQualityCheck(Product p) { }
    public void rejectProduct(String productId) { }
    public void updateInventory(InventoryChange c) { }
    public void orderRawMaterials(Material m) { }
    public void scheduleMaintenance(Machine machine) { }
    public void performMaintenance(String machineId) { }
    public void checkCompliance(Product p) { }
    public void generateReport(String type) { }
    public void trackShipment(String shipmentId) { }
    public void optimizeProduction() { }
    public void handleDefect(Defect d) { }
    public void calibrateMachine(Machine m) { }
}'''
    },
    {
        'id': 11,
        'expected': 'GodClass',
        'description': 'Media streaming service',
        'code': '''
public class MediaStreamingService {
    private ContentLibrary contentLibrary;
    private UserProfileManager userProfileManager;
    private StreamingEngine streamingEngine;
    private RecommendationEngine recommendationEngine;
    private SubscriptionManager subscriptionManager;
    private AnalyticsCollector analyticsCollector;
    
    public void addContent(Media media) { }
    public void removeContent(String contentId) { }
    public void createProfile(User user) { }
    public void updateProfile(Profile profile) { }
    public void startStream(String contentId, String userId) { }
    public void pauseStream(String sessionId) { }
    public void stopStream(String sessionId) { }
    public void generateRecommendations(String userId) { }
    public void subscribe(String userId, Plan plan) { }
    public void cancelSubscription(String userId) { }
    public void collectAnalytics(Event event) { }
    public void handleBuffering(String sessionId) { }
    public void adjustQuality(String sessionId, Quality quality) { }
    public void addToWatchlist(String userId, String contentId) { }
    public void rateContent(String userId, String contentId, int rating) { }
}'''
    },
    {
        'id': 12,
        'expected': 'GodClass',
        'description': 'Logistics dispatch center',
        'code': '''
public class LogisticsDispatchCenter {
    private VehicleFleet vehicleFleet;
    private DriverManager driverManager;
    private RouteOptimizer routeOptimizer;
    private DeliveryTracker deliveryTracker;
    private CustomerService customerService;
    private FuelManager fuelManager;
    
    public void assignDriver(String driverId, String vehicleId) { }
    public void scheduleDelivery(Delivery delivery) { }
    public void optimizeRoute(String deliveryId) { }
    public void trackDelivery(String deliveryId) { }
    public void updateDeliveryStatus(String deliveryId, Status status) { }
    public void handleDelay(String deliveryId) { }
    public void notifyCustomer(String customerId, String message) { }
    public void processReturn(String deliveryId) { }
    public void manageFuel(String vehicleId) { }
    public void scheduleMaintenance(String vehicleId) { }
    public void handleAccident(String vehicleId) { }
    public void generateManifest(String deliveryId) { }
    public void calculateCost(Delivery delivery) { }
    public void processPayment(String deliveryId) { }
    public void generatePerformanceReport() { }
}'''
    },
    {
        'id': 13,
        'expected': 'GodClass',
        'description': 'Enterprise resource planning',
        'code': '''
public class EnterpriseResourcePlanning {
    private FinanceModule financeModule;
    private HRModule hrModule;
    private ProcurementModule procurementModule;
    private SalesModule salesModule;
    private ManufacturingModule manufacturingModule;
    private ReportingEngine reportingEngine;
    
    public void manageAccounts() { }
    public void processPayroll() { }
    public void handleRecruitment() { }
    public void createPurchaseOrder(PurchaseOrder po) { }
    public void approvePurchaseOrder(String poId) { }
    public void manageSales() { }
    public void generateQuote(Quote quote) { }
    public void scheduleManufacturing(ProductionOrder order) { }
    public void trackInventory() { }
    public void generateFinancialReport() { }
    public void generateHRReport() { }
    public void generateSalesReport() { }
    public void syncDepartments() { }
    public void auditTransactions() { }
    public void manageCompliance() { }
}'''
    },
    {
        'id': 14,
        'expected': 'GodClass',
        'description': 'Customer relationship orchestrator',
        'code': '''
public class CRMOrchestrator {
    private ContactManager contactManager;
    private LeadTracker leadTracker;
    private OpportunityManager opportunityManager;
    private SalesForecaster salesForecaster;
    private EmailCampaigner emailCampaigner;
    private SupportTicketManager supportTicketManager;
    
    public void createContact(Contact contact) { }
    public void updateContact(Contact contact) { }
    public void captureeLead(Lead lead) { }
    public void qualifyLead(String leadId) { }
    public void createOpportunity(Opportunity opp) { }
    public void updateOpportunity(String oppId, Status status) { }
    public void forecastSales(String period) { }
    public void createEmailCampaign(Campaign campaign) { }
    public void sendCampaign(String campaignId) { }
    public void trackCampaign(String campaignId) { }
    public void createTicket(Ticket ticket) { }
    public void assignTicket(String ticketId, String agentId) { }
    public void resolveTicket(String ticketId) { }
    public void generateReport(String type) { }
    public void syncWithEmail() { }
}'''
    },
    {
        'id': 15,
        'expected': 'GodClass',
        'description': 'Food delivery platform',
        'code': '''
public class FoodDeliveryPlatform {
    private RestaurantManager restaurantManager;
    private MenuManager menuManager;
    private OrderProcessor orderProcessor;
    private DeliveryDispatcher deliveryDispatcher;
    private PaymentGateway paymentGateway;
    private RatingSystem ratingSystem;
    
    public void registerRestaurant(Restaurant restaurant) { }
    public void updateRestaurant(Restaurant restaurant) { }
    public void addMenuItem(MenuItem item) { }
    public void updateMenuItem(MenuItem item) { }
    public void placeOrder(Order order) { }
    public void confirmOrder(String orderId) { }
    public void assignDelivery(String orderId, String driverId) { }
    public void trackDelivery(String orderId) { }
    public void processPayment(Payment payment) { }
    public void refundPayment(String orderId) { }
    public void rateRestaurant(String restaurantId, int rating) { }
    public void rateDriver(String driverId, int rating) { }
    public void handleComplaint(Complaint complaint) { }
    public void applyPromotion(String promoCode) { }
    public void generateAnalytics() { }
}'''
    },
    {
        'id': 16,
        'expected': 'GodClass',
        'description': 'IoT device management platform',
        'code': '''
public class IoTDeviceManagementPlatform {
    private DeviceRegistry deviceRegistry;
    private FirmwareUpdater firmwareUpdater;
    private TelemetryCollector telemetryCollector;
    private AlertManager alertManager;
    private SecurityManager securityManager;
    private ConfigurationManager configurationManager;
    
    public void registerDevice(Device device) { }
    public void deregisterDevice(String deviceId) { }
    public void updateFirmware(String deviceId, Firmware firmware) { }
    public void collectTelemetry(String deviceId) { }
    public void processTelemetry(Telemetry data) { }
    public void createAlert(Alert alert) { }
    public void resolveAlert(String alertId) { }
    public void authenticateDevice(String deviceId) { }
    public void revokeAccess(String deviceId) { }
    public void updateConfiguration(String deviceId, Configuration config) { }
    public void monitorHealth(String deviceId) { }
    public void executeCommand(String deviceId, Command command) { }
    public void generateReport(String deviceId) { }
    public void optimizeNetwork() { }
    public void syncDevices() { }
}'''
    },

    # ==================== DataClass (16 cases) ====================
    {
        'id': 17,
        'expected': 'DataClass',
        'description': 'Invoice DTO',
        'code': '''
public class Invoice {
    private String invoiceNumber;
    private LocalDate invoiceDate;
    private BigDecimal totalAmount;
    private String customerName;
    
    public String getInvoiceNumber() { return invoiceNumber; }
    public void setInvoiceNumber(String invoiceNumber) { this.invoiceNumber = invoiceNumber; }
    public LocalDate getInvoiceDate() { return invoiceDate; }
    public void setInvoiceDate(LocalDate invoiceDate) { this.invoiceDate = invoiceDate; }
    public BigDecimal getTotalAmount() { return totalAmount; }
    public void setTotalAmount(BigDecimal totalAmount) { this.totalAmount = totalAmount; }
    public String getCustomerName() { return customerName; }
    public void setCustomerName(String customerName) { this.customerName = customerName; }
}'''
    },
    {
        'id': 18,
        'expected': 'DataClass',
        'description': 'Appointment entity',
        'code': '''
public class Appointment {
    private Long id;
    private LocalDateTime appointmentTime;
    private String patientName;
    private String doctorName;
    private String reason;
    
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public LocalDateTime getAppointmentTime() { return appointmentTime; }
    public void setAppointmentTime(LocalDateTime appointmentTime) { this.appointmentTime = appointmentTime; }
    public String getPatientName() { return patientName; }
    public void setPatientName(String patientName) { this.patientName = patientName; }
    public String getDoctorName() { return doctorName; }
    public void setDoctorName(String doctorName) { this.doctorName = doctorName; }
    public String getReason() { return reason; }
    public void setReason(String reason) { this.reason = reason; }
}'''
    },
    {
        'id': 19,
        'expected': 'DataClass',
        'description': 'Restaurant table data',
        'code': '''
public class RestaurantTable {
    private int tableNumber;
    private int capacity;
    private String location;
    private boolean isReserved;
    
    public int getTableNumber() { return tableNumber; }
    public void setTableNumber(int tableNumber) { this.tableNumber = tableNumber; }
    public int getCapacity() { return capacity; }
    public void setCapacity(int capacity) { this.capacity = capacity; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public boolean isReserved() { return isReserved; }
    public void setReserved(boolean reserved) { isReserved = reserved; }
}'''
    },
    {
        'id': 20,
        'expected': 'DataClass',
        'description': 'Shipment tracking info',
        'code': '''
public class ShipmentInfo {
    private String trackingNumber;
    private String origin;
    private String destination;
    private LocalDate estimatedDelivery;
    private String status;
    
    public String getTrackingNumber() { return trackingNumber; }
    public void setTrackingNumber(String trackingNumber) { this.trackingNumber = trackingNumber; }
    public String getOrigin() { return origin; }
    public void setOrigin(String origin) { this.origin = origin; }
    public String getDestination() { return destination; }
    public void setDestination(String destination) { this.destination = destination; }
    public LocalDate getEstimatedDelivery() { return estimatedDelivery; }
    public void setEstimatedDelivery(LocalDate estimatedDelivery) { this.estimatedDelivery = estimatedDelivery; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}'''
    },
    {
        'id': 21,
        'expected': 'DataClass',
        'description': 'Course enrollment record',
        'code': '''
public class CourseEnrollment {
    private Long enrollmentId;
    private String studentId;
    private String courseId;
    private LocalDate enrollmentDate;
    private String semester;
    
    public Long getEnrollmentId() { return enrollmentId; }
    public void setEnrollmentId(Long enrollmentId) { this.enrollmentId = enrollmentId; }
    public String getStudentId() { return studentId; }
    public void setStudentId(String studentId) { this.studentId = studentId; }
    public String getCourseId() { return courseId; }
    public void setCourseId(String courseId) { this.courseId = courseId; }
    public LocalDate getEnrollmentDate() { return enrollmentDate; }
    public void setEnrollmentDate(LocalDate enrollmentDate) { this.enrollmentDate = enrollmentDate; }
    public String getSemester() { return semester; }
    public void setSemester(String semester) { this.semester = semester; }
}'''
    },
    {
        'id': 22,
        'expected': 'DataClass',
        'description': 'Credit card details',
        'code': '''
public class CreditCardDetails {
    private String cardNumber;
    private String cardHolderName;
    private String expiryDate;
    private String cvv;
    private String billingAddress;
    
    public String getCardNumber() { return cardNumber; }
    public void setCardNumber(String cardNumber) { this.cardNumber = cardNumber; }
    public String getCardHolderName() { return cardHolderName; }
    public void setCardHolderName(String cardHolderName) { this.cardHolderName = cardHolderName; }
    public String getExpiryDate() { return expiryDate; }
    public void setExpiryDate(String expiryDate) { this.expiryDate = expiryDate; }
    public String getCvv() { return cvv; }
    public void setCvv(String cvv) { this.cvv = cvv; }
    public String getBillingAddress() { return billingAddress; }
    public void setBillingAddress(String billingAddress) { this.billingAddress = billingAddress; }
}'''
    },
    {
        'id': 23,
        'expected': 'DataClass',
        'description': 'Sensor reading data',
        'code': '''
public class SensorReading {
    private Long readingId;
    private String sensorId;
    private double temperature;
    private double humidity;
    private LocalDateTime timestamp;
    
    public Long getReadingId() { return readingId; }
    public void setReadingId(Long readingId) { this.readingId = readingId; }
    public String getSensorId() { return sensorId; }
    public void setSensorId(String sensorId) { this.sensorId = sensorId; }
    public double getTemperature() { return temperature; }
    public void setTemperature(double temperature) { this.temperature = temperature; }
    public double getHumidity() { return humidity; }
    public void setHumidity(double humidity) { this.humidity = humidity; }
    public LocalDateTime getTimestamp() { return timestamp; }
    public void setTimestamp(LocalDateTime timestamp) { this.timestamp = timestamp; }
}'''
    },
    {
        'id': 24,
        'expected': 'DataClass',
        'description': 'Job application bean',
        'code': '''
public class JobApplication {
    private Long applicationId;
    private String applicantName;
    private String position;
    private LocalDate applicationDate;
    private String status;
    
    public Long getApplicationId() { return applicationId; }
    public void setApplicationId(Long applicationId) { this.applicationId = applicationId; }
    public String getApplicantName() { return applicantName; }
    public void setApplicantName(String applicantName) { this.applicantName = applicantName; }
    public String getPosition() { return position; }
    public void setPosition(String position) { this.position = position; }
    public LocalDate getApplicationDate() { return applicationDate; }
    public void setApplicationDate(LocalDate applicationDate) { this.applicationDate = applicationDate; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}'''
    },
    {
        'id': 25,
        'expected': 'DataClass',
        'description': 'Transaction record',
        'code': '''
public class TransactionRecord {
    private String transactionId;
    private BigDecimal amount;
    private String currency;
    private LocalDateTime transactionTime;
    private String transactionType;
    
    public String getTransactionId() { return transactionId; }
    public void setTransactionId(String transactionId) { this.transactionId = transactionId; }
    public BigDecimal getAmount() { return amount; }
    public void setAmount(BigDecimal amount) { this.amount = amount; }
    public String getCurrency() { return currency; }
    public void setCurrency(String currency) { this.currency = currency; }
    public LocalDateTime getTransactionTime() { return transactionTime; }
    public void setTransactionTime(LocalDateTime transactionTime) { this.transactionTime = transactionTime; }
    public String getTransactionType() { return transactionType; }
    public void setTransactionType(String transactionType) { this.transactionType = transactionType; }
}'''
    },
    {
        'id': 26,
        'expected': 'DataClass',
        'description': 'Insurance policy DTO',
        'code': '''
public class InsurancePolicy {
    private String policyNumber;
    private String policyHolderName;
    private String coverageType;
    private BigDecimal premium;
    private LocalDate expiryDate;
    
    public String getPolicyNumber() { return policyNumber; }
    public void setPolicyNumber(String policyNumber) { this.policyNumber = policyNumber; }
    public String getPolicyHolderName() { return policyHolderName; }
    public void setPolicyHolderName(String policyHolderName) { this.policyHolderName = policyHolderName; }
    public String getCoverageType() { return coverageType; }
    public void setCoverageType(String coverageType) { this.coverageType = coverageType; }
    public BigDecimal getPremium() { return premium; }
    public void setPremium(BigDecimal premium) { this.premium = premium; }
    public LocalDate getExpiryDate() { return expiryDate; }
    public void setExpiryDate(LocalDate expiryDate) { this.expiryDate = expiryDate; }
}'''
    },
    {
        'id': 27,
        'expected': 'DataClass',
        'description': 'Parking spot info',
        'code': '''
public class ParkingSpot {
    private String spotId;
    private String level;
    private String zone;
    private boolean isOccupied;
    private String vehicleType;
    
    public String getSpotId() { return spotId; }
    public void setSpotId(String spotId) { this.spotId = spotId; }
    public String getLevel() { return level; }
    public void setLevel(String level) { this.level = level; }
    public String getZone() { return zone; }
    public void setZone(String zone) { this.zone = zone; }
    public boolean isOccupied() { return isOccupied; }
    public void setOccupied(boolean occupied) { isOccupied = occupied; }
    public String getVehicleType() { return vehicleType; }
    public void setVehicleType(String vehicleType) { this.vehicleType = vehicleType; }
}'''
    },
    {
        'id': 28,
        'expected': 'DataClass',
        'description': 'Lab test result',
        'code': '''
public class LabTestResult {
    private Long resultId;
    private String testName;
    private String patientId;
    private String resultValue;
    private LocalDateTime testDate;
    
    public Long getResultId() { return resultId; }
    public void setResultId(Long resultId) { this.resultId = resultId; }
    public String getTestName() { return testName; }
    public void setTestName(String testName) { this.testName = testName; }
    public String getPatientId() { return patientId; }
    public void setPatientId(String patientId) { this.patientId = patientId; }
    public String getResultValue() { return resultValue; }
    public void setResultValue(String resultValue) { this.resultValue = resultValue; }
    public LocalDateTime getTestDate() { return testDate; }
    public void setTestDate(LocalDateTime testDate) { this.testDate = testDate; }
}'''
    },
    {
        'id': 29,
        'expected': 'DataClass',
        'description': 'Subscription plan data',
        'code': '''
public class SubscriptionPlan {
    private String planId;
    private String planName;
    private BigDecimal monthlyPrice;
    private int features;
    private String billingCycle;
    
    public String getPlanId() { return planId; }
    public void setPlanId(String planId) { this.planId = planId; }
    public String getPlanName() { return planName; }
    public void setPlanName(String planName) { this.planName = planName; }
    public BigDecimal getMonthlyPrice() { return monthlyPrice; }
    public void setMonthlyPrice(BigDecimal monthlyPrice) { this.monthlyPrice = monthlyPrice; }
    public int getFeatures() { return features; }
    public void setFeatures(int features) { this.features = features; }
    public String getBillingCycle() { return billingCycle; }
    public void setBillingCycle(String billingCycle) { this.billingCycle = billingCycle; }
}'''
    },
    {
        'id': 30,
        'expected': 'DataClass',
        'description': 'Work schedule entry',
        'code': '''
public class WorkSchedule {
    private Long scheduleId;
    private String employeeId;
    private LocalDate workDate;
    private LocalTime startTime;
    private LocalTime endTime;
    
    public Long getScheduleId() { return scheduleId; }
    public void setScheduleId(Long scheduleId) { this.scheduleId = scheduleId; }
    public String getEmployeeId() { return employeeId; }
    public void setEmployeeId(String employeeId) { this.employeeId = employeeId; }
    public LocalDate getWorkDate() { return workDate; }
    public void setWorkDate(LocalDate workDate) { this.workDate = workDate; }
    public LocalTime getStartTime() { return startTime; }
    public void setStartTime(LocalTime startTime) { this.startTime = startTime; }
    public LocalTime getEndTime() { return endTime; }
    public void setEndTime(LocalTime endTime) { this.endTime = endTime; }
}'''
    },
    {
        'id': 31,
        'expected': 'DataClass',
        'description': 'Warehouse location',
        'code': '''
public class WarehouseLocation {
    private String locationCode;
    private String aisle;
    private String shelf;
    private String bin;
    private int capacity;
    
    public String getLocationCode() { return locationCode; }
    public void setLocationCode(String locationCode) { this.locationCode = locationCode; }
    public String getAisle() { return aisle; }
    public void setAisle(String aisle) { this.aisle = aisle; }
    public String getShelf() { return shelf; }
    public void setShelf(String shelf) { this.shelf = shelf; }
    public String getBin() { return bin; }
    public void setBin(String bin) { this.bin = bin; }
    public int getCapacity() { return capacity; }
    public void setCapacity(int capacity) { this.capacity = capacity; }
}'''
    },
    {
        'id': 32,
        'expected': 'DataClass',
        'description': 'Ticket reservation',
        'code': '''
public class TicketReservation {
    private String reservationId;
    private String eventName;
    private LocalDateTime eventDate;
    private String seatNumber;
    private BigDecimal price;
    
    public String getReservationId() { return reservationId; }
    public void setReservationId(String reservationId) { this.reservationId = reservationId; }
    public String getEventName() { return eventName; }
    public void setEventName(String eventName) { this.eventName = eventName; }
    public LocalDateTime getEventDate() { return eventDate; }
    public void setEventDate(LocalDateTime eventDate) { this.eventDate = eventDate; }
    public String getSeatNumber() { return seatNumber; }
    public void setSeatNumber(String seatNumber) { this.seatNumber = seatNumber; }
    public BigDecimal getPrice() { return price; }
    public void setPrice(BigDecimal price) { this.price = price; }
}'''
    },

    # ==================== Clean (16 cases) ====================
    {
        'id': 33,
        'expected': 'Clean',
        'description': 'Authentication service',
        'code': '''
public class AuthenticationService {
    private final TokenGenerator tokenGenerator;
    private final UserRepository userRepository;
    
    public AuthenticationService(TokenGenerator tokenGenerator, UserRepository userRepository) {
        this.tokenGenerator = tokenGenerator;
        this.userRepository = userRepository;
    }
    
    public AuthToken authenticate(String username, String password) {
        User user = userRepository.findByUsername(username);
        if (user != null && user.verifyPassword(password)) {
            return tokenGenerator.generate(user);
        }
        return null;
    }
}'''
    },
    {
        'id': 34,
        'expected': 'Clean',
        'description': 'Invoice calculator',
        'code': '''
public class InvoiceCalculator {
    private static final double TAX_RATE = 0.15;
    
    public double calculateTotal(List<LineItem> items) {
        double subtotal = items.stream()
            .mapToDouble(LineItem::getAmount)
            .sum();
        return subtotal * (1 + TAX_RATE);
    }
    
    public double calculateTax(List<LineItem> items) {
        double subtotal = calculateSubtotal(items);
        return subtotal * TAX_RATE;
    }
    
    private double calculateSubtotal(List<LineItem> items) {
        return items.stream().mapToDouble(LineItem::getAmount).sum();
    }
}'''
    },
    {
        'id': 35,
        'expected': 'Clean',
        'description': 'URL shortener',
        'code': '''
public class URLShortener {
    private final HashGenerator hashGenerator;
    
    public URLShortener(HashGenerator hashGenerator) {
        this.hashGenerator = hashGenerator;
    }
    
    public String shorten(String longUrl) {
        String hash = hashGenerator.generate(longUrl);
        return "https://short.url/" + hash;
    }
    
    public boolean isValidUrl(String url) {
        return url != null && url.matches("^https?://.*");
    }
}'''
    },
    {
        'id': 36,
        'expected': 'Clean',
        'description': 'Distance calculator',
        'code': '''
public class DistanceCalculator {
    private static final double EARTH_RADIUS_KM = 6371.0;
    
    public double calculateDistance(Coordinate point1, Coordinate point2) {
        double lat1 = Math.toRadians(point1.getLatitude());
        double lat2 = Math.toRadians(point2.getLatitude());
        double deltaLat = lat2 - lat1;
        double deltaLon = Math.toRadians(point2.getLongitude() - point1.getLongitude());
        
        double a = Math.sin(deltaLat / 2) * Math.sin(deltaLat / 2) +
                   Math.cos(lat1) * Math.cos(lat2) *
                   Math.sin(deltaLon / 2) * Math.sin(deltaLon / 2);
        
        return 2 * EARTH_RADIUS_KM * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    }
}'''
    },
    {
        'id': 37,
        'expected': 'Clean',
        'description': 'Text sanitizer',
        'code': '''
public class TextSanitizer {
    private final Set<String> prohibitedWords;
    
    public TextSanitizer(Set<String> prohibitedWords) {
        this.prohibitedWords = prohibitedWords;
    }
    
    public String sanitize(String input) {
        String result = input.trim().toLowerCase();
        for (String word : prohibitedWords) {
            result = result.replaceAll(word, "***");
        }
        return result;
    }
    
    public boolean containsProhibitedWords(String input) {
        return prohibitedWords.stream().anyMatch(input.toLowerCase()::contains);
    }
}'''
    },
    {
        'id': 38,
        'expected': 'Clean',
        'description': 'Retry handler',
        'code': '''
public class RetryHandler {
    private final int maxRetries;
    private final long delayMillis;
    
    public RetryHandler(int maxRetries, long delayMillis) {
        this.maxRetries = maxRetries;
        this.delayMillis = delayMillis;
    }
    
    public <T> T execute(Callable<T> operation) throws Exception {
        int attempts = 0;
        while (attempts < maxRetries) {
            try {
                return operation.call();
            } catch (Exception e) {
                attempts++;
                if (attempts >= maxRetries) throw e;
                Thread.sleep(delayMillis);
            }
        }
        throw new RuntimeException("Max retries exceeded");
    }
}'''
    },
    {
        'id': 39,
        'expected': 'Clean',
        'description': 'JSON serializer',
        'code': '''
public class JsonSerializer {
    private final ObjectMapper mapper;
    
    public JsonSerializer() {
        this.mapper = new ObjectMapper();
    }
    
    public String serialize(Object obj) throws JsonProcessingException {
        return mapper.writeValueAsString(obj);
    }
    
    public <T> T deserialize(String json, Class<T> clazz) throws JsonProcessingException {
        return mapper.readValue(json, clazz);
    }
}'''
    },
    {
        'id': 40,
        'expected': 'Clean',
        'description': 'Thread pool executor',
        'code': '''
public class ThreadPoolExecutor {
    private final ExecutorService executor;
    
    public ThreadPoolExecutor(int poolSize) {
        this.executor = Executors.newFixedThreadPool(poolSize);
    }
    
    public Future<?> submit(Runnable task) {
        return executor.submit(task);
    }
    
    public void shutdown() {
        executor.shutdown();
    }
    
    public boolean awaitTermination(long timeout, TimeUnit unit) throws InterruptedException {
        return executor.awaitTermination(timeout, unit);
    }
}'''
    },
    {
        'id': 41,
        'expected': 'Clean',
        'description': 'Rate limiter',
        'code': '''
public class RateLimiter {
    private final int maxRequests;
    private final long windowMillis;
    private final Map<String, Queue<Long>> requestTimestamps;
    
    public RateLimiter(int maxRequests, long windowMillis) {
        this.maxRequests = maxRequests;
        this.windowMillis = windowMillis;
        this.requestTimestamps = new ConcurrentHashMap<>();
    }
    
    public boolean allowRequest(String clientId) {
        long now = System.currentTimeMillis();
        Queue<Long> timestamps = requestTimestamps.computeIfAbsent(clientId, k -> new LinkedList<>());
        
        timestamps.removeIf(timestamp -> now - timestamp > windowMillis);
        
        if (timestamps.size() < maxRequests) {
            timestamps.add(now);
            return true;
        }
        return false;
    }
}'''
    },
    {
        'id': 42,
        'expected': 'Clean',
        'description': 'CSV parser',
        'code': '''
public class CSVParser {
    private final String delimiter;
    
    public CSVParser(String delimiter) {
        this.delimiter = delimiter;
    }
    
    public List<String[]> parse(String csvContent) {
        return Arrays.stream(csvContent.split("\\n"))
            .map(line -> line.split(delimiter))
            .collect(Collectors.toList());
    }
    
    public String[] parseHeaders(String csvContent) {
        String firstLine = csvContent.split("\\n")[0];
        return firstLine.split(delimiter);
    }
}'''
    },
    {
        'id': 43,
        'expected': 'Clean',
        'description': 'Color converter',
        'code': '''
public class ColorConverter {
    public String rgbToHex(int r, int g, int b) {
        return String.format("#%02x%02x%02x", r, g, b);
    }
    
    public int[] hexToRgb(String hex) {
        hex = hex.replace("#", "");
        return new int[] {
            Integer.parseInt(hex.substring(0, 2), 16),
            Integer.parseInt(hex.substring(2, 4), 16),
            Integer.parseInt(hex.substring(4, 6), 16)
        };
    }
}'''
    },
    {
        'id': 44,
        'expected': 'Clean',
        'description': 'Pagination helper',
        'code': '''
public class PaginationHelper {
    private final int pageSize;
    
    public PaginationHelper(int pageSize) {
        this.pageSize = pageSize;
    }
    
    public <T> List<T> getPage(List<T> items, int pageNumber) {
        int start = pageNumber * pageSize;
        int end = Math.min(start + pageSize, items.size());
        return items.subList(start, end);
    }
    
    public int getTotalPages(int totalItems) {
        return (int) Math.ceil((double) totalItems / pageSize);
    }
}'''
    },
    {
        'id': 45,
        'expected': 'Clean',
        'description': 'Markdown renderer',
        'code': '''
public class MarkdownRenderer {
    public String renderBold(String text) {
        return "<strong>" + text + "</strong>";
    }
    
    public String renderItalic(String text) {
        return "<em>" + text + "</em>";
    }
    
    public String renderLink(String text, String url) {
        return String.format("<a href=\"%s\">%s</a>", url, text);
    }
    
    public String renderCode(String code) {
        return "<code>" + code + "</code>";
    }
}'''
    },
    {
        'id': 46,
        'expected': 'Clean',
        'description': 'UUID generator',
        'code': '''
public class UUIDGenerator {
    private final SecureRandom random;
    
    public UUIDGenerator() {
        this.random = new SecureRandom();
    }
    
    public String generate() {
        return UUID.randomUUID().toString();
    }
    
    public String generateShort() {
        byte[] bytes = new byte[8];
        random.nextBytes(bytes);
        return Base64.getUrlEncoder().withoutPadding().encodeToString(bytes);
    }
}'''
    },
    {
        'id': 47,
        'expected': 'Clean',
        'description': 'Phone formatter',
        'code': '''
public class PhoneNumberFormatter {
    public String format(String phoneNumber) {
        String digits = phoneNumber.replaceAll("[^0-9]", "");
        if (digits.length() == 10) {
            return String.format("(%s) %s-%s", 
                digits.substring(0, 3),
                digits.substring(3, 6),
                digits.substring(6));
        }
        return phoneNumber;
    }
    
    public boolean isValid(String phoneNumber) {
        String digits = phoneNumber.replaceAll("[^0-9]", "");
        return digits.length() == 10;
    }
}'''
    },
    {
        'id': 48,
        'expected': 'Clean',
        'description': 'Circuit breaker',
        'code': '''
public class CircuitBreaker {
    private final int threshold;
    private int failureCount;
    private boolean isOpen;
    
    public CircuitBreaker(int threshold) {
        this.threshold = threshold;
        this.failureCount = 0;
        this.isOpen = false;
    }
    
    public <T> T execute(Callable<T> operation) throws Exception {
        if (isOpen) {
            throw new RuntimeException("Circuit is open");
        }
        try {
            T result = operation.call();
            reset();
            return result;
        } catch (Exception e) {
            recordFailure();
            throw e;
        }
    }
    
    private void recordFailure() {
        failureCount++;
        if (failureCount >= threshold) {
            isOpen = true;
        }
    }
    
    private void reset() {
        failureCount = 0;
        isOpen = false;
    }
}'''
    },

    # ==================== LongMethod (16 cases) ====================
    {
        'id': 49,
        'expected': 'LongMethod',
        'description': 'Complex order fulfillment',
        'code': '''
public class OrderFulfillment {
    public void fulfillOrder(Order order) {
        if (order == null || order.getItems() == null) {
            throw new IllegalArgumentException("Invalid order");
        }
        
        double total = 0;
        for (OrderItem item : order.getItems()) {
            total += item.getPrice() * item.getQuantity();
        }
        
        if (order.getDiscountCode() != null) {
            double discount = calculateDiscount(order.getDiscountCode());
            total = total * (1 - discount);
        }
        
        double tax = total * 0.08;
        total += tax;
        
        if (total > 100) {
            order.setShippingCost(0);
        } else {
            order.setShippingCost(10);
        }
        total += order.getShippingCost();
        
        for (OrderItem item : order.getItems()) {
            if (getStock(item.getProductId()) < item.getQuantity()) {
                throw new RuntimeException("Insufficient stock");
            }
            reduceStock(item.getProductId(), item.getQuantity());
        }
        
        Payment payment = new Payment();
        payment.setAmount(total);
        payment.setOrderId(order.getId());
        processPayment(payment);
        
        order.setStatus("FULFILLED");
        order.setTotal(total);
        saveOrder(order);
        
        sendConfirmationEmail(order);
        updateAnalytics(order);
    }
}'''
    },
    {
        'id': 50,
        'expected': 'LongMethod',
        'description': 'Student grade processor',
        'code': '''
public class GradeProcessor {
    public void processGrades(Student student, List<Assignment> assignments) {
        double totalScore = 0;
        int totalWeight = 0;
        
        for (Assignment assignment : assignments) {
            if (assignment.getSubmission() != null) {
                double score = assignment.getSubmission().getScore();
                int weight = assignment.getWeight();
                totalScore += score * weight;
                totalWeight += weight;
            }
        }
        
        double average = totalWeight > 0 ? totalScore / totalWeight : 0;
        
        String letterGrade;
        if (average >= 90) {
            letterGrade = "A";
        } else if (average >= 80) {
            letterGrade = "B";
        } else if (average >= 70) {
            letterGrade = "C";
        } else if (average >= 60) {
            letterGrade = "D";
        } else {
            letterGrade = "F";
        }
        
        student.setGrade(letterGrade);
        student.setGPA(calculateGPA(letterGrade));
        
        if (letterGrade.equals("F")) {
            sendFailureNotification(student);
            createRemediationPlan(student);
        } else if (average >= 95) {
            nominateForHonors(student);
        }
        
        saveStudent(student);
        updateTranscript(student);
        notifyParents(student);
        logGradeChange(student, letterGrade);
    }
}'''
    },
    {
        'id': 51,
        'expected': 'LongMethod',
        'description': 'Reservation system handler',
        'code': '''
public class ReservationHandler {
    public void createReservation(ReservationRequest request) {
        if (request.getStartDate() == null || request.getEndDate() == null) {
            throw new IllegalArgumentException("Dates required");
        }
        
        if (request.getStartDate().isAfter(request.getEndDate())) {
            throw new IllegalArgumentException("Invalid date range");
        }
        
        List<Room> availableRooms = findAvailableRooms(request.getStartDate(), request.getEndDate());
        
        if (availableRooms.isEmpty()) {
            throw new RuntimeException("No rooms available");
        }
        
        Room selectedRoom = null;
        for (Room room : availableRooms) {
            if (room.getCapacity() >= request.getGuestCount() && 
                room.getType().equals(request.getRoomType())) {
                selectedRoom = room;
                break;
            }
        }
        
        if (selectedRoom == null) {
            throw new RuntimeException("No suitable room found");
        }
        
        long days = ChronoUnit.DAYS.between(request.getStartDate(), request.getEndDate());
        double totalCost = days * selectedRoom.getPricePerNight();
        
        if (request.getCustomer().isVIP()) {
            totalCost *= 0.9;
        }
        
        Reservation reservation = new Reservation();
        reservation.setRoom(selectedRoom);
        reservation.setCustomer(request.getCustomer());
        reservation.setStartDate(request.getStartDate());
        reservation.setEndDate(request.getEndDate());
        reservation.setTotalCost(totalCost);
        reservation.setStatus("CONFIRMED");
        
        saveReservation(reservation);
        blockRoom(selectedRoom, request.getStartDate(), request.getEndDate());
        sendConfirmation(reservation);
        updateLoyaltyPoints(request.getCustomer(), totalCost);
    }
}'''
    },
    {
        'id': 52,
        'expected': 'LongMethod',
        'description': 'Insurance claim processor',
        'code': '''
public class ClaimProcessor {
    public void processClaim(Claim claim) {
        if (claim.getPolicyNumber() == null) {
            throw new IllegalArgumentException("Policy number required");
        }
        
        Policy policy = findPolicy(claim.getPolicyNumber());
        if (policy == null) {
            claim.setStatus("REJECTED");
            claim.setReason("Policy not found");
            saveClaim(claim);
            return;
        }
        
        if (!policy.isActive()) {
            claim.setStatus("REJECTED");
            claim.setReason("Policy inactive");
            saveClaim(claim);
            return;
        }
        
        if (claim.getAmount() > policy.getCoverageLimit()) {
            claim.setStatus("REJECTED");
            claim.setReason("Amount exceeds coverage");
            saveClaim(claim);
            return;
        }
        
        double deductible = policy.getDeductible();
        double approvedAmount = claim.getAmount() - deductible;
        
        if (approvedAmount <= 0) {
            claim.setStatus("REJECTED");
            claim.setReason("Amount below deductible");
            saveClaim(claim);
            return;
        }
        
        if (claim.getAmount() > 10000) {
            claim.setStatus("UNDER_REVIEW");
            assignToReviewer(claim);
            sendReviewNotification(claim);
        } else {
            claim.setStatus("APPROVED");
            claim.setApprovedAmount(approvedAmount);
            initiatePayment(claim);
        }
        
        saveClaim(claim);
        updatePolicyUsage(policy, approvedAmount);
        sendNotification(claim.getCustomerId(), claim.getStatus());
    }
}'''
    },
    {
        'id': 53,
        'expected': 'LongMethod',
        'description': 'Loan application validator',
        'code': '''
public class LoanValidator {
    public void validateLoanApplication(LoanApplication app) {
        if (app.getApplicant() == null) {
            throw new IllegalArgumentException("Applicant required");
        }
        
        if (app.getAmount() <= 0) {
            app.setStatus("REJECTED");
            app.setReason("Invalid amount");
            return;
        }
        
        if (app.getAmount() > 1000000) {
            app.setStatus("REJECTED");
            app.setReason("Amount exceeds limit");
            return;
        }
        
        int creditScore = getCreditScore(app.getApplicant().getSocialSecurityNumber());
        
        if (creditScore < 600) {
            app.setStatus("REJECTED");
            app.setReason("Credit score too low");
            return;
        }
        
        double income = app.getApplicant().getAnnualIncome();
        double dtiRatio = calculateDebtToIncome(app.getApplicant());
        
        if (dtiRatio > 0.43) {
            app.setStatus("REJECTED");
            app.setReason("DTI ratio too high");
            return;
        }
        
        double maxLoan = income * 4;
        if (app.getAmount() > maxLoan) {
            app.setStatus("REJECTED");
            app.setReason("Loan amount too high for income");
            return;
        }
        
        if (creditScore >= 750 && dtiRatio < 0.3) {
            app.setInterestRate(3.5);
            app.setStatus("APPROVED");
        } else if (creditScore >= 700) {
            app.setInterestRate(4.5);
            app.setStatus("APPROVED");
        } else {
            app.setInterestRate(6.0);
            app.setStatus("CONDITIONAL");
        }
        
        saveLoanApplication(app);
        sendNotification(app);
    }
}'''
    },
    {
        'id': 54,
        'expected': 'LongMethod',
        'description': 'Product inventory sync',
        'code': '''
public class InventorySync {
    public void syncInventory(List<Product> products) {
        for (Product product : products) {
            if (product.getSku() == null) {
                logError("Product missing SKU");
                continue;
            }
            
            Product existing = findBySku(product.getSku());
            
            if (existing == null) {
                product.setCreatedDate(LocalDate.now());
                product.setUpdatedDate(LocalDate.now());
                saveProduct(product);
                logInfo("Created product: " + product.getSku());
            } else {
                if (!existing.getName().equals(product.getName())) {
                    existing.setName(product.getName());
                    existing.setUpdatedDate(LocalDate.now());
                }
                
                if (existing.getPrice() != product.getPrice()) {
                    createPriceHistory(existing, product.getPrice());
                    existing.setPrice(product.getPrice());
                    existing.setUpdatedDate(LocalDate.now());
                }
                
                if (existing.getQuantity() != product.getQuantity()) {
                    int difference = product.getQuantity() - existing.getQuantity();
                    createInventoryTransaction(existing, difference);
                    existing.setQuantity(product.getQuantity());
                    existing.setUpdatedDate(LocalDate.now());
                    
                    if (product.getQuantity() < 10) {
                        sendLowStockAlert(product);
                    }
                }
                
                updateProduct(existing);
                logInfo("Updated product: " + product.getSku());
            }
        }
        
        updateLastSyncTime();
        generateSyncReport();
    }
}'''
    },
    {
        'id': 55,
        'expected': 'LongMethod',
        'description': 'Tournament bracket generator',
        'code': '''
public class BracketGenerator {
    public void generateBracket(Tournament tournament) {
        List<Team> teams = tournament.getTeams();
        
        if (teams.size() < 2) {
            throw new IllegalArgumentException("Need at least 2 teams");
        }
        
        teams.sort((t1, t2) -> Integer.compare(t2.getSeedRating(), t1.getSeedRating()));
        
        int rounds = (int) Math.ceil(Math.log(teams.size()) / Math.log(2));
        int totalSlots = (int) Math.pow(2, rounds);
        
        List<Team> bracket = new ArrayList<>(totalSlots);
        for (int i = 0; i < totalSlots; i++) {
            if (i < teams.size()) {
                bracket.add(teams.get(i));
            } else {
                bracket.add(null);
            }
        }
        
        List<Match> matches = new ArrayList<>();
        for (int round = 1; round <= rounds; round++) {
            int matchesInRound = totalSlots / (int) Math.pow(2, round);
            for (int i = 0; i < matchesInRound; i++) {
                Match match = new Match();
                match.setRound(round);
                match.setMatchNumber(i + 1);
                
                if (round == 1) {
                    int index1 = i * 2;
                    int index2 = i * 2 + 1;
                    match.setTeam1(bracket.get(index1));
                    match.setTeam2(bracket.get(index2));
                }
                
                matches.add(match);
            }
        }
        
        tournament.setMatches(matches);
        tournament.setStatus("BRACKET_GENERATED");
        saveTournament(tournament);
        notifyTeams(tournament);
    }
}'''
    },
    {
        'id': 56,
        'expected': 'LongMethod',
        'description': 'Shipping rate calculator',
        'code': '''
public class ShippingCalculator {
    public double calculateShipping(Order order, Address destination) {
        double weight = 0;
        for (OrderItem item : order.getItems()) {
            weight += item.getWeight() * item.getQuantity();
        }
        
        double distance = calculateDistance(order.getOrigin(), destination);
        
        double baseRate;
        if (weight <= 1) {
            baseRate = 5.0;
        } else if (weight <= 5) {
            baseRate = 10.0;
        } else if (weight <= 10) {
            baseRate = 20.0;
        } else {
            baseRate = 30.0;
        }
        
        double distanceMultiplier;
        if (distance <= 100) {
            distanceMultiplier = 1.0;
        } else if (distance <= 500) {
            distanceMultiplier = 1.5;
        } else if (distance <= 1000) {
            distanceMultiplier = 2.0;
        } else {
            distanceMultiplier = 3.0;
        }
        
        double shippingCost = baseRate * distanceMultiplier;
        
        if (order.getShippingSpeed().equals("EXPRESS")) {
            shippingCost *= 2.0;
        } else if (order.getShippingSpeed().equals("OVERNIGHT")) {
            shippingCost *= 3.0;
        }
        
        if (destination.isRemote()) {
            shippingCost += 15.0;
        }
        
        if (order.getCustomer().isPremium()) {
            shippingCost *= 0.8;
        }
        
        if (order.getTotal() > 100) {
            shippingCost = Math.max(0, shippingCost - 10);
        }
        
        return Math.round(shippingCost * 100.0) / 100.0;
    }
}'''
    },
    {
        'id': 57,
        'expected': 'LongMethod',
        'description': 'Contract renewal processor',
        'code': '''
public class ContractRenewal {
    public void processRenewal(Contract contract) {
        if (contract.getEndDate().isBefore(LocalDate.now())) {
            contract.setStatus("EXPIRED");
            saveContract(contract);
            return;
        }
        
        long daysUntilExpiry = ChronoUnit.DAYS.between(LocalDate.now(), contract.getEndDate());
        
        if (daysUntilExpiry > 90) {
            return;
        }
        
        if (daysUntilExpiry <= 30 && !contract.isRenewalNoticeSent()) {
            sendRenewalNotice(contract);
            contract.setRenewalNoticeSent(true);
            saveContract(contract);
        }
        
        if (contract.isAutoRenew()) {
            Contract newContract = new Contract();
            newContract.setCustomerId(contract.getCustomerId());
            newContract.setStartDate(contract.getEndDate().plusDays(1));
            newContract.setEndDate(contract.getEndDate().plusYears(1));
            
            double newPrice = contract.getPrice();
            if (contract.getCustomer().isLongTermCustomer()) {
                newPrice *= 0.95;
            } else {
                newPrice *= 1.05;
            }
            
            newContract.setPrice(newPrice);
            newContract.setStatus("ACTIVE");
            newContract.setAutoRenew(contract.isAutoRenew());
            
            saveContract(newContract);
            
            contract.setStatus("RENEWED");
            contract.setRenewalContractId(newContract.getId());
            saveContract(contract);
            
            sendRenewalConfirmation(contract.getCustomerId(), newContract);
            updateBilling(newContract);
        }
    }
}'''
    },
    {
        'id': 58,
        'expected': 'LongMethod',
        'description': 'Medical prescription validator',
        'code': '''
public class PrescriptionValidator {
    public void validatePrescription(Prescription prescription) {
        if (prescription.getPatientId() == null || prescription.getDoctorId() == null) {
            throw new IllegalArgumentException("Patient and doctor required");
        }
        
        Patient patient = findPatient(prescription.getPatientId());
        if (patient == null) {
            prescription.setStatus("INVALID");
            prescription.setReason("Patient not found");
            return;
        }
        
        Doctor doctor = findDoctor(prescription.getDoctorId());
        if (doctor == null || !doctor.isLicensed()) {
            prescription.setStatus("INVALID");
            prescription.setReason("Doctor not authorized");
            return;
        }
        
        Medication medication = findMedication(prescription.getMedicationId());
        if (medication == null) {
            prescription.setStatus("INVALID");
            prescription.setReason("Medication not found");
            return;
        }
        
        if (medication.isControlled() && !doctor.hasControlledSubstanceLicense()) {
            prescription.setStatus("INVALID");
            prescription.setReason("Doctor not authorized for controlled substances");
            return;
        }
        
        List<Allergy> allergies = getPatientAllergies(patient.getId());
        for (Allergy allergy : allergies) {
            if (medication.getIngredients().contains(allergy.getAllergen())) {
                prescription.setStatus("INVALID");
                prescription.setReason("Patient allergic to ingredient");
                sendAllergyAlert(patient, medication);
                return;
            }
        }
        
        List<Prescription> currentMedications = getCurrentPrescriptions(patient.getId());
        for (Prescription current : currentMedications) {
            if (hasInteraction(medication, current.getMedication())) {
                prescription.setStatus("REQUIRES_REVIEW");
                prescription.setReason("Drug interaction detected");
                alertDoctor(doctor, prescription);
                return;
            }
        }
        
        prescription.setStatus("VALID");
        savePrescription(prescription);
        sendToPharmacy(prescription);
    }
}'''
    },
    {
        'id': 59,
        'expected': 'LongMethod',
        'description': 'Event scheduler with conflicts',
        'code': '''
public class EventScheduler {
    public void scheduleEvent(Event event) {
        if (event.getStartTime() == null || event.getEndTime() == null) {
            throw new IllegalArgumentException("Event times required");
        }
        
        if (event.getStartTime().isAfter(event.getEndTime())) {
            throw new IllegalArgumentException("Invalid time range");
        }
        
        List<Event> conflicts = findConflictingEvents(event.getStartTime(), event.getEndTime(), event.getVenueId());
        
        if (!conflicts.isEmpty()) {
            event.setStatus("CONFLICT");
            for (Event conflict : conflicts) {
                createConflictNotification(event, conflict);
            }
            saveEvent(event);
            return;
        }
        
        Venue venue = findVenue(event.getVenueId());
        if (venue == null) {
            event.setStatus("REJECTED");
            event.setReason("Venue not found");
            saveEvent(event);
            return;
        }
        
        if (event.getAttendeeCount() > venue.getCapacity()) {
            event.setStatus("REJECTED");
            event.setReason("Exceeds venue capacity");
            saveEvent(event);
            return;
        }
        
        double cost = calculateEventCost(event, venue);
        event.setCost(cost);
        
        if (event.isRecurring()) {
            List<LocalDateTime> occurrences = generateOccurrences(event.getStartTime(), event.getRecurrencePattern(), event.getRecurrenceEnd());
            for (LocalDateTime occurrence : occurrences) {
                Event recurring = cloneEvent(event);
                recurring.setStartTime(occurrence);
                recurring.setEndTime(occurrence.plusHours(ChronoUnit.HOURS.between(event.getStartTime(), event.getEndTime())));
                saveEvent(recurring);
            }
        }
        
        event.setStatus("SCHEDULED");
        saveEvent(event);
        reserveVenue(venue, event);
        sendInvitations(event);
    }
}'''
    },
    {
        'id': 60,
        'expected': 'LongMethod',
        'description': 'Tax calculation with deductions',
        'code': '''
public class TaxCalculator {
    public double calculateTax(TaxReturn taxReturn) {
        double income = taxReturn.getGrossIncome();
        
        double standardDeduction = 12000;
        if (taxReturn.getFilingStatus().equals("MARRIED")) {
            standardDeduction = 24000;
        } else if (taxReturn.getFilingStatus().equals("HEAD_OF_HOUSEHOLD")) {
            standardDeduction = 18000;
        }
        
        double itemizedDeductions = 0;
        for (Deduction deduction : taxReturn.getDeductions()) {
            if (deduction.getType().equals("MORTGAGE_INTEREST")) {
                itemizedDeductions += Math.min(deduction.getAmount(), 10000);
            } else if (deduction.getType().equals("CHARITABLE")) {
                itemizedDeductions += deduction.getAmount();
            } else if (deduction.getType().equals("MEDICAL")) {
                double threshold = income * 0.075;
                if (deduction.getAmount() > threshold) {
                    itemizedDeductions += deduction.getAmount() - threshold;
                }
            }
        }
        
        double totalDeduction = Math.max(standardDeduction, itemizedDeductions);
        double taxableIncome = Math.max(0, income - totalDeduction);
        
        double tax = 0;
        if (taxableIncome <= 10000) {
            tax = taxableIncome * 0.10;
        } else if (taxableIncome <= 40000) {
            tax = 1000 + (taxableIncome - 10000) * 0.12;
        } else if (taxableIncome <= 85000) {
            tax = 4600 + (taxableIncome - 40000) * 0.22;
        } else {
            tax = 14500 + (taxableIncome - 85000) * 0.24;
        }
        
        for (Credit credit : taxReturn.getCredits()) {
            tax -= credit.getAmount();
        }
        
        tax = Math.max(0, tax);
        
        double withheld = taxReturn.getWithheldAmount();
        if (withheld > tax) {
            taxReturn.setRefund(withheld - tax);
        } else {
            taxReturn.setAmountDue(tax - withheld);
        }
        
        return tax;
    }
}'''
    },
    {
        'id': 61,
        'expected': 'LongMethod',
        'description': 'Subscription billing handler',
        'code': '''
public class SubscriptionBilling {
    public void processBilling(Subscription subscription) {
        if (subscription.getStatus().equals("CANCELLED")) {
            return;
        }
        
        LocalDate lastBillingDate = subscription.getLastBillingDate();
        LocalDate today = LocalDate.now();
        
        if (lastBillingDate == null) {
            lastBillingDate = subscription.getStartDate();
        }
        
        LocalDate nextBillingDate = lastBillingDate;
        if (subscription.getBillingCycle().equals("MONTHLY")) {
            nextBillingDate = lastBillingDate.plusMonths(1);
        } else if (subscription.getBillingCycle().equals("QUARTERLY")) {
            nextBillingDate = lastBillingDate.plusMonths(3);
        } else if (subscription.getBillingCycle().equals("YEARLY")) {
            nextBillingDate = lastBillingDate.plusYears(1);
        }
        
        if (today.isBefore(nextBillingDate)) {
            return;
        }
        
        Customer customer = findCustomer(subscription.getCustomerId());
        PaymentMethod paymentMethod = customer.getDefaultPaymentMethod();
        
        if (paymentMethod == null) {
            subscription.setStatus("PAYMENT_FAILED");
            sendPaymentMethodRequiredEmail(customer);
            saveSubscription(subscription);
            return;
        }
        
        double amount = subscription.getPrice();
        
        if (subscription.getPromoCode() != null) {
            PromoCode promo = findPromoCode(subscription.getPromoCode());
            if (promo != null && promo.isValid()) {
                if (promo.getDiscountType().equals("PERCENTAGE")) {
                    amount *= (1 - promo.getDiscountValue() / 100.0);
                } else {
                    amount -= promo.getDiscountValue();
                }
            }
        }
        
        Payment payment = new Payment();
        payment.setAmount(amount);
        payment.setPaymentMethod(paymentMethod);
        payment.setCustomerId(customer.getId());
        
        boolean success = processPayment(payment);
        
        if (success) {
            subscription.setLastBillingDate(today);
            subscription.setStatus("ACTIVE");
            sendInvoice(customer, payment);
        } else {
            subscription.setFailedPaymentCount(subscription.getFailedPaymentCount() + 1);
            if (subscription.getFailedPaymentCount() >= 3) {
                subscription.setStatus("SUSPENDED");
            }
            sendPaymentFailedEmail(customer);
        }
        
        saveSubscription(subscription);
    }
}'''
    },
    {
        'id': 62,
        'expected': 'LongMethod',
        'description': 'Exam result calculator',
        'code': '''
public class ExamResultProcessor {
    public void processExamResults(Exam exam, List<Answer> answers) {
        int totalQuestions = exam.getQuestions().size();
        int correctAnswers = 0;
        int partialCredit = 0;
        
        for (Answer answer : answers) {
            Question question = findQuestion(exam, answer.getQuestionId());
            
            if (question.getType().equals("MULTIPLE_CHOICE")) {
                if (answer.getSelectedOption().equals(question.getCorrectAnswer())) {
                    correctAnswers++;
                }
            } else if (question.getType().equals("TRUE_FALSE")) {
                if (answer.getSelectedOption().equals(question.getCorrectAnswer())) {
                    correctAnswers++;
                }
            } else if (question.getType().equals("MULTIPLE_SELECT")) {
                Set<String> selected = answer.getSelectedOptions();
                Set<String> correct = question.getCorrectAnswers();
                if (selected.equals(correct)) {
                    correctAnswers++;
                } else {
                    int matching = 0;
                    for (String option : selected) {
                        if (correct.contains(option)) {
                            matching++;
                        }
                    }
                    partialCredit += (matching * 50) / correct.size();
                }
            }
        }
        
        double score = ((correctAnswers * 100.0) + partialCredit) / totalQuestions;
        
        String grade;
        if (score >= 90) {
            grade = "A";
        } else if (score >= 80) {
            grade = "B";
        } else if (score >= 70) {
            grade = "C";
        } else if (score >= 60) {
            grade = "D";
        } else {
            grade = "F";
        }
        
        ExamResult result = new ExamResult();
        result.setExamId(exam.getId());
        result.setStudentId(exam.getStudentId());
        result.setScore(score);
        result.setGrade(grade);
        result.setCorrectAnswers(correctAnswers);
        result.setTotalQuestions(totalQuestions);
        
        saveExamResult(result);
        updateStudentGrade(exam.getStudentId(), exam.getCourseId(), grade);
        sendResultNotification(exam.getStudentId(), result);
        
        if (grade.equals("F")) {
            scheduleRetakeExam(exam.getStudentId(), exam.getId());
        }
    }
}'''
    },
    {
        'id': 63,
        'expected': 'LongMethod',
        'description': 'Supply chain reorder handler',
        'code': '''
public class ReorderHandler {
    public void checkAndReorder(Product product) {
        int currentStock = product.getQuantity();
        int reorderPoint = product.getReorderPoint();
        
        if (currentStock > reorderPoint) {
            return;
        }
        
        int averageDailySales = calculateAverageDailySales(product, 30);
        int leadTimeDays = product.getSupplier().getLeadTimeDays();
        int safetyStock = averageDailySales * 7;
        
        int optimalOrderQuantity = (averageDailySales * leadTimeDays) + safetyStock - currentStock;
        
        if (product.getMinOrderQuantity() > 0 && optimalOrderQuantity < product.getMinOrderQuantity()) {
            optimalOrderQuantity = product.getMinOrderQuantity();
        }
        
        if (product.getOrderMultiple() > 0) {
            optimalOrderQuantity = ((optimalOrderQuantity + product.getOrderMultiple() - 1) / product.getOrderMultiple()) * product.getOrderMultiple();
        }
        
        double totalCost = optimalOrderQuantity * product.getSupplierPrice();
        
        if (totalCost > 10000) {
            createApprovalRequest(product, optimalOrderQuantity, totalCost);
            return;
        }
        
        PurchaseOrder po = new PurchaseOrder();
        po.setProductId(product.getId());
        po.setSupplierId(product.getSupplier().getId());
        po.setQuantity(optimalOrderQuantity);
        po.setUnitPrice(product.getSupplierPrice());
        po.setTotalCost(totalCost);
        po.setExpectedDeliveryDate(LocalDate.now().plusDays(leadTimeDays));
        po.setStatus("PENDING");
        
        savePurchaseOrder(po);
        sendPOToSupplier(po);
        updateReorderHistory(product, optimalOrderQuantity);
        notifyWarehouse(po);
    }
}'''
    },
    {
        'id': 64,
        'expected': 'LongMethod',
        'description': 'Performance review calculator',
        'code': '''
public class PerformanceReview {
    public void calculatePerformanceScore(Employee employee, ReviewPeriod period) {
        List<Goal> goals = getGoalsForPeriod(employee.getId(), period);
        
        double goalScore = 0;
        for (Goal goal : goals) {
            if (goal.getStatus().equals("COMPLETED")) {
                goalScore += goal.getWeight();
            } else if (goal.getStatus().equals("PARTIALLY_COMPLETED")) {
                goalScore += goal.getWeight() * goal.getCompletionPercentage() / 100.0;
            }
        }
        
        List<Competency> competencies = getCompetencies(employee.getRole());
        double competencyScore = 0;
        
        for (Competency competency : competencies) {
            Rating rating = getRating(employee.getId(), competency.getId(), period);
            if (rating != null) {
                competencyScore += rating.getScore() * competency.getWeight();
            }
        }
        
        List<Feedback> feedback = getPeerFeedback(employee.getId(), period);
        double peerScore = 0;
        
        for (Feedback fb : feedback) {
            peerScore += fb.getRating();
        }
        if (!feedback.isEmpty()) {
            peerScore /= feedback.size();
        }
        
        double attendanceScore = calculateAttendanceScore(employee, period);
        
        double totalScore = (goalScore * 0.4) + (competencyScore * 0.3) + (peerScore * 0.2) + (attendanceScore * 0.1);
        
        String rating;
        if (totalScore >= 90) {
            rating = "EXCEPTIONAL";
        } else if (totalScore >= 75) {
            rating = "EXCEEDS_EXPECTATIONS";
        } else if (totalScore >= 60) {
            rating = "MEETS_EXPECTATIONS";
        } else if (totalScore >= 45) {
            rating = "NEEDS_IMPROVEMENT";
        } else {
            rating = "UNSATISFACTORY";
        }
        
        Review review = new Review();
        review.setEmployeeId(employee.getId());
        review.setPeriod(period);
        review.setScore(totalScore);
        review.setRating(rating);
        
        saveReview(review);
        
        if (rating.equals("EXCEPTIONAL")) {
            nominateForBonus(employee);
        } else if (rating.equals("UNSATISFACTORY")) {
            createImprovementPlan(employee);
        }
        
        scheduleReviewMeeting(employee, review);
    }
}'''
    },

    # ==================== FeatureEnvy (16 cases) ====================
    {
        'id': 65,
        'expected': 'FeatureEnvy',
        'description': 'Customer profile formatter',
        'code': '''
public class CustomerProfileFormatter {
    public String formatProfile(Customer customer) {
        StringBuilder sb = new StringBuilder();
        sb.append("Name: ").append(customer.getProfile().getPersonalInfo().getFirstName())
          .append(" ").append(customer.getProfile().getPersonalInfo().getLastName()).append("\\n");
        sb.append("Email: ").append(customer.getProfile().getContactInfo().getEmail()).append("\\n");
        sb.append("Phone: ").append(customer.getProfile().getContactInfo().getPhone()).append("\\n");
        sb.append("Address: ").append(customer.getProfile().getAddress().getStreet())
          .append(", ").append(customer.getProfile().getAddress().getCity())
          .append(", ").append(customer.getProfile().getAddress().getState()).append("\\n");
        sb.append("Member Since: ").append(customer.getProfile().getMembershipInfo().getJoinDate()).append("\\n");
        return sb.toString();
    }
}'''
    },
    {
        'id': 66,
        'expected': 'FeatureEnvy',
        'description': 'Vehicle status reporter',
        'code': '''
public class VehicleStatusReporter {
    public String generateReport(Vehicle vehicle) {
        return String.format(
            "Vehicle: %s %s %s\\nMileage: %d\\nFuel: %.1f%%\\nEngine Temp: %.1f°C\\nOil Pressure: %.1f PSI\\nTire Pressure: %.1f PSI",
            vehicle.getDetails().getMake(),
            vehicle.getDetails().getModel(),
            vehicle.getDetails().getYear(),
            vehicle.getOdometer().getCurrentMileage(),
            vehicle.getFuelSystem().getCurrentLevel() / vehicle.getFuelSystem().getTankCapacity() * 100,
            vehicle.getEngine().getTemperature(),
            vehicle.getEngine().getOilPressure(),
            vehicle.getTires().getAveragePressure()
        );
    }
}'''
    },
    {
        'id': 67,
        'expected': 'FeatureEnvy',
        'description': 'Product price calculator',
        'code': '''
public class ProductPriceCalculator {
    public double calculateFinalPrice(Product product) {
        double basePrice = product.getPricing().getBasePrice();
        double discount = product.getPricing().getDiscount().getPercentage();
        double tax = product.getPricing().getTax().getRate();
        double shipping = product.getShipping().getCost();
        
        double discounted = basePrice * (1 - discount / 100);
        double withTax = discounted * (1 + tax);
        return withTax + shipping;
    }
}'''
    },
    {
        'id': 68,
        'expected': 'FeatureEnvy',
        'description': 'Employee compensation summarizer',
        'code': '''
public class CompensationSummarizer {
    public String summarize(Employee employee) {
        return String.format(
            "Base Salary: $%.2f\\nBonus: $%.2f\\nStock Options: %d\\nInsurance: $%.2f\\n401k Match: $%.2f\\nTotal: $%.2f",
            employee.getCompensation().getSalary().getBaseAmount(),
            employee.getCompensation().getBonus().getAmount(),
            employee.getCompensation().getEquity().getStockOptions(),
            employee.getBenefits().getHealthInsurance().getPremium(),
            employee.getBenefits().getRetirement().getEmployerMatch(),
            employee.getCompensation().calculateTotal()
        );
    }
}'''
    },
    {
        'id': 69,
        'expected': 'FeatureEnvy',
        'description': 'Property listing formatter',
        'code': '''
public class PropertyListingFormatter {
    public String formatListing(Property property) {
        return String.format(
            "%s\\n%s, %s %s\\n%d bed, %d bath\\n%d sqft\\n$%,.2f",
            property.getAddress().getStreet(),
            property.getAddress().getCity(),
            property.getAddress().getState(),
            property.getAddress().getZipCode(),
            property.getFeatures().getBedrooms(),
            property.getFeatures().getBathrooms(),
            property.getFeatures().getSquareFeet(),
            property.getListing().getPrice()
        );
    }
}'''
    },
    {
        'id': 70,
        'expected': 'FeatureEnvy',
        'description': 'Medical record printer',
        'code': '''
public class MedicalRecordPrinter {
    public void printVitals(Patient patient) {
        System.out.println("Patient: " + patient.getProfile().getName());
        System.out.println("DOB: " + patient.getProfile().getDateOfBirth());
        System.out.println("Blood Pressure: " + patient.getVitals().getBloodPressure().getSystolic() + 
                           "/" + patient.getVitals().getBloodPressure().getDiastolic());
        System.out.println("Heart Rate: " + patient.getVitals().getHeartRate());
        System.out.println("Temperature: " + patient.getVitals().getTemperature());
        System.out.println("Weight: " + patient.getVitals().getWeight());
    }
}'''
    },
    {
        'id': 71,
        'expected': 'FeatureEnvy',
        'description': 'Flight itinerary builder',
        'code': '''
public class ItineraryBuilder {
    public String buildItinerary(Flight flight) {
        return flight.getDeparture().getAirport().getCode() + " -> " +
               flight.getArrival().getAirport().getCode() + "\\n" +
               "Departs: " + flight.getDeparture().getDateTime() + "\\n" +
               "Arrives: " + flight.getArrival().getDateTime() + "\\n" +
               "Carrier: " + flight.getCarrier().getName() + " " + flight.getFlightNumber() + "\\n" +
               "Duration: " + flight.getDuration().toHours() + "h " + flight.getDuration().toMinutesPart() + "m";
    }
}'''
    },
    {
        'id': 72,
        'expected': 'FeatureEnvy',
        'description': 'Portfolio performance analyzer',
        'code': '''
public class PortfolioPerformanceAnalyzer {
    public double calculateROI(Portfolio portfolio) {
        double initialValue = portfolio.getHoldings().stream()
            .mapToDouble(h -> h.getPurchasePrice() * h.getQuantity())
            .sum();
        
        double currentValue = portfolio.getHoldings().stream()
            .mapToDouble(h -> h.getCurrentPrice() * h.getQuantity())
            .sum();
        
        double dividends = portfolio.getTransactions().stream()
            .filter(t -> t.getType().equals("DIVIDEND"))
            .mapToDouble(t -> t.getAmount())
            .sum();
        
        return ((currentValue + dividends - initialValue) / initialValue) * 100;
    }
}'''
    },
    {
        'id': 73,
        'expected': 'FeatureEnvy',
        'description': 'Restaurant menu pricer',
        'code': '''
public class MenuPricer {
    public double calculateMenuItemCost(MenuItem item) {
        double ingredientCost = item.getIngredients().stream()
            .mapToDouble(i -> i.getUnitPrice() * i.getQuantity())
            .sum();
        
        double laborCost = item.getPreparation().getTimeMinutes() * 
                          item.getPreparation().getHourlyRate() / 60.0;
        
        double overhead = (ingredientCost + laborCost) * 
                         item.getRestaurant().getOverheadRate();
        
        return (ingredientCost + laborCost + overhead) * item.getRestaurant().getMarkupMultiplier();
    }
}'''
    },
    {
        'id': 74,
        'expected': 'FeatureEnvy',
        'description': 'Course progress tracker',
        'code': '''
public class CourseProgressTracker {
    public double calculateProgress(Student student, Course course) {
        int completedLessons = (int) student.getEnrollment(course.getId())
            .getProgress().getCompletedLessons().size();
        int totalLessons = course.getCurriculum().getLessons().size();
        
        int completedAssignments = (int) student.getEnrollment(course.getId())
            .getProgress().getSubmittedAssignments().size();
        int totalAssignments = course.getCurriculum().getAssignments().size();
        
        double lessonProgress = (double) completedLessons / totalLessons * 50;
        double assignmentProgress = (double) completedAssignments / totalAssignments * 50;
        
        return lessonProgress + assignmentProgress;
    }
}'''
    },
    {
        'id': 75,
        'expected': 'FeatureEnvy',
        'description': 'Workout session summarizer',
        'code': '''
public class WorkoutSummarizer {
    public String summarizeSession(WorkoutSession session) {
        return String.format(
            "Duration: %d minutes\\nCalories: %d\\nDistance: %.2f km\\nAvg HR: %d\\nMax HR: %d\\nAvg Pace: %s",
            session.getMetrics().getDuration().toMinutes(),
            session.getMetrics().getCaloriesBurned(),
            session.getMetrics().getDistance().getKilometers(),
            session.getHeartRate().getAverage(),
            session.getHeartRate().getMax(),
            session.getPace().getAverage().toString()
        );
    }
}'''
    },
    {
        'id': 76,
        'expected': 'FeatureEnvy',
        'description': 'Shipping label generator',
        'code': '''
public class ShippingLabelGenerator {
    public String generateLabel(Shipment shipment) {
        return "FROM:\\n" +
               shipment.getSender().getCompany().getName() + "\\n" +
               shipment.getSender().getAddress().getStreet() + "\\n" +
               shipment.getSender().getAddress().getCity() + ", " +
               shipment.getSender().getAddress().getState() + " " +
               shipment.getSender().getAddress().getZipCode() + "\\n\\n" +
               "TO:\\n" +
               shipment.getRecipient().getName() + "\\n" +
               shipment.getRecipient().getAddress().getStreet() + "\\n" +
               shipment.getRecipient().getAddress().getCity() + ", " +
               shipment.getRecipient().getAddress().getState() + " " +
               shipment.getRecipient().getAddress().getZipCode();
    }
}'''
    },
    {
        'id': 77,
        'expected': 'FeatureEnvy',
        'description': 'Movie rating calculator',
        'code': '''
public class MovieRatingCalculator {
    public double calculateAverageRating(Movie movie) {
        double criticsScore = movie.getReviews().getCritics().stream()
            .mapToDouble(r -> r.getRating().getScore())
            .average()
            .orElse(0.0);
        
        double audienceScore = movie.getReviews().getAudience().stream()
            .mapToDouble(r -> r.getRating().getScore())
            .average()
            .orElse(0.0);
        
        return (criticsScore * movie.getWeighting().getCriticsWeight() +
                audienceScore * movie.getWeighting().getAudienceWeight()) /
               (movie.getWeighting().getCriticsWeight() + movie.getWeighting().getAudienceWeight());
    }
}'''
    },
    {
        'id': 78,
        'expected': 'FeatureEnvy',
        'description': 'Tournament standings calculator',
        'code': '''
public class StandingsCalculator {
    public int calculatePoints(Team team) {
        int wins = team.getStats().getWins() * team.getLeague().getPointsPerWin();
        int draws = team.getStats().getDraws() * team.getLeague().getPointsPerDraw();
        int losses = team.getStats().getLosses() * team.getLeague().getPointsPerLoss();
        
        int goalDifference = team.getStats().getGoalsFor() - team.getStats().getGoalsAgainst();
        int bonus = goalDifference > 10 ? team.getLeague().getBonusPoints() : 0;
        
        return wins + draws + losses + bonus;
    }
}'''
    },
    {
        'id': 79,
        'expected': 'FeatureEnvy',
        'description': 'Energy consumption reporter',
        'code': '''
public class EnergyConsumptionReporter {
    public String generateReport(Building building) {
        return String.format(
            "Building: %s\\nTotal Consumption: %.2f kWh\\nHeating: %.2f kWh\\nCooling: %.2f kWh\\nLighting: %.2f kWh\\nAppliances: %.2f kWh\\nCost: $%.2f",
            building.getInfo().getName(),
            building.getMetrics().getEnergyUsage().getTotal(),
            building.getMetrics().getEnergyUsage().getHeating(),
            building.getMetrics().getEnergyUsage().getCooling(),
            building.getMetrics().getEnergyUsage().getLighting(),
            building.getMetrics().getEnergyUsage().getAppliances(),
            building.getMetrics().getEnergyUsage().getTotal() * building.getUtility().getRatePerKwh()
        );
    }
}'''
    },
    {
        'id': 80,
        'expected': 'FeatureEnvy',
        'description': 'Social media engagement calculator',
        'code': '''
public class EngagementCalculator {
    public double calculateScore(Post post) {
        double likes = post.getMetrics().getLikes().getCount();
        double comments = post.getMetrics().getComments().getCount();
        double shares = post.getMetrics().getShares().getCount();
        double views = post.getMetrics().getViews().getCount();
        
        double likeWeight = post.getPlatform().getAlgorithm().getLikeWeight();
        double commentWeight = post.getPlatform().getAlgorithm().getCommentWeight();
        double shareWeight = post.getPlatform().getAlgorithm().getShareWeight();
        
        double engagement = (likes * likeWeight + comments * commentWeight + shares * shareWeight) / views * 100;
        
        return engagement * post.getAccount().getFollowerCount() / 1000.0;
    }
}'''
    }
]


def load_models():
    """Load the trained models"""
    models = ps.load_models()
    print("📂 Loading models...")
    print("   ✅ Loaded Ultimate Model (RF)")
    print("   ✅ Loaded Gradient Boosting")
    print("   ✅ Loaded XGBoost")
    print("   ✅ Models loaded successfully!\n")
    return models


def run_tests():
    """Run all test cases"""
    print("="*120)
    print(" " * 35 + "🧪 FRESH 80 TEST CASES - CODE SMELL DETECTION")
    print(" " * 30 + "Categories: GodClass | DataClass | Clean | LongMethod | FeatureEnvy")
    print("="*120)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*120 + "\n")
    
    models = load_models()
    
    results = []
    correct = 0
    total = len(TEST_CASES)
    
    category_stats = {
        'GodClass': {'correct': 0, 'total': 0},
        'DataClass': {'correct': 0, 'total': 0},
        'Clean': {'correct': 0, 'total': 0},
        'LongMethod': {'correct': 0, 'total': 0},
        'FeatureEnvy': {'correct': 0, 'total': 0}
    }
    
    # Header
    print("-" * 120)
    print(f"{'#':>3} | {'Expected':^13} | {'Actual':^13} | {'Conf':>6} | {'Result':^7} | {'Description'}")
    print("-" * 120)
    
    for test in TEST_CASES:
        result = ps.predict_smell_compat(test['code'], models)
        prediction = result['prediction']
        confidence = result['confidence']
        
        is_correct = prediction == test['expected']
        if is_correct:
            correct += 1
            category_stats[test['expected']]['correct'] += 1
        
        category_stats[test['expected']]['total'] += 1
        
        status = "✅" if is_correct else "❌"
        
        print(f"{test['id']:>3} | {test['expected']:^13} | {prediction:^13} | {confidence:>5.1f}% | {status:^7} | {test['description']}")
        
        results.append({
            'id': test['id'],
            'expected': test['expected'],
            'predicted': prediction,
            'confidence': confidence,
            'correct': is_correct,
            'description': test['description']
        })
    
    print("-" * 120)
    
    # Summary
    accuracy = (correct / total) * 100
    print("\n" + "="*120)
    print(" " * 45 + "📊 TEST RESULTS SUMMARY")
    print("="*120 + "\n")
    
    print(f"   Total Tests:    {total}")
    print(f"   ✅ Correct:      {correct}")
    print(f"   ❌ Wrong:        {total - correct}")
    print(f"   📈 Accuracy:     {accuracy:.1f}%\n")
    
    print("   Category Breakdown:")
    print("   " + "-" * 80)
    for category in ['GodClass', 'DataClass', 'Clean', 'LongMethod', 'FeatureEnvy']:
        stats = category_stats[category]
        pct = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
        status = "✅" if pct == 100 else "🟡"
        bar_length = int(pct / 5)
        bar = "█" * bar_length + "░" * (20 - bar_length)
        print(f"   {status} {category:15s} | {stats['correct']:2d}/{stats['total']:2d} | {bar} | {pct:5.1f}%")
    print("   " + "-" * 80)
    
    # List incorrect predictions
    incorrect = [r for r in results if not r['correct']]
    if incorrect:
        print(f"\n   ❌ INCORRECT PREDICTIONS ({len(incorrect)}):")
        print("   " + "-" * 115)
        for r in incorrect:
            print(f"   #{r['id']:3d}: Expected {r['expected']:13s} → Got {r['predicted']:13s} ({r['confidence']:.1f}%)")
            print(f"         {r['description']}")
        print("   " + "-" * 115)
    
    # Overall grade
    print("\n   " + "="*115)
    if accuracy >= 95:
        grade = "A (EXCELLENT)"
    elif accuracy >= 90:
        grade = "B (VERY GOOD)"
    elif accuracy >= 80:
        grade = "C (GOOD)"
    elif accuracy >= 70:
        grade = "D (FAIR)"
    else:
        grade = "F (NEEDS IMPROVEMENT)"
    
    print(f"   🌟 FINAL GRADE: {grade}")
    print(f"   🌟 MODEL ACCURACY: {accuracy:.1f}%")
    print("   " + "="*115)
    
    print("\n📝 Detailed report saved to: FRESH_80_TEST_REPORT.txt")
    print("📊 JSON results saved to: FRESH_80_TEST_RESULTS.json\n")
    
    print("="*120)
    
    # Save results
    save_results(results, accuracy, category_stats)
    
    return accuracy


def save_results(results, accuracy, category_stats):
    """Save test results to files"""
    import json
    
    # Save JSON
    with open('FRESH_80_TEST_RESULTS.json', 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'total_tests': len(results),
            'accuracy': accuracy,
            'category_stats': category_stats,
            'results': results
        }, f, indent=2)
    
    # Save text report
    with open('FRESH_80_TEST_REPORT.txt', 'w', encoding='utf-8') as f:
        f.write("="*120 + "\n")
        f.write(" " * 35 + "FRESH 80 TEST CASES - CODE SMELL DETECTION\n")
        f.write(" " * 30 + "Categories: GodClass | DataClass | Clean | LongMethod | FeatureEnvy\n")
        f.write("="*120 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*120 + "\n\n")
        
        f.write(f"Overall Accuracy: {accuracy:.1f}%\n")
        f.write(f"Correct: {sum(1 for r in results if r['correct'])}/{len(results)}\n\n")
        
        f.write("Category Breakdown:\n")
        for category, stats in category_stats.items():
            pct = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
            f.write(f"  {category:15s}: {stats['correct']:2d}/{stats['total']:2d} ({pct:5.1f}%)\n")
        
        f.write("\n" + "-"*120 + "\n")
        f.write("Detailed Results:\n")
        f.write("-"*120 + "\n\n")
        
        for r in results:
            status = "✅ CORRECT" if r['correct'] else "❌ INCORRECT"
            f.write(f"Test #{r['id']:3d}: {status}\n")
            f.write(f"  Description: {r['description']}\n")
            f.write(f"  Expected: {r['expected']}\n")
            f.write(f"  Predicted: {r['predicted']} ({r['confidence']:.1f}%)\n\n")


if __name__ == "__main__":
    run_tests()
