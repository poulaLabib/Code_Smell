"""
╔════════════════════════════════════════════════════════════════════════════════╗
║                    50 ADDITIONAL TEST CASES FOR CODE SMELL DETECTION            ║
║                          Second Validation Suite                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
import predict_smell_extended as ps

# ============================================================================
# 50 ADDITIONAL TEST SAMPLES - 10 per category (5 categories, excluding DeadCode)
# ============================================================================

TEST_SAMPLES = [
    # ========================================================================
    # GODCLASS SAMPLES (1-10) - Classes doing too much
    # ========================================================================
    {
        "id": 1,
        "expected": "GodClass",
        "description": "E-commerce platform manager",
        "code": """
public class ECommercePlatform {
    private ProductCatalog catalog;
    private ShoppingCart cart;
    private PaymentProcessor payment;
    private InventoryManager inventory;
    private ShippingService shipping;
    private CustomerService customers;
    private ReportingEngine reports;
    
    public void addProduct(Product p) { catalog.add(p); }
    public void removeProduct(String id) { catalog.remove(id); }
    public void updatePrice(String id, double price) { catalog.updatePrice(id, price); }
    public void addToCart(String productId) { cart.add(productId); }
    public void removeFromCart(String productId) { cart.remove(productId); }
    public void checkout() { payment.process(cart.getTotal()); }
    public void refund(String orderId) { payment.refund(orderId); }
    public void updateStock(String id, int qty) { inventory.update(id, qty); }
    public void reorderStock(String id) { inventory.reorder(id); }
    public void shipOrder(String orderId) { shipping.ship(orderId); }
    public void trackShipment(String trackingId) { shipping.track(trackingId); }
    public void registerCustomer(Customer c) { customers.register(c); }
    public void generateSalesReport() { reports.sales(); }
    public void generateInventoryReport() { reports.inventory(); }
}"""
    },
    {
        "id": 2,
        "expected": "GodClass",
        "description": "Banking system controller",
        "code": """
public class BankingSystem {
    private AccountManager accounts;
    private TransactionProcessor transactions;
    private LoanService loans;
    private CreditCardService cards;
    private NotificationService notifications;
    
    public void openAccount(Customer c) { accounts.open(c); }
    public void closeAccount(String id) { accounts.close(id); }
    public void deposit(String id, double amt) { transactions.deposit(id, amt); }
    public void withdraw(String id, double amt) { transactions.withdraw(id, amt); }
    public void transfer(String from, String to, double amt) { transactions.transfer(from, to, amt); }
    public void applyForLoan(String customerId, double amt) { loans.apply(customerId, amt); }
    public void approveLoan(String loanId) { loans.approve(loanId); }
    public void rejectLoan(String loanId) { loans.reject(loanId); }
    public void issueCard(String customerId) { cards.issue(customerId); }
    public void blockCard(String cardId) { cards.block(cardId); }
    public void activateCard(String cardId) { cards.activate(cardId); }
    public void sendAlert(String customerId, String msg) { notifications.send(customerId, msg); }
    public void generateStatement(String accountId) { accounts.statement(accountId); }
}"""
    },
    {
        "id": 3,
        "expected": "GodClass",
        "description": "Healthcare management system",
        "code": """
public class HealthcareSystem {
    private PatientRegistry patients;
    private DoctorScheduler scheduler;
    private AppointmentManager appointments;
    private BillingService billing;
    private PrescriptionService prescriptions;
    private LabService labs;
    
    public void registerPatient(Patient p) { patients.register(p); }
    public void updatePatientInfo(String id, Patient p) { patients.update(id, p); }
    public void addDoctor(Doctor d) { scheduler.addDoctor(d); }
    public void scheduleAppointment(String patientId, String doctorId) { appointments.schedule(patientId, doctorId); }
    public void cancelAppointment(String appointmentId) { appointments.cancel(appointmentId); }
    public void rescheduleAppointment(String id, Date newDate) { appointments.reschedule(id, newDate); }
    public void createBill(String patientId) { billing.create(patientId); }
    public void processPayment(String billId) { billing.pay(billId); }
    public void prescribeMedicine(String patientId, Medicine m) { prescriptions.prescribe(patientId, m); }
    public void orderLabTest(String patientId, String testType) { labs.order(patientId, testType); }
    public void updateLabResults(String testId, Results r) { labs.update(testId, r); }
    public void generatePatientReport(String patientId) { patients.report(patientId); }
}"""
    },
    {
        "id": 4,
        "expected": "GodClass",
        "description": "Social media platform",
        "code": """
public class SocialMediaPlatform {
    private UserManager users;
    private PostService posts;
    private CommentService comments;
    private FriendService friends;
    private MessagingService messaging;
    private NotificationService notifications;
    
    public void createUser(User u) { users.create(u); }
    public void deleteUser(String id) { users.delete(id); }
    public void updateProfile(String id, Profile p) { users.updateProfile(id, p); }
    public void createPost(String userId, Post p) { posts.create(userId, p); }
    public void deletePost(String postId) { posts.delete(postId); }
    public void likePost(String userId, String postId) { posts.like(userId, postId); }
    public void addComment(String userId, String postId, String text) { comments.add(userId, postId, text); }
    public void deleteComment(String commentId) { comments.delete(commentId); }
    public void sendFriendRequest(String from, String to) { friends.request(from, to); }
    public void acceptFriendRequest(String requestId) { friends.accept(requestId); }
    public void sendMessage(String from, String to, String msg) { messaging.send(from, to, msg); }
    public void markMessageRead(String msgId) { messaging.markRead(msgId); }
    public void sendNotification(String userId, String msg) { notifications.send(userId, msg); }
}"""
    },
    {
        "id": 5,
        "expected": "GodClass",
        "description": "Travel booking system",
        "code": """
public class TravelBookingSystem {
    private FlightService flights;
    private HotelService hotels;
    private CarRentalService cars;
    private PaymentProcessor payments;
    private BookingManager bookings;
    private CustomerService customers;
    
    public void searchFlights(String from, String to, Date date) { flights.search(from, to, date); }
    public void bookFlight(String flightId, Customer c) { bookings.bookFlight(flightId, c); }
    public void cancelFlight(String bookingId) { bookings.cancelFlight(bookingId); }
    public void searchHotels(String city, Date checkIn, Date checkOut) { hotels.search(city, checkIn, checkOut); }
    public void bookHotel(String hotelId, Customer c) { bookings.bookHotel(hotelId, c); }
    public void cancelHotel(String bookingId) { bookings.cancelHotel(bookingId); }
    public void searchCars(String location, Date from, Date to) { cars.search(location, from, to); }
    public void bookCar(String carId, Customer c) { bookings.bookCar(carId, c); }
    public void cancelCar(String bookingId) { bookings.cancelCar(bookingId); }
    public void processPayment(String bookingId, PaymentInfo info) { payments.process(bookingId, info); }
    public void issueRefund(String bookingId) { payments.refund(bookingId); }
    public void registerCustomer(Customer c) { customers.register(c); }
}"""
    },
    {
        "id": 6,
        "expected": "GodClass",
        "description": "Project management tool",
        "code": """
public class ProjectManagementTool {
    private ProjectService projects;
    private TaskService tasks;
    private TeamService teams;
    private TimeTracker timeTracker;
    private ReportService reports;
    private NotificationService notifications;
    
    public void createProject(Project p) { projects.create(p); }
    public void updateProject(String id, Project p) { projects.update(id, p); }
    public void deleteProject(String id) { projects.delete(id); }
    public void createTask(String projectId, Task t) { tasks.create(projectId, t); }
    public void assignTask(String taskId, String userId) { tasks.assign(taskId, userId); }
    public void completeTask(String taskId) { tasks.complete(taskId); }
    public void addTeamMember(String projectId, User u) { teams.addMember(projectId, u); }
    public void removeTeamMember(String projectId, String userId) { teams.removeMember(projectId, userId); }
    public void startTimer(String taskId, String userId) { timeTracker.start(taskId, userId); }
    public void stopTimer(String taskId, String userId) { timeTracker.stop(taskId, userId); }
    public void generateProjectReport(String projectId) { reports.project(projectId); }
    public void generateTimeReport(String userId) { reports.time(userId); }
    public void sendNotification(String userId, String msg) { notifications.send(userId, msg); }
}"""
    },
    {
        "id": 7,
        "expected": "GodClass",
        "description": "Content management system",
        "code": """
public class ContentManagementSystem {
    private ArticleService articles;
    private MediaService media;
    private CategoryService categories;
    private UserService users;
    private CommentService comments;
    private SearchService search;
    private AnalyticsService analytics;
    
