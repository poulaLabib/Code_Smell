"""
╔════════════════════════════════════════════════════════════════════════════════╗
║                    FINAL 100 TEST CASES - CODE SMELL DETECTION                  ║
║                  GodClass | DataClass | Clean | LongMethod | FeatureEnvy        ║
║                              (Excluding DeadCode)                               ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import predict_smell_extended as ps
from datetime import datetime
import json

# ============================================================================
# FINAL 100 TEST SAMPLES - 20 per category (5 categories)
# ============================================================================

FINAL_TEST_SAMPLES = [
    # ========================================================================
    # GOD CLASS SAMPLES (1-20)
    # ========================================================================
    {"id": 1, "expected": "GodClass", "description": "Order management system", "code": """
public class OrderManager {
    private Database db; private Logger logger; private EmailService email; private PaymentGateway payment;
    public void createOrder(Order o) { } public void updateOrder(Order o) { } public void deleteOrder(Order o) { }
    public void validateOrder(Order o) { } public void processPayment(Order o) { } public void sendConfirmation(Order o) { }
    public void updateInventory(Order o) { } public void generateInvoice(Order o) { } public void calculateShipping(Order o) { }
    public void applyDiscount(Order o) { } public void handleRefund(Order o) { } public void notifyWarehouse(Order o) { }
    public void trackShipment(Order o) { } public void generateReport() { } public void exportData() { }
}"""},
    {"id": 2, "expected": "GodClass", "description": "Application controller", "code": """
public class AppController {
    private UserService users; private ProductService products; private OrderService orders; private PaymentService payments;
    public void handleLogin() { } public void handleLogout() { } public void handleRegistration() { }
    public void displayProducts() { } public void addToCart() { } public void removeFromCart() { }
    public void checkout() { } public void processPayment() { } public void sendOrderConfirmation() { }
    public void generateDailyReport() { } public void handleCustomerSupport() { } public void manageInventory() { }
    public void updatePricing() { } public void handleReturns() { } public void sendNotifications() { }
}"""},
    {"id": 3, "expected": "GodClass", "description": "Hospital system", "code": """
public class HospitalSystem {
    private PatientRegistry patients; private DoctorRegistry doctors; private AppointmentScheduler scheduler;
    public void registerPatient(Patient p) { } public void updatePatientRecord(Patient p) { }
    public void scheduleAppointment(Appointment a) { } public void cancelAppointment(Appointment a) { }
    public void assignDoctor(Patient p, Doctor d) { } public void createPrescription(Prescription rx) { }
    public void orderLabTest(LabTest test) { } public void viewLabResults(Patient p) { }
    public void generateBill(Patient p) { } public void processInsuranceClaim(Claim c) { }
    public void updateInventory(Medicine m) { } public void dispenseMediation(Prescription rx) { }
    public void generateReport(String type) { } public void sendReminder(Patient p) { }
}"""},
    {"id": 4, "expected": "GodClass", "description": "E-commerce platform", "code": """
public class EcommercePlatform {
    private ProductCatalog catalog; private ShoppingCart cart; private PaymentProcessor payment; private ShippingService shipping;
    public void listProducts() { } public void searchProducts(String query) { } public void filterProducts(Map filters) { }
    public void addToCart(Product p) { } public void removeFromCart(Product p) { } public void updateCartQuantity(Product p, int qty) { }
    public void applyPromoCode(String code) { } public void calculateTotal() { } public void processCheckout() { }
    public void processPayment(Payment p) { } public void calculateShipping() { } public void trackOrder(Order o) { }
    public void submitReview(Review r) { } public void respondToReview(Review r) { } public void generateSalesReport() { }
}"""},
    {"id": 5, "expected": "GodClass", "description": "School management", "code": """
public class SchoolManagement {
    private StudentRegistry students; private TeacherRegistry teachers; private CourseManager courses; private GradeBook grades;
    public void enrollStudent(Student s) { } public void withdrawStudent(Student s) { } public void assignTeacher(Course c, Teacher t) { }
    public void createCourse(Course c) { } public void registerForCourse(Student s, Course c) { } public void dropCourse(Student s, Course c) { }
    public void recordAttendance(Student s, Course c) { } public void submitGrade(Student s, Course c, Grade g) { }
    public void calculateGPA(Student s) { } public void generateTranscript(Student s) { } public void collectFees(Student s) { }
    public void issueRefund(Student s) { } public void scheduleExam(Exam e) { } public void publishResults(Exam e) { }
}"""},
    {"id": 6, "expected": "GodClass", "description": "Banking system", "code": """
public class BankingSystem {
    private AccountRepository accounts; private TransactionProcessor transactions; private LoanProcessor loans;
    public void openAccount(Customer c) { } public void closeAccount(Account a) { } public void deposit(Account a, double amount) { }
    public void withdraw(Account a, double amount) { } public void transfer(Account from, Account to, double amount) { }
    public void applyForLoan(Customer c, Loan l) { } public void approveLoan(Loan l) { } public void rejectLoan(Loan l) { }
    public void issueCard(Customer c) { } public void blockCard(Card c) { } public void generateStatement(Account a) { }
    public void detectFraud(Transaction t) { } public void sendAlert(Customer c) { } public void calculateInterest(Account a) { }
}"""},
    {"id": 7, "expected": "GodClass", "description": "Social media platform", "code": """
public class SocialMediaPlatform {
    private UserManager users; private PostManager posts; private CommentManager comments; private MessageService messages;
    public void createUser(User u) { } public void updateProfile(User u) { } public void deleteUser(User u) { }
    public void createPost(Post p) { } public void editPost(Post p) { } public void deletePost(Post p) { }
    public void likePost(Post p, User u) { } public void commentOnPost(Post p, Comment c) { } public void sharePost(Post p, User u) { }
    public void sendMessage(User from, User to, Message m) { } public void followUser(User follower, User followed) { }
    public void unfollowUser(User follower, User followed) { } public void blockUser(User blocker, User blocked) { }
    public void reportContent(Content c) { } public void moderateContent(Content c) { }
}"""},
    {"id": 8, "expected": "GodClass", "description": "Project management", "code": """
public class ProjectManagement {
    private ProjectRepository projects; private TaskManager tasks; private TeamManager teams; private TimeTracker timeTracker;
    public void createProject(Project p) { } public void updateProject(Project p) { } public void deleteProject(Project p) { }
    public void addTask(Project p, Task t) { } public void updateTask(Task t) { } public void deleteTask(Task t) { }
    public void assignTask(Task t, User u) { } public void completeTask(Task t) { } public void addTeamMember(Project p, User u) { }
    public void removeTeamMember(Project p, User u) { } public void logTime(Task t, Duration d) { }
    public void generateReport(Project p) { } public void setMilestone(Project p, Milestone m) { } public void trackProgress(Project p) { }
}"""},
    {"id": 9, "expected": "GodClass", "description": "Restaurant manager", "code": """
public class RestaurantManager {
    private MenuService menu; private OrderService orders; private TableManager tables; private KitchenDisplay kitchen;
    public void addMenuItem(MenuItem item) { } public void updateMenuItem(MenuItem item) { } public void removeMenuItem(MenuItem item) { }
    public void createOrder(Order o) { } public void updateOrder(Order o) { } public void cancelOrder(Order o) { }
    public void assignTable(Reservation r) { } public void releaseTable(Table t) { } public void sendToKitchen(Order o) { }
    public void markAsReady(Order o) { } public void processPayment(Order o) { } public void splitBill(Order o, int ways) { }
    public void updateInventory(Item i) { } public void generateDailyReport() { } public void manageStaff(Staff s) { }
}"""},
    {"id": 10, "expected": "GodClass", "description": "Library system", "code": """
public class LibrarySystem {
    private BookCatalog books; private MemberRegistry members; private LoanManager loans; private FineCalculator fines;
    public void addBook(Book b) { } public void removeBook(Book b) { } public void updateBook(Book b) { }
    public void searchBooks(String query) { } public void registerMember(Member m) { } public void updateMember(Member m) { }
    public void cancelMembership(Member m) { } public void checkoutBook(Member m, Book b) { } public void returnBook(Member m, Book b) { }
    public void renewBook(Member m, Book b) { } public void reserveBook(Member m, Book b) { } public void cancelReservation(Reservation r) { }
    public void calculateFine(Loan l) { } public void collectFine(Member m) { } public void generateReport(String type) { }
}"""},
    {"id": 11, "expected": "GodClass", "description": "HR management", "code": """
public class HRManagement {
    private EmployeeRegistry employees; private PayrollProcessor payroll; private LeaveManager leaves; private PerformanceTracker performance;
    public void hireEmployee(Employee e) { } public void terminateEmployee(Employee e) { } public void updateEmployee(Employee e) { }
    public void processPayroll() { } public void calculateSalary(Employee e) { } public void requestLeave(Employee e, Leave l) { }
    public void approveLeave(Leave l) { } public void rejectLeave(Leave l) { } public void conductReview(Employee e) { }
    public void setGoals(Employee e, List goals) { } public void postJob(JobPosting jp) { } public void reviewApplications(JobPosting jp) { }
    public void scheduleInterview(Candidate c) { } public void enrollTraining(Employee e, Training t) { } public void generateReport(String type) { }
}"""},
    {"id": 12, "expected": "GodClass", "description": "CRM system", "code": """
public class CRMSystem {
    private ContactManager contacts; private LeadManager leads; private OpportunityManager opportunities; private CampaignManager campaigns;
    public void addContact(Contact c) { } public void updateContact(Contact c) { } public void deleteContact(Contact c) { }
    public void createLead(Lead l) { } public void convertLead(Lead l) { } public void qualifyLead(Lead l) { }
    public void createOpportunity(Opportunity o) { } public void updateOpportunity(Opportunity o) { } public void closeOpportunity(Opportunity o) { }
    public void launchCampaign(Campaign c) { } public void trackCampaign(Campaign c) { } public void createTicket(SupportTicket t) { }
    public void resolveTicket(SupportTicket t) { } public void escalateTicket(SupportTicket t) { } public void generateReport(String type) { }
}"""},
    {"id": 13, "expected": "GodClass", "description": "Inventory controller", "code": """
