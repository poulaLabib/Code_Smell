"""
╔════════════════════════════════════════════════════════════════════════════════╗
║                    100 TEST CASES FOR CODE SMELL DETECTION                      ║
║                          Expected vs Actual Results                             ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import predict_smell_extended as ps
from datetime import datetime

# ============================================================================
# 100 TEST SAMPLES - Each with Expected Label
# ============================================================================

TEST_SAMPLES = [
    # ========================================================================
    # GOD CLASS SAMPLES (1-20)
    # ========================================================================
    {
        "id": 1,
        "expected": "GodClass",
        "description": "Order management with too many responsibilities",
        "code": """
public class OrderManager {
    private Database db;
    private Logger logger;
    private EmailService email;
    private PaymentGateway payment;
    private InventoryService inventory;
    
    public void createOrder(Order o) { }
    public void updateOrder(Order o) { }
    public void deleteOrder(Order o) { }
    public void validateOrder(Order o) { }
    public void processPayment(Order o) { }
    public void sendConfirmation(Order o) { }
    public void updateInventory(Order o) { }
    public void generateInvoice(Order o) { }
    public void calculateShipping(Order o) { }
    public void applyDiscount(Order o) { }
    public void handleRefund(Order o) { }
    public void notifyWarehouse(Order o) { }
    public void trackShipment(Order o) { }
    public void generateReport() { }
    public void exportData() { }
}"""
    },
    {
        "id": 2,
        "expected": "GodClass",
        "description": "Application controller doing everything",
        "code": """
public class ApplicationController {
    private UserService userService;
    private ProductService productService;
    private OrderService orderService;
    private PaymentService paymentService;
    private NotificationService notificationService;
    private ReportService reportService;
    
    public void handleUserLogin() { }
    public void handleUserLogout() { }
    public void handleUserRegistration() { }
    public void displayProducts() { }
    public void addToCart() { }
    public void removeFromCart() { }
    public void checkout() { }
    public void processPayment() { }
    public void sendOrderConfirmation() { }
    public void generateDailyReport() { }
    public void handleCustomerSupport() { }
    public void manageInventory() { }
    public void updatePricing() { }
    public void handleReturns() { }
    public void sendNotifications() { }
    public void backupDatabase() { }
}"""
    },
    {
        "id": 3,
        "expected": "GodClass",
        "description": "Utility class with mixed responsibilities",
        "code": """
public class UtilityManager {
    private FileHandler fileHandler;
    private NetworkClient networkClient;
    private DatabaseConnection dbConnection;
    private CacheManager cacheManager;
    
    public void readFile(String path) { }
    public void writeFile(String path) { }
    public void deleteFile(String path) { }
    public void sendHttpRequest(String url) { }
    public void parseJson(String json) { }
    public void parseXml(String xml) { }
    public void executeQuery(String sql) { }
    public void updateCache(String key) { }
    public void clearCache() { }
    public void compressData(byte[] data) { }
    public void encryptData(byte[] data) { }
    public void decryptData(byte[] data) { }
    public void validateInput(String input) { }
    public void formatOutput(Object output) { }
    public void logMessage(String message) { }
    public void handleException(Exception e) { }
}"""
    },
    {
        "id": 4,
        "expected": "GodClass",
        "description": "Customer management with too many methods",
        "code": """
public class CustomerHandler {
    private Database db;
    private EmailService emailService;
    private SmsService smsService;
    private AnalyticsService analytics;
    private LoyaltyProgram loyalty;
    
    public void createCustomer(Customer c) { }
    public void updateCustomer(Customer c) { }
    public void deleteCustomer(Customer c) { }
    public void findCustomer(Long id) { }
    public void searchCustomers(String query) { }
    public void sendEmail(Customer c) { }
    public void sendSms(Customer c) { }
    public void trackActivity(Customer c) { }
    public void calculateLoyaltyPoints(Customer c) { }
    public void redeemPoints(Customer c) { }
    public void generateCustomerReport(Customer c) { }
    public void exportCustomerData(Customer c) { }
    public void importCustomerData(List<Customer> list) { }
    public void mergeCustomerAccounts(Customer c1, Customer c2) { }
    public void validateCustomerData(Customer c) { }
    public void archiveCustomer(Customer c) { }
}"""
    },
    {
        "id": 5,
        "expected": "GodClass",
        "description": "E-commerce platform class",
        "code": """
public class EcommercePlatform {
    private ProductCatalog catalog;
    private ShoppingCart cart;
    private PaymentProcessor payment;
    private ShippingService shipping;
    private ReviewSystem reviews;
    private PromotionEngine promotions;
    
    public void listProducts() { }
    public void searchProducts(String query) { }
    public void filterProducts(Map<String, Object> filters) { }
    public void addToCart(Product p) { }
    public void removeFromCart(Product p) { }
    public void updateCartQuantity(Product p, int qty) { }
    public void applyPromoCode(String code) { }
    public void calculateTotal() { }
    public void processCheckout() { }
    public void processPayment(Payment p) { }
    public void calculateShipping() { }
    public void trackOrder(Order o) { }
    public void submitReview(Review r) { }
    public void respondToReview(Review r) { }
    public void generateSalesReport() { }
    public void manageInventory() { }
}"""
    },
    {
        "id": 6,
        "expected": "GodClass",
        "description": "Hospital management system",
        "code": """
public class HospitalSystem {
    private PatientRegistry patients;
    private DoctorRegistry doctors;
    private AppointmentScheduler scheduler;
    private BillingSystem billing;
    private PharmacyInventory pharmacy;
    private LabSystem lab;
    
    public void registerPatient(Patient p) { }
    public void updatePatientRecord(Patient p) { }
    public void scheduleAppointment(Appointment a) { }
    public void cancelAppointment(Appointment a) { }
    public void assignDoctor(Patient p, Doctor d) { }
    public void createPrescription(Prescription rx) { }
    public void orderLabTest(LabTest test) { }
    public void viewLabResults(Patient p) { }
    public void generateBill(Patient p) { }
    public void processInsuranceClaim(Claim c) { }
    public void updateInventory(Medicine m) { }
    public void dispenseMediation(Prescription rx) { }
    public void generateReport(String type) { }
    public void sendReminder(Patient p) { }
    public void archiveRecord(Patient p) { }
    public void auditTrail(String action) { }
}"""
    },
    {
        "id": 7,
        "expected": "GodClass",
        "description": "School management system",
        "code": """
public class SchoolManagement {
    private StudentRegistry students;
    private TeacherRegistry teachers;
    private CourseManager courses;
    private GradeBook grades;
    private AttendanceTracker attendance;
    private FeeManager fees;
    
    public void enrollStudent(Student s) { }
    public void withdrawStudent(Student s) { }
    public void assignTeacher(Course c, Teacher t) { }
    public void createCourse(Course c) { }
    public void registerForCourse(Student s, Course c) { }
    public void dropCourse(Student s, Course c) { }
    public void recordAttendance(Student s, Course c) { }
    public void submitGrade(Student s, Course c, Grade g) { }
    public void calculateGPA(Student s) { }
    public void generateTranscript(Student s) { }
    public void collectFees(Student s) { }
    public void issueRefund(Student s) { }
    public void scheduleExam(Exam e) { }
    public void publishResults(Exam e) { }
    public void sendNotification(String msg) { }
    public void generateReport(String type) { }
}"""
    },
    {
        "id": 8,
        "expected": "GodClass",
        "description": "Bank account management",
        "code": """
public class BankingSystem {
    private AccountRepository accounts;
    private TransactionProcessor transactions;
    private LoanProcessor loans;
    private CardService cards;
    private NotificationService notifications;
    private FraudDetection fraud;
    
    public void openAccount(Customer c) { }
    public void closeAccount(Account a) { }
    public void deposit(Account a, double amount) { }
    public void withdraw(Account a, double amount) { }
    public void transfer(Account from, Account to, double amount) { }
    public void applyForLoan(Customer c, Loan l) { }
    public void approveLoan(Loan l) { }
    public void rejectLoan(Loan l) { }
    public void issueCard(Customer c) { }
    public void blockCard(Card c) { }
    public void generateStatement(Account a) { }
    public void detectFraud(Transaction t) { }
    public void sendAlert(Customer c) { }
    public void calculateInterest(Account a) { }
    public void processPayment(Payment p) { }
    public void auditTransaction(Transaction t) { }
}"""
    },
    {
        "id": 9,
        "expected": "GodClass",
        "description": "Social media platform",
        "code": """
public class SocialMediaPlatform {
    private UserManager users;
    private PostManager posts;
    private CommentManager comments;
    private MessageService messages;
    private NotificationService notifications;
    private AnalyticsService analytics;
    
    public void createUser(User u) { }
    public void updateProfile(User u) { }
    public void deleteUser(User u) { }
    public void createPost(Post p) { }
    public void editPost(Post p) { }
    public void deletePost(Post p) { }
    public void likePost(Post p, User u) { }
    public void commentOnPost(Post p, Comment c) { }
    public void sharePost(Post p, User u) { }
    public void sendMessage(User from, User to, Message m) { }
    public void followUser(User follower, User followed) { }
    public void unfollowUser(User follower, User followed) { }
    public void blockUser(User blocker, User blocked) { }
    public void reportContent(Content c) { }
    public void moderateContent(Content c) { }
    public void generateFeed(User u) { }
}"""
    },
    {
        "id": 10,
        "expected": "GodClass",
        "description": "Project management tool",
        "code": """
public class ProjectManagement {
    private ProjectRepository projects;
    private TaskManager tasks;
    private TeamManager teams;
    private TimeTracker timeTracker;
    private ReportGenerator reports;
    private NotificationService notifications;
    
    public void createProject(Project p) { }
    public void updateProject(Project p) { }
    public void deleteProject(Project p) { }
    public void addTask(Project p, Task t) { }
    public void updateTask(Task t) { }
    public void deleteTask(Task t) { }
    public void assignTask(Task t, User u) { }
    public void completeTask(Task t) { }
    public void addTeamMember(Project p, User u) { }
    public void removeTeamMember(Project p, User u) { }
    public void logTime(Task t, Duration d) { }
    public void generateReport(Project p) { }
    public void setMilestone(Project p, Milestone m) { }
    public void trackProgress(Project p) { }
    public void sendNotification(User u, String msg) { }
    public void archiveProject(Project p) { }
}"""
    },
    {
        "id": 11,
        "expected": "GodClass",
        "description": "Restaurant management",
        "code": """
public class RestaurantManager {
    private MenuService menu;
    private OrderService orders;
    private TableManager tables;
    private KitchenDisplay kitchen;
    private PaymentProcessor payments;
    private InventoryManager inventory;
    
    public void addMenuItem(MenuItem item) { }
    public void updateMenuItem(MenuItem item) { }
    public void removeMenuItem(MenuItem item) { }
    public void createOrder(Order o) { }
    public void updateOrder(Order o) { }
    public void cancelOrder(Order o) { }
    public void assignTable(Reservation r) { }
    public void releaseTable(Table t) { }
    public void sendToKitchen(Order o) { }
    public void markAsReady(Order o) { }
    public void processPayment(Order o) { }
    public void splitBill(Order o, int ways) { }
    public void updateInventory(Item i) { }
    public void generateDailyReport() { }
    public void manageSaff(Staff s) { }
    public void handleReservation(Reservation r) { }
}"""
    },
    {
        "id": 12,
        "expected": "GodClass",
        "description": "Library system",
        "code": """
public class LibrarySystem {
    private BookCatalog books;
    private MemberRegistry members;
    private LoanManager loans;
    private FineCalculator fines;
    private ReservationSystem reservations;
    private ReportGenerator reports;
    
    public void addBook(Book b) { }
    public void removeBook(Book b) { }
    public void updateBook(Book b) { }
    public void searchBooks(String query) { }
    public void registerMember(Member m) { }
    public void updateMember(Member m) { }
    public void cancelMembership(Member m) { }
    public void checkoutBook(Member m, Book b) { }
    public void returnBook(Member m, Book b) { }
    public void renewBook(Member m, Book b) { }
    public void reserveBook(Member m, Book b) { }
    public void cancelReservation(Reservation r) { }
    public void calculateFine(Loan l) { }
    public void collectFine(Member m) { }
    public void generateReport(String type) { }
    public void sendReminder(Member m) { }
}"""
    },
    {
        "id": 13,
        "expected": "GodClass",
        "description": "Inventory management",
        "code": """
public class InventoryController {
    private ProductCatalog products;
    private WarehouseManager warehouses;
    private SupplierManager suppliers;
    private PurchaseOrderManager orders;
    private ShipmentTracker shipments;
    private ReportService reports;
    
    public void addProduct(Product p) { }
    public void updateProduct(Product p) { }
    public void deleteProduct(Product p) { }
    public void checkStock(Product p) { }
    public void adjustStock(Product p, int qty) { }
    public void transferStock(Warehouse from, Warehouse to) { }
    public void createPurchaseOrder(PurchaseOrder po) { }
    public void receivePurchaseOrder(PurchaseOrder po) { }
    public void addSupplier(Supplier s) { }
    public void updateSupplier(Supplier s) { }
    public void trackShipment(Shipment s) { }
    public void generateStockReport() { }
    public void setReorderLevel(Product p, int level) { }
    public void autoReorder(Product p) { }
    public void conductAudit(Warehouse w) { }
    public void handleDamaged(Product p, int qty) { }
}"""
    },
    {
        "id": 14,
        "expected": "GodClass",
        "description": "HR management system",
        "code": """