    public void createArticle(Article a) { articles.create(a); }
    public void publishArticle(String id) { articles.publish(id); }
    public void unpublishArticle(String id) { articles.unpublish(id); }
    public void deleteArticle(String id) { articles.delete(id); }
    public void uploadMedia(MultipartFile file) { media.upload(file); }
    public void deleteMedia(String id) { media.delete(id); }
    public void createCategory(Category c) { categories.create(c); }
    public void deleteCategory(String id) { categories.delete(id); }
    public void createUser(User u) { users.create(u); }
    public void approveComment(String id) { comments.approve(id); }
    public void deleteComment(String id) { comments.delete(id); }
    public void searchContent(String query) { search.search(query); }
    public void trackPageView(String articleId) { analytics.trackView(articleId); }
}"""
    },
    {
        "id": 8,
        "expected": "GodClass",
        "description": "Restaurant chain management",
        "code": """
public class RestaurantChainManager {
    private MenuService menu;
    private OrderService orders;
    private InventoryService inventory;
    private StaffService staff;
    private ReservationService reservations;
    private ReportingService reporting;
    
    public void addMenuItem(MenuItem item) { menu.add(item); }
    public void removeMenuItem(String id) { menu.remove(id); }
    public void updatePrice(String id, double price) { menu.updatePrice(id, price); }
    public void createOrder(Order o) { orders.create(o); }
    public void cancelOrder(String id) { orders.cancel(id); }
    public void completeOrder(String id) { orders.complete(id); }
    public void updateInventory(String itemId, int qty) { inventory.update(itemId, qty); }
    public void reorderSupplies(String itemId) { inventory.reorder(itemId); }
    public void hireStaff(Staff s) { staff.hire(s); }
    public void fireStaff(String id) { staff.terminate(id); }
    public void scheduleShift(String staffId, Shift shift) { staff.schedule(staffId, shift); }
    public void makeReservation(Reservation r) { reservations.make(r); }
    public void cancelReservation(String id) { reservations.cancel(id); }
    public void generateDailyReport() { reporting.daily(); }
}"""
    },
    {
        "id": 9,
        "expected": "GodClass",
        "description": "Learning management system",
        "code": """
public class LearningManagementSystem {
    private CourseService courses;
    private StudentService students;
    private InstructorService instructors;
    private AssignmentService assignments;
    private GradingService grading;
    private CertificateService certificates;
    
    public void createCourse(Course c) { courses.create(c); }
    public void deleteCourse(String id) { courses.delete(id); }
    public void enrollStudent(String studentId, String courseId) { students.enroll(studentId, courseId); }
    public void dropStudent(String studentId, String courseId) { students.drop(studentId, courseId); }
    public void addInstructor(Instructor i) { instructors.add(i); }
    public void assignInstructor(String instructorId, String courseId) { instructors.assign(instructorId, courseId); }
    public void createAssignment(String courseId, Assignment a) { assignments.create(courseId, a); }
    public void submitAssignment(String studentId, String assignmentId, Submission s) { assignments.submit(studentId, assignmentId, s); }
    public void gradeAssignment(String submissionId, Grade g) { grading.grade(submissionId, g); }
    public void calculateFinalGrade(String studentId, String courseId) { grading.calculateFinal(studentId, courseId); }
    public void issueCertificate(String studentId, String courseId) { certificates.issue(studentId, courseId); }
    public void generateTranscript(String studentId) { students.transcript(studentId); }
}"""
    },
    {
        "id": 10,
        "expected": "GodClass",
        "description": "Supply chain management",
        "code": """
public class SupplyChainManager {
    private SupplierService suppliers;
    private WarehouseService warehouses;
    private TransportService transport;
    private OrderService orders;
    private QualityService quality;
    private ReportingService reporting;
    
    public void addSupplier(Supplier s) { suppliers.add(s); }
    public void removeSupplier(String id) { suppliers.remove(id); }
    public void placeOrder(String supplierId, Order o) { orders.place(supplierId, o); }
    public void receiveShipment(Shipment s) { warehouses.receive(s); }
    public void storeInventory(String warehouseId, String itemId, int qty) { warehouses.store(warehouseId, itemId, qty); }
    public void pickOrder(String orderId) { warehouses.pick(orderId); }
    public void shipOrder(String orderId) { transport.ship(orderId); }
    public void trackShipment(String trackingId) { transport.track(trackingId); }
    public void inspectQuality(String itemId) { quality.inspect(itemId); }
    public void reportDefect(String itemId, Defect d) { quality.report(itemId, d); }
    public void generateInventoryReport() { reporting.inventory(); }
    public void generateSupplierReport() { reporting.supplier(); }
    public void optimizeRoutes() { transport.optimize(); }
}"""
    },
    
    # ========================================================================
    # DATACLASS SAMPLES (11-20) - Classes with only data
    # ========================================================================
    {
        "id": 11,
        "expected": "DataClass",
        "description": "Weather data entity",
        "code": """
public class WeatherData {
    private double temperature;
    private double humidity;
    private double windSpeed;
    private String windDirection;
    private double pressure;
    private int visibility;
    private String condition;
    
    public double getTemperature() { return temperature; }
    public void setTemperature(double temperature) { this.temperature = temperature; }
    public double getHumidity() { return humidity; }
    public void setHumidity(double humidity) { this.humidity = humidity; }
    public double getWindSpeed() { return windSpeed; }
    public void setWindSpeed(double windSpeed) { this.windSpeed = windSpeed; }
    public String getWindDirection() { return windDirection; }
    public void setWindDirection(String windDirection) { this.windDirection = windDirection; }
    public double getPressure() { return pressure; }
    public void setPressure(double pressure) { this.pressure = pressure; }
    public int getVisibility() { return visibility; }
    public void setVisibility(int visibility) { this.visibility = visibility; }
    public String getCondition() { return condition; }
    public void setCondition(String condition) { this.condition = condition; }
}"""
    },
    {
        "id": 12,
        "expected": "DataClass",
        "description": "User profile DTO",
        "code": """