public class InventoryController {
    private ProductCatalog products; private WarehouseManager warehouses; private SupplierManager suppliers; private PurchaseOrderManager orders;
    public void addProduct(Product p) { } public void updateProduct(Product p) { } public void deleteProduct(Product p) { }
    public void checkStock(Product p) { } public void adjustStock(Product p, int qty) { } public void transferStock(Warehouse from, Warehouse to) { }
    public void createPurchaseOrder(PurchaseOrder po) { } public void receivePurchaseOrder(PurchaseOrder po) { }
    public void addSupplier(Supplier s) { } public void updateSupplier(Supplier s) { } public void trackShipment(Shipment s) { }
    public void generateStockReport() { } public void setReorderLevel(Product p, int level) { } public void autoReorder(Product p) { }
}"""},
    {"id": 14, "expected": "GodClass", "description": "Gaming platform", "code": """
public class GamingPlatform {
    private PlayerManager players; private GameLibrary games; private MatchmakingService matchmaking; private ChatService chat;
    public void registerPlayer(Player p) { } public void updateProfile(Player p) { } public void addFriend(Player p1, Player p2) { }
    public void removeFriend(Player p1, Player p2) { } public void startGame(Game g) { } public void endGame(Game g) { }
    public void findMatch(Player p) { } public void joinMatch(Player p, Match m) { } public void leaveMatch(Player p) { }
    public void sendMessage(Player p, String msg) { } public void updateLeaderboard(Player p) { } public void purchaseItem(Player p, Item i) { }
    public void redeemCode(Player p, String code) { } public void reportPlayer(Player reporter, Player reported) { } public void banPlayer(Player p) { }
}"""},
    {"id": 15, "expected": "GodClass", "description": "Event management", "code": """
public class EventManagement {
    private EventRegistry events; private VenueManager venues; private TicketService tickets; private AttendeeManager attendees;
    public void createEvent(Event e) { } public void updateEvent(Event e) { } public void cancelEvent(Event e) { }
    public void bookVenue(Event e, Venue v) { } public void releaseVenue(Venue v) { } public void sellTicket(Event e, Attendee a) { }
    public void refundTicket(Ticket t) { } public void checkIn(Attendee a) { } public void inviteSpeaker(Event e, Speaker s) { }
    public void confirmSpeaker(Speaker s) { } public void addSponsor(Event e, Sponsor s) { } public void manageBudget(Event e) { }
    public void sendReminders(Event e) { } public void collectFeedback(Event e) { } public void generateReport(Event e) { }
}"""},
    {"id": 16, "expected": "GodClass", "description": "Fitness application", "code": """
public class FitnessApp {
    private UserManager users; private WorkoutManager workouts; private NutritionTracker nutrition; private GoalTracker goals;
    public void registerUser(User u) { } public void updateProfile(User u) { } public void createWorkout(Workout w) { }
    public void logWorkout(User u, Workout w) { } public void trackCalories(User u, Meal m) { } public void logMeal(User u, Meal m) { }
    public void setGoal(User u, Goal g) { } public void trackProgress(User u) { } public void updateWeight(User u, double weight) { }
    public void followUser(User u1, User u2) { } public void shareWorkout(User u, Workout w) { } public void joinChallenge(User u, Challenge c) { }
    public void earnBadge(User u, Badge b) { } public void generateReport(User u) { } public void syncDevice(User u, Device d) { }
}"""},
    {"id": 17, "expected": "GodClass", "description": "Airline booking", "code": """
public class AirlineBooking {
    private FlightManager flights; private BookingManager bookings; private PassengerManager passengers; private SeatManager seats;
    public void searchFlights(SearchCriteria c) { } public void getFlightDetails(Flight f) { } public void createBooking(Booking b) { }
    public void cancelBooking(Booking b) { } public void modifyBooking(Booking b) { } public void selectSeat(Booking b, Seat s) { }
    public void addPassenger(Booking b, Passenger p) { } public void checkIn(Booking b) { } public void printBoardingPass(Booking b) { }
    public void processPayment(Payment p) { } public void refundPayment(Booking b) { } public void addBaggage(Booking b, Baggage bg) { }
    public void upgradeSeat(Booking b) { } public void sendConfirmation(Booking b) { } public void handleDelay(Flight f) { }
}"""},
    {"id": 18, "expected": "GodClass", "description": "Real estate platform", "code": """
public class RealEstatePlatform {
    private PropertyManager properties; private AgentManager agents; private ClientManager clients; private ListingService listings;
    public void addProperty(Property p) { } public void updateProperty(Property p) { } public void removeProperty(Property p) { }
    public void searchProperties(SearchCriteria c) { } public void createListing(Listing l) { } public void featureListing(Listing l) { }
    public void registerAgent(Agent a) { } public void assignAgent(Property p, Agent a) { } public void registerClient(Client c) { }
    public void scheduleViewing(Client c, Property p) { } public void submitOffer(Client c, Property p, Offer o) { }
    public void negotiateOffer(Offer o) { } public void createContract(Contract c) { } public void signContract(Contract c) { }
}"""},
    {"id": 19, "expected": "GodClass", "description": "Insurance system", "code": """
public class InsuranceSystem {
    private PolicyManager policies; private ClaimProcessor claims; private CustomerService customers; private UnderwritingEngine underwriting;
    public void createPolicy(Policy p) { } public void updatePolicy(Policy p) { } public void cancelPolicy(Policy p) { }
    public void renewPolicy(Policy p) { } public void calculatePremium(Policy p) { } public void submitClaim(Claim c) { }
    public void processClaim(Claim c) { } public void approveClaim(Claim c) { } public void rejectClaim(Claim c) { }
    public void registerCustomer(Customer c) { } public void updateCustomer(Customer c) { } public void assessRisk(Application a) { }
    public void generateQuote(Quote q) { } public void sendReminder(Policy p) { } public void generateReport(String type) { }
}"""},
    {"id": 20, "expected": "GodClass", "description": "Logistics management", "code": """
public class LogisticsManagement {
    private ShipmentTracker shipments; private RouteOptimizer routes; private FleetManager fleet; private WarehouseManager warehouses;
    public void createShipment(Shipment s) { } public void updateShipment(Shipment s) { } public void cancelShipment(Shipment s) { }
    public void trackShipment(Shipment s) { } public void optimizeRoute(Route r) { } public void assignDriver(Shipment s, Driver d) { }
    public void assignVehicle(Shipment s, Vehicle v) { } public void schedulePickup(Shipment s) { } public void scheduleDelivery(Shipment s) { }
    public void confirmDelivery(Shipment s) { } public void handleException(Shipment s) { } public void manageInventory(Warehouse w) { }
    public void maintainVehicle(Vehicle v) { } public void calculateCost(Shipment s) { } public void generateReport(String type) { }
}"""},

    # ========================================================================
    # DATA CLASS SAMPLES (21-40)
    # ========================================================================
    {"id": 21, "expected": "DataClass", "description": "Person entity", "code": """
public class Person {
    private String firstName; private String lastName; private int age; private String email;
    public String getFirstName() { return firstName; } public void setFirstName(String firstName) { this.firstName = firstName; }
    public String getLastName() { return lastName; } public void setLastName(String lastName) { this.lastName = lastName; }
    public int getAge() { return age; } public void setAge(int age) { this.age = age; }
    public String getEmail() { return email; } public void setEmail(String email) { this.email = email; }
}"""},
    {"id": 22, "expected": "DataClass", "description": "Address DTO", "code": """
public class Address {
    private String street; private String city; private String state; private String zipCode; private String country;
    public String getStreet() { return street; } public void setStreet(String street) { this.street = street; }
    public String getCity() { return city; } public void setCity(String city) { this.city = city; }
    public String getState() { return state; } public void setState(String state) { this.state = state; }
    public String getZipCode() { return zipCode; } public void setZipCode(String zipCode) { this.zipCode = zipCode; }
    public String getCountry() { return country; } public void setCountry(String country) { this.country = country; }
}"""},
    {"id": 23, "expected": "DataClass", "description": "Product DTO", "code": """
public class ProductDTO {
    private Long id; private String name; private String description; private double price; private int quantity;
    public Long getId() { return id; } public void setId(Long id) { this.id = id; }
    public String getName() { return name; } public void setName(String name) { this.name = name; }
    public String getDescription() { return description; } public void setDescription(String description) { this.description = description; }
    public double getPrice() { return price; } public void setPrice(double price) { this.price = price; }
    public int getQuantity() { return quantity; } public void setQuantity(int quantity) { this.quantity = quantity; }
}"""},
    {"id": 24, "expected": "DataClass", "description": "User profile", "code": """
public class UserProfile {
    private String username; private String email; private String phone; private Date birthDate; private String avatar;
    public String getUsername() { return username; } public void setUsername(String username) { this.username = username; }
    public String getEmail() { return email; } public void setEmail(String email) { this.email = email; }
    public String getPhone() { return phone; } public void setPhone(String phone) { this.phone = phone; }
    public Date getBirthDate() { return birthDate; } public void setBirthDate(Date birthDate) { this.birthDate = birthDate; }
    public String getAvatar() { return avatar; } public void setAvatar(String avatar) { this.avatar = avatar; }
}"""},
    {"id": 25, "expected": "DataClass", "description": "Order details", "code": """
public class OrderDetails {
    private Long orderId; private Date orderDate; private String status; private double total; private String shippingAddress;
    public Long getOrderId() { return orderId; } public void setOrderId(Long orderId) { this.orderId = orderId; }
    public Date getOrderDate() { return orderDate; } public void setOrderDate(Date orderDate) { this.orderDate = orderDate; }
    public String getStatus() { return status; } public void setStatus(String status) { this.status = status; }
    public double getTotal() { return total; } public void setTotal(double total) { this.total = total; }
    public String getShippingAddress() { return shippingAddress; } public void setShippingAddress(String shippingAddress) { this.shippingAddress = shippingAddress; }
}"""},
    {"id": 26, "expected": "DataClass", "description": "Employee record", "code": """
public class EmployeeRecord {
    private String employeeId; private String department; private String position; private double salary; private Date hireDate;
    public String getEmployeeId() { return employeeId; } public void setEmployeeId(String employeeId) { this.employeeId = employeeId; }
    public String getDepartment() { return department; } public void setDepartment(String department) { this.department = department; }
    public String getPosition() { return position; } public void setPosition(String position) { this.position = position; }
    public double getSalary() { return salary; } public void setSalary(double salary) { this.salary = salary; }
    public Date getHireDate() { return hireDate; } public void setHireDate(Date hireDate) { this.hireDate = hireDate; }
}"""},
    {"id": 27, "expected": "DataClass", "description": "Config settings", "code": """