public class HRManagement {
    private EmployeeRegistry employees;
    private PayrollProcessor payroll;
    private LeaveManager leaves;
    private PerformanceTracker performance;
    private RecruitmentService recruitment;
    private TrainingManager training;
    
    public void hireEmployee(Employee e) { }
    public void terminateEmployee(Employee e) { }
    public void updateEmployee(Employee e) { }
    public void processPayroll() { }
    public void calculateSalary(Employee e) { }
    public void requestLeave(Employee e, Leave l) { }
    public void approveLeave(Leave l) { }
    public void rejectLeave(Leave l) { }
    public void conductReview(Employee e) { }
    public void setGoals(Employee e, List<Goal> goals) { }
    public void postJob(JobPosting jp) { }
    public void reviewApplications(JobPosting jp) { }
    public void scheduleInterview(Candidate c) { }
    public void enrollTraining(Employee e, Training t) { }
    public void generateReport(String type) { }
    public void handleGrievance(Grievance g) { }
}"""
    },
    {
        "id": 15,
        "expected": "GodClass",
        "description": "CRM system",
        "code": """
public class CRMSystem {
    private ContactManager contacts;
    private LeadManager leads;
    private OpportunityManager opportunities;
    private CampaignManager campaigns;
    private SupportTicketManager tickets;
    private ReportService reports;
    
    public void addContact(Contact c) { }
    public void updateContact(Contact c) { }
    public void deleteContact(Contact c) { }
    public void createLead(Lead l) { }
    public void convertLead(Lead l) { }
    public void qualifyLead(Lead l) { }
    public void createOpportunity(Opportunity o) { }
    public void updateOpportunity(Opportunity o) { }
    public void closeOpportunity(Opportunity o) { }
    public void launchCampaign(Campaign c) { }
    public void trackCampaign(Campaign c) { }
    public void createTicket(SupportTicket t) { }
    public void resolveTicket(SupportTicket t) { }
    public void escalateTicket(SupportTicket t) { }
    public void generateReport(String type) { }
    public void sendEmail(Contact c, Email e) { }
}"""
    },
    {
        "id": 16,
        "expected": "GodClass",
        "description": "Gaming platform",
        "code": """
public class GamingPlatform {
    private PlayerManager players;
    private GameLibrary games;
    private MatchmakingService matchmaking;
    private ChatService chat;
    private LeaderboardService leaderboards;
    private StoreService store;
    
    public void registerPlayer(Player p) { }
    public void updateProfile(Player p) { }
    public void addFriend(Player p1, Player p2) { }
    public void removeFriend(Player p1, Player p2) { }
    public void startGame(Game g) { }
    public void endGame(Game g) { }
    public void findMatch(Player p) { }
    public void joinMatch(Player p, Match m) { }
    public void leaveMatch(Player p) { }
    public void sendMessage(Player p, String msg) { }
    public void updateLeaderboard(Player p) { }
    public void purchaseItem(Player p, Item i) { }
    public void redeemCode(Player p, String code) { }
    public void reportPlayer(Player reporter, Player reported) { }
    public void banPlayer(Player p) { }
    public void generateStats(Player p) { }
}"""
    },
    {
        "id": 17,
        "expected": "GodClass",
        "description": "Event management",
        "code": """
public class EventManagement {
    private EventRegistry events;
    private VenueManager venues;
    private TicketService tickets;
    private AttendeeManager attendees;
    private SpeakerManager speakers;
    private SponsorManager sponsors;
    
    public void createEvent(Event e) { }
    public void updateEvent(Event e) { }
    public void cancelEvent(Event e) { }
    public void bookVenue(Event e, Venue v) { }
    public void releaseVenue(Venue v) { }
    public void sellTicket(Event e, Attendee a) { }
    public void refundTicket(Ticket t) { }
    public void checkIn(Attendee a) { }
    public void inviteSpeaker(Event e, Speaker s) { }
    public void confirmSpeaker(Speaker s) { }
    public void addSponsor(Event e, Sponsor s) { }
    public void manageBudget(Event e) { }
    public void sendReminders(Event e) { }
    public void collectFeedback(Event e) { }
    public void generateReport(Event e) { }
    public void archiveEvent(Event e) { }
}"""
    },
    {
        "id": 18,
        "expected": "GodClass",
        "description": "Fitness application",
        "code": """
public class FitnessApp {
    private UserManager users;
    private WorkoutManager workouts;
    private NutritionTracker nutrition;
    private GoalTracker goals;
    private SocialFeatures social;
    private AnalyticsService analytics;
    
    public void registerUser(User u) { }
    public void updateProfile(User u) { }
    public void createWorkout(Workout w) { }
    public void logWorkout(User u, Workout w) { }
    public void trackCalories(User u, Meal m) { }
    public void logMeal(User u, Meal m) { }
    public void setGoal(User u, Goal g) { }
    public void trackProgress(User u) { }
    public void updateWeight(User u, double weight) { }
    public void followUser(User u1, User u2) { }
    public void shareWorkout(User u, Workout w) { }
    public void joinChallenge(User u, Challenge c) { }
    public void earnBadge(User u, Badge b) { }
    public void generateReport(User u) { }
    public void syncDevice(User u, Device d) { }
    public void sendReminder(User u) { }
}"""
    },
    {
        "id": 19,
        "expected": "GodClass",
        "description": "Airline booking system",
        "code": """
public class AirlineBooking {
    private FlightManager flights;
    private BookingManager bookings;
    private PassengerManager passengers;
    private SeatManager seats;
    private PaymentProcessor payments;
    private NotificationService notifications;
    
    public void searchFlights(SearchCriteria c) { }
    public void getFlightDetails(Flight f) { }
    public void createBooking(Booking b) { }
    public void cancelBooking(Booking b) { }
    public void modifyBooking(Booking b) { }
    public void selectSeat(Booking b, Seat s) { }
    public void addPassenger(Booking b, Passenger p) { }
    public void checkIn(Booking b) { }
    public void printBoardingPass(Booking b) { }
    public void processPayment(Payment p) { }
    public void refundPayment(Booking b) { }
    public void addBaggage(Booking b, Baggage bg) { }
    public void upgradeSeat(Booking b) { }
    public void sendConfirmation(Booking b) { }
    public void sendReminder(Booking b) { }
    public void handleDelay(Flight f) { }
}"""
    },
    {
        "id": 20,
        "expected": "GodClass",
        "description": "Real estate platform",
        "code": """
public class RealEstatePlatform {
    private PropertyManager properties;
    private AgentManager agents;
    private ClientManager clients;
    private ListingService listings;
    private AppointmentService appointments;
    private ContractService contracts;
    
    public void addProperty(Property p) { }
    public void updateProperty(Property p) { }
    public void removeProperty(Property p) { }
    public void searchProperties(SearchCriteria c) { }
    public void createListing(Listing l) { }
    public void featureListing(Listing l) { }
    public void registerAgent(Agent a) { }
    public void assignAgent(Property p, Agent a) { }
    public void registerClient(Client c) { }
    public void scheduleViewing(Client c, Property p) { }
    public void submitOffer(Client c, Property p, Offer o) { }
    public void negotiateOffer(Offer o) { }
    public void createContract(Contract c) { }
    public void signContract(Contract c) { }
    public void calculateCommission(Sale s) { }
    public void generateReport(String type) { }
}"""
    },
    
    # ========================================================================
    # DATA CLASS SAMPLES (21-40)
    # ========================================================================
    {
        "id": 21,
        "expected": "DataClass",
        "description": "Simple person data holder",
        "code": """
public class Person {
    private String firstName;
    private String lastName;
    private int age;
    private String email;
    