public class UserProfileDTO {
    private String username;
    private String email;
    private String firstName;
    private String lastName;
    private String phoneNumber;
    private String avatarUrl;
    private Date birthDate;
    
    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getFirstName() { return firstName; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public String getLastName() { return lastName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
    public String getPhoneNumber() { return phoneNumber; }
    public void setPhoneNumber(String phoneNumber) { this.phoneNumber = phoneNumber; }
    public String getAvatarUrl() { return avatarUrl; }
    public void setAvatarUrl(String avatarUrl) { this.avatarUrl = avatarUrl; }
    public Date getBirthDate() { return birthDate; }
    public void setBirthDate(Date birthDate) { this.birthDate = birthDate; }
}"""
    },
    {
        "id": 13,
        "expected": "DataClass",
        "description": "Vehicle information bean",
        "code": """
public class VehicleInfo {
    private String vin;
    private String make;
    private String model;
    private int year;
    private String color;
    private int mileage;
    private String fuelType;
    private String transmission;
    
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
    public int getMileage() { return mileage; }
    public void setMileage(int mileage) { this.mileage = mileage; }
    public String getFuelType() { return fuelType; }
    public void setFuelType(String fuelType) { this.fuelType = fuelType; }
    public String getTransmission() { return transmission; }
    public void setTransmission(String transmission) { this.transmission = transmission; }
}"""
    },
    {
        "id": 14,
        "expected": "DataClass",
        "description": "Recipe data holder",
        "code": """
public class RecipeData {
    private String name;
    private String description;
    private int prepTime;
    private int cookTime;
    private int servings;
    private String difficulty;
    private List<String> ingredients;
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public int getPrepTime() { return prepTime; }
    public void setPrepTime(int prepTime) { this.prepTime = prepTime; }
    public int getCookTime() { return cookTime; }
    public void setCookTime(int cookTime) { this.cookTime = cookTime; }
    public int getServings() { return servings; }
    public void setServings(int servings) { this.servings = servings; }
    public String getDifficulty() { return difficulty; }
    public void setDifficulty(String difficulty) { this.difficulty = difficulty; }
    public List<String> getIngredients() { return ingredients; }
    public void setIngredients(List<String> ingredients) { this.ingredients = ingredients; }
}"""
    },
    {
        "id": 15,
        "expected": "DataClass",
        "description": "Event registration info",
        "code": """
public class EventRegistration {
    private String registrationId;
    private String eventId;
    private String attendeeName;
    private String attendeeEmail;
    private Date registrationDate;
    private String ticketType;
    private double amountPaid;
    
    public String getRegistrationId() { return registrationId; }
    public void setRegistrationId(String registrationId) { this.registrationId = registrationId; }
    public String getEventId() { return eventId; }
    public void setEventId(String eventId) { this.eventId = eventId; }
    public String getAttendeeName() { return attendeeName; }
    public void setAttendeeName(String attendeeName) { this.attendeeName = attendeeName; }
    public String getAttendeeEmail() { return attendeeEmail; }
    public void setAttendeeEmail(String attendeeEmail) { this.attendeeEmail = attendeeEmail; }
    public Date getRegistrationDate() { return registrationDate; }
    public void setRegistrationDate(Date registrationDate) { this.registrationDate = registrationDate; }
    public String getTicketType() { return ticketType; }
    public void setTicketType(String ticketType) { this.ticketType = ticketType; }
    public double getAmountPaid() { return amountPaid; }
    public void setAmountPaid(double amountPaid) { this.amountPaid = amountPaid; }
}"""
    },
    {
        "id": 16,
        "expected": "DataClass",
        "description": "Job posting entity",
        "code": """
public class JobPosting {
    private String jobId;
    private String title;
    private String company;
    private String location;
    private String description;
    private double salary;
    private String jobType;
    private Date postedDate;
    
    public String getJobId() { return jobId; }
    public void setJobId(String jobId) { this.jobId = jobId; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getCompany() { return company; }
    public void setCompany(String company) { this.company = company; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public double getSalary() { return salary; }
    public void setSalary(double salary) { this.salary = salary; }
    public String getJobType() { return jobType; }
    public void setJobType(String jobType) { this.jobType = jobType; }
    public Date getPostedDate() { return postedDate; }
    public void setPostedDate(Date postedDate) { this.postedDate = postedDate; }
}"""
    },
    {
        "id": 17,
        "expected": "DataClass",
        "description": "Sensor reading data",
        "code": """
public class SensorReading {
    private String sensorId;
    private String sensorType;
    private double value;
    private String unit;
    private Date timestamp;
    private String location;
    private boolean isValid;
    
    public String getSensorId() { return sensorId; }
    public void setSensorId(String sensorId) { this.sensorId = sensorId; }
    public String getSensorType() { return sensorType; }
    public void setSensorType(String sensorType) { this.sensorType = sensorType; }
    public double getValue() { return value; }
    public void setValue(double value) { this.value = value; }
    public String getUnit() { return unit; }
    public void setUnit(String unit) { this.unit = unit; }
    public Date getTimestamp() { return timestamp; }
    public void setTimestamp(Date timestamp) { this.timestamp = timestamp; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public boolean isValid() { return isValid; }
    public void setValid(boolean valid) { isValid = valid; }
}"""
    },
    {
        "id": 18,
        "expected": "DataClass",
        "description": "Property listing data",
        "code": """
public class PropertyListing {
    private String listingId;
    private String address;
    private String propertyType;
    private int bedrooms;
    private int bathrooms;
    private double squareFeet;
    private double price;
    private String status;
    
    public String getListingId() { return listingId; }
    public void setListingId(String listingId) { this.listingId = listingId; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
    public String getPropertyType() { return propertyType; }
    public void setPropertyType(String propertyType) { this.propertyType = propertyType; }
    public int getBedrooms() { return bedrooms; }
    public void setBedrooms(int bedrooms) { this.bedrooms = bedrooms; }
    public int getBathrooms() { return bathrooms; }
    public void setBathrooms(int bathrooms) { this.bathrooms = bathrooms; }
    public double getSquareFeet() { return squareFeet; }
    public void setSquareFeet(double squareFeet) { this.squareFeet = squareFeet; }
    public double getPrice() { return price; }
    public void setPrice(double price) { this.price = price; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}"""
    },
    {
        "id": 19,
        "expected": "DataClass",
        "description": "Ticket information bean",
        "code": """
public class TicketInfo {
    private String ticketId;
    private String eventName;
    private String seatNumber;
    private String section;
    private Date eventDate;
    private double price;
    private String status;
    
    public String getTicketId() { return ticketId; }
    public void setTicketId(String ticketId) { this.ticketId = ticketId; }
    public String getEventName() { return eventName; }
    public void setEventName(String eventName) { this.eventName = eventName; }
    public String getSeatNumber() { return seatNumber; }
    public void setSeatNumber(String seatNumber) { this.seatNumber = seatNumber; }
    public String getSection() { return section; }
    public void setSection(String section) { this.section = section; }
    public Date getEventDate() { return eventDate; }
    public void setEventDate(Date eventDate) { this.eventDate = eventDate; }
    public double getPrice() { return price; }
    public void setPrice(double price) { this.price = price; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}"""
    },
    {
        "id": 20,
        "expected": "DataClass",
        "description": "Notification payload",
        "code": """
public class NotificationPayload {
    private String notificationId;
    private String recipientId;
    private String title;
    private String message;
    private String type;
    private Date createdAt;
    private boolean isRead;
    
    public String getNotificationId() { return notificationId; }
    public void setNotificationId(String notificationId) { this.notificationId = notificationId; }
    public String getRecipientId() { return recipientId; }
    public void setRecipientId(String recipientId) { this.recipientId = recipientId; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }
    public String getType() { return type; }
    public void setType(String type) { this.type = type; }
    public Date getCreatedAt() { return createdAt; }
    public void setCreatedAt(Date createdAt) { this.createdAt = createdAt; }
    public boolean isRead() { return isRead; }
    public void setRead(boolean read) { isRead = read; }
}"""
    },
    
    # ========================================================================
    # LONGMETHOD SAMPLES (21-30) - Methods that are too long
    # ========================================================================
    {
        "id": 21,
        "expected": "LongMethod",
        "description": "Tax calculation with many rules",
        "code": """
public class TaxCalculator {
    public double calculateTax(TaxPayer taxpayer) {
        double grossIncome = taxpayer.getSalary();
        double additionalIncome = taxpayer.getInvestmentIncome();
        double rentalIncome = taxpayer.getRentalIncome();
        double businessIncome = taxpayer.getBusinessIncome();
        
        double totalIncome = grossIncome + additionalIncome + rentalIncome + businessIncome;
        
        double standardDeduction = 12950;
        double itemizedDeductions = 0;
        
        if (taxpayer.getMortgageInterest() > 0) {
            itemizedDeductions += taxpayer.getMortgageInterest();
        }
        if (taxpayer.getCharitableDonations() > 0) {
            itemizedDeductions += Math.min(taxpayer.getCharitableDonations(), totalIncome * 0.6);
        }
        if (taxpayer.getMedicalExpenses() > 0) {
            double medicalThreshold = totalIncome * 0.075;
            if (taxpayer.getMedicalExpenses() > medicalThreshold) {
                itemizedDeductions += taxpayer.getMedicalExpenses() - medicalThreshold;
            }
        }
        if (taxpayer.getStateTaxes() > 0) {
            itemizedDeductions += Math.min(taxpayer.getStateTaxes(), 10000);
        }
        
        double deductions = Math.max(standardDeduction, itemizedDeductions);
        double taxableIncome = totalIncome - deductions;
        
        double tax = 0;
        if (taxableIncome <= 10275) {
            tax = taxableIncome * 0.10;
        } else if (taxableIncome <= 41775) {
            tax = 1027.50 + (taxableIncome - 10275) * 0.12;
        } else if (taxableIncome <= 89075) {
            tax = 4807.50 + (taxableIncome - 41775) * 0.22;
        } else if (taxableIncome <= 170050) {
            tax = 15213.50 + (taxableIncome - 89075) * 0.24;
        } else if (taxableIncome <= 215950) {
            tax = 34647.50 + (taxableIncome - 170050) * 0.32;
        } else if (taxableIncome <= 539900) {
            tax = 49335.50 + (taxableIncome - 215950) * 0.35;
        } else {
            tax = 162718 + (taxableIncome - 539900) * 0.37;
        }
        
        double credits = 0;
        if (taxpayer.getChildren() > 0) {
            credits += taxpayer.getChildren() * 2000;
        }
        if (taxpayer.isEligibleForEIC()) {
            credits += calculateEIC(taxpayer);
        }
        
        return Math.max(0, tax - credits);
    }
}"""
    },
    {
        "id": 22,
        "expected": "LongMethod",
        "description": "Document parser with many formats",
        "code": """
public class DocumentParser {
    public Document parseDocument(String content, String format) {
        Document doc = new Document();
        
        if (format.equals("JSON")) {
            content = content.trim();
            if (content.startsWith("{")) {
                int depth = 0;
                StringBuilder key = new StringBuilder();
                StringBuilder value = new StringBuilder();
                boolean inKey = true;
                boolean inString = false;
                
                for (int i = 1; i < content.length() - 1; i++) {
                    char c = content.charAt(i);
                    if (c == '"') {
                        inString = !inString;
                    } else if (c == ':' && !inString) {
                        inKey = false;
                    } else if (c == ',' && !inString && depth == 0) {
                        doc.addField(key.toString().trim(), value.toString().trim());
                        key = new StringBuilder();
                        value = new StringBuilder();
                        inKey = true;
                    } else if (c == '{' || c == '[') {
                        depth++;
                        if (!inKey) value.append(c);
                    } else if (c == '}' || c == ']') {
                        depth--;
                        if (!inKey) value.append(c);
                    } else {
                        if (inKey) key.append(c);
                        else value.append(c);
                    }
                }
                if (key.length() > 0) {
                    doc.addField(key.toString().trim(), value.toString().trim());
                }
            }
        } else if (format.equals("XML")) {
            Stack<String> tags = new Stack<>();
            StringBuilder currentTag = new StringBuilder();
            StringBuilder currentValue = new StringBuilder();
            boolean inTag = false;
            boolean isClosing = false;
            
            for (int i = 0; i < content.length(); i++) {
                char c = content.charAt(i);
                if (c == '<') {
                    if (currentValue.length() > 0 && !tags.isEmpty()) {
                        doc.addField(tags.peek(), currentValue.toString().trim());
                    }
                    currentValue = new StringBuilder();
                    inTag = true;
                    isClosing = false;
                } else if (c == '>') {
                    String tag = currentTag.toString();
                    if (isClosing) {
                        if (!tags.isEmpty()) tags.pop();
                    } else if (!tag.endsWith("/")) {
                        tags.push(tag);
                    }
                    currentTag = new StringBuilder();
                    inTag = false;
                } else if (c == '/' && inTag) {
                    isClosing = true;
                } else if (inTag) {
                    currentTag.append(c);
                } else {
                    currentValue.append(c);
                }
            }
        }
        
        return doc;
    }
}"""
    },
    {
        "id": 23,
        "expected": "LongMethod",
        "description": "Form validation with many fields",
        "code": """
public class FormValidator {
    public ValidationResult validateForm(RegistrationForm form) {
        ValidationResult result = new ValidationResult();
        
        String username = form.getUsername();
        if (username == null || username.isEmpty()) {
            result.addError("username", "Username is required");
        } else if (username.length() < 3) {
            result.addError("username", "Username must be at least 3 characters");
        } else if (username.length() > 20) {
            result.addError("username", "Username must be at most 20 characters");
        } else if (!username.matches("^[a-zA-Z0-9_]+$")) {
            result.addError("username", "Username can only contain letters, numbers, and underscores");
        }
        
        String email = form.getEmail();
        if (email == null || email.isEmpty()) {
            result.addError("email", "Email is required");
        } else if (!email.matches("^[A-Za-z0-9+_.-]+@(.+)$")) {
            result.addError("email", "Invalid email format");
        }
        
        String password = form.getPassword();
        if (password == null || password.isEmpty()) {
            result.addError("password", "Password is required");
        } else if (password.length() < 8) {
            result.addError("password", "Password must be at least 8 characters");
        } else if (!password.matches(".*[A-Z].*")) {
            result.addError("password", "Password must contain at least one uppercase letter");
        } else if (!password.matches(".*[a-z].*")) {
            result.addError("password", "Password must contain at least one lowercase letter");
        } else if (!password.matches(".*[0-9].*")) {
            result.addError("password", "Password must contain at least one digit");
        } else if (!password.matches(".*[!@#$%^&*()].*")) {
            result.addError("password", "Password must contain at least one special character");
        }
        
        String confirmPassword = form.getConfirmPassword();
        if (!password.equals(confirmPassword)) {
            result.addError("confirmPassword", "Passwords do not match");
        }
        
        String phone = form.getPhone();
        if (phone != null && !phone.isEmpty()) {
            if (!phone.matches("^\\+?[0-9]{10,14}$")) {
                result.addError("phone", "Invalid phone number format");
            }
        }
        
        Date birthDate = form.getBirthDate();
        if (birthDate != null) {
            Calendar cal = Calendar.getInstance();
            cal.add(Calendar.YEAR, -13);
            if (birthDate.after(cal.getTime())) {
                result.addError("birthDate", "You must be at least 13 years old");
            }
        }
        
        return result;
    }
}"""
    },
    {
        "id": 24,
        "expected": "LongMethod",
        "description": "Export data with multiple formats",
        "code": """
public class DataExporter {
    public byte[] exportData(List<Record> records, String format, ExportOptions options) {
        ByteArrayOutputStream output = new ByteArrayOutputStream();
        
        if ("CSV".equals(format)) {
            StringBuilder csv = new StringBuilder();
            
            if (options.includeHeader()) {
                csv.append("id,name,email,department,salary,hireDate\\n");
            }
            
            for (Record record : records) {
                csv.append(record.getId()).append(",");
                csv.append(escapeCSV(record.getName())).append(",");
                csv.append(escapeCSV(record.getEmail())).append(",");
                csv.append(escapeCSV(record.getDepartment())).append(",");
                csv.append(record.getSalary()).append(",");
                csv.append(formatDate(record.getHireDate())).append("\\n");
            }
            
            try {
                output.write(csv.toString().getBytes("UTF-8"));
            } catch (Exception e) {
                throw new RuntimeException("Export failed", e);
            }
        } else if ("EXCEL".equals(format)) {
            Workbook workbook = new XSSFWorkbook();
            Sheet sheet = workbook.createSheet("Data");
            
            int rowNum = 0;
            if (options.includeHeader()) {
                Row header = sheet.createRow(rowNum++);
                header.createCell(0).setCellValue("ID");
                header.createCell(1).setCellValue("Name");
                header.createCell(2).setCellValue("Email");
                header.createCell(3).setCellValue("Department");
                header.createCell(4).setCellValue("Salary");
                header.createCell(5).setCellValue("Hire Date");
            }
            
            for (Record record : records) {
                Row row = sheet.createRow(rowNum++);
                row.createCell(0).setCellValue(record.getId());
                row.createCell(1).setCellValue(record.getName());
                row.createCell(2).setCellValue(record.getEmail());
                row.createCell(3).setCellValue(record.getDepartment());
                row.createCell(4).setCellValue(record.getSalary());
                row.createCell(5).setCellValue(formatDate(record.getHireDate()));
            }
            
            if (options.autoSizeColumns()) {
                for (int i = 0; i <= 5; i++) {
                    sheet.autoSizeColumn(i);
                }
            }
            
            try {
                workbook.write(output);
            } catch (Exception e) {
                throw new RuntimeException("Export failed", e);
            }
        } else if ("PDF".equals(format)) {
            PdfDocument pdf = new PdfDocument();
            PdfPage page = pdf.addPage();
            PdfTable table = new PdfTable(6);
            
            if (options.includeHeader()) {
                table.addHeaderRow("ID", "Name", "Email", "Department", "Salary", "Hire Date");
            }
            
            for (Record record : records) {
                table.addRow(
                    String.valueOf(record.getId()),
                    record.getName(),
                    record.getEmail(),
                    record.getDepartment(),
                    formatCurrency(record.getSalary()),
                    formatDate(record.getHireDate())
                );
            }
            
            page.addTable(table);
            pdf.writeTo(output);
        }
        
        return output.toByteArray();
    }
}"""
    },
    {
        "id": 25,
        "expected": "LongMethod",
        "description": "Order fulfillment with many steps",
        "code": """
public class OrderFulfillment {
    public FulfillmentResult fulfillOrder(Order order) {
        FulfillmentResult result = new FulfillmentResult();
        
        if (order == null) {
            result.setStatus("FAILED");
            result.setError("Order is null");
            return result;
        }
        
        if (order.getItems() == null || order.getItems().isEmpty()) {
            result.setStatus("FAILED");
            result.setError("Order has no items");
            return result;
        }
        
        for (OrderItem item : order.getItems()) {
            int availableStock = inventoryService.getStock(item.getSku());
            if (availableStock < item.getQuantity()) {
                result.setStatus("BACKORDERED");
                result.addBackorderedItem(item.getSku(), item.getQuantity() - availableStock);
            }
        }
        
        if (result.getBackorderedItems().isEmpty()) {
            for (OrderItem item : order.getItems()) {
                inventoryService.reserve(item.getSku(), item.getQuantity());
            }
            
            Address shippingAddress = order.getShippingAddress();
            if (shippingAddress == null) {
                result.setStatus("FAILED");
                result.setError("No shipping address");
                return result;
            }
            
            String carrier = shippingService.selectCarrier(shippingAddress, order.getShippingMethod());
            double shippingCost = shippingService.calculateCost(carrier, order.getTotalWeight(), shippingAddress);
            
            PackingSlip slip = new PackingSlip();
            slip.setOrderId(order.getId());
            slip.setCustomerName(order.getCustomerName());
            slip.setShippingAddress(shippingAddress);
            slip.setItems(order.getItems());
            
            Shipment shipment = new Shipment();
            shipment.setCarrier(carrier);
            shipment.setPackingSlip(slip);
            shipment.setEstimatedDelivery(shippingService.estimateDelivery(carrier, shippingAddress));
            
            String trackingNumber = shippingService.createShipment(shipment);
            result.setTrackingNumber(trackingNumber);
            
            for (OrderItem item : order.getItems()) {
                inventoryService.deduct(item.getSku(), item.getQuantity());
            }
            
            emailService.sendShippingConfirmation(order.getCustomerEmail(), trackingNumber);
            
            result.setStatus("SHIPPED");
            result.setShippingCost(shippingCost);
        }
        
        return result;
    }
}"""
    },
    {
        "id": 26,
        "expected": "LongMethod",
        "description": "Loan application processing",
        "code": """
public class LoanProcessor {
    public LoanDecision processApplication(LoanApplication app) {
        LoanDecision decision = new LoanDecision();
        
        int creditScore = creditService.getCreditScore(app.getSsn());
        decision.setCreditScore(creditScore);
        
        if (creditScore < 300) {
            decision.setStatus("REJECTED");
            decision.setReason("Credit score too low");
            return decision;
        }
        
        double monthlyIncome = app.getAnnualIncome() / 12;
        double existingDebts = app.getMonthlyDebtPayments();
        double proposedPayment = calculateMonthlyPayment(app.getRequestedAmount(), app.getTerm(), app.getInterestRate());
        
        double dti = (existingDebts + proposedPayment) / monthlyIncome;
        decision.setDebtToIncomeRatio(dti);
        
        if (dti > 0.43) {
            decision.setStatus("REJECTED");
            decision.setReason("Debt-to-income ratio too high");
            return decision;
        }
        
        int employmentYears = app.getYearsEmployed();
        if (employmentYears < 2) {
            if (creditScore < 680) {
                decision.setStatus("REJECTED");
                decision.setReason("Insufficient employment history");
                return decision;
            }
        }
        
        boolean hasCollateral = app.getCollateralValue() > 0;
        double loanToValue = app.getRequestedAmount() / Math.max(app.getCollateralValue(), 1);
        
        double adjustedRate = app.getInterestRate();
        if (creditScore >= 760) {
            adjustedRate -= 0.5;
        } else if (creditScore >= 700) {
            adjustedRate -= 0.25;
        } else if (creditScore < 640) {
            adjustedRate += 1.0;
        }
        
        if (hasCollateral && loanToValue < 0.8) {
            adjustedRate -= 0.25;
        }
        
        double maxAmount = monthlyIncome * 0.35 * app.getTerm() * 12 - existingDebts * app.getTerm() * 12;
        if (app.getRequestedAmount() > maxAmount) {
            decision.setApprovedAmount(maxAmount);
        } else {
            decision.setApprovedAmount(app.getRequestedAmount());
        }
        
        decision.setApprovedRate(adjustedRate);
        decision.setStatus("APPROVED");
        decision.setMonthlyPayment(calculateMonthlyPayment(decision.getApprovedAmount(), app.getTerm(), adjustedRate));
        
        return decision;
    }
}"""
    },
    {
        "id": 27,
        "expected": "LongMethod",
        "description": "Image processing pipeline",
        "code": """
public class ImageProcessor {
    public ProcessedImage processImage(BufferedImage source, ProcessingOptions options) {
        ProcessedImage result = new ProcessedImage();
        BufferedImage current = source;
        
        if (options.getResize() != null) {
            int newWidth = options.getResize().getWidth();
            int newHeight = options.getResize().getHeight();
            BufferedImage resized = new BufferedImage(newWidth, newHeight, current.getType());
            Graphics2D g = resized.createGraphics();
            g.setRenderingHint(RenderingHints.KEY_INTERPOLATION, RenderingHints.VALUE_INTERPOLATION_BILINEAR);
            g.drawImage(current, 0, 0, newWidth, newHeight, null);
            g.dispose();
            current = resized;
            result.addOperation("resize", newWidth + "x" + newHeight);
        }
        
        if (options.getCrop() != null) {
            Rectangle crop = options.getCrop();
            current = current.getSubimage(crop.x, crop.y, crop.width, crop.height);
            result.addOperation("crop", crop.toString());
        }
        
        if (options.getRotation() != 0) {
            double radians = Math.toRadians(options.getRotation());
            int w = current.getWidth();
            int h = current.getHeight();
            BufferedImage rotated = new BufferedImage(w, h, current.getType());
            Graphics2D g = rotated.createGraphics();
            g.rotate(radians, w / 2, h / 2);
            g.drawImage(current, 0, 0, null);
            g.dispose();
            current = rotated;
            result.addOperation("rotate", options.getRotation() + " degrees");
        }
        
        if (options.getBrightness() != 0) {
            float scale = 1.0f + options.getBrightness() / 100.0f;
            RescaleOp op = new RescaleOp(scale, 0, null);
            current = op.filter(current, null);
            result.addOperation("brightness", options.getBrightness() + "%");
        }
        
        if (options.getContrast() != 0) {
            float scale = 1.0f + options.getContrast() / 100.0f;
            float offset = 128 * (1 - scale);
            RescaleOp op = new RescaleOp(scale, offset, null);
            current = op.filter(current, null);
            result.addOperation("contrast", options.getContrast() + "%");
        }
        
        if (options.isGrayscale()) {
            BufferedImage gray = new BufferedImage(current.getWidth(), current.getHeight(), BufferedImage.TYPE_BYTE_GRAY);
            Graphics g = gray.getGraphics();
            g.drawImage(current, 0, 0, null);
            g.dispose();
            current = gray;
            result.addOperation("grayscale", "true");
        }
        
        if (options.isFlipHorizontal()) {
            AffineTransform tx = AffineTransform.getScaleInstance(-1, 1);
            tx.translate(-current.getWidth(), 0);
            AffineTransformOp op = new AffineTransformOp(tx, AffineTransformOp.TYPE_NEAREST_NEIGHBOR);
            current = op.filter(current, null);
            result.addOperation("flipHorizontal", "true");
        }
        
        result.setImage(current);
        return result;
    }
}"""
    },
    {
        "id": 28,
        "expected": "LongMethod",
        "description": "API request handling with auth",
        "code": """
public class ApiRequestHandler {
    public ApiResponse handleRequest(ApiRequest request) {
        ApiResponse response = new ApiResponse();
        
        if (request.getMethod() == null) {
            response.setStatus(400);
            response.setError("Method is required");
            return response;
        }
        
        if (request.getPath() == null) {
            response.setStatus(400);
            response.setError("Path is required");
            return response;
        }
        
        String authHeader = request.getHeader("Authorization");
        if (authHeader == null || !authHeader.startsWith("Bearer ")) {
            response.setStatus(401);
            response.setError("Authentication required");
            return response;
        }
        
        String token = authHeader.substring(7);
        TokenInfo tokenInfo = tokenService.validate(token);
        if (tokenInfo == null) {
            response.setStatus(401);
            response.setError("Invalid token");
            return response;
        }
        
        if (tokenInfo.isExpired()) {
            response.setStatus(401);
            response.setError("Token expired");
            return response;
        }
        
        String permission = getRequiredPermission(request.getMethod(), request.getPath());
        if (!tokenInfo.hasPermission(permission)) {
            response.setStatus(403);
            response.setError("Insufficient permissions");
            return response;
        }
        
        rateLimiter.checkLimit(tokenInfo.getUserId());
        
        if (request.getBody() != null && request.getMethod().equals("POST")) {
            ValidationResult validation = validateRequestBody(request.getPath(), request.getBody());
            if (!validation.isValid()) {
                response.setStatus(400);
                response.setError(validation.getErrors().get(0));
                return response;
            }
        }
        
        try {
            Object result = routeHandler.handle(request.getMethod(), request.getPath(), request.getBody());
            response.setStatus(200);
            response.setBody(result);
        } catch (NotFoundException e) {
            response.setStatus(404);
            response.setError("Resource not found");
        } catch (ConflictException e) {
            response.setStatus(409);
            response.setError("Conflict: " + e.getMessage());
        } catch (Exception e) {
            response.setStatus(500);
            response.setError("Internal server error");
            logger.error("Request failed", e);
        }
        
        response.addHeader("X-Request-Id", request.getRequestId());
        response.addHeader("X-Response-Time", System.currentTimeMillis() - request.getTimestamp() + "ms");
        
        return response;
    }
}"""
    },
    {
        "id": 29,
        "expected": "LongMethod",
        "description": "Event scheduling with conflicts",
        "code": """
public class EventScheduler {
    public ScheduleResult scheduleEvent(Event event, ScheduleOptions options) {
        ScheduleResult result = new ScheduleResult();
        
        if (event.getTitle() == null || event.getTitle().isEmpty()) {
            result.setSuccess(false);
            result.addError("Event title is required");
            return result;
        }
        
        if (event.getStartTime() == null || event.getEndTime() == null) {
            result.setSuccess(false);
            result.addError("Start and end times are required");
            return result;
        }
        
        if (event.getEndTime().before(event.getStartTime())) {
            result.setSuccess(false);
            result.addError("End time must be after start time");
            return result;
        }
        
        List<Resource> requiredResources = new ArrayList<>();
        if (event.getRoomId() != null) {
            Room room = roomService.findById(event.getRoomId());
            if (room == null) {
                result.setSuccess(false);
                result.addError("Room not found");
                return result;
            }
            requiredResources.add(room);
        }
        
        for (String attendeeId : event.getAttendees()) {
            User attendee = userService.findById(attendeeId);
            if (attendee == null) {
                result.addWarning("Attendee not found: " + attendeeId);
                continue;
            }
            requiredResources.add(attendee);
        }
        
        List<Conflict> conflicts = new ArrayList<>();
        for (Resource resource : requiredResources) {
            List<Event> existingEvents = eventRepository.findByResourceAndTimeRange(
                resource.getId(), event.getStartTime(), event.getEndTime());
            for (Event existing : existingEvents) {
                conflicts.add(new Conflict(resource, existing));
            }
        }
        
        if (!conflicts.isEmpty() && !options.isForceSchedule()) {
            if (options.isFindAlternative()) {
                Date alternativeStart = findNextAvailableSlot(requiredResources, 
                    event.getStartTime(), getDuration(event));
                if (alternativeStart != null) {
                    result.setAlternativeTime(alternativeStart);
                }
            }
            result.setSuccess(false);
            result.setConflicts(conflicts);
            return result;
        }
        
        event.setId(generateEventId());
        event.setCreatedAt(new Date());
        eventRepository.save(event);
        
        for (String attendeeId : event.getAttendees()) {
            notificationService.sendInvite(attendeeId, event);
        }
        
        if (event.getReminder() != null) {
            reminderService.schedule(event.getId(), event.getReminder());
        }
        
        result.setSuccess(true);
        result.setEventId(event.getId());
        return result;
    }
}"""
    },
    {
        "id": 30,
        "expected": "LongMethod",
        "description": "Search with facets and filters",
        "code": """
public class SearchEngine {
    public SearchResult search(SearchQuery query) {
        SearchResult result = new SearchResult();
        
        if (query.getTerm() == null || query.getTerm().isEmpty()) {
            result.setItems(Collections.emptyList());
            return result;
        }
        
        String processedTerm = query.getTerm().toLowerCase().trim();
        processedTerm = removeStopWords(processedTerm);
        List<String> tokens = tokenize(processedTerm);
        
        List<Document> candidates = new ArrayList<>();
        for (String token : tokens) {
            List<Document> matches = index.search(token);
            candidates.addAll(matches);
        }
        
        if (query.getFilters() != null) {
            for (Filter filter : query.getFilters()) {
                candidates = applyFilter(candidates, filter);
            }
        }
        
        if (query.getDateRange() != null) {
            candidates = candidates.stream()
                .filter(d -> d.getDate().after(query.getDateRange().getStart()))
                .filter(d -> d.getDate().before(query.getDateRange().getEnd()))
                .collect(Collectors.toList());
        }
        
        if (query.getCategory() != null) {
            candidates = candidates.stream()
                .filter(d -> d.getCategory().equals(query.getCategory()))
                .collect(Collectors.toList());
        }
        
        Map<Document, Double> scored = new HashMap<>();
        for (Document doc : candidates) {
            double score = calculateRelevanceScore(doc, tokens);
            if (query.getBoostRecent()) {
                score *= getRecencyBoost(doc.getDate());
            }
            if (query.getBoostPopular()) {
                score *= getPopularityBoost(doc.getViewCount());
            }
            scored.put(doc, score);
        }
        
        List<Document> sorted = scored.entrySet().stream()
            .sorted((a, b) -> Double.compare(b.getValue(), a.getValue()))
            .map(Map.Entry::getKey)
            .collect(Collectors.toList());
        
        int start = query.getPage() * query.getPageSize();
        int end = Math.min(start + query.getPageSize(), sorted.size());
        List<Document> page = sorted.subList(start, end);
        
        result.setItems(page);
        result.setTotalCount(sorted.size());
        result.setPage(query.getPage());
        result.setPageSize(query.getPageSize());
        
        if (query.isIncludeFacets()) {
            result.setFacets(calculateFacets(sorted));
        }
        
        return result;
    }
}"""
    },
    
    # ========================================================================
    # FEATUREENVY SAMPLES (31-40) - Methods using other objects' data
    # ========================================================================
    {
        "id": 31,
        "expected": "FeatureEnvy",
        "description": "Bonus calculator using employee data",
        "code": """
public class BonusCalculator {
    public double calculateBonus(Employee employee) {
        double baseSalary = employee.getBaseSalary();
        int yearsOfService = employee.getYearsOfService();
        String department = employee.getDepartment();
        double performanceRating = employee.getPerformanceRating();
        boolean isManager = employee.isManager();
        int teamSize = employee.getTeamSize();
        
        double bonus = baseSalary * 0.10;
        
        if (yearsOfService > 5) {
            bonus += baseSalary * 0.02 * (yearsOfService - 5);
        }
        
        if (performanceRating >= 4.5) {
            bonus *= 1.5;
        } else if (performanceRating >= 4.0) {
            bonus *= 1.25;
        }
        
        if (isManager && teamSize > 5) {
            bonus += teamSize * 500;
        }
        
        return bonus;
    }
}"""
    },
    {
        "id": 32,
        "expected": "FeatureEnvy",
        "description": "Bill generator using service data",
        "code": """
public class BillGenerator {
    public Bill generateBill(ServiceSubscription subscription) {
        String planName = subscription.getPlanName();
        double monthlyRate = subscription.getMonthlyRate();
        int dataUsed = subscription.getDataUsedGB();
        int dataLimit = subscription.getDataLimitGB();
        int callMinutes = subscription.getCallMinutes();
        boolean hasInsurance = subscription.hasDeviceInsurance();
        
        double total = monthlyRate;
        
        if (dataUsed > dataLimit) {
            int overage = dataUsed - dataLimit;
            total += overage * 10;
        }
        
        if (callMinutes > 1000) {
            total += (callMinutes - 1000) * 0.05;
        }
        
        if (hasInsurance) {
            total += 12.99;
        }
        
        Bill bill = new Bill();
        bill.setAmount(total);
        bill.setPlan(planName);
        return bill;
    }
}"""
    },
    {
        "id": 33,
        "expected": "FeatureEnvy",
        "description": "Shipping cost using package data",
        "code": """
public class ShippingCostCalculator {
    public double calculateShipping(Package pkg) {
        double weight = pkg.getWeightKg();
        double length = pkg.getLengthCm();
        double width = pkg.getWidthCm();
        double height = pkg.getHeightCm();
        String destination = pkg.getDestinationCountry();
        boolean isFragile = pkg.isFragile();
        boolean requiresSignature = pkg.requiresSignature();
        
        double volumetricWeight = (length * width * height) / 5000;
        double chargeableWeight = Math.max(weight, volumetricWeight);
        
        double cost = chargeableWeight * 2.50;
        
        if (destination.equals("US")) {
            cost += 5.00;
        } else if (destination.equals("EU")) {
            cost += 10.00;
        } else {
            cost += 20.00;
        }
        
        if (isFragile) {
            cost += 15.00;
        }
        
        if (requiresSignature) {
            cost += 5.00;
        }
        
        return cost;
    }
}"""
    },
    {
        "id": 34,
        "expected": "FeatureEnvy",
        "description": "Risk assessor using client data",
        "code": """
public class RiskAssessor {
    public RiskLevel assessRisk(InsuranceClient client) {
        int age = client.getAge();
        String occupation = client.getOccupation();
        boolean isSmoker = client.isSmoker();
        double bmi = client.getBMI();
        int familyHistory = client.getFamilyHistoryScore();
        boolean hasPreexisting = client.hasPreexistingConditions();
        
        int riskScore = 0;
        
        if (age > 60) riskScore += 3;
        else if (age > 45) riskScore += 2;
        else if (age > 30) riskScore += 1;
        
        if (occupation.equals("HIGH_RISK")) riskScore += 3;
        else if (occupation.equals("MEDIUM_RISK")) riskScore += 1;
        
        if (isSmoker) riskScore += 4;
        if (bmi > 30) riskScore += 2;
        if (familyHistory > 3) riskScore += 2;
        if (hasPreexisting) riskScore += 3;
        
        if (riskScore > 10) return RiskLevel.HIGH;
        if (riskScore > 5) return RiskLevel.MEDIUM;
        return RiskLevel.LOW;
    }
}"""
    },
    {
        "id": 35,
        "expected": "FeatureEnvy",
        "description": "Delivery time estimator using order data",
        "code": """
public class DeliveryEstimator {
    public DeliveryEstimate estimateDelivery(CustomerOrder order) {
        String zipCode = order.getDeliveryZipCode();
        String shippingMethod = order.getShippingMethod();
        int itemCount = order.getItemCount();
        boolean hasHazmat = order.containsHazardousMaterials();
        boolean requiresAssembly = order.requiresAssembly();
        Date orderDate = order.getOrderDate();
        
        int baseDays = 5;
        
        if (shippingMethod.equals("EXPRESS")) {
            baseDays = 2;
        } else if (shippingMethod.equals("OVERNIGHT")) {
            baseDays = 1;
        }
        
        if (zipCode.startsWith("9")) {
            baseDays += 1;
        }
        
        if (itemCount > 10) {
            baseDays += 1;
        }
        
        if (hasHazmat) {
            baseDays += 3;
        }
        
        if (requiresAssembly) {
            baseDays += 2;
        }
        
        DeliveryEstimate estimate = new DeliveryEstimate();
        estimate.setDays(baseDays);
        return estimate;
    }
}"""
    },
    {
        "id": 36,
        "expected": "FeatureEnvy",
        "description": "Course grade calculator",
        "code": """
public class CourseGradeCalculator {
    public GradeResult calculate(StudentRecord student) {
        double midtermScore = student.getMidtermScore();
        double finalExamScore = student.getFinalExamScore();
        double homeworkAverage = student.getHomeworkAverage();
        double projectScore = student.getProjectScore();
        int attendancePercentage = student.getAttendancePercentage();
        boolean submittedExtraCredit = student.hasSubmittedExtraCredit();
        
        double weighted = midtermScore * 0.20 + 
                         finalExamScore * 0.30 + 
                         homeworkAverage * 0.25 + 
                         projectScore * 0.25;
        
        if (attendancePercentage >= 90) {
            weighted += 2;
        }
        
        if (submittedExtraCredit) {
            weighted += 5;
        }
        
        String letterGrade;
        if (weighted >= 90) letterGrade = "A";
        else if (weighted >= 80) letterGrade = "B";
        else if (weighted >= 70) letterGrade = "C";
        else if (weighted >= 60) letterGrade = "D";
        else letterGrade = "F";
        
        return new GradeResult(weighted, letterGrade);
    }
}"""
    },
    {
        "id": 37,
        "expected": "FeatureEnvy",
        "description": "Quote generator using request data",
        "code": """
public class QuoteGenerator {
    public Quote generateQuote(ServiceRequest request) {
        String serviceType = request.getServiceType();
        int squareFootage = request.getSquareFootage();
        int floors = request.getNumberOfFloors();
        boolean hasBasement = request.hasBasement();
        String preferredDate = request.getPreferredDate();
        boolean isUrgent = request.isUrgent();
        
        double basePrice = squareFootage * 0.15;
        
        if (floors > 1) {
            basePrice *= (1 + (floors - 1) * 0.20);
        }
        
        if (hasBasement) {
            basePrice += 150;
        }
        
        if (serviceType.equals("DEEP_CLEAN")) {
            basePrice *= 1.5;
        } else if (serviceType.equals("MOVE_OUT")) {
            basePrice *= 1.75;
        }
        
        if (isUrgent) {
            basePrice *= 1.25;
        }
        
        Quote quote = new Quote();
        quote.setPrice(basePrice);
        quote.setServiceType(serviceType);
        return quote;
    }
}"""
    },
    {
        "id": 38,
        "expected": "FeatureEnvy",
        "description": "Fitness score calculator",
        "code": """
public class FitnessScoreCalculator {
    public FitnessScore calculate(HealthProfile profile) {
        int restingHeartRate = profile.getRestingHeartRate();
        double vo2Max = profile.getVO2Max();
        double bodyFatPercentage = profile.getBodyFatPercentage();
        int pushupCount = profile.getPushupCount();
        int situpCount = profile.getSitupCount();
        double runTime5K = profile.getRunTime5K();
        
        double cardioScore = 100 - (restingHeartRate - 40) * 0.5;
        cardioScore += vo2Max * 1.5;
        cardioScore -= runTime5K * 0.1;
        
        double strengthScore = pushupCount * 1.2 + situpCount * 0.8;
        
        double compositionScore = 100 - (bodyFatPercentage - 10) * 2;
        
        double totalScore = (cardioScore * 0.4 + strengthScore * 0.3 + compositionScore * 0.3);
        
        FitnessScore result = new FitnessScore();
        result.setOverallScore(totalScore);
        result.setCardioScore(cardioScore);
        result.setStrengthScore(strengthScore);
        return result;
    }
}"""
    },
    {
        "id": 39,
        "expected": "FeatureEnvy",
        "description": "Rental price calculator",
        "code": """
public class RentalPriceCalculator {
    public RentalPrice calculate(RentalProperty property) {
        int bedrooms = property.getBedrooms();
        int bathrooms = property.getBathrooms();
        double squareFeet = property.getSquareFeet();
        String neighborhood = property.getNeighborhood();
        boolean hasParkcing = property.hasParking();
        boolean petsAllowed = property.arePetsAllowed();
        int yearBuilt = property.getYearBuilt();
        
        double basePrice = squareFeet * 1.5;
        basePrice += bedrooms * 200;
        basePrice += bathrooms * 100;
        
        double multiplier = 1.0;
        if (neighborhood.equals("DOWNTOWN")) multiplier = 1.4;
        else if (neighborhood.equals("SUBURBS")) multiplier = 1.0;
        else if (neighborhood.equals("UPTOWN")) multiplier = 1.25;
        
        basePrice *= multiplier;
        
        if (hasParkcing) basePrice += 150;
        if (petsAllowed) basePrice += 50;
        
        int age = 2024 - yearBuilt;
        if (age < 5) basePrice *= 1.1;
        else if (age > 30) basePrice *= 0.9;
        
        return new RentalPrice(basePrice);
    }
}"""
    },
    {
        "id": 40,
        "expected": "FeatureEnvy",
        "description": "Meal plan calculator",
        "code": """
public class MealPlanCalculator {
    public MealPlan calculate(NutritionProfile profile) {
        int age = profile.getAge();
        double weight = profile.getWeightKg();
        double height = profile.getHeightCm();
        String activityLevel = profile.getActivityLevel();
        String goal = profile.getGoal();
        boolean isVegetarian = profile.isVegetarian();
        
        double bmr = 10 * weight + 6.25 * height - 5 * age;
        
        double multiplier = 1.2;
        if (activityLevel.equals("MODERATE")) multiplier = 1.55;
        else if (activityLevel.equals("ACTIVE")) multiplier = 1.725;
        else if (activityLevel.equals("VERY_ACTIVE")) multiplier = 1.9;
        
        double tdee = bmr * multiplier;
        
        if (goal.equals("LOSE_WEIGHT")) {
            tdee -= 500;
        } else if (goal.equals("GAIN_WEIGHT")) {
            tdee += 500;
        }
        
        double protein = weight * 2.0;
        double fat = tdee * 0.25 / 9;
        double carbs = (tdee - protein * 4 - fat * 9) / 4;
        
        MealPlan plan = new MealPlan();
        plan.setCalories(tdee);
        plan.setProtein(protein);
        plan.setCarbs(carbs);
        plan.setFat(fat);
        return plan;
    }
}"""
    },
    
    # ========================================================================
    # CLEAN CODE SAMPLES (41-50) - Well-designed patterns
    # ========================================================================
    {
        "id": 41,
        "expected": "Clean",
        "description": "User repository with CRUD operations",
        "code": """
public class UserRepository {
    private final JdbcTemplate jdbcTemplate;
    
    public UserRepository(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }
    
    public User findById(Long id) {
        return jdbcTemplate.queryForObject(
            "SELECT * FROM users WHERE id = ?",
            new UserRowMapper(), id);
    }
    
    public List<User> findAll() {
        return jdbcTemplate.query("SELECT * FROM users", new UserRowMapper());
    }
    
    public void save(User user) {
        if (user.getId() == null) {
            jdbcTemplate.update("INSERT INTO users (name, email) VALUES (?, ?)",
                user.getName(), user.getEmail());
        } else {
            jdbcTemplate.update("UPDATE users SET name = ?, email = ? WHERE id = ?",
                user.getName(), user.getEmail(), user.getId());
        }
    }
    
    public void delete(Long id) {
        jdbcTemplate.update("DELETE FROM users WHERE id = ?", id);
    }
}"""
    },
    {
        "id": 42,
        "expected": "Clean",
        "description": "Payment processor with strategy",
        "code": """
public interface PaymentStrategy {
    PaymentResult process(PaymentRequest request);
}

public class CreditCardPayment implements PaymentStrategy {
    private final CreditCardGateway gateway;
    
    public CreditCardPayment(CreditCardGateway gateway) {
        this.gateway = gateway;
    }
    
    @Override
    public PaymentResult process(PaymentRequest request) {
        return gateway.charge(request.getAmount(), request.getCardDetails());
    }
}

public class PayPalPayment implements PaymentStrategy {
    private final PayPalClient client;
    
    public PayPalPayment(PayPalClient client) {
        this.client = client;
    }
    
    @Override
    public PaymentResult process(PaymentRequest request) {
        return client.createPayment(request.getAmount(), request.getEmail());
    }
}"""
    },
    {
        "id": 43,
        "expected": "Clean",
        "description": "Event publisher with observer pattern",
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
        for (EventListener listener : listeners) {
            listener.onEvent(event);
        }
    }
}

public interface EventListener {
    void onEvent(Event event);
}

public class EmailNotifier implements EventListener {
    @Override
    public void onEvent(Event event) {
        sendEmail(event);
    }
}"""
    },
    {
        "id": 44,
        "expected": "Clean",
        "description": "Immutable money value object",
        "code": """
public final class Money {
    private final BigDecimal amount;
    private final Currency currency;
    
    public Money(BigDecimal amount, Currency currency) {
        this.amount = amount;
        this.currency = currency;
    }
    
    public Money add(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new IllegalArgumentException("Currencies must match");
        }
        return new Money(this.amount.add(other.amount), this.currency);
    }
    
    public Money subtract(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new IllegalArgumentException("Currencies must match");
        }
        return new Money(this.amount.subtract(other.amount), this.currency);
    }
    
    public Money multiply(int factor) {
        return new Money(this.amount.multiply(BigDecimal.valueOf(factor)), this.currency);
    }
    
    public BigDecimal getAmount() { return amount; }
    public Currency getCurrency() { return currency; }
}"""
    },
    {
        "id": 45,
        "expected": "Clean",
        "description": "Query builder with fluent API",
        "code": """
public class QueryBuilder {
    private String table;
    private List<String> columns = new ArrayList<>();
    private List<String> conditions = new ArrayList<>();
    private String orderBy;
    private int limit;
    
    public QueryBuilder from(String table) {
        this.table = table;
        return this;
    }
    
    public QueryBuilder select(String... columns) {
        this.columns.addAll(Arrays.asList(columns));
        return this;
    }
    
    public QueryBuilder where(String condition) {
        this.conditions.add(condition);
        return this;
    }
    
    public QueryBuilder orderBy(String column) {
        this.orderBy = column;
        return this;
    }
    
    public QueryBuilder limit(int limit) {
        this.limit = limit;
        return this;
    }
    
    public String build() {
        StringBuilder sql = new StringBuilder("SELECT ");
        sql.append(columns.isEmpty() ? "*" : String.join(", ", columns));
        sql.append(" FROM ").append(table);
        if (!conditions.isEmpty()) {
            sql.append(" WHERE ").append(String.join(" AND ", conditions));
        }
        if (orderBy != null) sql.append(" ORDER BY ").append(orderBy);
        if (limit > 0) sql.append(" LIMIT ").append(limit);
        return sql.toString();
    }
}"""
    },
    {
        "id": 46,
        "expected": "Clean",
        "description": "Template method for data processing",
        "code": """
public abstract class DataProcessor {
    public final void process(String source) {
        String data = readData(source);
        String validated = validateData(data);
        String transformed = transformData(validated);
        saveData(transformed);
        notifyComplete();
    }
    
    protected abstract String readData(String source);
    protected abstract String validateData(String data);
    protected abstract String transformData(String data);
    protected abstract void saveData(String data);
    
    protected void notifyComplete() {
        System.out.println("Processing complete");
    }
}

public class CsvProcessor extends DataProcessor {
    @Override
    protected String readData(String source) { return readCsv(source); }
    @Override
    protected String validateData(String data) { return validateCsv(data); }
    @Override
    protected String transformData(String data) { return transformCsv(data); }
    @Override
    protected void saveData(String data) { saveCsv(data); }
}"""
    },
    {
        "id": 47,
        "expected": "Clean",
        "description": "Decorator for logging",
        "code": """
public interface Service {
    Result execute(Request request);
}

public class CoreService implements Service {
    @Override
    public Result execute(Request request) {
        return doExecute(request);
    }
}

public class LoggingDecorator implements Service {
    private final Service wrapped;
    private final Logger logger;
    
    public LoggingDecorator(Service wrapped, Logger logger) {
        this.wrapped = wrapped;
        this.logger = logger;
    }
    
    @Override
    public Result execute(Request request) {
        logger.info("Executing request: " + request.getId());
        long start = System.currentTimeMillis();
        Result result = wrapped.execute(request);
        long elapsed = System.currentTimeMillis() - start;
        logger.info("Completed in " + elapsed + "ms");
        return result;
    }
}"""
    },
    {
        "id": 48,
        "expected": "Clean",
        "description": "Factory for notification channels",
        "code": """
public interface NotificationChannel {
    void send(Notification notification);
}

public class NotificationFactory {
    public static NotificationChannel create(String type) {
        switch (type) {
            case "EMAIL":
                return new EmailChannel();
            case "SMS":
                return new SmsChannel();
            case "PUSH":
                return new PushChannel();
            default:
                throw new IllegalArgumentException("Unknown channel: " + type);
        }
    }
}

public class EmailChannel implements NotificationChannel {
    @Override
    public void send(Notification notification) {
        sendEmail(notification.getRecipient(), notification.getMessage());
    }
}

public class SmsChannel implements NotificationChannel {
    @Override
    public void send(Notification notification) {
        sendSms(notification.getPhone(), notification.getMessage());
    }
}"""
    },
    {
        "id": 49,
        "expected": "Clean",
        "description": "Command pattern for actions",
        "code": """
public interface Command {
    void execute();
    void undo();
}

public class CommandExecutor {
    private final Stack<Command> history = new Stack<>();
    
    public void execute(Command command) {
        command.execute();
        history.push(command);
    }
    
    public void undo() {
        if (!history.isEmpty()) {
            Command command = history.pop();
            command.undo();
        }
    }
}

public class CreateFileCommand implements Command {
    private final String path;
    
    public CreateFileCommand(String path) {
        this.path = path;
    }
    
    @Override
    public void execute() {
        createFile(path);
    }
    
    @Override
    public void undo() {
        deleteFile(path);
    }
}"""
    },
    {
        "id": 50,
        "expected": "Clean",
        "description": "Specification pattern for filtering",
        "code": """
public interface Specification<T> {
    boolean isSatisfiedBy(T item);
    
    default Specification<T> and(Specification<T> other) {
        return item -> this.isSatisfiedBy(item) && other.isSatisfiedBy(item);
    }
    
    default Specification<T> or(Specification<T> other) {
        return item -> this.isSatisfiedBy(item) || other.isSatisfiedBy(item);
    }
}

public class AgeSpecification implements Specification<User> {
    private final int minAge;
    
    public AgeSpecification(int minAge) {
        this.minAge = minAge;
    }
    
    @Override
    public boolean isSatisfiedBy(User user) {
        return user.getAge() >= minAge;
    }
}

public class ActiveSpecification implements Specification<User> {
    @Override
    public boolean isSatisfiedBy(User user) {
        return user.isActive();
    }
}"""
    }
]


def run_tests():
    """Run all 50 additional test cases"""
    
    print("=" * 80)
    print("   🧪 RUNNING 50 ADDITIONAL TEST CASES")
    print("=" * 80)
    print()
    
    print("📂 Loading models...")
    models = ps.load_models()
    print("   ✅ Models loaded successfully!")
    print()
    
    results = {
        "total": 0,
        "correct": 0,
        "wrong": 0,
        "by_category": {
            "GodClass": {"total": 0, "correct": 0},
            "DataClass": {"total": 0, "correct": 0},
            "LongMethod": {"total": 0, "correct": 0},
            "FeatureEnvy": {"total": 0, "correct": 0},
            "Clean": {"total": 0, "correct": 0}
        },
        "failures": []
    }
    
    print(f"{'#':>3} | {'Expected':^12} | {'Predicted':^12} | {'Conf':>5} | {'Result':^7} | Description")
    print("-" * 80)
    
    for sample in TEST_SAMPLES:
        results["total"] += 1
        sample_id = sample["id"]
        expected = sample["expected"]
        description = sample["description"][:30]
        code = sample["code"]
        
        results["by_category"][expected]["total"] += 1
        
        try:
            result = ps.predict_smell_compat(code, models)
            predicted = result["prediction"]
            confidence = result["confidence"]
        except Exception as e:
            predicted = "ERROR"
            confidence = 0
        
        is_correct = predicted == expected
        if is_correct:
            results["correct"] += 1
            results["by_category"][expected]["correct"] += 1
            status = "✓"
        else:
            results["wrong"] += 1
            status = "✗"
            results["failures"].append({
                "id": sample_id,
                "expected": expected,
                "predicted": predicted,
                "confidence": confidence,
                "description": sample["description"]
            })
        
        print(f"{sample_id:3} | {expected:^12} | {predicted:^12} | {confidence:>4.0f}% | {status:^7} | {description}")
    
    print("-" * 80)
    print()
    
    # Print summary
    print("=" * 80)
    print("   📊 TEST RESULTS SUMMARY")
    print("=" * 80)
    print()
    
    accuracy = (results["correct"] / results["total"]) * 100 if results["total"] > 0 else 0
    
    print(f"   Total Tests:    {results['total']}")
    print(f"   ✓ Correct:      {results['correct']}")
    print(f"   ✗ Wrong:        {results['wrong']}")
    print(f"   📈 Accuracy:     {accuracy:.1f}%")
    print()
    
    print("   Category Breakdown:")
    print("   " + "-" * 50)
    for category, stats in results["by_category"].items():
        cat_accuracy = (stats["correct"] / stats["total"]) * 100 if stats["total"] > 0 else 0
        print(f"   {category:15} | {stats['correct']}/{stats['total']} correct | {cat_accuracy:5.1f}%")
    print("   " + "-" * 50)
    print()
    
    if results["failures"]:
        print(f"   ✗ INCORRECT PREDICTIONS ({len(results['failures'])}):")
        print("   " + "-" * 70)
        for f in results["failures"]:
            print(f"   #{f['id']:2}: Expected {f['expected']:12} → Got {f['predicted']:12} ({f['confidence']:.0f}%)")
            print(f"         {f['description']}")
        print("   " + "-" * 70)
    
    print()
    print("=" * 80)
    
    return accuracy >= 90


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