public class ConfigSettings {
    private String serverUrl; private int port; private int timeout; private boolean enableSsl; private String apiKey;
    public String getServerUrl() { return serverUrl; } public void setServerUrl(String serverUrl) { this.serverUrl = serverUrl; }
    public int getPort() { return port; } public void setPort(int port) { this.port = port; }
    public int getTimeout() { return timeout; } public void setTimeout(int timeout) { this.timeout = timeout; }
    public boolean isEnableSsl() { return enableSsl; } public void setEnableSsl(boolean enableSsl) { this.enableSsl = enableSsl; }
    public String getApiKey() { return apiKey; } public void setApiKey(String apiKey) { this.apiKey = apiKey; }
}"""},
    {"id": 28, "expected": "DataClass", "description": "Book info", "code": """
public class BookInfo {
    private String isbn; private String title; private String author; private String publisher; private int year;
    public String getIsbn() { return isbn; } public void setIsbn(String isbn) { this.isbn = isbn; }
    public String getTitle() { return title; } public void setTitle(String title) { this.title = title; }
    public String getAuthor() { return author; } public void setAuthor(String author) { this.author = author; }
    public String getPublisher() { return publisher; } public void setPublisher(String publisher) { this.publisher = publisher; }
    public int getYear() { return year; } public void setYear(int year) { this.year = year; }
}"""},
    {"id": 29, "expected": "DataClass", "description": "Vehicle details", "code": """
public class VehicleDetails {
    private String vin; private String make; private String model; private int year; private String color;
    public String getVin() { return vin; } public void setVin(String vin) { this.vin = vin; }
    public String getMake() { return make; } public void setMake(String make) { this.make = make; }
    public String getModel() { return model; } public void setModel(String model) { this.model = model; }
    public int getYear() { return year; } public void setYear(int year) { this.year = year; }
    public String getColor() { return color; } public void setColor(String color) { this.color = color; }
}"""},
    {"id": 30, "expected": "DataClass", "description": "Customer contact", "code": """
public class CustomerContact {
    private String name; private String email; private String phone; private String company; private String notes;
    public String getName() { return name; } public void setName(String name) { this.name = name; }
    public String getEmail() { return email; } public void setEmail(String email) { this.email = email; }
    public String getPhone() { return phone; } public void setPhone(String phone) { this.phone = phone; }
    public String getCompany() { return company; } public void setCompany(String company) { this.company = company; }
    public String getNotes() { return notes; } public void setNotes(String notes) { this.notes = notes; }
}"""},
    {"id": 31, "expected": "DataClass", "description": "Payment info", "code": """
public class PaymentInfo {
    private String cardNumber; private String cardHolder; private String expiryDate; private String cvv; private String billingAddress;
    public String getCardNumber() { return cardNumber; } public void setCardNumber(String cardNumber) { this.cardNumber = cardNumber; }
    public String getCardHolder() { return cardHolder; } public void setCardHolder(String cardHolder) { this.cardHolder = cardHolder; }
    public String getExpiryDate() { return expiryDate; } public void setExpiryDate(String expiryDate) { this.expiryDate = expiryDate; }
    public String getCvv() { return cvv; } public void setCvv(String cvv) { this.cvv = cvv; }
    public String getBillingAddress() { return billingAddress; } public void setBillingAddress(String billingAddress) { this.billingAddress = billingAddress; }
}"""},
    {"id": 32, "expected": "DataClass", "description": "Student record", "code": """
public class StudentRecord {
    private String studentId; private String name; private String major; private double gpa; private int credits;
    public String getStudentId() { return studentId; } public void setStudentId(String studentId) { this.studentId = studentId; }
    public String getName() { return name; } public void setName(String name) { this.name = name; }
    public String getMajor() { return major; } public void setMajor(String major) { this.major = major; }
    public double getGpa() { return gpa; } public void setGpa(double gpa) { this.gpa = gpa; }
    public int getCredits() { return credits; } public void setCredits(int credits) { this.credits = credits; }
}"""},
    {"id": 33, "expected": "DataClass", "description": "Event data", "code": """
public class EventData {
    private String eventId; private String title; private Date startTime; private Date endTime; private String location;
    public String getEventId() { return eventId; } public void setEventId(String eventId) { this.eventId = eventId; }
    public String getTitle() { return title; } public void setTitle(String title) { this.title = title; }
    public Date getStartTime() { return startTime; } public void setStartTime(Date startTime) { this.startTime = startTime; }
    public Date getEndTime() { return endTime; } public void setEndTime(Date endTime) { this.endTime = endTime; }
    public String getLocation() { return location; } public void setLocation(String location) { this.location = location; }
}"""},
    {"id": 34, "expected": "DataClass", "description": "Message entity", "code": """
public class MessageEntity {
    private Long id; private String sender; private String recipient; private String content; private Date timestamp;
    public Long getId() { return id; } public void setId(Long id) { this.id = id; }
    public String getSender() { return sender; } public void setSender(String sender) { this.sender = sender; }
    public String getRecipient() { return recipient; } public void setRecipient(String recipient) { this.recipient = recipient; }
    public String getContent() { return content; } public void setContent(String content) { this.content = content; }
    public Date getTimestamp() { return timestamp; } public void setTimestamp(Date timestamp) { this.timestamp = timestamp; }
}"""},
    {"id": 35, "expected": "DataClass", "description": "Flight info", "code": """
public class FlightInfo {
    private String flightNumber; private String origin; private String destination; private Date departureTime; private Date arrivalTime;
    public String getFlightNumber() { return flightNumber; } public void setFlightNumber(String flightNumber) { this.flightNumber = flightNumber; }
    public String getOrigin() { return origin; } public void setOrigin(String origin) { this.origin = origin; }
    public String getDestination() { return destination; } public void setDestination(String destination) { this.destination = destination; }
    public Date getDepartureTime() { return departureTime; } public void setDepartureTime(Date departureTime) { this.departureTime = departureTime; }
    public Date getArrivalTime() { return arrivalTime; } public void setArrivalTime(Date arrivalTime) { this.arrivalTime = arrivalTime; }
}"""},
    {"id": 36, "expected": "DataClass", "description": "Hotel room", "code": """
public class HotelRoom {
    private String roomNumber; private String roomType; private double pricePerNight; private int capacity; private boolean available;
    public String getRoomNumber() { return roomNumber; } public void setRoomNumber(String roomNumber) { this.roomNumber = roomNumber; }
    public String getRoomType() { return roomType; } public void setRoomType(String roomType) { this.roomType = roomType; }
    public double getPricePerNight() { return pricePerNight; } public void setPricePerNight(double pricePerNight) { this.pricePerNight = pricePerNight; }
    public int getCapacity() { return capacity; } public void setCapacity(int capacity) { this.capacity = capacity; }
    public boolean isAvailable() { return available; } public void setAvailable(boolean available) { this.available = available; }
}"""},
    {"id": 37, "expected": "DataClass", "description": "Movie info", "code": """
public class MovieInfo {
    private String movieId; private String title; private String director; private int duration; private String genre;
    public String getMovieId() { return movieId; } public void setMovieId(String movieId) { this.movieId = movieId; }
    public String getTitle() { return title; } public void setTitle(String title) { this.title = title; }
    public String getDirector() { return director; } public void setDirector(String director) { this.director = director; }
    public int getDuration() { return duration; } public void setDuration(int duration) { this.duration = duration; }
    public String getGenre() { return genre; } public void setGenre(String genre) { this.genre = genre; }
}"""},
    {"id": 38, "expected": "DataClass", "description": "Recipe data", "code": """
public class RecipeData {
    private String recipeId; private String name; private String ingredients; private int prepTime; private int cookTime;
    public String getRecipeId() { return recipeId; } public void setRecipeId(String recipeId) { this.recipeId = recipeId; }
    public String getName() { return name; } public void setName(String name) { this.name = name; }
    public String getIngredients() { return ingredients; } public void setIngredients(String ingredients) { this.ingredients = ingredients; }
    public int getPrepTime() { return prepTime; } public void setPrepTime(int prepTime) { this.prepTime = prepTime; }
    public int getCookTime() { return cookTime; } public void setCookTime(int cookTime) { this.cookTime = cookTime; }
}"""},
    {"id": 39, "expected": "DataClass", "description": "Weather data", "code": """
public class WeatherData {
    private String location; private double temperature; private int humidity; private double windSpeed; private String condition;
    public String getLocation() { return location; } public void setLocation(String location) { this.location = location; }
    public double getTemperature() { return temperature; } public void setTemperature(double temperature) { this.temperature = temperature; }
    public int getHumidity() { return humidity; } public void setHumidity(int humidity) { this.humidity = humidity; }
    public double getWindSpeed() { return windSpeed; } public void setWindSpeed(double windSpeed) { this.windSpeed = windSpeed; }
    public String getCondition() { return condition; } public void setCondition(String condition) { this.condition = condition; }
}"""},
    {"id": 40, "expected": "DataClass", "description": "Notification bean", "code": """
public class NotificationBean {
    private Long notificationId; private String title; private String message; private boolean read; private Date createdAt;
    public Long getNotificationId() { return notificationId; } public void setNotificationId(Long notificationId) { this.notificationId = notificationId; }
    public String getTitle() { return title; } public void setTitle(String title) { this.title = title; }
    public String getMessage() { return message; } public void setMessage(String message) { this.message = message; }
    public boolean isRead() { return read; } public void setRead(boolean read) { this.read = read; }
    public Date getCreatedAt() { return createdAt; } public void setCreatedAt(Date createdAt) { this.createdAt = createdAt; }
}"""},

    # ========================================================================
    # CLEAN CODE SAMPLES (41-60)
    # ========================================================================
    {"id": 41, "expected": "Clean", "description": "User service", "code": """
public class UserService {
    private final UserRepository repository;
    public UserService(UserRepository repository) { this.repository = repository; }
    public User findById(Long id) { return repository.findById(id); }
    public User save(User user) { return repository.save(user); }
}"""},
    {"id": 42, "expected": "Clean", "description": "Calculator", "code": """
public class Calculator {
    public int add(int a, int b) { return a + b; }
    public int subtract(int a, int b) { return a - b; }
    public int multiply(int a, int b) { return a * b; }
    public double divide(int a, int b) { if (b == 0) throw new IllegalArgumentException(); return (double) a / b; }
}"""},
    {"id": 43, "expected": "Clean", "description": "Email validator", "code": """
public class EmailValidator {
    private static final Pattern EMAIL_PATTERN = Pattern.compile("^[A-Za-z0-9+_.-]+@(.+)$");
    public boolean isValid(String email) {
        if (email == null || email.isEmpty()) { return false; }
        return EMAIL_PATTERN.matcher(email).matches();
    }
}"""},
    {"id": 44, "expected": "Clean", "description": "Logger wrapper", "code": """