    public String getFirstName() { return firstName; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public String getLastName() { return lastName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
}"""
    },
    {
        "id": 22,
        "expected": "DataClass",
        "description": "Address data transfer object",
        "code": """
public class Address {
    private String street;
    private String city;
    private String state;
    private String zipCode;
    private String country;
    
    public String getStreet() { return street; }
    public void setStreet(String street) { this.street = street; }
    public String getCity() { return city; }
    public void setCity(String city) { this.city = city; }
    public String getState() { return state; }
    public void setState(String state) { this.state = state; }
    public String getZipCode() { return zipCode; }
    public void setZipCode(String zipCode) { this.zipCode = zipCode; }
    public String getCountry() { return country; }
    public void setCountry(String country) { this.country = country; }
}"""
    },
    {
        "id": 23,
        "expected": "DataClass",
        "description": "Product DTO",
        "code": """
public class ProductDTO {
    private Long id;
    private String name;
    private String description;
    private double price;
    private int quantity;
    
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public double getPrice() { return price; }
    public void setPrice(double price) { this.price = price; }
    public int getQuantity() { return quantity; }
    public void setQuantity(int quantity) { this.quantity = quantity; }
}"""
    },
    {
        "id": 24,
        "expected": "DataClass",
        "description": "User profile entity",
        "code": """
public class UserProfile {
    private String username;
    private String email;
    private String phone;
    private Date birthDate;
    private String avatar;
    
    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public Date getBirthDate() { return birthDate; }
    public void setBirthDate(Date birthDate) { this.birthDate = birthDate; }
    public String getAvatar() { return avatar; }
    public void setAvatar(String avatar) { this.avatar = avatar; }
}"""
    },
    {
        "id": 25,
        "expected": "DataClass",
        "description": "Order details bean",
        "code": """
public class OrderDetails {
    private Long orderId;
    private Date orderDate;
    private String status;
    private double total;
    private String shippingAddress;
    
    public Long getOrderId() { return orderId; }
    public void setOrderId(Long orderId) { this.orderId = orderId; }
    public Date getOrderDate() { return orderDate; }
    public void setOrderDate(Date orderDate) { this.orderDate = orderDate; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    public double getTotal() { return total; }
    public void setTotal(double total) { this.total = total; }
    public String getShippingAddress() { return shippingAddress; }
    public void setShippingAddress(String shippingAddress) { this.shippingAddress = shippingAddress; }
}"""
    },
    {
        "id": 26,
        "expected": "DataClass",
        "description": "Employee record",
        "code": """
public class EmployeeRecord {
    private String employeeId;
    private String department;
    private String position;
    private double salary;
    private Date hireDate;
    
    public String getEmployeeId() { return employeeId; }
    public void setEmployeeId(String employeeId) { this.employeeId = employeeId; }
    public String getDepartment() { return department; }
    public void setDepartment(String department) { this.department = department; }
    public String getPosition() { return position; }
    public void setPosition(String position) { this.position = position; }
    public double getSalary() { return salary; }
    public void setSalary(double salary) { this.salary = salary; }
    public Date getHireDate() { return hireDate; }
    public void setHireDate(Date hireDate) { this.hireDate = hireDate; }
}"""
    },
    {
        "id": 27,
        "expected": "DataClass",
        "description": "Configuration settings",
        "code": """
public class ConfigSettings {
    private String serverUrl;
    private int port;
    private int timeout;
    private boolean enableSsl;
    private String apiKey;
    
    public String getServerUrl() { return serverUrl; }
    public void setServerUrl(String serverUrl) { this.serverUrl = serverUrl; }
    public int getPort() { return port; }
    public void setPort(int port) { this.port = port; }
    public int getTimeout() { return timeout; }
    public void setTimeout(int timeout) { this.timeout = timeout; }
    public boolean isEnableSsl() { return enableSsl; }
    public void setEnableSsl(boolean enableSsl) { this.enableSsl = enableSsl; }
    public String getApiKey() { return apiKey; }
    public void setApiKey(String apiKey) { this.apiKey = apiKey; }
}"""
    },
    {
        "id": 28,
        "expected": "DataClass",
        "description": "Book information",
        "code": """
public class BookInfo {
    private String isbn;
    private String title;
    private String author;
    private String publisher;
    private int year;
    
    public String getIsbn() { return isbn; }
    public void setIsbn(String isbn) { this.isbn = isbn; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getAuthor() { return author; }
    public void setAuthor(String author) { this.author = author; }
    public String getPublisher() { return publisher; }
    public void setPublisher(String publisher) { this.publisher = publisher; }
    public int getYear() { return year; }
    public void setYear(int year) { this.year = year; }
}"""
    },
    {
        "id": 29,
        "expected": "DataClass",
        "description": "Vehicle details",
        "code": """
public class VehicleDetails {
    private String vin;
    private String make;
    private String model;
    private int year;
    private String color;
    
    public String getVin() { return vin; }
    public void setVin(String vin) { this.vin = vin; }
    public String getMake() { return make; }
    public void setMake(String make) { this.make = make; }
    public String getModel() { return model; }
    public void setModel(String model) { this.model = model; }
    public int getYear() { return year; }
    public void setYear(int year) { this.year = year; }
    public String getColor() { return color; }
    public void setColor(String color) { this.color = color; }
}"""
    },
    {
        "id": 30,
        "expected": "DataClass",
        "description": "Customer contact",
        "code": """
public class CustomerContact {
    private String name;
    private String email;
    private String phone;
    private String company;
    private String notes;
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getCompany() { return company; }
    public void setCompany(String company) { this.company = company; }
    public String getNotes() { return notes; }
    public void setNotes(String notes) { this.notes = notes; }
}"""
    },
    {
        "id": 31,
        "expected": "DataClass",
        "description": "Payment info",
        "code": """
public class PaymentInfo {
    private String cardNumber;
    private String cardHolder;
    private String expiryDate;
    private String cvv;
    private String billingAddress;
    
    public String getCardNumber() { return cardNumber; }
    public void setCardNumber(String cardNumber) { this.cardNumber = cardNumber; }
    public String getCardHolder() { return cardHolder; }
    public void setCardHolder(String cardHolder) { this.cardHolder = cardHolder; }
    public String getExpiryDate() { return expiryDate; }
    public void setExpiryDate(String expiryDate) { this.expiryDate = expiryDate; }
    public String getCvv() { return cvv; }
    public void setCvv(String cvv) { this.cvv = cvv; }
    public String getBillingAddress() { return billingAddress; }
    public void setBillingAddress(String billingAddress) { this.billingAddress = billingAddress; }
}"""
    },
    {
        "id": 32,
        "expected": "DataClass",
        "description": "Student record",
        "code": """
public class StudentRecord {
    private String studentId;
    private String name;
    private String major;
    private double gpa;
    private int credits;
    
    public String getStudentId() { return studentId; }
    public void setStudentId(String studentId) { this.studentId = studentId; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getMajor() { return major; }
    public void setMajor(String major) { this.major = major; }
    public double getGpa() { return gpa; }
    public void setGpa(double gpa) { this.gpa = gpa; }
    public int getCredits() { return credits; }
    public void setCredits(int credits) { this.credits = credits; }
}"""
    },
    {
        "id": 33,
        "expected": "DataClass",
        "description": "Event data",
        "code": """
public class EventData {
    private String eventId;
    private String title;
    private Date startTime;
    private Date endTime;
    private String location;
    
    public String getEventId() { return eventId; }
    public void setEventId(String eventId) { this.eventId = eventId; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public Date getStartTime() { return startTime; }
    public void setStartTime(Date startTime) { this.startTime = startTime; }
    public Date getEndTime() { return endTime; }
    public void setEndTime(Date endTime) { this.endTime = endTime; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
}"""
    },
    {
        "id": 34,
        "expected": "DataClass",
        "description": "Message entity",
        "code": """
public class MessageEntity {
    private Long id;
    private String sender;
    private String recipient;
    private String content;
    private Date timestamp;
    
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getSender() { return sender; }
    public void setSender(String sender) { this.sender = sender; }
    public String getRecipient() { return recipient; }
    public void setRecipient(String recipient) { this.recipient = recipient; }
    public String getContent() { return content; }
    public void setContent(String content) { this.content = content; }
    public Date getTimestamp() { return timestamp; }
    public void setTimestamp(Date timestamp) { this.timestamp = timestamp; }
}"""
    },
    {
        "id": 35,
        "expected": "DataClass",
        "description": "Flight info",
        "code": """
public class FlightInfo {
    private String flightNumber;
    private String origin;
    private String destination;
    private Date departureTime;
    private Date arrivalTime;
    
    public String getFlightNumber() { return flightNumber; }
    public void setFlightNumber(String flightNumber) { this.flightNumber = flightNumber; }
    public String getOrigin() { return origin; }
    public void setOrigin(String origin) { this.origin = origin; }
    public String getDestination() { return destination; }
    public void setDestination(String destination) { this.destination = destination; }
    public Date getDepartureTime() { return departureTime; }
    public void setDepartureTime(Date departureTime) { this.departureTime = departureTime; }
    public Date getArrivalTime() { return arrivalTime; }
    public void setArrivalTime(Date arrivalTime) { this.arrivalTime = arrivalTime; }
}"""
    },
    {
        "id": 36,
        "expected": "DataClass",
        "description": "Hotel room",
        "code": """
public class HotelRoom {
    private String roomNumber;
    private String roomType;
    private double pricePerNight;
    private int capacity;
    private boolean available;
    
    public String getRoomNumber() { return roomNumber; }
    public void setRoomNumber(String roomNumber) { this.roomNumber = roomNumber; }
    public String getRoomType() { return roomType; }
    public void setRoomType(String roomType) { this.roomType = roomType; }
    public double getPricePerNight() { return pricePerNight; }
    public void setPricePerNight(double pricePerNight) { this.pricePerNight = pricePerNight; }
    public int getCapacity() { return capacity; }
    public void setCapacity(int capacity) { this.capacity = capacity; }
    public boolean isAvailable() { return available; }
    public void setAvailable(boolean available) { this.available = available; }
}"""
    },
    {
        "id": 37,
        "expected": "DataClass",
        "description": "Movie info",
        "code": """
public class MovieInfo {
    private String movieId;
    private String title;
    private String director;
    private int duration;
    private String genre;
    
    public String getMovieId() { return movieId; }
    public void setMovieId(String movieId) { this.movieId = movieId; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getDirector() { return director; }
    public void setDirector(String director) { this.director = director; }
    public int getDuration() { return duration; }
    public void setDuration(int duration) { this.duration = duration; }
    public String getGenre() { return genre; }
    public void setGenre(String genre) { this.genre = genre; }
}"""
    },
    {
        "id": 38,
        "expected": "DataClass",
        "description": "Recipe data",
        "code": """
public class RecipeData {
    private String recipeId;
    private String name;
    private String ingredients;
    private int prepTime;
    private int cookTime;
    
    public String getRecipeId() { return recipeId; }
    public void setRecipeId(String recipeId) { this.recipeId = recipeId; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getIngredients() { return ingredients; }
    public void setIngredients(String ingredients) { this.ingredients = ingredients; }
    public int getPrepTime() { return prepTime; }
    public void setPrepTime(int prepTime) { this.prepTime = prepTime; }
    public int getCookTime() { return cookTime; }
    public void setCookTime(int cookTime) { this.cookTime = cookTime; }
}"""
    },
    {
        "id": 39,
        "expected": "DataClass",
        "description": "Weather data",
        "code": """
public class WeatherData {
    private String location;
    private double temperature;
    private int humidity;
    private double windSpeed;
    private String condition;
    
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public double getTemperature() { return temperature; }
    public void setTemperature(double temperature) { this.temperature = temperature; }
    public int getHumidity() { return humidity; }
    public void setHumidity(int humidity) { this.humidity = humidity; }
    public double getWindSpeed() { return windSpeed; }
    public void setWindSpeed(double windSpeed) { this.windSpeed = windSpeed; }
    public String getCondition() { return condition; }
    public void setCondition(String condition) { this.condition = condition; }
}"""
    },
    {
        "id": 40,
        "expected": "DataClass",
        "description": "Notification bean",
        "code": """
public class NotificationBean {
    private Long notificationId;
    private String title;
    private String message;
    private boolean read;
    private Date createdAt;
    
    public Long getNotificationId() { return notificationId; }
    public void setNotificationId(Long notificationId) { this.notificationId = notificationId; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }
    public boolean isRead() { return read; }
    public void setRead(boolean read) { this.read = read; }
    public Date getCreatedAt() { return createdAt; }
    public void setCreatedAt(Date createdAt) { this.createdAt = createdAt; }
}"""
    },
    
    # ========================================================================
    # CLEAN CODE SAMPLES (41-60)
    # ========================================================================
    {
        "id": 41,
        "expected": "Clean",
        "description": "Simple user service",
        "code": """
public class UserService {
    private final UserRepository repository;
    
    public UserService(UserRepository repository) {
        this.repository = repository;
    }
    
    public User findById(Long id) {
        return repository.findById(id);
    }
    
    public User save(User user) {
        return repository.save(user);
    }
}"""
    },
    {
        "id": 42,
        "expected": "Clean",
        "description": "Calculator with single responsibility",
        "code": """
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
    
    public int subtract(int a, int b) {
        return a - b;
    }
    
    public int multiply(int a, int b) {
        return a * b;
    }
    
    public double divide(int a, int b) {
        if (b == 0) throw new IllegalArgumentException("Cannot divide by zero");
        return (double) a / b;
    }
}"""
    },
    {
        "id": 43,
        "expected": "Clean",
        "description": "Email validator",
        "code": """
public class EmailValidator {
    private static final Pattern EMAIL_PATTERN = 
        Pattern.compile("^[A-Za-z0-9+_.-]+@(.+)$");
    
    public boolean isValid(String email) {
        if (email == null || email.isEmpty()) {
            return false;
        }
        return EMAIL_PATTERN.matcher(email).matches();
    }
}"""
    },
    {
        "id": 44,
        "expected": "Clean",
        "description": "Logger wrapper",
        "code": """
public class AppLogger {
    private final Logger logger;
    
    public AppLogger(Class<?> clazz) {
        this.logger = LoggerFactory.getLogger(clazz);
    }
    
    public void info(String message) {
        logger.info(message);
    }
    
    public void error(String message, Throwable t) {
        logger.error(message, t);
    }
}"""
    },
    {
        "id": 45,
        "expected": "Clean",
        "description": "Date formatter utility",
        "code": """
public class DateFormatter {
    private final DateTimeFormatter formatter;
    
    public DateFormatter(String pattern) {
        this.formatter = DateTimeFormatter.ofPattern(pattern);
    }
    
    public String format(LocalDate date) {
        return date.format(formatter);
    }
    
    public LocalDate parse(String dateString) {
        return LocalDate.parse(dateString, formatter);
    }
}"""
    },
    {
        "id": 46,
        "expected": "Clean",
        "description": "File reader helper",
        "code": """
public class FileReader {
    public String readContent(Path filePath) throws IOException {
        return Files.readString(filePath);
    }
    
    public List<String> readLines(Path filePath) throws IOException {
        return Files.readAllLines(filePath);
    }
    
    public boolean exists(Path filePath) {
        return Files.exists(filePath);
    }
}"""
    },
    {
        "id": 47,
        "expected": "Clean",
        "description": "Password hasher",
        "code": """
public class PasswordHasher {
    private final BCryptPasswordEncoder encoder;
    
    public PasswordHasher() {
        this.encoder = new BCryptPasswordEncoder();
    }
    
    public String hash(String password) {
        return encoder.encode(password);
    }
    
    public boolean verify(String password, String hash) {
        return encoder.matches(password, hash);
    }
}"""
    },
    {
        "id": 48,
        "expected": "Clean",
        "description": "Queue implementation",
        "code": """
public class SimpleQueue<T> {
    private final LinkedList<T> items = new LinkedList<>();
    
    public void enqueue(T item) {
        items.addLast(item);
    }
    
    public T dequeue() {
        return items.removeFirst();
    }
    
    public boolean isEmpty() {
        return items.isEmpty();
    }
    
    public int size() {
        return items.size();
    }
}"""
    },
    {
        "id": 49,
        "expected": "Clean",
        "description": "Counter class",
        "code": """
public class Counter {
    private int count;
    
    public Counter() {
        this.count = 0;
    }
    
    public void increment() {
        count++;
    }
    
    public void decrement() {
        count--;
    }
    
    public int getCount() {
        return count;
    }
    
    public void reset() {
        count = 0;
    }
}"""
    },
    {
        "id": 50,
        "expected": "Clean",
        "description": "String utils",
        "code": """
public class StringUtils {
    public boolean isEmpty(String str) {
        return str == null || str.isEmpty();
    }
    
    public String capitalize(String str) {
        if (isEmpty(str)) return str;
        return str.substring(0, 1).toUpperCase() + str.substring(1);
    }
    
    public String reverse(String str) {
        return new StringBuilder(str).reverse().toString();
    }
}"""
    },
    {
        "id": 51,
        "expected": "Clean",
        "description": "Price calculator",
        "code": """
public class PriceCalculator {
    private final double taxRate;
    
    public PriceCalculator(double taxRate) {
        this.taxRate = taxRate;
    }
    
    public double calculateTax(double price) {
        return price * taxRate;
    }
    
    public double calculateTotal(double price) {
        return price + calculateTax(price);
    }
}"""
    },
    {
        "id": 52,
        "expected": "Clean",
        "description": "Repository base",
        "code": """
public class BaseRepository<T> {
    private final EntityManager em;
    private final Class<T> entityClass;
    
    public BaseRepository(EntityManager em, Class<T> entityClass) {
        this.em = em;
        this.entityClass = entityClass;
    }
    
    public T findById(Long id) {
        return em.find(entityClass, id);
    }
    
    public void save(T entity) {
        em.persist(entity);
    }
}"""
    },
    {
        "id": 53,
        "expected": "Clean",
        "description": "Timer utility",
        "code": """
public class Timer {
    private long startTime;
    
    public void start() {
        startTime = System.currentTimeMillis();
    }
    
    public long getElapsedTime() {
        return System.currentTimeMillis() - startTime;
    }
    
    public void reset() {
        startTime = 0;
    }
}"""
    },
    {
        "id": 54,
        "expected": "Clean",
        "description": "Random generator",
        "code": """
public class RandomGenerator {
    private final Random random = new Random();
    
    public int nextInt(int bound) {
        return random.nextInt(bound);
    }
    
    public double nextDouble() {
        return random.nextDouble();
    }
    
    public boolean nextBoolean() {
        return random.nextBoolean();
    }
}"""
    },
    {
        "id": 55,
        "expected": "Clean",
        "description": "Configuration reader",
        "code": """
public class ConfigReader {
    private final Properties properties;
    
    public ConfigReader(String filename) throws IOException {
        properties = new Properties();
        properties.load(new FileInputStream(filename));
    }
    
    public String get(String key) {
        return properties.getProperty(key);
    }
    
    public int getInt(String key) {
        return Integer.parseInt(get(key));
    }
}"""
    },
    {
        "id": 56,
        "expected": "Clean",
        "description": "Event publisher",
        "code": """
public class EventPublisher {
    private final List<EventListener> listeners = new ArrayList<>();
    
    public void subscribe(EventListener listener) {
        listeners.add(listener);
    }
    
    public void unsubscribe(EventListener listener) {
        listeners.remove(listener);
    }
    
    public void publish(Event event) {
        listeners.forEach(l -> l.onEvent(event));
    }
}"""
    },
    {
        "id": 57,
        "expected": "Clean",
        "description": "Cache implementation",
        "code": """
public class SimpleCache<K, V> {
    private final Map<K, V> cache = new HashMap<>();
    
    public void put(K key, V value) {
        cache.put(key, value);
    }
    
    public V get(K key) {
        return cache.get(key);
    }
    
    public boolean contains(K key) {
        return cache.containsKey(key);
    }
    
    public void clear() {
        cache.clear();
    }
}"""
    },
    {
        "id": 58,
        "expected": "Clean",
        "description": "Stack implementation",
        "code": """
public class Stack<T> {
    private final List<T> items = new ArrayList<>();
    
    public void push(T item) {
        items.add(item);
    }
    
    public T pop() {
        return items.remove(items.size() - 1);
    }
    
    public T peek() {
        return items.get(items.size() - 1);
    }
    
    public boolean isEmpty() {
        return items.isEmpty();
    }
}"""
    },
    {
        "id": 59,
        "expected": "Clean",
        "description": "Validator interface implementation",
        "code": """
public class AgeValidator implements Validator<Integer> {
    private final int minAge;
    private final int maxAge;
    
    public AgeValidator(int minAge, int maxAge) {
        this.minAge = minAge;
        this.maxAge = maxAge;
    }
    
    public boolean isValid(Integer age) {
        return age >= minAge && age <= maxAge;
    }
}"""
    },
    {
        "id": 60,
        "expected": "Clean",
        "description": "Converter utility",
        "code": """
public class TemperatureConverter {
    public double celsiusToFahrenheit(double celsius) {
        return (celsius * 9 / 5) + 32;
    }
    
    public double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5 / 9;
    }
    
    public double celsiusToKelvin(double celsius) {
        return celsius + 273.15;
    }
}"""
    },
    
    # ========================================================================
    # LONG METHOD SAMPLES (61-75)
    # ========================================================================
    {
        "id": 61,
        "expected": "LongMethod",
        "description": "Order processing with too many steps",
        "code": """
public class OrderProcessor {
    public void processOrder(Order order) {
        // Validate order
        if (order == null) throw new IllegalArgumentException("Order is null");
        if (order.getItems() == null) throw new IllegalArgumentException("No items");
        if (order.getItems().isEmpty()) throw new IllegalArgumentException("Empty order");
        if (order.getCustomer() == null) throw new IllegalArgumentException("No customer");
        
        // Calculate totals
        double subtotal = 0;
        for (OrderItem item : order.getItems()) {
            double itemTotal = item.getPrice() * item.getQuantity();
            subtotal += itemTotal;
        }
        
        // Apply discounts
        double discount = 0;
        if (order.getPromoCode() != null) {
            if (order.getPromoCode().equals("SAVE10")) discount = subtotal * 0.10;
            else if (order.getPromoCode().equals("SAVE20")) discount = subtotal * 0.20;
            else if (order.getPromoCode().equals("SAVE30")) discount = subtotal * 0.30;
        }
        if (order.getCustomer().isVip()) discount += subtotal * 0.05;
        
        // Calculate tax
        double taxableAmount = subtotal - discount;
        double tax = taxableAmount * 0.08;
        
        // Calculate shipping
        double shipping = 0;
        if (subtotal < 50) shipping = 5.99;
        else if (subtotal < 100) shipping = 3.99;
        
        // Set totals
        order.setSubtotal(subtotal);
        order.setDiscount(discount);
        order.setTax(tax);
        order.setShipping(shipping);
        order.setTotal(taxableAmount + tax + shipping);
        
        // Update inventory
        for (OrderItem item : order.getItems()) {
            Product product = item.getProduct();
            int newQty = product.getQuantity() - item.getQuantity();
            product.setQuantity(newQty);
        }
        
        // Save order
        order.setStatus("CONFIRMED");
        order.setOrderDate(new Date());
        orderRepository.save(order);
        
        // Send notification
        String message = "Order confirmed: " + order.getId();
        emailService.send(order.getCustomer().getEmail(), message);
    }
}"""
    },
    {
        "id": 62,
        "expected": "LongMethod",
        "description": "Report generator with many steps",
        "code": """
public class ReportGenerator {
    public String generateReport(List<Sale> sales) {
        StringBuilder report = new StringBuilder();
        
        // Header
        report.append("=================================\\n");
        report.append("       SALES REPORT              \\n");
        report.append("=================================\\n");
        report.append("Generated: ").append(new Date()).append("\\n\\n");
        
        // Group by category
        Map<String, List<Sale>> byCategory = new HashMap<>();
        for (Sale sale : sales) {
            String cat = sale.getCategory();
            if (!byCategory.containsKey(cat)) {
                byCategory.put(cat, new ArrayList<>());
            }
            byCategory.get(cat).add(sale);
        }
        
        // Calculate totals per category
        double grandTotal = 0;
        for (String category : byCategory.keySet()) {
            report.append("Category: ").append(category).append("\\n");
            report.append("---------------------------------\\n");
            
            double categoryTotal = 0;
            List<Sale> categorySales = byCategory.get(category);
            for (Sale sale : categorySales) {
                report.append("  ").append(sale.getProduct());
                report.append(" - $").append(sale.getAmount()).append("\\n");
                categoryTotal += sale.getAmount();
            }
            
            report.append("  Category Total: $").append(categoryTotal).append("\\n\\n");
            grandTotal += categoryTotal;
        }
        
        // Summary
        report.append("=================================\\n");
        report.append("GRAND TOTAL: $").append(grandTotal).append("\\n");
        report.append("Total Transactions: ").append(sales.size()).append("\\n");
        report.append("Average Sale: $").append(grandTotal / sales.size()).append("\\n");
        
        return report.toString();
    }
}"""
    },
    {
        "id": 63,
        "expected": "LongMethod",
        "description": "Data import with many validation steps",
        "code": """
public class DataImporter {
    public void importData(String filePath) {
        List<String> lines = readFile(filePath);
        List<Record> records = new ArrayList<>();
        List<String> errors = new ArrayList<>();
        
        // Parse header
        String[] headers = lines.get(0).split(",");
        int nameIndex = -1, emailIndex = -1, ageIndex = -1;
        for (int i = 0; i < headers.length; i++) {
            if (headers[i].equals("name")) nameIndex = i;
            if (headers[i].equals("email")) emailIndex = i;
            if (headers[i].equals("age")) ageIndex = i;
        }
        
        // Validate header
        if (nameIndex == -1) errors.add("Missing name column");
        if (emailIndex == -1) errors.add("Missing email column");
        if (ageIndex == -1) errors.add("Missing age column");
        
        if (!errors.isEmpty()) {
            throw new ImportException(errors);
        }
        
        // Parse records
        for (int i = 1; i < lines.size(); i++) {
            String[] values = lines.get(i).split(",");
            
            // Validate record
            if (values.length != headers.length) {
                errors.add("Line " + i + ": Invalid column count");
                continue;
            }
            
            String name = values[nameIndex].trim();
            String email = values[emailIndex].trim();
            String ageStr = values[ageIndex].trim();
            
            // Validate fields
            if (name.isEmpty()) {
                errors.add("Line " + i + ": Empty name");
                continue;
            }
            if (!email.contains("@")) {
                errors.add("Line " + i + ": Invalid email");
                continue;
            }
            
            int age;
            try {
                age = Integer.parseInt(ageStr);
            } catch (NumberFormatException e) {
                errors.add("Line " + i + ": Invalid age");
                continue;
            }
            
            records.add(new Record(name, email, age));
        }
        
        // Save records
        for (Record record : records) {
            repository.save(record);
        }
        
        // Log results
        logger.info("Imported " + records.size() + " records");
        logger.info("Errors: " + errors.size());
    }
}"""
    },
    {
        "id": 64,
        "expected": "LongMethod",
        "description": "Form validation with many checks",
        "code": """
public class FormValidator {
    public ValidationResult validate(UserForm form) {
        List<String> errors = new ArrayList<>();
        
        // Validate username
        String username = form.getUsername();
        if (username == null || username.isEmpty()) {
            errors.add("Username is required");
        } else if (username.length() < 3) {
            errors.add("Username must be at least 3 characters");
        } else if (username.length() > 20) {
            errors.add("Username must be at most 20 characters");
        } else if (!username.matches("[a-zA-Z0-9_]+")) {
            errors.add("Username can only contain letters, numbers, and underscores");
        }
        
        // Validate email
        String email = form.getEmail();
        if (email == null || email.isEmpty()) {
            errors.add("Email is required");
        } else if (!email.contains("@")) {
            errors.add("Invalid email format");
        } else if (email.length() > 100) {
            errors.add("Email is too long");
        }
        
        // Validate password
        String password = form.getPassword();
        if (password == null || password.isEmpty()) {
            errors.add("Password is required");
        } else if (password.length() < 8) {
            errors.add("Password must be at least 8 characters");
        } else if (!password.matches(".*[A-Z].*")) {
            errors.add("Password must contain uppercase letter");
        } else if (!password.matches(".*[a-z].*")) {
            errors.add("Password must contain lowercase letter");
        } else if (!password.matches(".*[0-9].*")) {
            errors.add("Password must contain a number");
        }
        
        // Validate confirm password
        if (!password.equals(form.getConfirmPassword())) {
            errors.add("Passwords do not match");
        }
        
        // Validate age
        Integer age = form.getAge();
        if (age == null) {
            errors.add("Age is required");
        } else if (age < 18) {
            errors.add("Must be at least 18 years old");
        } else if (age > 120) {
            errors.add("Invalid age");
        }
        
        return new ValidationResult(errors.isEmpty(), errors);
    }
}"""
    },
    {
        "id": 65,
        "expected": "LongMethod",
        "description": "Payment processing with many steps",
        "code": """
public class PaymentProcessor {
    public PaymentResult processPayment(PaymentRequest request) {
        // Validate request
        if (request == null) {
            return PaymentResult.failure("Invalid request");
        }
        if (request.getAmount() <= 0) {
            return PaymentResult.failure("Invalid amount");
        }
        if (request.getCardNumber() == null) {
            return PaymentResult.failure("Card number required");
        }
        
        // Format card number
        String cardNumber = request.getCardNumber().replaceAll("\\s", "");
        if (cardNumber.length() != 16) {
            return PaymentResult.failure("Invalid card number");
        }
        
        // Determine card type
        String cardType;
        if (cardNumber.startsWith("4")) {
            cardType = "VISA";
        } else if (cardNumber.startsWith("5")) {
            cardType = "MASTERCARD";
        } else if (cardNumber.startsWith("3")) {
            cardType = "AMEX";
        } else {
            return PaymentResult.failure("Unsupported card type");
        }
        
        // Validate expiry
        String expiry = request.getExpiry();
        String[] parts = expiry.split("/");
        int month = Integer.parseInt(parts[0]);
        int year = Integer.parseInt(parts[1]) + 2000;
        LocalDate expiryDate = LocalDate.of(year, month, 1);
        if (expiryDate.isBefore(LocalDate.now())) {
            return PaymentResult.failure("Card expired");
        }
        
        // Process with gateway
        GatewayRequest gwRequest = new GatewayRequest();
        gwRequest.setMerchantId(merchantId);
        gwRequest.setAmount(request.getAmount());
        gwRequest.setCardNumber(cardNumber);
        gwRequest.setExpiry(expiry);
        gwRequest.setCvv(request.getCvv());
        
        GatewayResponse response = gateway.process(gwRequest);
        
        // Handle response
        if (response.isSuccess()) {
            Transaction tx = new Transaction();
            tx.setAmount(request.getAmount());
            tx.setCardType(cardType);
            tx.setTransactionId(response.getTransactionId());
            tx.setTimestamp(new Date());
            transactionRepository.save(tx);
            
            return PaymentResult.success(response.getTransactionId());
        } else {
            return PaymentResult.failure(response.getErrorMessage());
        }
    }
}"""
    },
    {
        "id": 66,
        "expected": "LongMethod",
        "description": "User registration with many steps",
        "code": """
public class RegistrationService {
    public RegistrationResult register(RegistrationForm form) {
        // Check if username exists
        if (userRepository.existsByUsername(form.getUsername())) {
            return RegistrationResult.failure("Username already taken");
        }
        
        // Check if email exists
        if (userRepository.existsByEmail(form.getEmail())) {
            return RegistrationResult.failure("Email already registered");
        }
        
        // Create user
        User user = new User();
        user.setUsername(form.getUsername());
        user.setEmail(form.getEmail());
        
        // Hash password
        String salt = generateSalt();
        String hashedPassword = hashPassword(form.getPassword(), salt);
        user.setPasswordHash(hashedPassword);
        user.setPasswordSalt(salt);
        
        // Set defaults
        user.setActive(false);
        user.setCreatedAt(new Date());
        user.setRole("USER");
        
        // Generate verification token
        String token = UUID.randomUUID().toString();
        user.setVerificationToken(token);
        user.setTokenExpiry(new Date(System.currentTimeMillis() + 86400000));
        
        // Save user
        userRepository.save(user);
        
        // Create profile
        UserProfile profile = new UserProfile();
        profile.setUserId(user.getId());
        profile.setFirstName(form.getFirstName());
        profile.setLastName(form.getLastName());
        profileRepository.save(profile);
        
        // Send verification email
        String verifyUrl = baseUrl + "/verify?token=" + token;
        String emailBody = "Click here to verify: " + verifyUrl;
        emailService.send(form.getEmail(), "Verify your account", emailBody);
        
        // Log registration
        auditLog.log("USER_REGISTERED", user.getId());
        
        return RegistrationResult.success(user.getId());
    }
}"""
    },
    {
        "id": 67,
        "expected": "LongMethod",
        "description": "Search with multiple filters",
        "code": """
public class SearchService {
    public SearchResult search(SearchCriteria criteria) {
        StringBuilder query = new StringBuilder("SELECT * FROM products WHERE 1=1");
        List<Object> params = new ArrayList<>();
        
        // Filter by keyword
        if (criteria.getKeyword() != null && !criteria.getKeyword().isEmpty()) {
            query.append(" AND (name LIKE ? OR description LIKE ?)");
            params.add("%" + criteria.getKeyword() + "%");
            params.add("%" + criteria.getKeyword() + "%");
        }
        
        // Filter by category
        if (criteria.getCategory() != null) {
            query.append(" AND category_id = ?");
            params.add(criteria.getCategory());
        }
        
        // Filter by price range
        if (criteria.getMinPrice() != null) {
            query.append(" AND price >= ?");
            params.add(criteria.getMinPrice());
        }
        if (criteria.getMaxPrice() != null) {
            query.append(" AND price <= ?");
            params.add(criteria.getMaxPrice());
        }
        
        // Filter by availability
        if (criteria.isInStockOnly()) {
            query.append(" AND quantity > 0");
        }
        
        // Filter by rating
        if (criteria.getMinRating() != null) {
            query.append(" AND rating >= ?");
            params.add(criteria.getMinRating());
        }
        
        // Filter by brand
        if (criteria.getBrands() != null && !criteria.getBrands().isEmpty()) {
            query.append(" AND brand IN (");
            for (int i = 0; i < criteria.getBrands().size(); i++) {
                if (i > 0) query.append(",");
                query.append("?");
                params.add(criteria.getBrands().get(i));
            }
            query.append(")");
        }
        
        // Add sorting
        String sortField = criteria.getSortBy() != null ? criteria.getSortBy() : "name";
        String sortDir = criteria.getSortDirection() != null ? criteria.getSortDirection() : "ASC";
        query.append(" ORDER BY ").append(sortField).append(" ").append(sortDir);
        
        // Add pagination
        int page = criteria.getPage() != null ? criteria.getPage() : 0;
        int size = criteria.getPageSize() != null ? criteria.getPageSize() : 20;
        query.append(" LIMIT ? OFFSET ?");
        params.add(size);
        params.add(page * size);
        
        // Execute query
        List<Product> products = jdbcTemplate.query(query.toString(), params.toArray());
        
        // Get total count
        String countQuery = query.toString().replaceFirst("SELECT \\*", "SELECT COUNT(*)");
        int total = jdbcTemplate.queryForObject(countQuery, Integer.class);
        
        return new SearchResult(products, total, page, size);
    }
}"""
    },
    {
        "id": 68,
        "expected": "LongMethod",
        "description": "Export data with formatting",
        "code": """
public class DataExporter {
    public byte[] exportToExcel(List<Employee> employees) {
        Workbook workbook = new XSSFWorkbook();
        Sheet sheet = workbook.createSheet("Employees");
        
        // Create header style
        CellStyle headerStyle = workbook.createCellStyle();
        headerStyle.setFillForegroundColor(IndexedColors.BLUE.getIndex());
        headerStyle.setFillPattern(FillPatternType.SOLID_FOREGROUND);
        Font headerFont = workbook.createFont();
        headerFont.setColor(IndexedColors.WHITE.getIndex());
        headerFont.setBold(true);
        headerStyle.setFont(headerFont);
        
        // Create headers
        Row headerRow = sheet.createRow(0);
        String[] headers = {"ID", "Name", "Email", "Department", "Salary", "Hire Date"};
        for (int i = 0; i < headers.length; i++) {
            Cell cell = headerRow.createCell(i);
            cell.setCellValue(headers[i]);
            cell.setCellStyle(headerStyle);
        }
        
        // Create date style
        CellStyle dateStyle = workbook.createCellStyle();
        dateStyle.setDataFormat(workbook.createDataFormat().getFormat("yyyy-mm-dd"));
        
        // Create currency style
        CellStyle currencyStyle = workbook.createCellStyle();
        currencyStyle.setDataFormat(workbook.createDataFormat().getFormat("$#,##0.00"));
        
        // Populate data
        int rowNum = 1;
        for (Employee emp : employees) {
            Row row = sheet.createRow(rowNum++);
            
            row.createCell(0).setCellValue(emp.getId());
            row.createCell(1).setCellValue(emp.getName());
            row.createCell(2).setCellValue(emp.getEmail());
            row.createCell(3).setCellValue(emp.getDepartment());
            
            Cell salaryCell = row.createCell(4);
            salaryCell.setCellValue(emp.getSalary());
            salaryCell.setCellStyle(currencyStyle);
            
            Cell dateCell = row.createCell(5);
            dateCell.setCellValue(emp.getHireDate());
            dateCell.setCellStyle(dateStyle);
        }
        
        // Auto-size columns
        for (int i = 0; i < headers.length; i++) {
            sheet.autoSizeColumn(i);
        }
        
        // Write to bytes
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        workbook.write(out);
        workbook.close();
        
        return out.toByteArray();
    }
}"""
    },
    {
        "id": 69,
        "expected": "LongMethod",
        "description": "Email template builder",
        "code": """
public class EmailTemplateBuilder {
    public String buildOrderConfirmation(Order order) {
        StringBuilder html = new StringBuilder();
        
        // HTML header
        html.append("<!DOCTYPE html>");
        html.append("<html><head>");
        html.append("<style>");
        html.append("body { font-family: Arial, sans-serif; }");
        html.append("table { border-collapse: collapse; width: 100%; }");
        html.append("th, td { border: 1px solid #ddd; padding: 8px; }");
        html.append("th { background-color: #4CAF50; color: white; }");
        html.append(".total { font-weight: bold; font-size: 18px; }");
        html.append("</style>");
        html.append("</head><body>");
        
        // Header
        html.append("<h1>Order Confirmation</h1>");
        html.append("<p>Thank you for your order!</p>");
        html.append("<p>Order Number: <strong>").append(order.getId()).append("</strong></p>");
        html.append("<p>Order Date: ").append(order.getOrderDate()).append("</p>");
        
        // Customer info
        html.append("<h2>Shipping Address</h2>");
        html.append("<p>").append(order.getCustomer().getName()).append("<br>");
        html.append(order.getShippingAddress().getStreet()).append("<br>");
        html.append(order.getShippingAddress().getCity()).append(", ");
        html.append(order.getShippingAddress().getState()).append(" ");
        html.append(order.getShippingAddress().getZip()).append("</p>");
        
        // Order items
        html.append("<h2>Order Items</h2>");
        html.append("<table><tr><th>Item</th><th>Qty</th><th>Price</th><th>Total</th></tr>");
        for (OrderItem item : order.getItems()) {
            html.append("<tr>");
            html.append("<td>").append(item.getProduct().getName()).append("</td>");
            html.append("<td>").append(item.getQuantity()).append("</td>");
            html.append("<td>$").append(item.getPrice()).append("</td>");
            html.append("<td>$").append(item.getPrice() * item.getQuantity()).append("</td>");
            html.append("</tr>");
        }
        html.append("</table>");
        
        // Totals
        html.append("<p>Subtotal: $").append(order.getSubtotal()).append("</p>");
        html.append("<p>Shipping: $").append(order.getShipping()).append("</p>");
        html.append("<p>Tax: $").append(order.getTax()).append("</p>");
        html.append("<p class='total'>Total: $").append(order.getTotal()).append("</p>");
        
        // Footer
        html.append("<p>Questions? Contact us at support@example.com</p>");
        html.append("</body></html>");
        
        return html.toString();
    }
}"""
    },
    {
        "id": 70,
        "expected": "LongMethod",
        "description": "Configuration parser",
        "code": """
public class ConfigurationParser {
    public Configuration parse(String configFile) throws Exception {
        Configuration config = new Configuration();
        Properties props = new Properties();
        props.load(new FileInputStream(configFile));
        
        // Parse server settings
        String host = props.getProperty("server.host", "localhost");
        config.setServerHost(host);
        
        String portStr = props.getProperty("server.port", "8080");
        int port = Integer.parseInt(portStr);
        if (port < 1 || port > 65535) {
            throw new ConfigException("Invalid port: " + port);
        }
        config.setServerPort(port);
        
        // Parse database settings
        String dbUrl = props.getProperty("db.url");
        if (dbUrl == null || dbUrl.isEmpty()) {
            throw new ConfigException("Database URL required");
        }
        config.setDatabaseUrl(dbUrl);
        
        String dbUser = props.getProperty("db.user");
        config.setDatabaseUser(dbUser);
        
        String dbPass = props.getProperty("db.password");
        config.setDatabasePassword(dbPass);
        
        String poolSizeStr = props.getProperty("db.pool.size", "10");
        int poolSize = Integer.parseInt(poolSizeStr);
        config.setConnectionPoolSize(poolSize);
        
        // Parse cache settings
        String cacheEnabled = props.getProperty("cache.enabled", "true");
        config.setCacheEnabled(Boolean.parseBoolean(cacheEnabled));
        
        String cacheTtl = props.getProperty("cache.ttl", "3600");
        config.setCacheTtlSeconds(Integer.parseInt(cacheTtl));
        
        // Parse logging settings
        String logLevel = props.getProperty("log.level", "INFO");
        if (!Arrays.asList("DEBUG", "INFO", "WARN", "ERROR").contains(logLevel)) {
            throw new ConfigException("Invalid log level: " + logLevel);
        }
        config.setLogLevel(logLevel);
        
        String logFile = props.getProperty("log.file", "app.log");
        config.setLogFile(logFile);
        
        // Parse security settings
        String sslEnabled = props.getProperty("ssl.enabled", "false");
        config.setSslEnabled(Boolean.parseBoolean(sslEnabled));
        
        if (config.isSslEnabled()) {
            String keystore = props.getProperty("ssl.keystore");
            if (keystore == null) {
                throw new ConfigException("SSL keystore required");
            }
            config.setSslKeystore(keystore);
            config.setSslKeystorePassword(props.getProperty("ssl.keystore.password"));
        }
        
        return config;
    }
}"""
    },
    {
        "id": 71,
        "expected": "LongMethod",
        "description": "Invoice generator",
        "code": """
public class InvoiceGenerator {
    public Invoice generateInvoice(Order order) {
        Invoice invoice = new Invoice();
        invoice.setInvoiceNumber(generateInvoiceNumber());
        invoice.setInvoiceDate(new Date());
        invoice.setDueDate(calculateDueDate(30));
        
        // Set customer details
        Customer customer = order.getCustomer();
        invoice.setCustomerName(customer.getName());
        invoice.setCustomerEmail(customer.getEmail());
        invoice.setCustomerAddress(formatAddress(customer.getAddress()));
        
        // Set company details
        invoice.setCompanyName("ACME Corporation");
        invoice.setCompanyAddress("123 Business St, City, ST 12345");
        invoice.setCompanyPhone("1-800-555-1234");
        invoice.setCompanyEmail("billing@acme.com");
        
        // Calculate line items
        List<InvoiceLineItem> lineItems = new ArrayList<>();
        double subtotal = 0;
        
        for (OrderItem item : order.getItems()) {
            InvoiceLineItem lineItem = new InvoiceLineItem();
            lineItem.setDescription(item.getProduct().getName());
            lineItem.setQuantity(item.getQuantity());
            lineItem.setUnitPrice(item.getPrice());
            lineItem.setAmount(item.getQuantity() * item.getPrice());
            lineItems.add(lineItem);
            subtotal += lineItem.getAmount();
        }
        invoice.setLineItems(lineItems);
        invoice.setSubtotal(subtotal);
        
        // Calculate discount
        double discountAmount = 0;
        if (order.getDiscount() != null) {
            discountAmount = order.getDiscount();
            invoice.setDiscountDescription(order.getPromoCode());
            invoice.setDiscountAmount(discountAmount);
        }
        
        // Calculate tax
        double taxableAmount = subtotal - discountAmount;
        double taxRate = getTaxRate(customer.getAddress().getState());
        double taxAmount = taxableAmount * taxRate;
        invoice.setTaxRate(taxRate);
        invoice.setTaxAmount(taxAmount);
        
        // Calculate shipping
        double shippingAmount = order.getShipping();
        invoice.setShippingAmount(shippingAmount);
        
        // Calculate total
        double total = taxableAmount + taxAmount + shippingAmount;
        invoice.setTotalAmount(total);
        
        // Add payment terms
        invoice.setPaymentTerms("Net 30");
        invoice.setNotes("Thank you for your business!");
        
        // Save invoice
        invoiceRepository.save(invoice);
        
        return invoice;
    }
}"""
    },
    {
        "id": 72,
        "expected": "LongMethod",
        "description": "File upload handler",
        "code": """
public class FileUploadHandler {
    public UploadResult handleUpload(MultipartFile file, String userId) {
        // Validate file
        if (file == null || file.isEmpty()) {
            return UploadResult.failure("No file provided");
        }
        
        // Check file size
        long maxSize = 10 * 1024 * 1024; // 10MB
        if (file.getSize() > maxSize) {
            return UploadResult.failure("File too large. Max size: 10MB");
        }
        
        // Check file type
        String originalName = file.getOriginalFilename();
        String extension = originalName.substring(originalName.lastIndexOf(".") + 1).toLowerCase();
        List<String> allowedTypes = Arrays.asList("jpg", "jpeg", "png", "gif", "pdf", "doc", "docx");
        if (!allowedTypes.contains(extension)) {
            return UploadResult.failure("File type not allowed: " + extension);
        }
        
        // Check content type
        String contentType = file.getContentType();
        if (contentType == null || !isValidContentType(contentType)) {
            return UploadResult.failure("Invalid content type");
        }
        
        // Generate unique filename
        String uniqueName = UUID.randomUUID().toString() + "." + extension;
        
        // Create user directory
        Path userDir = Paths.get(uploadDir, userId);
        if (!Files.exists(userDir)) {
            Files.createDirectories(userDir);
        }
        
        // Save file
        Path targetPath = userDir.resolve(uniqueName);
        Files.copy(file.getInputStream(), targetPath, StandardCopyOption.REPLACE_EXISTING);
        
        // Create thumbnail if image
        String thumbnailPath = null;
        if (isImage(extension)) {
            BufferedImage original = ImageIO.read(targetPath.toFile());
            BufferedImage thumbnail = createThumbnail(original, 150, 150);
            String thumbName = "thumb_" + uniqueName;
            Path thumbPath = userDir.resolve(thumbName);
            ImageIO.write(thumbnail, extension, thumbPath.toFile());
            thumbnailPath = thumbPath.toString();
        }
        
        // Create file record
        FileRecord record = new FileRecord();
        record.setUserId(userId);
        record.setOriginalName(originalName);
        record.setStoredName(uniqueName);
        record.setPath(targetPath.toString());
        record.setThumbnailPath(thumbnailPath);
        record.setSize(file.getSize());
        record.setContentType(contentType);
        record.setUploadedAt(new Date());
        fileRepository.save(record);
        
        // Return success
        String downloadUrl = baseUrl + "/files/" + record.getId();
        return UploadResult.success(record.getId(), downloadUrl);
    }
}"""
    },
    {
        "id": 73,
        "expected": "LongMethod",
        "description": "Notification sender with many channels",
        "code": """
public class NotificationSender {
    public void sendNotification(User user, Notification notification) {
        // Get user preferences
        NotificationPreferences prefs = user.getNotificationPreferences();
        
        // Send email notification
        if (prefs.isEmailEnabled()) {
            String emailBody = buildEmailBody(notification);
            String subject = notification.getTitle();
            
            EmailMessage email = new EmailMessage();
            email.setTo(user.getEmail());
            email.setSubject(subject);
            email.setBody(emailBody);
            email.setHtml(true);
            
            try {
                emailService.send(email);
                logNotification(user, "EMAIL", notification, "SUCCESS");
            } catch (Exception e) {
                logNotification(user, "EMAIL", notification, "FAILED: " + e.getMessage());
            }
        }
        
        // Send SMS notification
        if (prefs.isSmsEnabled() && user.getPhone() != null) {
            String smsBody = truncate(notification.getMessage(), 160);
            
            try {
                smsService.send(user.getPhone(), smsBody);
                logNotification(user, "SMS", notification, "SUCCESS");
            } catch (Exception e) {
                logNotification(user, "SMS", notification, "FAILED: " + e.getMessage());
            }
        }
        
        // Send push notification
        if (prefs.isPushEnabled() && user.getDeviceToken() != null) {
            PushMessage push = new PushMessage();
            push.setToken(user.getDeviceToken());
            push.setTitle(notification.getTitle());
            push.setBody(notification.getMessage());
            push.setData(notification.getData());
            
            try {
                pushService.send(push);
                logNotification(user, "PUSH", notification, "SUCCESS");
            } catch (Exception e) {
                logNotification(user, "PUSH", notification, "FAILED: " + e.getMessage());
            }
        }
        
        // Send in-app notification
        if (prefs.isInAppEnabled()) {
            InAppNotification inApp = new InAppNotification();
            inApp.setUserId(user.getId());
            inApp.setTitle(notification.getTitle());
            inApp.setMessage(notification.getMessage());
            inApp.setType(notification.getType());
            inApp.setRead(false);
            inApp.setCreatedAt(new Date());
            
            inAppRepository.save(inApp);
            logNotification(user, "IN_APP", notification, "SUCCESS");
            
            // Send real-time update via WebSocket
            if (websocketSessions.containsKey(user.getId())) {
                websocketService.send(user.getId(), inApp);
            }
        }
        
        // Update notification status
        notification.setSentAt(new Date());
        notification.setStatus("SENT");
        notificationRepository.save(notification);
    }
}"""
    },
    {
        "id": 74,
        "expected": "LongMethod",
        "description": "Report aggregator",
        "code": """
public class ReportAggregator {
    public AggregatedReport aggregate(List<Report> reports, AggregationCriteria criteria) {
        AggregatedReport result = new AggregatedReport();
        result.setGeneratedAt(new Date());
        result.setCriteria(criteria);
        
        // Filter by date range
        List<Report> filtered = new ArrayList<>();
        for (Report report : reports) {
            if (criteria.getStartDate() != null && report.getDate().before(criteria.getStartDate())) {
                continue;
            }
            if (criteria.getEndDate() != null && report.getDate().after(criteria.getEndDate())) {
                continue;
            }
            filtered.add(report);
        }
        
        // Group by specified field
        Map<String, List<Report>> grouped = new HashMap<>();
        for (Report report : filtered) {
            String key = getGroupKey(report, criteria.getGroupBy());
            if (!grouped.containsKey(key)) {
                grouped.put(key, new ArrayList<>());
            }
            grouped.get(key).add(report);
        }
        
        // Calculate aggregations
        List<AggregationResult> aggregations = new ArrayList<>();
        for (Map.Entry<String, List<Report>> entry : grouped.entrySet()) {
            AggregationResult agg = new AggregationResult();
            agg.setGroupKey(entry.getKey());
            
            List<Report> groupReports = entry.getValue();
            agg.setCount(groupReports.size());
            
            // Calculate sum
            double sum = 0;
            for (Report r : groupReports) {
                sum += r.getValue();
            }
            agg.setSum(sum);
            
            // Calculate average
            agg.setAverage(sum / groupReports.size());
            
            // Calculate min and max
            double min = Double.MAX_VALUE;
            double max = Double.MIN_VALUE;
            for (Report r : groupReports) {
                if (r.getValue() < min) min = r.getValue();
                if (r.getValue() > max) max = r.getValue();
            }
            agg.setMin(min);
            agg.setMax(max);
            
            // Calculate standard deviation
            double variance = 0;
            for (Report r : groupReports) {
                variance += Math.pow(r.getValue() - agg.getAverage(), 2);
            }
            agg.setStdDev(Math.sqrt(variance / groupReports.size()));
            
            aggregations.add(agg);
        }
        
        result.setAggregations(aggregations);
        result.setTotalRecords(filtered.size());
        result.setGroupCount(aggregations.size());
        
        return result;
    }
}"""
    },
    {
        "id": 75,
        "expected": "LongMethod",
        "description": "JSON to XML converter",
        "code": """
public class JsonToXmlConverter {
    public String convert(String json) {
        StringBuilder xml = new StringBuilder();
        xml.append("<?xml version=\\"1.0\\" encoding=\\"UTF-8\\"?>\\n");
        
        // Parse JSON
        JSONObject jsonObj;
        try {
            jsonObj = new JSONObject(json);
        } catch (JSONException e) {
            throw new ConversionException("Invalid JSON: " + e.getMessage());
        }
        
        // Determine root element
        String rootName = "root";
        if (jsonObj.has("_root")) {
            rootName = jsonObj.getString("_root");
            jsonObj.remove("_root");
        }
        
        xml.append("<").append(rootName).append(">\\n");
        
        // Convert each key-value pair
        for (String key : jsonObj.keySet()) {
            Object value = jsonObj.get(key);
            
            if (value instanceof JSONObject) {
                // Nested object
                xml.append(convertObject(key, (JSONObject) value, 1));
            } else if (value instanceof JSONArray) {
                // Array
                JSONArray arr = (JSONArray) value;
                for (int i = 0; i < arr.length(); i++) {
                    Object item = arr.get(i);
                    if (item instanceof JSONObject) {
                        xml.append(convertObject(key, (JSONObject) item, 1));
                    } else {
                        xml.append(indent(1)).append("<").append(key).append(">");
                        xml.append(escapeXml(item.toString()));
                        xml.append("</").append(key).append(">\\n");
                    }
                }
            } else if (value == JSONObject.NULL) {
                // Null value
                xml.append(indent(1)).append("<").append(key).append(" null=\\"true\\"/>\\n");
            } else {
                // Simple value
                xml.append(indent(1)).append("<").append(key).append(">");
                xml.append(escapeXml(value.toString()));
                xml.append("</").append(key).append(">\\n");
            }
        }
        
        xml.append("</").append(rootName).append(">");
        
        // Validate output
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            builder.parse(new InputSource(new StringReader(xml.toString())));
        } catch (Exception e) {
            throw new ConversionException("Generated invalid XML: " + e.getMessage());
        }
        
        return xml.toString();
    }
}"""
    },
    
    # ========================================================================
    # FEATURE ENVY SAMPLES (76-85)
    # ========================================================================
    {
        "id": 76,
        "expected": "FeatureEnvy",
        "description": "Method using another class's data excessively",
        "code": """
public class OrderPrinter {
    public String formatOrder(Order order) {
        return "Order: " + order.getId() + "\\n" +
               "Customer: " + order.getCustomer().getName() + "\\n" +
               "Email: " + order.getCustomer().getEmail() + "\\n" +
               "Phone: " + order.getCustomer().getPhone() + "\\n" +
               "Address: " + order.getCustomer().getAddress().getStreet() + "\\n" +
               "City: " + order.getCustomer().getAddress().getCity() + "\\n" +
               "Total: " + order.getTotal();
    }
}"""
    },
    {
        "id": 77,
        "expected": "FeatureEnvy",
        "description": "Calculator accessing another object's internals",
        "code": """
public class ShippingCalculator {
    public double calculateShipping(Package pkg) {
        double weight = pkg.getWeight();
        double length = pkg.getDimensions().getLength();
        double width = pkg.getDimensions().getWidth();
        double height = pkg.getDimensions().getHeight();
        double volume = length * width * height;
        double dimWeight = volume / 139;
        return Math.max(weight, dimWeight) * 0.5;
    }
}"""
    },
    {
        "id": 78,
        "expected": "FeatureEnvy",
        "description": "Tax calculator envying employee data",
        "code": """
public class TaxCalculator {
    public double calculateTax(Employee emp) {
        double salary = emp.getSalary();
        double bonus = emp.getBonus();
        double benefits = emp.getBenefits().getHealthInsurance() + 
                         emp.getBenefits().getDentalInsurance() +
                         emp.getBenefits().getRetirement401k();
        double taxableIncome = salary + bonus - benefits;
        return taxableIncome * emp.getTaxBracket().getRate();
    }
}"""
    },
    {
        "id": 79,
        "expected": "FeatureEnvy",
        "description": "Report builder envying sale data",
        "code": """
public class SaleReportBuilder {
    public String buildReport(Sale sale) {
        return "Sale #" + sale.getId() + 
               " | Product: " + sale.getProduct().getName() +
               " | SKU: " + sale.getProduct().getSku() +
               " | Category: " + sale.getProduct().getCategory().getName() +
               " | Price: $" + sale.getProduct().getPrice() +
               " | Qty: " + sale.getQuantity() +
               " | Rep: " + sale.getSalesRep().getName();
    }
}"""
    },
    {
        "id": 80,
        "expected": "FeatureEnvy",
        "description": "Validator accessing user fields",
        "code": """
public class UserValidator {
    public boolean isEligible(User user) {
        return user.getAge() >= 18 &&
               user.getProfile().isVerified() &&
               user.getProfile().getCompleteness() > 80 &&
               user.getAccount().getBalance() >= 0 &&
               user.getAccount().getStatus().equals("ACTIVE") &&
               user.getSubscription().isActive();
    }
}"""
    },
    {
        "id": 81,
        "expected": "FeatureEnvy",
        "description": "Formatter using book details",
        "code": """
public class BookFormatter {
    public String formatCitation(Book book) {
        return book.getAuthor().getLastName() + ", " +
               book.getAuthor().getFirstName() + ". " +
               "\\"" + book.getTitle() + ".\\" " +
               book.getPublisher().getName() + ", " +
               book.getPublicationDate().getYear() + ".";
    }
}"""
    },
    {
        "id": 82,
        "expected": "FeatureEnvy",
        "description": "Discount calculator envying cart",
        "code": """
public class DiscountCalculator {
    public double calculateDiscount(ShoppingCart cart) {
        double total = cart.getSubtotal();
        int itemCount = cart.getItems().size();
        boolean hasPromo = cart.getPromoCode() != null;
        boolean isMember = cart.getCustomer().isMember();
        double memberDiscount = cart.getCustomer().getMembershipLevel().getDiscount();
        
        double discount = 0;
        if (hasPromo) discount += total * 0.1;
        if (isMember) discount += total * memberDiscount;
        if (itemCount > 5) discount += total * 0.05;
        return discount;
    }
}"""
    },
    {
        "id": 83,
        "expected": "FeatureEnvy",
        "description": "Invoice line creator accessing product",
        "code": """
public class InvoiceLineCreator {
    public InvoiceLine createLine(OrderItem item) {
        InvoiceLine line = new InvoiceLine();
        line.setProductName(item.getProduct().getName());
        line.setProductCode(item.getProduct().getCode());
        line.setUnitPrice(item.getProduct().getPrice());
        line.setQuantity(item.getQuantity());
        line.setTaxRate(item.getProduct().getTaxRate());
        line.setDiscount(item.getProduct().getCurrentDiscount());
        return line;
    }
}"""
    },
    {
        "id": 84,
        "expected": "FeatureEnvy",
        "description": "Summary builder accessing transaction",
        "code": """
public class TransactionSummary {
    public String summarize(Transaction tx) {
        return "From: " + tx.getSource().getAccountNumber() + 
               " (" + tx.getSource().getOwner().getName() + ")\\n" +
               "To: " + tx.getDestination().getAccountNumber() +
               " (" + tx.getDestination().getOwner().getName() + ")\\n" +
               "Amount: $" + tx.getAmount() +
               " Fee: $" + tx.getFee() +
               " Date: " + tx.getTimestamp();
    }
}"""
    },
    {
        "id": 85,
        "expected": "FeatureEnvy",
        "description": "Address formatter accessing location",
        "code": """
public class AddressFormatter {
    public String format(Location loc) {
        return loc.getAddress().getStreet() + "\\n" +
               loc.getAddress().getCity() + ", " +
               loc.getAddress().getState() + " " +
               loc.getAddress().getZipCode() + "\\n" +
               loc.getAddress().getCountry().getName() + 
               " (" + loc.getAddress().getCountry().getCode() + ")";
    }
}"""
    },
    
    # ========================================================================
    # ADDITIONAL FEATURE ENVY SAMPLES (101-115)
    # ========================================================================
    {
        "id": 101,
        "expected": "FeatureEnvy",
        "description": "Receipt printer accessing order details",
        "code": """
public class ReceiptPrinter {
    public String printReceipt(Order order) {
        StringBuilder sb = new StringBuilder();
        sb.append("Store: " + order.getStore().getName() + "\\n");
        sb.append("Address: " + order.getStore().getAddress() + "\\n");
        sb.append("Phone: " + order.getStore().getPhone() + "\\n");
        sb.append("Cashier: " + order.getCashier().getName() + "\\n");
        sb.append("Date: " + order.getTimestamp() + "\\n");
        sb.append("Items: " + order.getItems().size() + "\\n");
        sb.append("Subtotal: $" + order.getSubtotal() + "\\n");
        sb.append("Tax: $" + order.getTax() + "\\n");
        sb.append("Total: $" + order.getTotal() + "\\n");
        return sb.toString();
    }
}"""
    },
    {
        "id": 102,
        "expected": "FeatureEnvy",
        "description": "Loan eligibility checker accessing customer",
        "code": """
public class LoanEligibilityChecker {
    public boolean checkEligibility(Customer customer) {
        int creditScore = customer.getCreditReport().getScore();
        double income = customer.getFinancials().getAnnualIncome();
        double debt = customer.getFinancials().getTotalDebt();
        int yearsEmployed = customer.getEmployment().getYearsAtCurrentJob();
        boolean hasCollateral = customer.getAssets().hasCollateral();
        double debtToIncome = debt / income;
        
        return creditScore > 650 && 
               debtToIncome < 0.4 && 
               yearsEmployed >= 2 && 
               hasCollateral;
    }
}"""
    },
    {
        "id": 103,
        "expected": "FeatureEnvy",
        "description": "Email composer accessing contact info",
        "code": """
public class EmailComposer {
    public Email composeWelcome(Member member) {
        Email email = new Email();
        email.setTo(member.getContactInfo().getEmail());
        email.setSubject("Welcome " + member.getProfile().getFirstName());
        email.setBody("Dear " + member.getProfile().getFullName() + ",\\n" +
                     "Your membership ID is: " + member.getMembership().getId() + "\\n" +
                     "Level: " + member.getMembership().getLevel().getName() + "\\n" +
                     "Expires: " + member.getMembership().getExpiryDate());
        return email;
    }
}"""
    },
    {
        "id": 104,
        "expected": "FeatureEnvy",
        "description": "Grade calculator accessing student records",
        "code": """
public class GradeCalculator {
    public double calculateFinalGrade(Student student) {
        double homework = student.getGrades().getHomeworkAverage() * 0.2;
        double quizzes = student.getGrades().getQuizAverage() * 0.2;
        double midterm = student.getGrades().getMidtermScore() * 0.25;
        double finalExam = student.getGrades().getFinalExamScore() * 0.35;
        double participation = student.getAttendance().getParticipationScore();
        double bonus = student.getExtras().getBonusPoints();
        return homework + quizzes + midterm + finalExam + participation + bonus;
    }
}"""
    },
    {
        "id": 105,
        "expected": "FeatureEnvy",
        "description": "Insurance quote generator",
        "code": """
public class InsuranceQuoteGenerator {
    public Quote generateQuote(Applicant applicant) {
        int age = applicant.getPersonalInfo().getAge();
        String gender = applicant.getPersonalInfo().getGender();
        boolean smoker = applicant.getHealthInfo().isSmoker();
        double bmi = applicant.getHealthInfo().getBmi();
        int accidents = applicant.getDrivingRecord().getAccidentCount();
        int tickets = applicant.getDrivingRecord().getTicketCount();
        String vehicleType = applicant.getVehicle().getType();
        int vehicleYear = applicant.getVehicle().getYear();
        
        double baseRate = 500;
        if (age < 25) baseRate *= 1.5;
        if (smoker) baseRate *= 1.3;
        if (accidents > 0) baseRate *= (1 + accidents * 0.2);
        return new Quote(baseRate);
    }
}"""
    },
    {
        "id": 106,
        "expected": "FeatureEnvy",
        "description": "Payroll processor accessing employee",
        "code": """
public class PayrollProcessor {
    public Paycheck calculatePay(Employee employee) {
        double baseSalary = employee.getCompensation().getBaseSalary();
        double hourlyRate = employee.getCompensation().getHourlyRate();
        int hoursWorked = employee.getTimesheet().getTotalHours();
        int overtimeHours = employee.getTimesheet().getOvertimeHours();
        double bonus = employee.getPerformance().getBonusAmount();
        double taxRate = employee.getTaxInfo().getFederalRate();
        double stateTax = employee.getTaxInfo().getStateRate();
        double deductions = employee.getBenefits().getTotalDeductions();
        
        double gross = baseSalary + (hourlyRate * hoursWorked) + 
                      (overtimeHours * hourlyRate * 1.5) + bonus;
        double net = gross * (1 - taxRate - stateTax) - deductions;
        return new Paycheck(gross, net);
    }
}"""
    },
    {
        "id": 107,
        "expected": "FeatureEnvy",
        "description": "Property valuation calculator",
        "code": """
public class PropertyValuator {
    public double estimateValue(Property property) {
        double sqft = property.getDimensions().getSquareFootage();
        int bedrooms = property.getLayout().getBedroomCount();
        int bathrooms = property.getLayout().getBathroomCount();
        int yearBuilt = property.getDetails().getYearBuilt();
        String condition = property.getDetails().getCondition();
        double lotSize = property.getLot().getAcres();
        String neighborhood = property.getLocation().getNeighborhood();
        double avgPrice = property.getLocation().getAreaAveragePrice();
        
        double value = sqft * avgPrice;
        value += bedrooms * 10000;
        value += bathrooms * 8000;
        if ("excellent".equals(condition)) value *= 1.2;
        return value;
    }
}"""
    },
    {
        "id": 108,
        "expected": "FeatureEnvy",
        "description": "Flight booking validator",
        "code": """
public class FlightBookingValidator {
    public ValidationResult validate(Booking booking) {
        Passenger p = booking.getPassenger();
        Flight f = booking.getFlight();
        
        boolean validPassport = p.getDocuments().getPassport().isValid();
        boolean visaRequired = f.getDestination().requiresVisa(p.getNationality());
        boolean hasVisa = p.getDocuments().hasValidVisa(f.getDestination().getCountry());
        int baggageCount = booking.getBaggage().getCheckedCount();
        int allowedBaggage = f.getTicketClass().getBaggageAllowance();
        boolean seatAvailable = f.getSeating().isSeatAvailable(booking.getPreferredSeat());
        
        return new ValidationResult(validPassport && (!visaRequired || hasVisa) && 
                                   baggageCount <= allowedBaggage && seatAvailable);
    }
}"""
    },
    {
        "id": 109,
        "expected": "FeatureEnvy",
        "description": "Restaurant bill calculator",
        "code": """
public class BillCalculator {
    public Bill calculateBill(TableOrder tableOrder) {
        double foodTotal = tableOrder.getItems().getFoodSubtotal();
        double drinkTotal = tableOrder.getItems().getDrinkSubtotal();
        double subtotal = foodTotal + drinkTotal;
        double taxRate = tableOrder.getRestaurant().getTaxRate();
        double serviceFee = tableOrder.getRestaurant().getServiceFee();
        int partySize = tableOrder.getParty().getSize();
        boolean autoGratuity = partySize >= tableOrder.getRestaurant().getAutoGratuityThreshold();
        double gratuity = autoGratuity ? subtotal * 0.18 : 0;
        
        return new Bill(subtotal, subtotal * taxRate, serviceFee, gratuity);
    }
}"""
    },
    {
        "id": 110,
        "expected": "FeatureEnvy",
        "description": "Shipping label generator",
        "code": """
public class ShippingLabelGenerator {
    public Label generateLabel(Shipment shipment) {
        Label label = new Label();
        label.setSender(shipment.getSender().getName());
        label.setSenderAddress(shipment.getSender().getAddress().getFullAddress());
        label.setSenderPhone(shipment.getSender().getContact().getPhone());
        label.setRecipient(shipment.getRecipient().getName());
        label.setRecipientAddress(shipment.getRecipient().getAddress().getFullAddress());
        label.setRecipientPhone(shipment.getRecipient().getContact().getPhone());
        label.setWeight(shipment.getPackage().getWeight());
        label.setDimensions(shipment.getPackage().getDimensions().toString());
        label.setTrackingNumber(shipment.getTracking().getNumber());
        return label;
    }
}"""
    },
    {
        "id": 111,
        "expected": "FeatureEnvy",
        "description": "Medical record summarizer",
        "code": """
public class MedicalRecordSummarizer {
    public String summarize(Patient patient) {
        return "Patient: " + patient.getPersonalInfo().getFullName() + "\\n" +
               "DOB: " + patient.getPersonalInfo().getDateOfBirth() + "\\n" +
               "Blood Type: " + patient.getMedicalInfo().getBloodType() + "\\n" +
               "Allergies: " + patient.getMedicalInfo().getAllergies() + "\\n" +
               "Medications: " + patient.getPrescriptions().getCurrentMedications() + "\\n" +
               "Primary Doctor: " + patient.getCareTeam().getPrimaryPhysician().getName() + "\\n" +
               "Insurance: " + patient.getInsurance().getProvider().getName() + "\\n" +
               "Policy: " + patient.getInsurance().getPolicyNumber();
    }
}"""
    },
    {
        "id": 112,
        "expected": "FeatureEnvy",
        "description": "Rental car price calculator",
        "code": """
public class RentalPriceCalculator {
    public double calculatePrice(Rental rental) {
        double dailyRate = rental.getVehicle().getCategory().getDailyRate();
        int days = rental.getPeriod().getNumberOfDays();
        double insuranceRate = rental.getInsurance().getDailyRate();
        int driverAge = rental.getDriver().getAge();
        double youngDriverFee = driverAge < 25 ? rental.getLocation().getYoungDriverFee() : 0;
        double dropOffFee = rental.isOneWay() ? rental.getDropOffLocation().getDropOffFee() : 0;
        double mileageRate = rental.getVehicle().getMileagePolicy().getRatePerMile();
        int estimatedMiles = rental.getEstimatedMileage();
        
        return (dailyRate + insuranceRate) * days + youngDriverFee + dropOffFee + 
               (estimatedMiles * mileageRate);
    }
}"""
    },
    {
        "id": 113,
        "expected": "FeatureEnvy",
        "description": "Subscription renewal checker",
        "code": """
public class SubscriptionRenewalChecker {
    public RenewalStatus checkRenewal(Subscriber subscriber) {
        Date expiryDate = subscriber.getSubscription().getExpiryDate();
        String plan = subscriber.getSubscription().getPlan().getName();
        double price = subscriber.getSubscription().getPlan().getPrice();
        PaymentMethod pm = subscriber.getPaymentInfo().getDefaultMethod();
        boolean autoRenew = subscriber.getPreferences().isAutoRenewEnabled();
        double balance = subscriber.getAccount().getBalance();
        boolean hasCredit = subscriber.getAccount().hasStoreCredit();
        
        return new RenewalStatus(expiryDate, plan, price, pm.isValid(), 
                                autoRenew, balance >= price || hasCredit);
    }
}"""
    },
    {
        "id": 114,
        "expected": "FeatureEnvy",
        "description": "Event ticket printer",
        "code": """
public class TicketPrinter {
    public String printTicket(Reservation reservation) {
        return "=== EVENT TICKET ===\\n" +
               "Event: " + reservation.getEvent().getName() + "\\n" +
               "Date: " + reservation.getEvent().getDateTime() + "\\n" +
               "Venue: " + reservation.getEvent().getVenue().getName() + "\\n" +
               "Address: " + reservation.getEvent().getVenue().getAddress() + "\\n" +
               "Section: " + reservation.getSeat().getSection() + "\\n" +
               "Row: " + reservation.getSeat().getRow() + "\\n" +
               "Seat: " + reservation.getSeat().getNumber() + "\\n" +
               "Attendee: " + reservation.getAttendee().getName() + "\\n" +
               "Confirmation: " + reservation.getConfirmation().getCode();
    }
}"""
    },
    {
        "id": 115,
        "expected": "FeatureEnvy",
        "description": "Investment portfolio analyzer",
        "code": """
public class PortfolioAnalyzer {
    public Analysis analyzePortfolio(Investor investor) {
        double totalStocks = investor.getPortfolio().getStocks().getTotalValue();
        double totalBonds = investor.getPortfolio().getBonds().getTotalValue();
        double totalCash = investor.getPortfolio().getCash().getBalance();
        double totalValue = totalStocks + totalBonds + totalCash;
        double riskScore = investor.getProfile().getRiskTolerance();
        int age = investor.getPersonalInfo().getAge();
        double targetStock = investor.getGoals().getTargetStockAllocation();
        double actualStock = totalStocks / totalValue;
        
        return new Analysis(totalValue, actualStock, targetStock, 
                           riskScore, isBalanced(actualStock, targetStock, age));
    }
}"""
    },
    
    # ========================================================================
    # DEAD CODE SAMPLES (86-95)
    # ========================================================================
    {
        "id": 86,
        "expected": "DeadCode",
        "description": "Unused private methods",
        "code": """
public class DataProcessor {
    public void process(Data data) {
        validate(data);
        transform(data);
    }
    
    private void validate(Data data) { }
    private void transform(Data data) { }
    
    // Unused methods
    private void oldProcess(Data data) { }
    private void legacyTransform(Data data) { }
    private void deprecatedValidate(Data data) { }
}"""
    },
    {
        "id": 87,
        "expected": "DeadCode",
        "description": "Commented out code blocks",
        "code": """
public class Calculator {
    public int calculate(int a, int b) {
        // Old implementation
        // int result = a + b;
        // result = result * 2;
        // return result;
        
        // Another old approach
        /*
        if (a > b) {
            return a - b;
        }
        */
        
        return a + b;
    }
}"""
    },
    {
        "id": 88,
        "expected": "DeadCode",
        "description": "Unreachable code after return",
        "code": """
public class StatusChecker {
    public String getStatus(int code) {
        if (code == 200) {
            return "OK";
        }
        return "ERROR";
        
        // This code is never reached
        System.out.println("Processing complete");
        logStatus(code);
    }
    
    private void logStatus(int code) { }
}"""
    },
    {
        "id": 89,
        "expected": "DeadCode",
        "description": "Unused local variables",
        "code": """
public class ReportBuilder {
    public String buildReport(List<Item> items) {
        int totalCount = items.size();
        double totalValue = 0;
        String reportTitle = "Inventory Report";
        String unusedHeader = "This is not used";
        int unusedCounter = 0;
        Date unusedDate = new Date();
        
        for (Item item : items) {
            totalValue += item.getValue();
        }
        
        return reportTitle + ": " + totalCount + " items, $" + totalValue;
    }
}"""
    },
    {
        "id": 90,
        "expected": "DeadCode",
        "description": "Empty catch blocks and unused exception",
        "code": """
public class FileProcessor {
    public void process(String path) {
        try {
            File file = new File(path);
            // process file
        } catch (Exception e) {
            // TODO: handle this later
        }
        
        try {
            // another operation
        } catch (IOException ioe) {
            // silently ignore
        } catch (Exception ex) {
            // do nothing
        }
    }
}"""
    },
    {
        "id": 91,
        "expected": "DeadCode",
        "description": "Obsolete TODO comments and dead code",
        "code": """
public class UserManager {
    // TODO: Remove this old method (deprecated since v1.0)
    // private void oldCreateUser() { }
    
    /* 
     * FIXME: This entire block is no longer needed
     * private void migrateUsers() {
     *     // migration logic
     * }
     */
    
    public void createUser(User user) {
        // Actual implementation
    }
    
    // NOTE: Keep for reference but never called
    private void legacyCreate(User user) { }
}"""
    },
    {
        "id": 92,
        "expected": "DeadCode",
        "description": "Conditional that's always false",
        "code": """
public class FeatureToggle {
    private static final boolean DEBUG = false;
    
    public void execute() {
        if (DEBUG) {
            System.out.println("Debug mode");
            printDebugInfo();
            logDetailedTrace();
        }
        
        // Actual logic
        doWork();
    }
    
    private void printDebugInfo() { }
    private void logDetailedTrace() { }
    private void doWork() { }
}"""
    },
    {
        "id": 93,
        "expected": "DeadCode",
        "description": "Unused class fields",
        "code": """
public class OrderService {
    private OrderRepository repository;
    private EmailService emailService;
    private SmsService smsService;  // Never used
    private FaxService faxService;  // Obsolete
    private PagerService pagerService;  // Who uses pagers?
    
    public void createOrder(Order order) {
        repository.save(order);
        emailService.sendConfirmation(order);
    }
}"""
    },
    {
        "id": 94,
        "expected": "DeadCode",
        "description": "Methods with only comments",
        "code": """
public class Processor {
    public void process() {
        // Main processing
        doWork();
    }
    
    private void doWork() {
        // actual work here
    }
    
    private void placeholder1() {
        // Will implement later
    }
    
    private void placeholder2() {
        /* Future enhancement */
    }
    
    private void emptyMethod() {
    }
}"""
    },
    {
        "id": 95,
        "expected": "DeadCode",
        "description": "Unused imports and constants",
        "code": """
import java.util.List;
import java.util.Map;  // unused
import java.util.Set;  // unused
import java.io.File;   // unused

public class Constants {
    public static final String APP_NAME = "MyApp";
    public static final String OLD_APP_NAME = "OldApp";  // unused
    public static final int VERSION = 2;
    public static final int OLD_VERSION = 1;  // unused
    public static final String DEPRECATED_URL = "http://old.example.com";  // unused
    
    public String getName() {
        return APP_NAME + " v" + VERSION;
    }
}"""
    },
    
    # ========================================================================
    # MIXED/EDGE CASES (96-100)
    # ========================================================================
    {
        "id": 96,
        "expected": "Clean",
        "description": "Well-designed service class",
        "code": """
public class ProductService {
    private final ProductRepository repository;
    private final ProductValidator validator;
    
    public ProductService(ProductRepository repository, ProductValidator validator) {
        this.repository = repository;
        this.validator = validator;
    }
    
    public Product create(Product product) {
        validator.validate(product);
        return repository.save(product);
    }
    
    public Optional<Product> findById(Long id) {
        return repository.findById(id);
    }
    
    public void delete(Long id) {
        repository.deleteById(id);
    }
}"""
    },
    {
        "id": 97,
        "expected": "Clean",
        "description": "Interface implementation",
        "code": """
public class EmailNotifier implements Notifier {
    private final EmailClient client;
    
    public EmailNotifier(EmailClient client) {
        this.client = client;
    }
    
    @Override
    public void notify(User user, String message) {
        client.send(user.getEmail(), message);
    }
    
    @Override
    public boolean isAvailable() {
        return client.isConnected();
    }
}"""
    },
    {
        "id": 98,
        "expected": "Clean",
        "description": "Simple factory",
        "code": """
public class ConnectionFactory {
    private final String url;
    private final String username;
    private final String password;
    
    public ConnectionFactory(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }
    
    public Connection create() throws SQLException {
        return DriverManager.getConnection(url, username, password);
    }
}"""
    },
    {
        "id": 99,
        "expected": "GodClass",
        "description": "Monolithic application class",
        "code": """
public class MonolithicApp {
    private Database db;
    private FileSystem fs;
    private Network net;
    private Cache cache;
    private Queue queue;
    private Logger logger;
    
    public void initDatabase() { }
    public void closeDatabase() { }
    public void executeQuery(String sql) { }
    public void readFile(String path) { }
    public void writeFile(String path, String content) { }
    public void deleteFile(String path) { }
    public void sendRequest(String url) { }
    public void receiveResponse() { }
    public void cacheData(String key, Object value) { }
    public void clearCache() { }
    public void enqueue(Object item) { }
    public void dequeue() { }
    public void logInfo(String msg) { }
    public void logError(String msg) { }
    public void backup() { }
    public void restore() { }
}"""
    },
    {
        "id": 100,
        "expected": "DataClass",
        "description": "Simple DTO with getters/setters",
        "code": """
public class OrderDTO {
    private Long id;
    private String customerName;
    private Date orderDate;
    private double amount;
    private String status;
    
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getCustomerName() { return customerName; }
    public void setCustomerName(String customerName) { this.customerName = customerName; }
    public Date getOrderDate() { return orderDate; }
    public void setOrderDate(Date orderDate) { this.orderDate = orderDate; }
    public double getAmount() { return amount; }
    public void setAmount(double amount) { this.amount = amount; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}"""
    },
]


def run_tests():
    """Run all 100 test cases and display results."""
    print("\n" + "="*80)
    print("   🧪 RUNNING 100 TEST CASES FOR CODE SMELL DETECTION MODEL")
    print("="*80)
    print(f"   Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80 + "\n")
    
    # Load models
    print("📂 Loading models...")
    try:
        models = ps.load_models()
        print("   ✅ Models loaded successfully!\n")
    except Exception as e:
        print(f"   ❌ Failed to load models: {e}")
        return
    
    # Track results
    results = []
    correct = 0
    wrong = 0
    
    # Category counters
    category_stats = {
        "GodClass": {"total": 0, "correct": 0},
        "DataClass": {"total": 0, "correct": 0},
        "Clean": {"total": 0, "correct": 0},
        "LongMethod": {"total": 0, "correct": 0},
        "FeatureEnvy": {"total": 0, "correct": 0},
        "DeadCode": {"total": 0, "correct": 0},
    }
    
    # Run each test
    print("-"*80)
    print(f"{'#':>3} | {'Expected':^12} | {'Actual':^12} | {'Conf':>6} | {'Result':^6} | Description")
    print("-"*80)
    
    for sample in TEST_SAMPLES:
        test_id = sample["id"]
        expected = sample["expected"]
        description = sample["description"][:35]
        code = sample["code"]
        
        # Get prediction
        try:
            result = ps.predict_smell_compat(code, models)
            actual = result["prediction"]
            confidence = result["confidence"]
        except Exception as e:
            actual = "ERROR"
            confidence = 0.0
        
        # Check if correct
        is_correct = (actual == expected)
        status = "✅" if is_correct else "❌"
        
        if is_correct:
            correct += 1
        else:
            wrong += 1
        
        # Update category stats
        if expected in category_stats:
            category_stats[expected]["total"] += 1
            if is_correct:
                category_stats[expected]["correct"] += 1
        
        # Store result
        results.append({
            "id": test_id,
            "expected": expected,
            "actual": actual,
            "confidence": confidence,
            "correct": is_correct,
            "description": sample["description"]
        })
        
        # Print result
        print(f"{test_id:>3} | {expected:^12} | {actual:^12} | {confidence:>5.1f}% | {status:^6} | {description}")
    
    print("-"*80)
    
    # Print summary
    accuracy = (correct / len(TEST_SAMPLES)) * 100
    
    print("\n" + "="*80)
    print("   📊 TEST RESULTS SUMMARY")
    print("="*80)
    print(f"\n   Total Tests:    {len(TEST_SAMPLES)}")
    print(f"   ✅ Correct:      {correct}")
    print(f"   ❌ Wrong:        {wrong}")
    print(f"   📈 Accuracy:     {accuracy:.1f}%")
    
    # Print category breakdown
    print("\n   Category Breakdown:")
    print("   " + "-"*50)
    for cat, stats in category_stats.items():
        if stats["total"] > 0:
            cat_acc = (stats["correct"] / stats["total"]) * 100
            print(f"   {cat:15} | {stats['correct']:>2}/{stats['total']:<2} correct | {cat_acc:>5.1f}%")
    print("   " + "-"*50)
    
    # Print wrong predictions
    wrong_predictions = [r for r in results if not r["correct"]]
    if wrong_predictions:
        print(f"\n   ❌ INCORRECT PREDICTIONS ({len(wrong_predictions)}):")
        print("   " + "-"*70)
        for r in wrong_predictions:
            print(f"   #{r['id']:>3}: Expected {r['expected']:12} → Got {r['actual']:12} ({r['confidence']:.1f}%)")
            print(f"         {r['description'][:60]}")
        print("   " + "-"*70)
    
    print("\n" + "="*80)
    
    # Generate detailed report
    print("\n📝 Generating detailed report...")
    
    report_path = "test_100_results.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("="*80 + "\n")
        f.write("   100 TEST CASES - CODE SMELL DETECTION RESULTS\n")
        f.write("="*80 + "\n")
        f.write(f"   Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"   Accuracy: {accuracy:.1f}% ({correct}/{len(TEST_SAMPLES)})\n")
        f.write("="*80 + "\n\n")
        
        for r in results:
            status = "✅ CORRECT" if r["correct"] else "❌ WRONG"
            f.write(f"TEST #{r['id']}\n")
            f.write(f"  Description: {r['description']}\n")
            f.write(f"  Expected:    {r['expected']}\n")
            f.write(f"  Actual:      {r['actual']}\n")
            f.write(f"  Confidence:  {r['confidence']:.1f}%\n")
            f.write(f"  Result:      {status}\n")
            f.write("-"*40 + "\n")
    
    print(f"   ✅ Report saved to: {report_path}\n")
    
    return results


if __name__ == "__main__":
    run_tests()