public class AppLogger {
    private final Logger logger;
    public AppLogger(Class<?> clazz) { this.logger = LoggerFactory.getLogger(clazz); }
    public void info(String message) { logger.info(message); }
    public void error(String message, Throwable t) { logger.error(message, t); }
}"""},
    {"id": 45, "expected": "Clean", "description": "Date formatter", "code": """
public class DateFormatter {
    private final DateTimeFormatter formatter;
    public DateFormatter(String pattern) { this.formatter = DateTimeFormatter.ofPattern(pattern); }
    public String format(LocalDate date) { return date.format(formatter); }
    public LocalDate parse(String dateString) { return LocalDate.parse(dateString, formatter); }
}"""},
    {"id": 46, "expected": "Clean", "description": "File reader", "code": """
public class FileReader {
    public String readContent(Path filePath) throws IOException { return Files.readString(filePath); }
    public List<String> readLines(Path filePath) throws IOException { return Files.readAllLines(filePath); }
    public boolean exists(Path filePath) { return Files.exists(filePath); }
}"""},
    {"id": 47, "expected": "Clean", "description": "Password hasher", "code": """
public class PasswordHasher {
    private final BCryptPasswordEncoder encoder;
    public PasswordHasher() { this.encoder = new BCryptPasswordEncoder(); }
    public String hash(String password) { return encoder.encode(password); }
    public boolean verify(String password, String hash) { return encoder.matches(password, hash); }
}"""},
    {"id": 48, "expected": "Clean", "description": "Queue implementation", "code": """
public class SimpleQueue<T> {
    private final LinkedList<T> items = new LinkedList<>();
    public void enqueue(T item) { items.addLast(item); }
    public T dequeue() { return items.removeFirst(); }
    public boolean isEmpty() { return items.isEmpty(); }
    public int size() { return items.size(); }
}"""},
    {"id": 49, "expected": "Clean", "description": "Counter class", "code": """
public class Counter {
    private int count;
    public Counter() { this.count = 0; }
    public void increment() { count++; }
    public void decrement() { count--; }
    public int getCount() { return count; }
    public void reset() { count = 0; }
}"""},
    {"id": 50, "expected": "Clean", "description": "String utils", "code": """
public class StringUtils {
    public boolean isEmpty(String str) { return str == null || str.isEmpty(); }
    public String capitalize(String str) { if (isEmpty(str)) return str; return str.substring(0, 1).toUpperCase() + str.substring(1); }
    public String reverse(String str) { return new StringBuilder(str).reverse().toString(); }
}"""},
    {"id": 51, "expected": "Clean", "description": "Price calculator", "code": """
public class PriceCalculator {
    private final double taxRate;
    public PriceCalculator(double taxRate) { this.taxRate = taxRate; }
    public double calculateTax(double price) { return price * taxRate; }
    public double calculateTotal(double price) { return price + calculateTax(price); }
}"""},
    {"id": 52, "expected": "Clean", "description": "Repository base", "code": """
public class BaseRepository<T> {
    private final EntityManager em;
    private final Class<T> entityClass;
    public BaseRepository(EntityManager em, Class<T> entityClass) { this.em = em; this.entityClass = entityClass; }
    public T findById(Long id) { return em.find(entityClass, id); }
    public void save(T entity) { em.persist(entity); }
}"""},
    {"id": 53, "expected": "Clean", "description": "Timer utility", "code": """
public class Timer {
    private long startTime;
    public void start() { startTime = System.currentTimeMillis(); }
    public long getElapsedTime() { return System.currentTimeMillis() - startTime; }
    public void reset() { startTime = 0; }
}"""},
    {"id": 54, "expected": "Clean", "description": "Random generator", "code": """
public class RandomGenerator {
    private final Random random = new Random();
    public int nextInt(int bound) { return random.nextInt(bound); }
    public double nextDouble() { return random.nextDouble(); }
    public boolean nextBoolean() { return random.nextBoolean(); }
}"""},
    {"id": 55, "expected": "Clean", "description": "Event publisher", "code": """
public class EventPublisher {
    private final List<EventListener> listeners = new ArrayList<>();
    public void subscribe(EventListener listener) { listeners.add(listener); }
    public void unsubscribe(EventListener listener) { listeners.remove(listener); }
    public void publish(Event event) { listeners.forEach(l -> l.onEvent(event)); }
}"""},
    {"id": 56, "expected": "Clean", "description": "Cache implementation", "code": """
public class SimpleCache<K, V> {
    private final Map<K, V> cache = new HashMap<>();
    public void put(K key, V value) { cache.put(key, value); }
    public V get(K key) { return cache.get(key); }
    public boolean contains(K key) { return cache.containsKey(key); }
    public void clear() { cache.clear(); }
}"""},
    {"id": 57, "expected": "Clean", "description": "Stack implementation", "code": """
public class Stack<T> {
    private final List<T> items = new ArrayList<>();
    public void push(T item) { items.add(item); }
    public T pop() { return items.remove(items.size() - 1); }
    public T peek() { return items.get(items.size() - 1); }
    public boolean isEmpty() { return items.isEmpty(); }
}"""},
    {"id": 58, "expected": "Clean", "description": "Age validator", "code": """
public class AgeValidator implements Validator<Integer> {
    private final int minAge;
    private final int maxAge;
    public AgeValidator(int minAge, int maxAge) { this.minAge = minAge; this.maxAge = maxAge; }
    public boolean isValid(Integer age) { return age >= minAge && age <= maxAge; }
}"""},
    {"id": 59, "expected": "Clean", "description": "Temperature converter", "code": """
public class TemperatureConverter {
    public double celsiusToFahrenheit(double celsius) { return (celsius * 9 / 5) + 32; }
    public double fahrenheitToCelsius(double fahrenheit) { return (fahrenheit - 32) * 5 / 9; }
    public double celsiusToKelvin(double celsius) { return celsius + 273.15; }
}"""},
    {"id": 60, "expected": "Clean", "description": "UUID generator", "code": """
public class UUIDGenerator {
    public String generate() { return UUID.randomUUID().toString(); }
    public String generateShort() { return UUID.randomUUID().toString().substring(0, 8); }
    public boolean isValid(String uuid) { try { UUID.fromString(uuid); return true; } catch (Exception e) { return false; } }
}"""},

    # ========================================================================
    # FEATURE ENVY SAMPLES (61-80)
    # ========================================================================
    {"id": 61, "expected": "FeatureEnvy", "description": "Order printer", "code": """
public class OrderPrinter {
    public String formatOrder(Order order) {
        return "Order: " + order.getId() + "\\n" + "Customer: " + order.getCustomer().getName() + "\\n" +
               "Email: " + order.getCustomer().getEmail() + "\\n" + "Phone: " + order.getCustomer().getPhone() + "\\n" +
               "Address: " + order.getCustomer().getAddress().getStreet() + "\\n" + "City: " + order.getCustomer().getAddress().getCity();
    }
}"""},
    {"id": 62, "expected": "FeatureEnvy", "description": "Shipping calculator", "code": """
public class ShippingCalculator {
    public double calculateShipping(Package pkg) {
        double weight = pkg.getWeight(); double length = pkg.getDimensions().getLength();
        double width = pkg.getDimensions().getWidth(); double height = pkg.getDimensions().getHeight();
        double volume = length * width * height; double dimWeight = volume / 139;
        return Math.max(weight, dimWeight) * 0.5;
    }
}"""},
    {"id": 63, "expected": "FeatureEnvy", "description": "Tax calculator", "code": """
public class TaxCalculator {
    public double calculateTax(Employee emp) {
        double salary = emp.getSalary(); double bonus = emp.getBonus();
        double benefits = emp.getBenefits().getHealthInsurance() + emp.getBenefits().getDentalInsurance() + emp.getBenefits().getRetirement401k();
        double taxableIncome = salary + bonus - benefits;
        return taxableIncome * emp.getTaxBracket().getRate();
    }
}"""},
    {"id": 64, "expected": "FeatureEnvy", "description": "Sale report builder", "code": """
public class SaleReportBuilder {
    public String buildReport(Sale sale) {
        return "Sale #" + sale.getId() + " | Product: " + sale.getProduct().getName() +
               " | SKU: " + sale.getProduct().getSku() + " | Category: " + sale.getProduct().getCategory().getName() +
               " | Price: $" + sale.getProduct().getPrice() + " | Qty: " + sale.getQuantity();
    }
}"""},
    {"id": 65, "expected": "FeatureEnvy", "description": "User validator", "code": """
public class UserValidator {
    public boolean isEligible(User user) {
        return user.getAge() >= 18 && user.getProfile().isVerified() && user.getProfile().getCompleteness() > 80 &&
               user.getAccount().getBalance() >= 0 && user.getAccount().getStatus().equals("ACTIVE") && user.getSubscription().isActive();
    }
}"""},
    {"id": 66, "expected": "FeatureEnvy", "description": "Book formatter", "code": """
public class BookFormatter {
    public String formatCitation(Book book) {
        return book.getAuthor().getLastName() + ", " + book.getAuthor().getFirstName() + ". " +
               "\\"" + book.getTitle() + ".\\" " + book.getPublisher().getName() + ", " + book.getPublicationDate().getYear() + ".";
    }
}"""},
    {"id": 67, "expected": "FeatureEnvy", "description": "Discount calculator", "code": """
public class DiscountCalculator {
    public double calculateDiscount(ShoppingCart cart) {
        double total = cart.getSubtotal(); int itemCount = cart.getItems().size();
        boolean hasPromo = cart.getPromoCode() != null; boolean isMember = cart.getCustomer().isMember();
        double memberDiscount = cart.getCustomer().getMembershipLevel().getDiscount();
        double discount = 0; if (hasPromo) discount += total * 0.1; if (isMember) discount += total * memberDiscount;
        return discount;
    }
}"""},
    {"id": 68, "expected": "FeatureEnvy", "description": "Invoice line creator", "code": """
public class InvoiceLineCreator {
    public InvoiceLine createLine(OrderItem item) {
        InvoiceLine line = new InvoiceLine(); line.setProductName(item.getProduct().getName());
        line.setProductCode(item.getProduct().getCode()); line.setUnitPrice(item.getProduct().getPrice());
        line.setQuantity(item.getQuantity()); line.setTaxRate(item.getProduct().getTaxRate());
        return line;
    }
}"""},
    {"id": 69, "expected": "FeatureEnvy", "description": "Transaction summary", "code": """
public class TransactionSummary {
    public String summarize(Transaction tx) {
        return "From: " + tx.getSource().getAccountNumber() + " (" + tx.getSource().getOwner().getName() + ")\\n" +
               "To: " + tx.getDestination().getAccountNumber() + " (" + tx.getDestination().getOwner().getName() + ")\\n" +
               "Amount: $" + tx.getAmount() + " Fee: $" + tx.getFee();
    }
}"""},
    {"id": 70, "expected": "FeatureEnvy", "description": "Address formatter", "code": """
public class AddressFormatter {
    public String format(Location loc) {
        return loc.getAddress().getStreet() + "\\n" + loc.getAddress().getCity() + ", " +
               loc.getAddress().getState() + " " + loc.getAddress().getZipCode() + "\\n" +
               loc.getAddress().getCountry().getName() + " (" + loc.getAddress().getCountry().getCode() + ")";
    }
}"""},
    {"id": 71, "expected": "FeatureEnvy", "description": "Receipt printer", "code": """
public class ReceiptPrinter {
    public String printReceipt(Order order) {
        StringBuilder sb = new StringBuilder();
        sb.append("Store: " + order.getStore().getName()); sb.append("Address: " + order.getStore().getAddress());
        sb.append("Cashier: " + order.getCashier().getName()); sb.append("Total: $" + order.getTotal());
        return sb.toString();
    }
}"""},
    {"id": 72, "expected": "FeatureEnvy", "description": "Loan eligibility checker", "code": """
public class LoanEligibilityChecker {
    public boolean checkEligibility(Customer customer) {
        int creditScore = customer.getCreditReport().getScore();
        double income = customer.getFinancials().getAnnualIncome(); double debt = customer.getFinancials().getTotalDebt();
        int yearsEmployed = customer.getEmployment().getYearsAtCurrentJob();
        return creditScore > 650 && (debt / income) < 0.4 && yearsEmployed >= 2;
    }
}"""},
    {"id": 73, "expected": "FeatureEnvy", "description": "Email composer", "code": """
public class EmailComposer {
    public Email composeWelcome(Member member) {
        Email email = new Email(); email.setTo(member.getContactInfo().getEmail());
        email.setSubject("Welcome " + member.getProfile().getFirstName());
        email.setBody("Your membership ID is: " + member.getMembership().getId() + " Level: " + member.getMembership().getLevel().getName());
        return email;
    }
}"""},
    {"id": 74, "expected": "FeatureEnvy", "description": "Grade calculator", "code": """
public class GradeCalculator {
    public double calculateFinalGrade(Student student) {
        double homework = student.getGrades().getHomeworkAverage() * 0.2;
        double quizzes = student.getGrades().getQuizAverage() * 0.2;
        double midterm = student.getGrades().getMidtermScore() * 0.25;
        double finalExam = student.getGrades().getFinalExamScore() * 0.35;
        return homework + quizzes + midterm + finalExam;
    }
}"""},
    {"id": 75, "expected": "FeatureEnvy", "description": "Insurance quote generator", "code": """
public class InsuranceQuoteGenerator {
    public Quote generateQuote(Applicant applicant) {
        int age = applicant.getPersonalInfo().getAge(); boolean smoker = applicant.getHealthInfo().isSmoker();
        int accidents = applicant.getDrivingRecord().getAccidentCount();
        double baseRate = 500; if (age < 25) baseRate *= 1.5; if (smoker) baseRate *= 1.3;
        return new Quote(baseRate);
    }
}"""},
    {"id": 76, "expected": "FeatureEnvy", "description": "Payroll processor", "code": """
public class PayrollProcessor {
    public Paycheck calculatePay(Employee employee) {
        double baseSalary = employee.getCompensation().getBaseSalary();
        int hoursWorked = employee.getTimesheet().getTotalHours();
        double bonus = employee.getPerformance().getBonusAmount();
        double taxRate = employee.getTaxInfo().getFederalRate();
        double gross = baseSalary + bonus; double net = gross * (1 - taxRate);
        return new Paycheck(gross, net);
    }
}"""},
    {"id": 77, "expected": "FeatureEnvy", "description": "Property valuator", "code": """
public class PropertyValuator {
    public double estimateValue(Property property) {
        double sqft = property.getDimensions().getSquareFootage();
        int bedrooms = property.getLayout().getBedroomCount(); int bathrooms = property.getLayout().getBathroomCount();
        String condition = property.getDetails().getCondition();
        double avgPrice = property.getLocation().getAreaAveragePrice();
        return sqft * avgPrice + bedrooms * 10000 + bathrooms * 8000;
    }
}"""},
    {"id": 78, "expected": "FeatureEnvy", "description": "Shipping label generator", "code": """
public class ShippingLabelGenerator {
    public Label generateLabel(Shipment shipment) {
        Label label = new Label(); label.setSender(shipment.getSender().getName());
        label.setSenderAddress(shipment.getSender().getAddress().getFullAddress());
        label.setRecipient(shipment.getRecipient().getName());
        label.setRecipientAddress(shipment.getRecipient().getAddress().getFullAddress());
        return label;
    }
}"""},
    {"id": 79, "expected": "FeatureEnvy", "description": "Medical record summarizer", "code": """
public class MedicalRecordSummarizer {
    public String summarize(Patient patient) {
        return "Patient: " + patient.getPersonalInfo().getFullName() + " DOB: " + patient.getPersonalInfo().getDateOfBirth() +
               " Blood Type: " + patient.getMedicalInfo().getBloodType() + " Allergies: " + patient.getMedicalInfo().getAllergies() +
               " Doctor: " + patient.getCareTeam().getPrimaryPhysician().getName();
    }
}"""},
    {"id": 80, "expected": "FeatureEnvy", "description": "Portfolio analyzer", "code": """
public class PortfolioAnalyzer {
    public Analysis analyzePortfolio(Investor investor) {
        double totalStocks = investor.getPortfolio().getStocks().getTotalValue();
        double totalBonds = investor.getPortfolio().getBonds().getTotalValue();
        double totalCash = investor.getPortfolio().getCash().getBalance();
        double riskScore = investor.getProfile().getRiskTolerance();
        return new Analysis(totalStocks + totalBonds + totalCash, riskScore);
    }
}"""},

    # ========================================================================
    # LONG METHOD SAMPLES (81-100)
    # ========================================================================
    {"id": 81, "expected": "LongMethod", "description": "Order processor with many steps", "code": """
public class OrderProcessor {
    public void processOrder(Order order) {
        if (order == null) throw new IllegalArgumentException("Order is null");
        if (order.getItems() == null) throw new IllegalArgumentException("No items");
        if (order.getItems().isEmpty()) throw new IllegalArgumentException("Empty order");
        double subtotal = 0;
        for (OrderItem item : order.getItems()) { double itemTotal = item.getPrice() * item.getQuantity(); subtotal += itemTotal; }
        double discount = 0;
        if (order.getPromoCode() != null) {
            if (order.getPromoCode().equals("SAVE10")) discount = subtotal * 0.10;
            else if (order.getPromoCode().equals("SAVE20")) discount = subtotal * 0.20;
        }
        double taxableAmount = subtotal - discount; double tax = taxableAmount * 0.08;
        double shipping = 0; if (subtotal < 50) shipping = 5.99; else if (subtotal < 100) shipping = 3.99;
        order.setSubtotal(subtotal); order.setDiscount(discount); order.setTax(tax); order.setShipping(shipping);
        order.setTotal(taxableAmount + tax + shipping); order.setStatus("CONFIRMED");
        for (OrderItem item : order.getItems()) { Product product = item.getProduct(); product.setQuantity(product.getQuantity() - item.getQuantity()); }
        orderRepository.save(order); emailService.send(order.getCustomer().getEmail(), "Order confirmed");
    }
}"""},
    {"id": 82, "expected": "LongMethod", "description": "Data import with validation", "code": """
public class DataImporter {
    public void importData(String filePath) {
        List<String> lines = readFile(filePath); List<Record> records = new ArrayList<>(); List<String> errors = new ArrayList<>();
        String[] headers = lines.get(0).split(","); int nameIndex = -1, emailIndex = -1, ageIndex = -1;
        for (int i = 0; i < headers.length; i++) {
            if (headers[i].equals("name")) nameIndex = i; if (headers[i].equals("email")) emailIndex = i; if (headers[i].equals("age")) ageIndex = i;
        }
        if (nameIndex == -1) errors.add("Missing name column"); if (emailIndex == -1) errors.add("Missing email column");
        for (int i = 1; i < lines.size(); i++) {
            String[] values = lines.get(i).split(",");
            if (values.length != headers.length) { errors.add("Line " + i + ": Invalid column count"); continue; }
            String name = values[nameIndex].trim(); String email = values[emailIndex].trim();
            if (name.isEmpty()) { errors.add("Line " + i + ": Empty name"); continue; }
            if (!email.contains("@")) { errors.add("Line " + i + ": Invalid email"); continue; }
            records.add(new Record(name, email, 0));
        }
        for (Record record : records) { repository.save(record); }
        logger.info("Imported " + records.size() + " records");
    }
}"""},
    {"id": 83, "expected": "LongMethod", "description": "Form validation with many checks", "code": """
public class FormValidator {
    public ValidationResult validate(UserForm form) {
        List<String> errors = new ArrayList<>();
        String username = form.getUsername();
        if (username == null || username.isEmpty()) { errors.add("Username is required"); }
        else if (username.length() < 3) { errors.add("Username must be at least 3 characters"); }
        else if (username.length() > 20) { errors.add("Username must be at most 20 characters"); }
        String email = form.getEmail();
        if (email == null || email.isEmpty()) { errors.add("Email is required"); }
        else if (!email.contains("@")) { errors.add("Invalid email format"); }
        String password = form.getPassword();
        if (password == null || password.isEmpty()) { errors.add("Password is required"); }
        else if (password.length() < 8) { errors.add("Password must be at least 8 characters"); }
        else if (!password.matches(".*[A-Z].*")) { errors.add("Password must contain uppercase letter"); }
        else if (!password.matches(".*[0-9].*")) { errors.add("Password must contain a number"); }
        if (!password.equals(form.getConfirmPassword())) { errors.add("Passwords do not match"); }
        Integer age = form.getAge();
        if (age == null) { errors.add("Age is required"); } else if (age < 18) { errors.add("Must be at least 18"); }
        return new ValidationResult(errors.isEmpty(), errors);
    }
}"""},
    {"id": 84, "expected": "LongMethod", "description": "Payment processing with many steps", "code": """
public class PaymentProcessor {
    public PaymentResult processPayment(PaymentRequest request) {
        if (request == null) { return PaymentResult.failure("Invalid request"); }
        if (request.getAmount() <= 0) { return PaymentResult.failure("Invalid amount"); }
        if (request.getCardNumber() == null) { return PaymentResult.failure("Card number required"); }
        String cardNumber = request.getCardNumber().replaceAll("\\\\s", "");
        if (cardNumber.length() != 16) { return PaymentResult.failure("Invalid card number"); }
        String cardType;
        if (cardNumber.startsWith("4")) { cardType = "VISA"; }
        else if (cardNumber.startsWith("5")) { cardType = "MASTERCARD"; }
        else { return PaymentResult.failure("Unsupported card type"); }
        String expiry = request.getExpiry(); String[] parts = expiry.split("/");
        int month = Integer.parseInt(parts[0]); int year = Integer.parseInt(parts[1]) + 2000;
        LocalDate expiryDate = LocalDate.of(year, month, 1);
        if (expiryDate.isBefore(LocalDate.now())) { return PaymentResult.failure("Card expired"); }
        GatewayRequest gwRequest = new GatewayRequest(); gwRequest.setAmount(request.getAmount());
        GatewayResponse response = gateway.process(gwRequest);
        if (response.isSuccess()) { return PaymentResult.success(response.getTransactionId()); }
        return PaymentResult.failure(response.getErrorMessage());
    }
}"""},
    {"id": 85, "expected": "LongMethod", "description": "User registration with many steps", "code": """
public class RegistrationService {
    public RegistrationResult register(RegistrationForm form) {
        if (userRepository.existsByUsername(form.getUsername())) { return RegistrationResult.failure("Username already taken"); }
        if (userRepository.existsByEmail(form.getEmail())) { return RegistrationResult.failure("Email already registered"); }
        User user = new User(); user.setUsername(form.getUsername()); user.setEmail(form.getEmail());
        String salt = generateSalt(); String hashedPassword = hashPassword(form.getPassword(), salt);
        user.setPasswordHash(hashedPassword); user.setPasswordSalt(salt);
        user.setActive(false); user.setCreatedAt(new Date()); user.setRole("USER");
        String token = UUID.randomUUID().toString(); user.setVerificationToken(token);
        user.setTokenExpiry(new Date(System.currentTimeMillis() + 86400000));
        userRepository.save(user);
        UserProfile profile = new UserProfile(); profile.setUserId(user.getId());
        profile.setFirstName(form.getFirstName()); profile.setLastName(form.getLastName());
        profileRepository.save(profile);
        String verifyUrl = baseUrl + "/verify?token=" + token;
        emailService.send(form.getEmail(), "Verify your account", verifyUrl);
        auditLog.log("USER_REGISTERED", user.getId());
        return RegistrationResult.success(user.getId());
    }
}"""},
    {"id": 86, "expected": "LongMethod", "description": "Search with multiple filters", "code": """
public class SearchService {
    public SearchResult search(SearchCriteria criteria) {
        StringBuilder query = new StringBuilder("SELECT * FROM products WHERE 1=1"); List<Object> params = new ArrayList<>();
        if (criteria.getKeyword() != null && !criteria.getKeyword().isEmpty()) {
            query.append(" AND (name LIKE ? OR description LIKE ?)");
            params.add("%" + criteria.getKeyword() + "%"); params.add("%" + criteria.getKeyword() + "%");
        }
        if (criteria.getCategory() != null) { query.append(" AND category_id = ?"); params.add(criteria.getCategory()); }
        if (criteria.getMinPrice() != null) { query.append(" AND price >= ?"); params.add(criteria.getMinPrice()); }
        if (criteria.getMaxPrice() != null) { query.append(" AND price <= ?"); params.add(criteria.getMaxPrice()); }
        if (criteria.isInStockOnly()) { query.append(" AND quantity > 0"); }
        if (criteria.getMinRating() != null) { query.append(" AND rating >= ?"); params.add(criteria.getMinRating()); }
        String sortField = criteria.getSortBy() != null ? criteria.getSortBy() : "name";
        query.append(" ORDER BY ").append(sortField);
        int page = criteria.getPage() != null ? criteria.getPage() : 0;
        int size = criteria.getPageSize() != null ? criteria.getPageSize() : 20;
        query.append(" LIMIT ? OFFSET ?"); params.add(size); params.add(page * size);
        List<Product> products = jdbcTemplate.query(query.toString(), params.toArray());
        return new SearchResult(products, products.size(), page, size);
    }
}"""},
    {"id": 87, "expected": "LongMethod", "description": "Report generator with formatting", "code": """
public class ReportGenerator {
    public String generateReport(List<Sale> sales) {
        StringBuilder report = new StringBuilder();
        report.append("=================================\\n"); report.append("       SALES REPORT              \\n");
        report.append("=================================\\n"); report.append("Generated: ").append(new Date()).append("\\n\\n");
        Map<String, List<Sale>> byCategory = new HashMap<>();
        for (Sale sale : sales) { String cat = sale.getCategory();
            if (!byCategory.containsKey(cat)) { byCategory.put(cat, new ArrayList<>()); }
            byCategory.get(cat).add(sale);
        }
        double grandTotal = 0;
        for (String category : byCategory.keySet()) {
            report.append("Category: ").append(category).append("\\n"); report.append("---------------------------------\\n");
            double categoryTotal = 0; List<Sale> categorySales = byCategory.get(category);
            for (Sale sale : categorySales) { report.append("  ").append(sale.getProduct());
                report.append(" - $").append(sale.getAmount()).append("\\n"); categoryTotal += sale.getAmount(); }
            report.append("  Category Total: $").append(categoryTotal).append("\\n\\n"); grandTotal += categoryTotal;
        }
        report.append("=================================\\n"); report.append("GRAND TOTAL: $").append(grandTotal).append("\\n");
        return report.toString();
    }
}"""},
    {"id": 88, "expected": "LongMethod", "description": "File upload handler", "code": """
public class FileUploadHandler {
    public UploadResult handleUpload(MultipartFile file, String userId) {
        if (file == null || file.isEmpty()) { return UploadResult.failure("No file provided"); }
        long maxSize = 10 * 1024 * 1024;
        if (file.getSize() > maxSize) { return UploadResult.failure("File too large. Max size: 10MB"); }
        String originalName = file.getOriginalFilename();
        String extension = originalName.substring(originalName.lastIndexOf(".") + 1).toLowerCase();
        List<String> allowedTypes = Arrays.asList("jpg", "jpeg", "png", "gif", "pdf");
        if (!allowedTypes.contains(extension)) { return UploadResult.failure("File type not allowed"); }
        String contentType = file.getContentType();
        if (contentType == null) { return UploadResult.failure("Invalid content type"); }
        String uniqueName = UUID.randomUUID().toString() + "." + extension;
        Path userDir = Paths.get(uploadDir, userId);
        if (!Files.exists(userDir)) { Files.createDirectories(userDir); }
        Path targetPath = userDir.resolve(uniqueName); Files.copy(file.getInputStream(), targetPath);
        FileRecord record = new FileRecord(); record.setUserId(userId); record.setOriginalName(originalName);
        record.setStoredName(uniqueName); record.setPath(targetPath.toString()); record.setSize(file.getSize());
        fileRepository.save(record);
        return UploadResult.success(record.getId(), baseUrl + "/files/" + record.getId());
    }
}"""},
    {"id": 89, "expected": "LongMethod", "description": "Invoice generator", "code": """
public class InvoiceGenerator {
    public Invoice generateInvoice(Order order) {
        Invoice invoice = new Invoice(); invoice.setInvoiceNumber(generateInvoiceNumber());
        invoice.setInvoiceDate(new Date()); invoice.setDueDate(calculateDueDate(30));
        Customer customer = order.getCustomer(); invoice.setCustomerName(customer.getName());
        invoice.setCustomerEmail(customer.getEmail()); invoice.setCustomerAddress(formatAddress(customer.getAddress()));
        invoice.setCompanyName("ACME Corporation"); invoice.setCompanyAddress("123 Business St");
        List<InvoiceLineItem> lineItems = new ArrayList<>(); double subtotal = 0;
        for (OrderItem item : order.getItems()) {
            InvoiceLineItem lineItem = new InvoiceLineItem(); lineItem.setDescription(item.getProduct().getName());
            lineItem.setQuantity(item.getQuantity()); lineItem.setUnitPrice(item.getPrice());
            lineItem.setAmount(item.getQuantity() * item.getPrice()); lineItems.add(lineItem);
            subtotal += lineItem.getAmount();
        }
        invoice.setLineItems(lineItems); invoice.setSubtotal(subtotal);
        double taxRate = 0.08; double taxAmount = subtotal * taxRate;
        invoice.setTaxRate(taxRate); invoice.setTaxAmount(taxAmount);
        invoice.setTotalAmount(subtotal + taxAmount); invoiceRepository.save(invoice);
        return invoice;
    }
}"""},
    {"id": 90, "expected": "LongMethod", "description": "Config parser", "code": """
public class ConfigurationParser {
    public Configuration parse(String configFile) throws Exception {
        Configuration config = new Configuration(); Properties props = new Properties();
        props.load(new FileInputStream(configFile));
        String host = props.getProperty("server.host", "localhost"); config.setServerHost(host);
        String portStr = props.getProperty("server.port", "8080"); int port = Integer.parseInt(portStr);
        if (port < 1 || port > 65535) { throw new ConfigException("Invalid port: " + port); }
        config.setServerPort(port);
        String dbUrl = props.getProperty("db.url");
        if (dbUrl == null || dbUrl.isEmpty()) { throw new ConfigException("Database URL required"); }
        config.setDatabaseUrl(dbUrl);
        String dbUser = props.getProperty("db.user"); config.setDatabaseUser(dbUser);
        String poolSizeStr = props.getProperty("db.pool.size", "10");
        config.setConnectionPoolSize(Integer.parseInt(poolSizeStr));
        String cacheEnabled = props.getProperty("cache.enabled", "true");
        config.setCacheEnabled(Boolean.parseBoolean(cacheEnabled));
        String logLevel = props.getProperty("log.level", "INFO");
        if (!Arrays.asList("DEBUG", "INFO", "WARN", "ERROR").contains(logLevel)) { throw new ConfigException("Invalid log level"); }
        config.setLogLevel(logLevel);
        return config;
    }
}"""},
    {"id": 91, "expected": "LongMethod", "description": "Email template builder", "code": """
public class EmailTemplateBuilder {
    public String buildOrderConfirmation(Order order) {
        StringBuilder html = new StringBuilder();
        html.append("<!DOCTYPE html>"); html.append("<html><head>");
        html.append("<style>"); html.append("body { font-family: Arial; }");
        html.append("table { border-collapse: collapse; width: 100%; }");
        html.append("th, td { border: 1px solid #ddd; padding: 8px; }"); html.append("</style>");
        html.append("</head><body>"); html.append("<h1>Order Confirmation</h1>");
        html.append("<p>Order Number: <strong>").append(order.getId()).append("</strong></p>");
        html.append("<h2>Shipping Address</h2>");
        html.append("<p>").append(order.getCustomer().getName()).append("<br>");
        html.append(order.getShippingAddress().getStreet()).append("</p>");
        html.append("<h2>Order Items</h2>"); html.append("<table><tr><th>Item</th><th>Qty</th><th>Price</th></tr>");
        for (OrderItem item : order.getItems()) {
            html.append("<tr><td>").append(item.getProduct().getName()).append("</td>");
            html.append("<td>").append(item.getQuantity()).append("</td>");
            html.append("<td>$").append(item.getPrice()).append("</td></tr>");
        }
        html.append("</table>"); html.append("<p>Total: $").append(order.getTotal()).append("</p>");
        html.append("</body></html>");
        return html.toString();
    }
}"""},
    {"id": 92, "expected": "LongMethod", "description": "Data export with formatting", "code": """
public class DataExporter {
    public byte[] exportToExcel(List<Employee> employees) {
        Workbook workbook = new XSSFWorkbook(); Sheet sheet = workbook.createSheet("Employees");
        CellStyle headerStyle = workbook.createCellStyle();
        headerStyle.setFillForegroundColor(IndexedColors.BLUE.getIndex());
        Font headerFont = workbook.createFont(); headerFont.setColor(IndexedColors.WHITE.getIndex());
        headerFont.setBold(true); headerStyle.setFont(headerFont);
        Row headerRow = sheet.createRow(0);
        String[] headers = {"ID", "Name", "Email", "Department", "Salary"};
        for (int i = 0; i < headers.length; i++) {
            Cell cell = headerRow.createCell(i); cell.setCellValue(headers[i]); cell.setCellStyle(headerStyle);
        }
        int rowNum = 1;
        for (Employee emp : employees) {
            Row row = sheet.createRow(rowNum++);
            row.createCell(0).setCellValue(emp.getId()); row.createCell(1).setCellValue(emp.getName());
            row.createCell(2).setCellValue(emp.getEmail()); row.createCell(3).setCellValue(emp.getDepartment());
            row.createCell(4).setCellValue(emp.getSalary());
        }
        for (int i = 0; i < headers.length; i++) { sheet.autoSizeColumn(i); }
        ByteArrayOutputStream out = new ByteArrayOutputStream(); workbook.write(out); workbook.close();
        return out.toByteArray();
    }
}"""},
    {"id": 93, "expected": "LongMethod", "description": "Notification sender", "code": """
public class NotificationSender {
    public void sendNotification(User user, Notification notification) {
        NotificationPreferences prefs = user.getNotificationPreferences();
        if (prefs.isEmailEnabled()) {
            String emailBody = buildEmailBody(notification); String subject = notification.getTitle();
            EmailMessage email = new EmailMessage(); email.setTo(user.getEmail());
            email.setSubject(subject); email.setBody(emailBody);
            try { emailService.send(email); logNotification(user, "EMAIL", "SUCCESS"); }
            catch (Exception e) { logNotification(user, "EMAIL", "FAILED"); }
        }
        if (prefs.isSmsEnabled() && user.getPhone() != null) {
            String smsBody = truncate(notification.getMessage(), 160);
            try { smsService.send(user.getPhone(), smsBody); logNotification(user, "SMS", "SUCCESS"); }
            catch (Exception e) { logNotification(user, "SMS", "FAILED"); }
        }
        if (prefs.isPushEnabled() && user.getDeviceToken() != null) {
            PushMessage push = new PushMessage(); push.setToken(user.getDeviceToken());
            push.setTitle(notification.getTitle()); push.setBody(notification.getMessage());
            try { pushService.send(push); logNotification(user, "PUSH", "SUCCESS"); }
            catch (Exception e) { logNotification(user, "PUSH", "FAILED"); }
        }
        notification.setSentAt(new Date()); notification.setStatus("SENT");
        notificationRepository.save(notification);
    }
}"""},
    {"id": 94, "expected": "LongMethod", "description": "Report aggregator", "code": """
public class ReportAggregator {
    public AggregatedReport aggregate(List<Report> reports, AggregationCriteria criteria) {
        AggregatedReport result = new AggregatedReport(); result.setGeneratedAt(new Date());
        List<Report> filtered = new ArrayList<>();
        for (Report report : reports) {
            if (criteria.getStartDate() != null && report.getDate().before(criteria.getStartDate())) { continue; }
            if (criteria.getEndDate() != null && report.getDate().after(criteria.getEndDate())) { continue; }
            filtered.add(report);
        }
        Map<String, List<Report>> grouped = new HashMap<>();
        for (Report report : filtered) {
            String key = getGroupKey(report, criteria.getGroupBy());
            if (!grouped.containsKey(key)) { grouped.put(key, new ArrayList<>()); }
            grouped.get(key).add(report);
        }
        List<AggregationResult> aggregations = new ArrayList<>();
        for (Map.Entry<String, List<Report>> entry : grouped.entrySet()) {
            AggregationResult agg = new AggregationResult(); agg.setGroupKey(entry.getKey());
            List<Report> groupReports = entry.getValue(); agg.setCount(groupReports.size());
            double sum = 0; for (Report r : groupReports) { sum += r.getValue(); }
            agg.setSum(sum); agg.setAverage(sum / groupReports.size());
            aggregations.add(agg);
        }
        result.setAggregations(aggregations);
        return result;
    }
}"""},
    {"id": 95, "expected": "LongMethod", "description": "JSON to XML converter", "code": """
public class JsonToXmlConverter {
    public String convert(String json) {
        StringBuilder xml = new StringBuilder();
        xml.append("<?xml version=\\"1.0\\" encoding=\\"UTF-8\\"?>\\n");
        JSONObject jsonObj;
        try { jsonObj = new JSONObject(json); }
        catch (JSONException e) { throw new ConversionException("Invalid JSON"); }
        String rootName = "root";
        if (jsonObj.has("_root")) { rootName = jsonObj.getString("_root"); jsonObj.remove("_root"); }
        xml.append("<").append(rootName).append(">\\n");
        for (String key : jsonObj.keySet()) {
            Object value = jsonObj.get(key);
            if (value instanceof JSONObject) { xml.append(convertObject(key, (JSONObject) value, 1)); }
            else if (value instanceof JSONArray) {
                JSONArray arr = (JSONArray) value;
                for (int i = 0; i < arr.length(); i++) { xml.append("<").append(key).append(">").append(arr.get(i)).append("</").append(key).append(">\\n"); }
            }
            else { xml.append("<").append(key).append(">").append(escapeXml(value.toString())).append("</").append(key).append(">\\n"); }
        }
        xml.append("</").append(rootName).append(">");
        return xml.toString();
    }
}"""},
    {"id": 96, "expected": "LongMethod", "description": "Batch processor", "code": """
public class BatchProcessor {
    public BatchResult processBatch(List<Record> records) {
        BatchResult result = new BatchResult(); int successCount = 0; int failCount = 0;
        List<String> errors = new ArrayList<>();
        for (int i = 0; i < records.size(); i++) {
            Record record = records.get(i);
            try {
                if (record.getId() == null) { errors.add("Record " + i + ": Missing ID"); failCount++; continue; }
                if (record.getData() == null) { errors.add("Record " + i + ": Missing data"); failCount++; continue; }
                if (!validateRecord(record)) { errors.add("Record " + i + ": Validation failed"); failCount++; continue; }
                Record existing = repository.findById(record.getId());
                if (existing != null) { existing.setData(record.getData()); existing.setUpdatedAt(new Date()); repository.save(existing); }
                else { record.setCreatedAt(new Date()); repository.save(record); }
                successCount++;
            } catch (Exception e) { errors.add("Record " + i + ": " + e.getMessage()); failCount++; }
        }
        result.setSuccessCount(successCount); result.setFailCount(failCount); result.setErrors(errors);
        result.setProcessedAt(new Date());
        return result;
    }
}"""},
    {"id": 97, "expected": "LongMethod", "description": "Data migration", "code": """
public class DataMigration {
    public MigrationResult migrate(String sourceDb, String targetDb) {
        MigrationResult result = new MigrationResult(); result.setStartTime(new Date());
        Connection sourceConn = null; Connection targetConn = null;
        try {
            sourceConn = DriverManager.getConnection(sourceDb); targetConn = DriverManager.getConnection(targetDb);
            List<String> tables = getTables(sourceConn);
            for (String table : tables) {
                logger.info("Migrating table: " + table);
                ResultSet rs = sourceConn.createStatement().executeQuery("SELECT * FROM " + table);
                ResultSetMetaData meta = rs.getMetaData(); int columnCount = meta.getColumnCount();
                StringBuilder insertSql = new StringBuilder("INSERT INTO " + table + " VALUES (");
                for (int i = 0; i < columnCount; i++) { if (i > 0) insertSql.append(","); insertSql.append("?"); }
                insertSql.append(")");
                PreparedStatement ps = targetConn.prepareStatement(insertSql.toString());
                int rowCount = 0;
                while (rs.next()) {
                    for (int i = 1; i <= columnCount; i++) { ps.setObject(i, rs.getObject(i)); }
                    ps.executeUpdate(); rowCount++;
                }
                result.addTableResult(table, rowCount);
            }
            result.setSuccess(true);
        } catch (Exception e) { result.setSuccess(false); result.setError(e.getMessage()); }
        finally { if (sourceConn != null) sourceConn.close(); if (targetConn != null) targetConn.close(); }
        result.setEndTime(new Date());
        return result;
    }
}"""},
    {"id": 98, "expected": "LongMethod", "description": "API request handler", "code": """
public class ApiRequestHandler {
    public ApiResponse handleRequest(ApiRequest request) {
        if (request == null) { return ApiResponse.error(400, "Invalid request"); }
        if (request.getApiKey() == null) { return ApiResponse.error(401, "API key required"); }
        if (!apiKeyService.isValid(request.getApiKey())) { return ApiResponse.error(401, "Invalid API key"); }
        if (rateLimiter.isExceeded(request.getApiKey())) { return ApiResponse.error(429, "Rate limit exceeded"); }
        String endpoint = request.getEndpoint();
        if (endpoint == null || endpoint.isEmpty()) { return ApiResponse.error(400, "Endpoint required"); }
        Map<String, String> params = request.getParameters();
        if (params == null) { params = new HashMap<>(); }
        Object result;
        try {
            if (endpoint.equals("/users")) { result = userService.getUsers(params); }
            else if (endpoint.equals("/products")) { result = productService.getProducts(params); }
            else if (endpoint.equals("/orders")) { result = orderService.getOrders(params); }
            else { return ApiResponse.error(404, "Endpoint not found"); }
        } catch (ValidationException e) { return ApiResponse.error(400, e.getMessage()); }
        catch (Exception e) { logger.error("API error", e); return ApiResponse.error(500, "Internal server error"); }
        auditLog.log(request.getApiKey(), endpoint, params);
        return ApiResponse.success(result);
    }
}"""},
    {"id": 99, "expected": "LongMethod", "description": "Scheduler job", "code": """
public class SchedulerJob {
    public void executeJob(JobConfig config) {
        logger.info("Starting job: " + config.getJobName());
        JobResult result = new JobResult(); result.setJobName(config.getJobName()); result.setStartTime(new Date());
        try {
            if (!config.isEnabled()) { logger.info("Job disabled, skipping"); return; }
            if (config.getSchedule() == null) { throw new JobException("Schedule not configured"); }
            List<String> targets = config.getTargets();
            if (targets == null || targets.isEmpty()) { throw new JobException("No targets configured"); }
            int successCount = 0; int failCount = 0;
            for (String target : targets) {
                try {
                    logger.info("Processing target: " + target);
                    if (config.getJobType().equals("BACKUP")) { backupService.backup(target); }
                    else if (config.getJobType().equals("CLEANUP")) { cleanupService.cleanup(target); }
                    else if (config.getJobType().equals("SYNC")) { syncService.sync(target); }
                    successCount++;
                } catch (Exception e) { logger.error("Failed to process: " + target, e); failCount++; }
            }
            result.setSuccessCount(successCount); result.setFailCount(failCount);
            result.setStatus(failCount == 0 ? "SUCCESS" : "PARTIAL");
        } catch (Exception e) { result.setStatus("FAILED"); result.setError(e.getMessage()); }
        result.setEndTime(new Date()); jobResultRepository.save(result);
        if (config.isNotifyOnComplete()) { notificationService.notify(config.getNotifyEmail(), result); }
    }
}"""},
    {"id": 100, "expected": "LongMethod", "description": "Checkout processor", "code": """
public class CheckoutProcessor {
    public CheckoutResult processCheckout(Cart cart, PaymentDetails payment, ShippingDetails shipping) {
        CheckoutResult result = new CheckoutResult();
        if (cart == null || cart.getItems().isEmpty()) { return result.fail("Cart is empty"); }
        if (payment == null) { return result.fail("Payment details required"); }
        if (shipping == null) { return result.fail("Shipping details required"); }
        double subtotal = 0;
        for (CartItem item : cart.getItems()) {
            if (item.getQuantity() > item.getProduct().getStock()) { return result.fail("Insufficient stock: " + item.getProduct().getName()); }
            subtotal += item.getPrice() * item.getQuantity();
        }
        double discount = 0;
        if (cart.getCouponCode() != null) {
            Coupon coupon = couponService.validate(cart.getCouponCode());
            if (coupon != null) { discount = coupon.calculateDiscount(subtotal); }
        }
        double shippingCost = shippingService.calculateCost(shipping, cart.getItems());
        double tax = taxService.calculateTax(subtotal - discount, shipping.getState());
        double total = subtotal - discount + shippingCost + tax;
        PaymentResult paymentResult = paymentService.charge(payment, total);
        if (!paymentResult.isSuccess()) { return result.fail("Payment failed: " + paymentResult.getError()); }
        Order order = new Order(); order.setItems(cart.getItems()); order.setSubtotal(subtotal);
        order.setDiscount(discount); order.setShipping(shippingCost); order.setTax(tax); order.setTotal(total);
        order.setPaymentId(paymentResult.getTransactionId()); order.setShippingAddress(shipping);
        orderRepository.save(order);
        for (CartItem item : cart.getItems()) { inventoryService.decreaseStock(item.getProduct().getId(), item.getQuantity()); }
        emailService.sendOrderConfirmation(order); cart.clear();
        return result.success(order.getId());
    }
}"""},
]


def run_final_tests():
    """Run all 100 final test cases and generate comprehensive report."""
    print("\n" + "="*80)
    print("   🏆 FINAL 100 TEST CASES - CODE SMELL DETECTION MODEL")
    print("   📊 Categories: GodClass | DataClass | Clean | LongMethod | FeatureEnvy")
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
        "GodClass": {"total": 0, "correct": 0, "predictions": []},
        "DataClass": {"total": 0, "correct": 0, "predictions": []},
        "Clean": {"total": 0, "correct": 0, "predictions": []},
        "LongMethod": {"total": 0, "correct": 0, "predictions": []},
        "FeatureEnvy": {"total": 0, "correct": 0, "predictions": []},
    }
    
    # Run each test
    print("-"*80)
    print(f"{'#':>3} | {'Expected':^12} | {'Actual':^12} | {'Conf':>6} | {'Result':^6} | Description")
    print("-"*80)
    
    for sample in FINAL_TEST_SAMPLES:
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
            category_stats[expected]["predictions"].append({
                "id": test_id,
                "actual": actual,
                "confidence": confidence,
                "correct": is_correct
            })
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
    
    # Calculate accuracy
    accuracy = (correct / len(FINAL_TEST_SAMPLES)) * 100
    
    # Print summary
    print("\n" + "="*80)
    print("   📊 FINAL TEST RESULTS SUMMARY")
    print("="*80)
    print(f"\n   Total Tests:    {len(FINAL_TEST_SAMPLES)}")
    print(f"   ✅ Correct:      {correct}")
    print(f"   ❌ Wrong:        {wrong}")
    print(f"   📈 Accuracy:     {accuracy:.1f}%")
    
    # Print category breakdown
    print("\n   " + "="*60)
    print("   CATEGORY BREAKDOWN")
    print("   " + "="*60)
    
    for cat, stats in category_stats.items():
        if stats["total"] > 0:
            cat_acc = (stats["correct"] / stats["total"]) * 100
            bar_len = int(cat_acc / 5)
            bar = "█" * bar_len + "░" * (20 - bar_len)
            status = "✅" if cat_acc == 100 else ("🟡" if cat_acc >= 80 else "🔴")
            print(f"   {status} {cat:15} | {stats['correct']:>2}/{stats['total']:<2} | {bar} | {cat_acc:>5.1f}%")
    
    print("   " + "="*60)
    
    # Print wrong predictions
    wrong_predictions = [r for r in results if not r["correct"]]
    if wrong_predictions:
        print(f"\n   ❌ INCORRECT PREDICTIONS ({len(wrong_predictions)}):")
        print("   " + "-"*70)
        for r in wrong_predictions:
            print(f"   #{r['id']:>3}: Expected {r['expected']:12} → Got {r['actual']:12} ({r['confidence']:.1f}%)")
        print("   " + "-"*70)
    else:
        print("\n   🎉 ALL 100 TESTS PASSED! PERFECT SCORE!")
    
    # Final grade
    print("\n   " + "="*60)
    if accuracy == 100:
        grade = "A+ (PERFECT)"
        emoji = "🏆"
    elif accuracy >= 95:
        grade = "A (EXCELLENT)"
        emoji = "🌟"
    elif accuracy >= 90:
        grade = "A- (GREAT)"
        emoji = "⭐"
    elif accuracy >= 85:
        grade = "B+ (VERY GOOD)"
        emoji = "👍"
    elif accuracy >= 80:
        grade = "B (GOOD)"
        emoji = "👌"
    else:
        grade = "C (NEEDS IMPROVEMENT)"
        emoji = "📈"
    
    print(f"   {emoji} FINAL GRADE: {grade}")
    print(f"   {emoji} MODEL ACCURACY: {accuracy:.1f}%")
    print("   " + "="*60)
    
    # Generate detailed report file
    report_path = "FINAL_100_TEST_REPORT.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("="*80 + "\n")
        f.write("   FINAL 100 TEST CASES - CODE SMELL DETECTION MODEL REPORT\n")
        f.write("="*80 + "\n")
        f.write(f"   Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"   Model Accuracy: {accuracy:.1f}%\n")
        f.write(f"   Grade: {grade}\n")
        f.write("="*80 + "\n\n")
        
        f.write("SUMMARY\n")
        f.write("-"*40 + "\n")
        f.write(f"Total Tests: {len(FINAL_TEST_SAMPLES)}\n")
        f.write(f"Correct: {correct}\n")
        f.write(f"Wrong: {wrong}\n")
        f.write(f"Accuracy: {accuracy:.1f}%\n\n")
        
        f.write("CATEGORY BREAKDOWN\n")
        f.write("-"*40 + "\n")
        for cat, stats in category_stats.items():
            if stats["total"] > 0:
                cat_acc = (stats["correct"] / stats["total"]) * 100
                f.write(f"{cat:15} | {stats['correct']:>2}/{stats['total']:<2} correct | {cat_acc:.1f}%\n")
        f.write("\n")
        
        f.write("DETAILED RESULTS\n")
        f.write("-"*40 + "\n")
        for r in results:
            status = "PASS" if r["correct"] else "FAIL"
            f.write(f"Test #{r['id']:>3} [{status}]\n")
            f.write(f"  Description: {r['description']}\n")
            f.write(f"  Expected:    {r['expected']}\n")
            f.write(f"  Actual:      {r['actual']}\n")
            f.write(f"  Confidence:  {r['confidence']:.1f}%\n")
            f.write("-"*40 + "\n")
    
    print(f"\n📝 Detailed report saved to: {report_path}")
    
    # Save JSON results
    json_path = "FINAL_100_TEST_RESULTS.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "generated": datetime.now().isoformat(),
            "accuracy": accuracy,
            "grade": grade,
            "total": len(FINAL_TEST_SAMPLES),
            "correct": correct,
            "wrong": wrong,
            "category_stats": {k: {"total": v["total"], "correct": v["correct"], 
                                   "accuracy": (v["correct"]/v["total"]*100) if v["total"] > 0 else 0} 
                              for k, v in category_stats.items()},
            "results": results
        }, f, indent=2)
    
    print(f"📊 JSON results saved to: {json_path}")
    print("\n" + "="*80 + "\n")
    
    return results, accuracy


if __name__ == "__main__":
    run_final_tests()
