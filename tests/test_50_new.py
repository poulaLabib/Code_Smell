"""
╔════════════════════════════════════════════════════════════════════════════════╗
║                    50 NEW TEST CASES FOR CODE SMELL DETECTION                   ║
║                          Fresh Validation Suite                                 ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import predict_smell_extended as ps
from datetime import datetime

TEST_SAMPLES = [
    # ========================================================================
    # GOD CLASS SAMPLES (1-8)
    # ========================================================================
    {
        "id": 1,
        "expected": "GodClass",
        "description": "Hotel booking system with too many responsibilities",
        "code": """
public class HotelBookingSystem {
    private RoomService roomService;
    private GuestService guestService;
    private PaymentProcessor paymentProcessor;
    private NotificationService notificationService;
    private ReportGenerator reportGenerator;
    private HousekeepingService housekeeping;
    
    public void bookRoom(Guest guest, Room room) { validateGuest(guest); checkAvailability(room); }
    public void cancelBooking(Booking booking) { processRefund(booking); notifyGuest(booking); }
    public void checkIn(Guest guest) { assignRoom(guest); generateKeyCard(guest); }
    public void checkOut(Guest guest) { calculateBill(guest); processPayment(guest); }
    public void processPayment(Guest guest) { chargeCard(guest); sendReceipt(guest); }
    public void sendConfirmation(Booking booking) { emailGuest(booking); smsGuest(booking); }
    public void generateReport() { collectData(); formatReport(); exportReport(); }
    public void manageHousekeeping() { assignTasks(); trackProgress(); updateStatus(); }
    public void handleComplaints(Complaint c) { logComplaint(c); assignStaff(c); resolve(c); }
    public void updateRoomStatus(Room r) { checkRoom(r); updateInventory(r); }
    public void manageMinibar(Room r) { checkStock(r); restock(r); chargeMinibar(r); }
    public void coordinateEvents(Event e) { bookVenue(e); arrangeFood(e); setupEquipment(e); }
    public void handleLostAndFound(Item i) { logItem(i); searchOwner(i); returnItem(i); }
    public void manageStaff(Staff s) { scheduleShifts(s); trackHours(s); processPayroll(s); }
    public void updatePricing() { analyzeMarket(); adjustRates(); publishRates(); }
}"""
    },
    {
        "id": 2,
        "expected": "GodClass",
        "description": "Library management doing everything",
        "code": """
public class LibraryManagement {
    private BookCatalog catalog;
    private MemberService members;
    private FineCalculator fineCalc;
    private NotificationEngine notifications;
    private ReservationSystem reservations;
    private AcquisitionDepartment acquisitions;
    
    public void addBook(Book b) { catalogBook(b); assignShelf(b); updateIndex(b); }
    public void removeBook(Book b) { delistBook(b); archiveRecord(b); }
    public void registerMember(Member m) { validateMember(m); createAccount(m); issueCard(m); }
    public void borrowBook(Member m, Book b) { checkEligibility(m); checkAvailability(b); }
    public void returnBook(Member m, Book b) { calculateFine(m, b); updateRecord(m, b); }
    public void calculateFines(Member m) { getDaysOverdue(m); applyPenalty(m); }
    public void sendReminders() { findOverdueBooks(); composeMessage(); sendEmails(); }
    public void generateReports() { collectStats(); formatData(); exportPDF(); }
    public void manageReservations() { processQueue(); notifyAvailable(); updateStatus(); }
    public void orderNewBooks() { analyzeRequests(); contactSuppliers(); processOrders(); }
    public void conductInventory() { scanShelves(); reconcileRecords(); reportDiscrepancies(); }
    public void organizeEvents() { planReadingClub(); scheduleAuthorVisits(); manageWorkshops(); }
    public void handleDonations(Donation d) { assessCondition(d); catalogDonation(d); sendThankYou(d); }
    public void manageDigitalResources() { updateEbooks(); manageSubscriptions(); trackUsage(); }
    public void processInterlibrary() { findPartnerLibraries(); arrangeTransfer(); trackLoans(); }
}"""
    },
    {
        "id": 3,
        "expected": "GodClass",
        "description": "Restaurant POS system",
        "code": """
public class RestaurantPOS {
    private MenuService menuService;
    private OrderProcessor orderProcessor;
    private PaymentGateway paymentGateway;
    private InventoryTracker inventory;
    private StaffManager staffManager;
    private ReservationHandler reservations;
    
    public void takeOrder(Table t, List<Item> items) { validateItems(items); sendToKitchen(items); }
    public void modifyOrder(Order o) { checkKitchenStatus(o); updateOrder(o); notifyStaff(o); }
    public void processPayment(Order o) { calculateTotal(o); applyDiscounts(o); chargeCard(o); }
    public void splitBill(Order o, int ways) { divideItems(o); generateBills(o); }
    public void manageReservations() { checkAvailability(); assignTables(); sendConfirmations(); }
    public void updateMenu() { addItems(); removeItems(); updatePrices(); printMenus(); }
    public void trackInventory() { checkLevels(); generateAlerts(); autoReorder(); }
    public void manageStaff() { scheduleShifts(); trackTips(); calculatePayroll(); }
    public void generateReports() { dailySales(); weeklyTrends(); monthlyAnalysis(); }
    public void handleComplaints(Complaint c) { logIssue(c); compensateCustomer(c); }
    public void manageDelivery() { assignDrivers(); trackOrders(); calculateETA(); }
    public void processRefunds(Order o) { validateRequest(o); reverseCharge(o); updateRecords(o); }
    public void managePromotions() { createCoupons(); trackRedemptions(); analyzeROI(); }
    public void syncOnlineOrders() { fetchOrders(); processQueue(); updateStatus(); }
    public void handleCatering(Event e) { planMenu(e); calculateCosts(e); coordinateDelivery(e); }
}"""
    },
    {
        "id": 4,
        "expected": "GodClass",
        "description": "Gym management system",
        "code": """
public class GymManagement {
    private MembershipService membership;
    private TrainerService trainers;
    private EquipmentTracker equipment;
    private ClassScheduler scheduler;
    private BillingSystem billing;
    private AccessControl access;
    
    public void registerMember(Member m) { collectInfo(m); choosePackage(m); processPayment(m); }
    public void cancelMembership(Member m) { calculateRefund(m); processCancel(m); revokeAccess(m); }
    public void scheduleClass(FitnessClass c) { checkRoom(c); assignTrainer(c); openBookings(c); }
    public void bookPersonalTraining(Member m, Trainer t) { checkAvailability(t); createSession(m, t); }
    public void trackAttendance(Member m) { scanCard(m); logEntry(m); updateStats(m); }
    public void processPayments() { generateInvoices(); chargeMembers(); sendReceipts(); }
    public void manageEquipment() { scheduleMainten(); trackUsage(); orderReplacements(); }
    public void generateReports() { membershipStats(); revenueAnalysis(); attendanceTrends(); }
    public void handleComplaints(Complaint c) { logIssue(c); investigatе(c); resolveIssue(c); }
    public void manageLockers() { assignLockers(); trackRentals(); handleLostKeys(); }
    public void coordinateEvents() { planCompetitions(); organizeOpenDays(); manageWorkshops(); }
    public void updatePricing() { reviewPackages(); adjustRates(); notifyMembers(); }
    public void manageTrainers() { scheduleShifts(); trackPerformance(); processPayroll(); }
    public void handleGuestPasses() { createPass(); validateEntry(); convertToMember(); }
    public void syncMobileApp() { pushNotifications(); syncSchedule(); updateProfile(); }
}"""
    },
    {
        "id": 5,
        "expected": "GodClass",
        "description": "School administration system",
        "code": """
public class SchoolAdministration {
    private StudentService students;
    private TeacherService teachers;
    private CourseManager courses;
    private GradeTracker grades;
    private AttendanceSystem attendance;
    private FeeCollection fees;
    
    public void enrollStudent(Student s) { validateDocuments(s); assignClass(s); createAccount(s); }
    public void registerTeacher(Teacher t) { verifyCredentials(t); assignSubjects(t); setupPayroll(t); }
    public void createCourse(Course c) { defineСurriculum(c); assignTeacher(c); scheduleClasses(c); }
    public void recordGrades(Student s, Course c) { validateGrade(s); updateTranscript(s); notifyParents(s); }
    public void trackAttendance() { collectData(); identifyAbsent(); sendAlerts(); }
    public void processFeеs() { generateInvoices(); trackPayments(); handleDefaulters(); }
    public void generateReportCards() { compileGrades(); calculateRanks(); printCards(); }
    public void scheduleExams() { createTimetable(); assignRooms(); notifyStudents(); }
    public void manageTransport() { planRoutes(); assignBuses(); trackVehicles(); }
    public void handleAdmissions() { processApplications(); conductTests(); selectCandidates(); }
    public void organizeEvents() { planAnnualDay(); coordinateSports(); manageFieldTrips(); }
    public void communicateParents() { sendNewsletters(); scheduleMe­etings(); handleQueries(); }
    public void manageLibrary() { catalogBooks(); trackLoans(); orderNewBooks(); }
    public void maintainInfrastructure() { scheduleRepairs(); manageSupplies(); ensureSafety(); }
    public void generateAnalytics() { performanceMetrics(); attendanceAnalysis(); feeRecovery(); }
}"""
    },
    {
        "id": 6,
        "expected": "GodClass",
        "description": "Insurance claim processor",
        "code": """
public class InsuranceClaimProcessor {
    private PolicyService policies;
    private ClaimValidatоr validator;
    private PaymentEngine payments;
    private FraudDetector fraud;
    private DocumentManager documents;
    private NotificationCenter notifications;
    
    public void submitClaim(Claim c) { validatePolicy(c); collectDocuments(c); createCase(c); }
    public void assessClaim(Claim c) { reviewEvidence(c); calculateAmount(c); makеDecision(c); }
    public void approveClaim(Claim c) { authorizePayment(c); updatePolicy(c); notifyCustomer(c); }
    public void rejectClaim(Claim c) { documentReasons(c); offerAppeal(c); closeCasе(c); }
    public void processPayment(Claim c) { calculateDeductible(c); issueCheck(c); updateRecords(c); }
    public void detectFraud(Claim c) { analyzePatterns(c); crossReference(c); flagSuspicious(c); }
    public void manageDocuments() { scanDocuments(); indexFiles(); archiveRecords(); }
    public void generateReports() { claimStatistics(); fraudAnalysis(); financialSummary(); }
    public void handleAppeals(Appeal a) { reviewCase(a); assignAdjuster(a); resolveDispute(a); }
    public void updatePolicies() { renewPolicies(); adjustPremiums(); processEndorsements(); }
    public void communicateCustomers() { sendUpdates(); answerQueries(); scheduleCallbacks(); }
    public void coordinateVendors() { assignRepairShops(); approveEstimates(); authorizeWork(); }
    public void manageAdjusters() { assignCases(); trackProgress(); evaluatePerformance(); }
    public void complianceReporting() { regulatoryReports(); auditTrails(); legalDocumentation(); }
    public void analyticsAndTrends() { lossRatios(); claimTrends(); riskAssessment(); }
}"""
    },
    {
        "id": 7,
        "expected": "GodClass",
        "description": "Event management platform",
        "code": """
public class EventManagementPlatform {
    private VenueService venues;
    private VendorCoordinator vendors;
    private TicketingSystem tickets;
    private MarketingEngine marketing;
    private BudgetTracker budget;
    private AttendeeManager attendees;
    
    public void createEvent(Event e) { defineDetails(e); setVenue(e); createTimeline(e); }
    public void bookVenue(Event e, Venue v) { checkAvailability(v); negotiateRate(v); signContract(v); }
    public void manageVendors() { sourcеVendors(); compareQuotes(); assignServices(); }
    public void sellTickets() { setupPricing(); launchSales(); trackRevenue(); }
    public void marketEvent() { createCampaign(); socialMedia(); emailBlasts(); trackROI(); }
    public void manageBudget() { allocateFunds(); trackExpenses(); generateForecasts(); }
    public void coordinateLogistics() { planSetup(); manageEquipment(); arrangeTransport(); }
    public void handleRegistrations() { processSignups(); issueConfirmations(); manageWaitlist(); }
    public void manageSponsors() { createPackages(); pitchSponsors(); fulfillBenefits(); }
    public void coordinateDay() { briefStaff(); manageSchedule(); handleEmergencies(); }
    public void collectFeedback() { createSurveys(); analyzeResponses(); generateInsights(); }
    public void processRefunds() { validateRequests(); calculateAmounts(); issueRefunds(); }
    public void generateReports() { attendanceStats(); financialSummary(); vendorPerformance(); }
    public void archiveEvent() { collectAssets(); documentLearnings(); updatePortfolio(); }
    public void planNextEvent() { analyzeData(); improveProcesses(); setGoals(); }
}"""
    },
    {
        "id": 8,
        "expected": "GodClass",
        "description": "Warehouse management system",
        "code": """
public class WarehouseManagement {
    private InventoryTracker inventory;
    private OrderFulfillment orders;
    private ShippingCoordinator shipping;
    private ReceivingDock receiving;
    private QualityControl qc;
    private WorkforceManager workforce;
    
    public void receiveShipment(Shipment s) { inspectGoods(s); updateInventory(s); storeItems(s); }
    public void pickOrder(Order o) { locateItems(o); retrieveItems(o); prepareShipment(o); }
    public void packOrder(Order o) { selectPackaging(o); packItems(o); printLabel(o); }
    public void shipOrder(Order o) { selectCarrier(o); schedulePickup(o); trackShipment(o); }
    public void manageInventory() { trackLevels(); reorderStock(); conductCounts(); }
    public void qualityCheck(Item i) { inspectItem(i); documentDefects(i); processReturns(i); }
    public void manageReturns(Return r) { processInbound(r); inspectCondition(r); restockOrDispose(r); }
    public void optimizeStorage() { analyzeMovement(); reorganizeLayout(); updateLocations(); }
    public void manageWorkforce() { scheduleShifts(); assignTasks(); trackProductivity(); }
    public void generateReports() { inventoryLevels(); fulfillmentRates(); laborMetrics(); }
    public void maintainEquipment() { scheduleMaintenance(); trackCondition(); orderParts(); }
    public void handleHazmat() { classifyMaterials(); ensureCompliance(); manageDisposal(); }
    public void coordinateTransport() { routeOptimization(); fleetManagement(); driverScheduling(); }
    public void manageSecurity() { accessControl(); surveillanceMonitoring(); incidentReporting(); }
    public void barcodeManagement() { printLabels(); scanItems(); updateDatabase(); }
}"""
    },
    
    # ========================================================================
    # DATA CLASS SAMPLES (9-16)
    # ========================================================================
    {
        "id": 9,
        "expected": "DataClass",
        "description": "Product entity with only getters/setters",
        "code": """
public class Product {
    private Long productId;
    private String name;
    private String description;
    private BigDecimal price;
    private String category;
    private int stockQuantity;
    
    public Long getProductId() { return productId; }
    public void setProductId(Long productId) { this.productId = productId; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public BigDecimal getPrice() { return price; }
    public void setPrice(BigDecimal price) { this.price = price; }
    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }
    public int getStockQuantity() { return stockQuantity; }
    public void setStockQuantity(int stockQuantity) { this.stockQuantity = stockQuantity; }
}"""
    },
    {
        "id": 10,
        "expected": "DataClass",
        "description": "Employee record with no logic",
        "code": """
public class Employee {
    private String employeeId;
    private String firstName;
    private String lastName;
    private String email;
    private String department;
    private Double salary;
    private Date hireDate;
    
    public String getEmployeeId() { return employeeId; }
    public void setEmployeeId(String employeeId) { this.employeeId = employeeId; }
    public String getFirstName() { return firstName; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public String getLastName() { return lastName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getDepartment() { return department; }
    public void setDepartment(String department) { this.department = department; }
    public Double getSalary() { return salary; }
    public void setSalary(Double salary) { this.salary = salary; }
    public Date getHireDate() { return hireDate; }
    public void setHireDate(Date hireDate) { this.hireDate = hireDate; }
}"""
    },
    {
        "id": 11,
        "expected": "DataClass",
        "description": "Invoice data holder",
        "code": """
public class Invoice {
    private String invoiceNumber;
    private Date invoiceDate;
    private String customerName;
    private Double subtotal;
    private Double tax;
    private Double total;
    
    public String getInvoiceNumber() { return invoiceNumber; }
    public void setInvoiceNumber(String invoiceNumber) { this.invoiceNumber = invoiceNumber; }
    public Date getInvoiceDate() { return invoiceDate; }
    public void setInvoiceDate(Date invoiceDate) { this.invoiceDate = invoiceDate; }
    public String getCustomerName() { return customerName; }
    public void setCustomerName(String customerName) { this.customerName = customerName; }
    public Double getSubtotal() { return subtotal; }
    public void setSubtotal(Double subtotal) { this.subtotal = subtotal; }
    public Double getTax() { return tax; }
    public void setTax(Double tax) { this.tax = tax; }
    public Double getTotal() { return total; }
    public void setTotal(Double total) { this.total = total; }
}"""
    },
    {
        "id": 12,
        "expected": "DataClass",
        "description": "Shipping address DTO",
        "code": """
public class ShippingAddress {
    private String street;
    private String city;
    private String state;
    private String zipCode;
    private String country;
    private String phoneNumber;
    
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
    public String getPhoneNumber() { return phoneNumber; }
    public void setPhoneNumber(String phoneNumber) { this.phoneNumber = phoneNumber; }
}"""
    },
    {
        "id": 13,
        "expected": "DataClass",
        "description": "Medical patient record",
        "code": """
public class PatientRecord {
    private String patientId;
    private String fullName;
    private Date dateOfBirth;
    private String bloodType;
    private String allergies;
    private String emergencyContact;
    
    public String getPatientId() { return patientId; }
    public void setPatientId(String patientId) { this.patientId = patientId; }
    public String getFullName() { return fullName; }
    public void setFullName(String fullName) { this.fullName = fullName; }
    public Date getDateOfBirth() { return dateOfBirth; }
    public void setDateOfBirth(Date dateOfBirth) { this.dateOfBirth = dateOfBirth; }
    public String getBloodType() { return bloodType; }
    public void setBloodType(String bloodType) { this.bloodType = bloodType; }
    public String getAllergies() { return allergies; }
    public void setAllergies(String allergies) { this.allergies = allergies; }
    public String getEmergencyContact() { return emergencyContact; }
    public void setEmergencyContact(String emergencyContact) { this.emergencyContact = emergencyContact; }
}"""
    },
    {
        "id": 14,
        "expected": "DataClass",
        "description": "Flight booking info",
        "code": """
public class FlightBooking {
    private String bookingRef;
    private String passengerName;
    private String flightNumber;
    private Date departureDate;
    private String origin;
    private String destination;
    private String seatNumber;
    
    public String getBookingRef() { return bookingRef; }
    public void setBookingRef(String bookingRef) { this.bookingRef = bookingRef; }
    public String getPassengerName() { return passengerName; }
    public void setPassengerName(String passengerName) { this.passengerName = passengerName; }
    public String getFlightNumber() { return flightNumber; }
    public void setFlightNumber(String flightNumber) { this.flightNumber = flightNumber; }
    public Date getDepartureDate() { return departureDate; }
    public void setDepartureDate(Date departureDate) { this.departureDate = departureDate; }
    public String getOrigin() { return origin; }
    public void setOrigin(String origin) { this.origin = origin; }
    public String getDestination() { return destination; }
    public void setDestination(String destination) { this.destination = destination; }
    public String getSeatNumber() { return seatNumber; }
    public void setSeatNumber(String seatNumber) { this.seatNumber = seatNumber; }
}"""
    },
    {
        "id": 15,
        "expected": "DataClass",
        "description": "Movie information bean",
        "code": """
public class MovieInfo {
    private String movieId;
    private String title;
    private String director;
    private int releaseYear;
    private String genre;
    private double rating;
    private int durationMinutes;
    
    public String getMovieId() { return movieId; }
    public void setMovieId(String movieId) { this.movieId = movieId; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getDirector() { return director; }
    public void setDirector(String director) { this.director = director; }
    public int getReleaseYear() { return releaseYear; }
    public void setReleaseYear(int releaseYear) { this.releaseYear = releaseYear; }
    public String getGenre() { return genre; }
    public void setGenre(String genre) { this.genre = genre; }
    public double getRating() { return rating; }
    public void setRating(double rating) { this.rating = rating; }
    public int getDurationMinutes() { return durationMinutes; }
    public void setDurationMinutes(int durationMinutes) { this.durationMinutes = durationMinutes; }
}"""
    },
    {
        "id": 16,
        "expected": "DataClass",
        "description": "Bank account details",
        "code": """
public class BankAccountDetails {
    private String accountNumber;
    private String accountHolder;
    private String accountType;
    private Double balance;
    private String branchCode;
    private Date openedDate;
    
    public String getAccountNumber() { return accountNumber; }
    public void setAccountNumber(String accountNumber) { this.accountNumber = accountNumber; }
    public String getAccountHolder() { return accountHolder; }
    public void setAccountHolder(String accountHolder) { this.accountHolder = accountHolder; }
    public String getAccountType() { return accountType; }
    public void setAccountType(String accountType) { this.accountType = accountType; }
    public Double getBalance() { return balance; }
    public void setBalance(Double balance) { this.balance = balance; }
    public String getBranchCode() { return branchCode; }
    public void setBranchCode(String branchCode) { this.branchCode = branchCode; }
    public Date getOpenedDate() { return openedDate; }
    public void setOpenedDate(Date openedDate) { this.openedDate = openedDate; }
}"""
    },
    
    # ========================================================================
    # LONG METHOD SAMPLES (17-24)
    # ========================================================================
    {
        "id": 17,
        "expected": "LongMethod",
        "description": "Order processing with too many steps",
        "code": """
public class OrderProcessor {
    public void processOrder(Order order) {
        // Step 1: Validate order
        if (order == null) {
            throw new IllegalArgumentException("Order cannot be null");
        }
        if (order.getItems() == null || order.getItems().isEmpty()) {
            throw new IllegalArgumentException("Order must have items");
        }
        if (order.getCustomer() == null) {
            throw new IllegalArgumentException("Order must have customer");
        }
        
        // Step 2: Check inventory
        for (OrderItem item : order.getItems()) {
            int available = inventoryService.getStock(item.getProductId());
            if (available < item.getQuantity()) {
                throw new InsufficientStockException("Not enough stock for " + item.getProductId());
            }
        }
        
        // Step 3: Calculate totals
        double subtotal = 0;
        for (OrderItem item : order.getItems()) {
            double price = pricingService.getPrice(item.getProductId());
            subtotal += price * item.getQuantity();
        }
        
        // Step 4: Apply discounts
        double discount = 0;
        if (order.getCouponCode() != null) {
            Coupon coupon = couponService.validate(order.getCouponCode());
            if (coupon != null && coupon.isValid()) {
                if (coupon.getType() == CouponType.PERCENTAGE) {
                    discount = subtotal * (coupon.getValue() / 100);
                } else {
                    discount = coupon.getValue();
                }
            }
        }
        
        // Step 5: Calculate tax
        double taxRate = taxService.getTaxRate(order.getShippingAddress().getState());
        double tax = (subtotal - discount) * taxRate;
        
        // Step 6: Calculate shipping
        double shipping = 0;
        double weight = 0;
        for (OrderItem item : order.getItems()) {
            weight += productService.getWeight(item.getProductId()) * item.getQuantity();
        }
        if (weight < 1) {
            shipping = 5.99;
        } else if (weight < 5) {
            shipping = 9.99;
        } else if (weight < 10) {
            shipping = 14.99;
        } else {
            shipping = 19.99 + (weight - 10) * 0.50;
        }
        
        // Step 7: Calculate final total
        double total = subtotal - discount + tax + shipping;
        order.setSubtotal(subtotal);
        order.setDiscount(discount);
        order.setTax(tax);
        order.setShipping(shipping);
        order.setTotal(total);
        
        // Step 8: Process payment
        PaymentResult result = paymentService.charge(order.getPaymentMethod(), total);
        if (!result.isSuccess()) {
            throw new PaymentFailedException(result.getError());
        }
        order.setPaymentConfirmation(result.getConfirmationNumber());
        
        // Step 9: Update inventory
        for (OrderItem item : order.getItems()) {
            inventoryService.decrementStock(item.getProductId(), item.getQuantity());
        }
        
        // Step 10: Save order
        order.setStatus(OrderStatus.CONFIRMED);
        order.setOrderDate(new Date());
        orderRepository.save(order);
        
        // Step 11: Send confirmation
        String emailBody = buildConfirmationEmail(order);
        emailService.send(order.getCustomer().getEmail(), "Order Confirmation", emailBody);
    }
}"""
    },
    {
        "id": 18,
        "expected": "LongMethod",
        "description": "Report generation with many sections",
        "code": """
public class ReportGenerator {
    public String generateMonthlyReport(int year, int month) {
        StringBuilder report = new StringBuilder();
        
        // Section 1: Header
        report.append("=".repeat(80)).append("\\n");
        report.append("MONTHLY FINANCIAL REPORT\\n");
        report.append("Period: ").append(month).append("/").append(year).append("\\n");
        report.append("Generated: ").append(new Date()).append("\\n");
        report.append("=".repeat(80)).append("\\n\\n");
        
        // Section 2: Revenue Summary
        report.append("REVENUE SUMMARY\\n");
        report.append("-".repeat(40)).append("\\n");
        List<Transaction> sales = transactionRepo.findSalesByMonth(year, month);
        double totalRevenue = 0;
        Map<String, Double> revenueByCategory = new HashMap<>();
        for (Transaction t : sales) {
            totalRevenue += t.getAmount();
            String category = t.getCategory();
            revenueByCategory.merge(category, t.getAmount(), Double::sum);
        }
        report.append("Total Revenue: $").append(String.format("%.2f", totalRevenue)).append("\\n");
        for (Map.Entry<String, Double> entry : revenueByCategory.entrySet()) {
            report.append("  ").append(entry.getKey()).append(": $");
            report.append(String.format("%.2f", entry.getValue())).append("\\n");
        }
        
        // Section 3: Expense Summary
        report.append("\\nEXPENSE SUMMARY\\n");
        report.append("-".repeat(40)).append("\\n");
        List<Transaction> expenses = transactionRepo.findExpensesByMonth(year, month);
        double totalExpenses = 0;
        Map<String, Double> expensesByCategory = new HashMap<>();
        for (Transaction t : expenses) {
            totalExpenses += t.getAmount();
            String category = t.getCategory();
            expensesByCategory.merge(category, t.getAmount(), Double::sum);
        }
        report.append("Total Expenses: $").append(String.format("%.2f", totalExpenses)).append("\\n");
        for (Map.Entry<String, Double> entry : expensesByCategory.entrySet()) {
            report.append("  ").append(entry.getKey()).append(": $");
            report.append(String.format("%.2f", entry.getValue())).append("\\n");
        }
        
        // Section 4: Profit/Loss
        report.append("\\nPROFIT/LOSS\\n");
        report.append("-".repeat(40)).append("\\n");
        double netProfit = totalRevenue - totalExpenses;
        report.append("Net Profit: $").append(String.format("%.2f", netProfit)).append("\\n");
        double profitMargin = (netProfit / totalRevenue) * 100;
        report.append("Profit Margin: ").append(String.format("%.1f", profitMargin)).append("%\\n");
        
        // Section 5: Year-to-Date Comparison
        report.append("\\nYEAR-TO-DATE\\n");
        report.append("-".repeat(40)).append("\\n");
        double ytdRevenue = transactionRepo.getYTDRevenue(year, month);
        double ytdExpenses = transactionRepo.getYTDExpenses(year, month);
        report.append("YTD Revenue: $").append(String.format("%.2f", ytdRevenue)).append("\\n");
        report.append("YTD Expenses: $").append(String.format("%.2f", ytdExpenses)).append("\\n");
        report.append("YTD Net: $").append(String.format("%.2f", ytdRevenue - ytdExpenses)).append("\\n");
        
        // Section 6: Accounts Receivable
        report.append("\\nACCOUNTS RECEIVABLE\\n");
        report.append("-".repeat(40)).append("\\n");
        List<Invoice> unpaidInvoices = invoiceRepo.findUnpaid();
        double totalAR = 0;
        for (Invoice inv : unpaidInvoices) {
            totalAR += inv.getAmount();
            report.append("  Invoice #").append(inv.getNumber());
            report.append(" - $").append(String.format("%.2f", inv.getAmount()));
            report.append(" - Due: ").append(inv.getDueDate()).append("\\n");
        }
        report.append("Total AR: $").append(String.format("%.2f", totalAR)).append("\\n");
        
        // Section 7: Footer
        report.append("\\n").append("=".repeat(80)).append("\\n");
        report.append("END OF REPORT\\n");
        
        return report.toString();
    }
}"""
    },
    {
        "id": 19,
        "expected": "LongMethod",
        "description": "User registration with many validations",
        "code": """
public class UserRegistration {
    public User registerUser(RegistrationRequest request) {
        // Validate username
        String username = request.getUsername();
        if (username == null || username.trim().isEmpty()) {
            throw new ValidationException("Username is required");
        }
        if (username.length() < 3) {
            throw new ValidationException("Username must be at least 3 characters");
        }
        if (username.length() > 20) {
            throw new ValidationException("Username cannot exceed 20 characters");
        }
        if (!username.matches("^[a-zA-Z0-9_]+$")) {
            throw new ValidationException("Username can only contain letters, numbers, and underscores");
        }
        if (userRepository.existsByUsername(username)) {
            throw new ValidationException("Username already taken");
        }
        
        // Validate email
        String email = request.getEmail();
        if (email == null || email.trim().isEmpty()) {
            throw new ValidationException("Email is required");
        }
        if (!email.matches("^[A-Za-z0-9+_.-]+@(.+)$")) {
            throw new ValidationException("Invalid email format");
        }
        if (userRepository.existsByEmail(email)) {
            throw new ValidationException("Email already registered");
        }
        
        // Validate password
        String password = request.getPassword();
        if (password == null || password.length() < 8) {
            throw new ValidationException("Password must be at least 8 characters");
        }
        if (!password.matches(".*[A-Z].*")) {
            throw new ValidationException("Password must contain an uppercase letter");
        }
        if (!password.matches(".*[a-z].*")) {
            throw new ValidationException("Password must contain a lowercase letter");
        }
        if (!password.matches(".*[0-9].*")) {
            throw new ValidationException("Password must contain a digit");
        }
        if (!password.matches(".*[!@#$%^&*].*")) {
            throw new ValidationException("Password must contain a special character");
        }
        if (!password.equals(request.getConfirmPassword())) {
            throw new ValidationException("Passwords do not match");
        }
        
        // Validate phone number
        String phone = request.getPhoneNumber();
        if (phone != null && !phone.isEmpty()) {
            if (!phone.matches("^\\+?[0-9]{10,15}$")) {
                throw new ValidationException("Invalid phone number format");
            }
        }
        
        // Validate date of birth
        Date dob = request.getDateOfBirth();
        if (dob != null) {
            Calendar cal = Calendar.getInstance();
            cal.add(Calendar.YEAR, -13);
            if (dob.after(cal.getTime())) {
                throw new ValidationException("Must be at least 13 years old");
            }
        }
        
        // Create user
        User user = new User();
        user.setUsername(username);
        user.setEmail(email);
        user.setPasswordHash(passwordEncoder.encode(password));
        user.setPhoneNumber(phone);
        user.setDateOfBirth(dob);
        user.setCreatedAt(new Date());
        user.setStatus(UserStatus.PENDING_VERIFICATION);
        
        // Save and send verification
        user = userRepository.save(user);
        String token = tokenService.generateVerificationToken(user);
        emailService.sendVerificationEmail(user.getEmail(), token);
        
        return user;
    }
}"""
    },
    {
        "id": 20,
        "expected": "LongMethod",
        "description": "Data import with many transformations",
        "code": """
public class DataImporter {
    public ImportResult importCsvFile(File file) {
        ImportResult result = new ImportResult();
        List<String> errors = new ArrayList<>();
        int successCount = 0;
        int failCount = 0;
        
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
            // Read and validate header
            String headerLine = reader.readLine();
            if (headerLine == null) {
                throw new ImportException("File is empty");
            }
            String[] headers = headerLine.split(",");
            if (headers.length < 5) {
                throw new ImportException("Invalid header format");
            }
            
            // Find column indices
            int nameIndex = -1;
            int emailIndex = -1;
            int phoneIndex = -1;
            int addressIndex = -1;
            int cityIndex = -1;
            for (int i = 0; i < headers.length; i++) {
                String header = headers[i].trim().toLowerCase();
                if (header.equals("name")) nameIndex = i;
                else if (header.equals("email")) emailIndex = i;
                else if (header.equals("phone")) phoneIndex = i;
                else if (header.equals("address")) addressIndex = i;
                else if (header.equals("city")) cityIndex = i;
            }
            
            // Validate required columns
            if (nameIndex == -1) throw new ImportException("Missing 'name' column");
            if (emailIndex == -1) throw new ImportException("Missing 'email' column");
            
            // Process data rows
            String line;
            int lineNumber = 1;
            while ((line = reader.readLine()) != null) {
                lineNumber++;
                try {
                    String[] values = parseCsvLine(line);
                    
                    // Extract and clean values
                    String name = values.length > nameIndex ? values[nameIndex].trim() : "";
                    String email = values.length > emailIndex ? values[emailIndex].trim() : "";
                    String phone = values.length > phoneIndex ? values[phoneIndex].trim() : "";
                    String address = values.length > addressIndex ? values[addressIndex].trim() : "";
                    String city = values.length > cityIndex ? values[cityIndex].trim() : "";
                    
                    // Validate name
                    if (name.isEmpty()) {
                        throw new ValidationException("Name is required");
                    }
                    name = WordUtils.capitalizeFully(name);
                    
                    // Validate and normalize email
                    if (email.isEmpty()) {
                        throw new ValidationException("Email is required");
                    }
                    email = email.toLowerCase();
                    if (!email.matches("^[A-Za-z0-9+_.-]+@(.+)$")) {
                        throw new ValidationException("Invalid email format");
                    }
                    
                    // Normalize phone
                    if (!phone.isEmpty()) {
                        phone = phone.replaceAll("[^0-9+]", "");
                    }
                    
                    // Create and save record
                    Contact contact = new Contact();
                    contact.setName(name);
                    contact.setEmail(email);
                    contact.setPhone(phone);
                    contact.setAddress(address);
                    contact.setCity(city);
                    contactRepository.save(contact);
                    successCount++;
                    
                } catch (Exception e) {
                    failCount++;
                    errors.add("Line " + lineNumber + ": " + e.getMessage());
                }
            }
        } catch (IOException e) {
            throw new ImportException("Error reading file: " + e.getMessage());
        }
        
        result.setSuccessCount(successCount);
        result.setFailCount(failCount);
        result.setErrors(errors);
        return result;
    }
}"""
    },
    {
        "id": 21,
        "expected": "LongMethod",
        "description": "Payment processing with many conditions",
        "code": """
public class PaymentProcessor {
    public PaymentResult processPayment(PaymentRequest request) {
        PaymentResult result = new PaymentResult();
        
        // Step 1: Validate payment method
        PaymentMethod method = request.getPaymentMethod();
        if (method == null) {
            result.setSuccess(false);
            result.setError("Payment method is required");
            return result;
        }
        
        // Step 2: Validate amount
        BigDecimal amount = request.getAmount();
        if (amount == null || amount.compareTo(BigDecimal.ZERO) <= 0) {
            result.setSuccess(false);
            result.setError("Invalid payment amount");
            return result;
        }
        if (amount.compareTo(new BigDecimal("10000")) > 0) {
            result.setSuccess(false);
            result.setError("Amount exceeds maximum limit");
            return result;
        }
        
        // Step 3: Process based on payment type
        if (method.getType() == PaymentType.CREDIT_CARD) {
            // Validate card number
            String cardNumber = method.getCardNumber();
            if (cardNumber == null || cardNumber.length() < 13 || cardNumber.length() > 19) {
                result.setSuccess(false);
                result.setError("Invalid card number");
                return result;
            }
            // Validate expiry
            String expiry = method.getExpiry();
            if (!isValidExpiry(expiry)) {
                result.setSuccess(false);
                result.setError("Card has expired");
                return result;
            }
            // Validate CVV
            String cvv = method.getCvv();
            if (cvv == null || cvv.length() < 3 || cvv.length() > 4) {
                result.setSuccess(false);
                result.setError("Invalid CVV");
                return result;
            }
            // Check for fraud
            if (fraudDetector.isSuspicious(request)) {
                result.setSuccess(false);
                result.setError("Transaction flagged for review");
                auditService.logSuspiciousActivity(request);
                return result;
            }
            // Process with card processor
            CardResponse response = cardProcessor.charge(cardNumber, expiry, cvv, amount);
            if (!response.isApproved()) {
                result.setSuccess(false);
                result.setError("Card declined: " + response.getDeclineReason());
                return result;
            }
            result.setTransactionId(response.getTransactionId());
            
        } else if (method.getType() == PaymentType.BANK_TRANSFER) {
            // Validate bank details
            String accountNumber = method.getAccountNumber();
            String routingNumber = method.getRoutingNumber();
            if (accountNumber == null || routingNumber == null) {
                result.setSuccess(false);
                result.setError("Bank account details required");
                return result;
            }
            // Verify account
            if (!bankService.verifyAccount(accountNumber, routingNumber)) {
                result.setSuccess(false);
                result.setError("Unable to verify bank account");
                return result;
            }
            // Initiate transfer
            TransferResponse response = bankService.initiateTransfer(accountNumber, routingNumber, amount);
            result.setTransactionId(response.getReferenceNumber());
            result.setNote("Transfer will complete in 2-3 business days");
            
        } else if (method.getType() == PaymentType.DIGITAL_WALLET) {
            // Process wallet payment
            String walletId = method.getWalletId();
            WalletResponse response = walletService.charge(walletId, amount);
            if (!response.isSuccess()) {
                result.setSuccess(false);
                result.setError("Wallet payment failed");
                return result;
            }
            result.setTransactionId(response.getPaymentId());
        }
        
        // Step 4: Record transaction
        Transaction transaction = new Transaction();
        transaction.setAmount(amount);
        transaction.setPaymentMethod(method.getType().toString());
        transaction.setTransactionId(result.getTransactionId());
        transaction.setTimestamp(new Date());
        transactionRepository.save(transaction);
        
        result.setSuccess(true);
        return result;
    }
}"""
    },
    {
        "id": 22,
        "expected": "LongMethod",
        "description": "Search filter with many parameters",
        "code": """
public class SearchService {
    public SearchResult search(SearchCriteria criteria) {
        StringBuilder queryBuilder = new StringBuilder();
        List<Object> parameters = new ArrayList<>();
        
        // Build base query
        queryBuilder.append("SELECT * FROM products WHERE 1=1");
        
        // Filter by keyword
        if (criteria.getKeyword() != null && !criteria.getKeyword().trim().isEmpty()) {
            String keyword = criteria.getKeyword().trim();
            queryBuilder.append(" AND (name LIKE ? OR description LIKE ? OR sku LIKE ?)");
            parameters.add("%" + keyword + "%");
            parameters.add("%" + keyword + "%");
            parameters.add("%" + keyword + "%");
        }
        
        // Filter by category
        if (criteria.getCategoryId() != null) {
            queryBuilder.append(" AND category_id = ?");
            parameters.add(criteria.getCategoryId());
        }
        
        // Filter by subcategory
        if (criteria.getSubcategoryId() != null) {
            queryBuilder.append(" AND subcategory_id = ?");
            parameters.add(criteria.getSubcategoryId());
        }
        
        // Filter by brand
        if (criteria.getBrandIds() != null && !criteria.getBrandIds().isEmpty()) {
            queryBuilder.append(" AND brand_id IN (");
            for (int i = 0; i < criteria.getBrandIds().size(); i++) {
                if (i > 0) queryBuilder.append(",");
                queryBuilder.append("?");
                parameters.add(criteria.getBrandIds().get(i));
            }
            queryBuilder.append(")");
        }
        
        // Filter by price range
        if (criteria.getMinPrice() != null) {
            queryBuilder.append(" AND price >= ?");
            parameters.add(criteria.getMinPrice());
        }
        if (criteria.getMaxPrice() != null) {
            queryBuilder.append(" AND price <= ?");
            parameters.add(criteria.getMaxPrice());
        }
        
        // Filter by rating
        if (criteria.getMinRating() != null) {
            queryBuilder.append(" AND average_rating >= ?");
            parameters.add(criteria.getMinRating());
        }
        
        // Filter by availability
        if (criteria.isInStockOnly()) {
            queryBuilder.append(" AND stock_quantity > 0");
        }
        
        // Filter by sale items
        if (criteria.isOnSaleOnly()) {
            queryBuilder.append(" AND sale_price IS NOT NULL AND sale_price < price");
        }
        
        // Filter by new arrivals
        if (criteria.isNewArrivalsOnly()) {
            queryBuilder.append(" AND created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY)");
        }
        
        // Filter by attributes
        if (criteria.getAttributes() != null) {
            for (Map.Entry<String, String> attr : criteria.getAttributes().entrySet()) {
                queryBuilder.append(" AND EXISTS (SELECT 1 FROM product_attributes pa");
                queryBuilder.append(" WHERE pa.product_id = products.id");
                queryBuilder.append(" AND pa.attribute_name = ? AND pa.attribute_value = ?)");
                parameters.add(attr.getKey());
                parameters.add(attr.getValue());
            }
        }
        
        // Add sorting
        String sortField = criteria.getSortBy() != null ? criteria.getSortBy() : "created_at";
        String sortDirection = criteria.getSortDirection() != null ? criteria.getSortDirection() : "DESC";
        queryBuilder.append(" ORDER BY ").append(sortField).append(" ").append(sortDirection);
        
        // Add pagination
        int page = criteria.getPage() != null ? criteria.getPage() : 0;
        int size = criteria.getPageSize() != null ? criteria.getPageSize() : 20;
        queryBuilder.append(" LIMIT ? OFFSET ?");
        parameters.add(size);
        parameters.add(page * size);
        
        // Execute query
        List<Product> products = jdbcTemplate.query(queryBuilder.toString(), 
            parameters.toArray(), productRowMapper);
        
        // Get total count
        String countQuery = queryBuilder.toString().replaceFirst("SELECT \\*", "SELECT COUNT(*)");
        countQuery = countQuery.substring(0, countQuery.indexOf("ORDER BY"));
        Long totalCount = jdbcTemplate.queryForObject(countQuery, 
            parameters.subList(0, parameters.size() - 2).toArray(), Long.class);
        
        SearchResult result = new SearchResult();
        result.setProducts(products);
        result.setTotalCount(totalCount);
        result.setPage(page);
        result.setPageSize(size);
        return result;
    }
}"""
    },
    {
        "id": 23,
        "expected": "LongMethod",
        "description": "Email template builder",
        "code": """
public class EmailTemplateBuilder {
    public String buildOrderConfirmationEmail(Order order) {
        StringBuilder email = new StringBuilder();
        
        // HTML Header
        email.append("<!DOCTYPE html>");
        email.append("<html><head>");
        email.append("<meta charset='UTF-8'>");
        email.append("<style>");
        email.append("body { font-family: Arial, sans-serif; line-height: 1.6; }");
        email.append(".container { max-width: 600px; margin: 0 auto; padding: 20px; }");
        email.append(".header { background-color: #4CAF50; color: white; padding: 20px; text-align: center; }");
        email.append(".order-details { background-color: #f9f9f9; padding: 15px; margin: 20px 0; }");
        email.append(".item-row { border-bottom: 1px solid #ddd; padding: 10px 0; }");
        email.append(".total-row { font-weight: bold; font-size: 18px; }");
        email.append(".footer { background-color: #333; color: white; padding: 15px; text-align: center; }");
        email.append("</style>");
        email.append("</head><body>");
        
        // Header section
        email.append("<div class='container'>");
        email.append("<div class='header'>");
        email.append("<h1>Order Confirmation</h1>");
        email.append("<p>Thank you for your order!</p>");
        email.append("</div>");
        
        // Order info
        email.append("<div class='order-details'>");
        email.append("<h2>Order #").append(order.getOrderNumber()).append("</h2>");
        email.append("<p>Order Date: ").append(formatDate(order.getOrderDate())).append("</p>");
        email.append("<p>Status: ").append(order.getStatus()).append("</p>");
        email.append("</div>");
        
        // Customer info
        email.append("<h3>Shipping To:</h3>");
        email.append("<p>");
        email.append(order.getShippingAddress().getName()).append("<br>");
        email.append(order.getShippingAddress().getStreet()).append("<br>");
        email.append(order.getShippingAddress().getCity()).append(", ");
        email.append(order.getShippingAddress().getState()).append(" ");
        email.append(order.getShippingAddress().getZipCode()).append("<br>");
        email.append(order.getShippingAddress().getCountry());
        email.append("</p>");
        
        // Order items
        email.append("<h3>Order Items:</h3>");
        email.append("<table width='100%'>");
        for (OrderItem item : order.getItems()) {
            email.append("<tr class='item-row'>");
            email.append("<td>").append(item.getProductName()).append("</td>");
            email.append("<td>Qty: ").append(item.getQuantity()).append("</td>");
            email.append("<td align='right'>$").append(formatCurrency(item.getPrice())).append("</td>");
            email.append("</tr>");
        }
        email.append("</table>");
        
        // Order totals
        email.append("<div class='order-details'>");
        email.append("<table width='100%'>");
        email.append("<tr><td>Subtotal:</td><td align='right'>$").append(formatCurrency(order.getSubtotal())).append("</td></tr>");
        if (order.getDiscount() > 0) {
            email.append("<tr><td>Discount:</td><td align='right'>-$").append(formatCurrency(order.getDiscount())).append("</td></tr>");
        }
        email.append("<tr><td>Shipping:</td><td align='right'>$").append(formatCurrency(order.getShipping())).append("</td></tr>");
        email.append("<tr><td>Tax:</td><td align='right'>$").append(formatCurrency(order.getTax())).append("</td></tr>");
        email.append("<tr class='total-row'><td>Total:</td><td align='right'>$").append(formatCurrency(order.getTotal())).append("</td></tr>");
        email.append("</table>");
        email.append("</div>");
        
        // Footer
        email.append("<div class='footer'>");
        email.append("<p>Questions? Contact us at support@example.com</p>");
        email.append("<p>&copy; 2024 Our Company. All rights reserved.</p>");
        email.append("</div>");
        
        email.append("</div></body></html>");
        
        return email.toString();
    }
}"""
    },
    {
        "id": 24,
        "expected": "LongMethod",
        "description": "Configuration loader with many settings",
        "code": """
public class ConfigurationLoader {
    public ApplicationConfig loadConfiguration(String configPath) {
        ApplicationConfig config = new ApplicationConfig();
        Properties props = new Properties();
        
        // Load properties file
        try (InputStream input = new FileInputStream(configPath)) {
            props.load(input);
        } catch (IOException e) {
            logger.error("Failed to load config file: " + configPath, e);
            throw new ConfigurationException("Cannot load configuration", e);
        }
        
        // Database settings
        config.setDbHost(props.getProperty("db.host", "localhost"));
        config.setDbPort(Integer.parseInt(props.getProperty("db.port", "5432")));
        config.setDbName(props.getProperty("db.name", "myapp"));
        config.setDbUsername(props.getProperty("db.username", "admin"));
        config.setDbPassword(props.getProperty("db.password"));
        config.setDbPoolSize(Integer.parseInt(props.getProperty("db.pool.size", "10")));
        config.setDbPoolTimeout(Integer.parseInt(props.getProperty("db.pool.timeout", "30000")));
        
        // Server settings
        config.setServerPort(Integer.parseInt(props.getProperty("server.port", "8080")));
        config.setServerHost(props.getProperty("server.host", "0.0.0.0"));
        config.setServerContextPath(props.getProperty("server.context-path", "/"));
        config.setServerMaxThreads(Integer.parseInt(props.getProperty("server.max-threads", "200")));
        config.setServerIdleTimeout(Integer.parseInt(props.getProperty("server.idle-timeout", "60000")));
        
        // Cache settings
        config.setCacheEnabled(Boolean.parseBoolean(props.getProperty("cache.enabled", "true")));
        config.setCacheType(props.getProperty("cache.type", "redis"));
        config.setCacheHost(props.getProperty("cache.host", "localhost"));
        config.setCachePort(Integer.parseInt(props.getProperty("cache.port", "6379")));
        config.setCacheTtl(Integer.parseInt(props.getProperty("cache.ttl", "3600")));
        
        // Security settings
        config.setSecurityEnabled(Boolean.parseBoolean(props.getProperty("security.enabled", "true")));
        config.setJwtSecret(props.getProperty("security.jwt.secret"));
        config.setJwtExpiration(Integer.parseInt(props.getProperty("security.jwt.expiration", "86400")));
        config.setCorsEnabled(Boolean.parseBoolean(props.getProperty("security.cors.enabled", "false")));
        config.setCorsOrigins(props.getProperty("security.cors.origins", "*"));
        
        // Logging settings
        config.setLogLevel(props.getProperty("logging.level", "INFO"));
        config.setLogPath(props.getProperty("logging.path", "/var/log/app"));
        config.setLogMaxSize(props.getProperty("logging.max-size", "10MB"));
        config.setLogMaxHistory(Integer.parseInt(props.getProperty("logging.max-history", "30")));
        
        // Email settings
        config.setSmtpHost(props.getProperty("mail.smtp.host"));
        config.setSmtpPort(Integer.parseInt(props.getProperty("mail.smtp.port", "587")));
        config.setSmtpUsername(props.getProperty("mail.smtp.username"));
        config.setSmtpPassword(props.getProperty("mail.smtp.password"));
        config.setSmtpTls(Boolean.parseBoolean(props.getProperty("mail.smtp.tls", "true")));
        
        // Validate required settings
        if (config.getDbPassword() == null || config.getDbPassword().isEmpty()) {
            throw new ConfigurationException("Database password is required");
        }
        if (config.getJwtSecret() == null || config.getJwtSecret().length() < 32) {
            throw new ConfigurationException("JWT secret must be at least 32 characters");
        }
        
        logger.info("Configuration loaded successfully from: " + configPath);
        return config;
    }
}"""
    },
    
    # ========================================================================
    # FEATURE ENVY SAMPLES (25-32)
    # ========================================================================
    {
        "id": 25,
        "expected": "FeatureEnvy",
        "description": "Invoice calculator using client data",
        "code": """
public class InvoiceCalculator {
    public double calculateTotal(Client client) {
        double baseAmount = client.getOrderAmount();
        String tier = client.getMembershipTier();
        int yearsActive = client.getYearsAsCustomer();
        boolean isPreferred = client.isPreferredClient();
        double creditBalance = client.getCreditBalance();
        
        double discount = 0;
        if (tier.equals("GOLD")) {
            discount = baseAmount * 0.15;
        } else if (tier.equals("SILVER")) {
            discount = baseAmount * 0.10;
        } else if (tier.equals("BRONZE")) {
            discount = baseAmount * 0.05;
        }
        
        if (yearsActive > 5) {
            discount += baseAmount * 0.02;
        }
        if (isPreferred) {
            discount += baseAmount * 0.03;
        }
        
        double total = baseAmount - discount;
        if (creditBalance > 0) {
            total -= Math.min(creditBalance, total);
        }
        
        return total;
    }
}"""
    },
    {
        "id": 26,
        "expected": "FeatureEnvy",
        "description": "Order validator accessing cart extensively",
        "code": """
public class OrderValidator {
    public boolean validateOrder(ShoppingCart cart) {
        List<CartItem> items = cart.getItems();
        String couponCode = cart.getCouponCode();
        double subtotal = cart.getSubtotal();
        Address shippingAddress = cart.getShippingAddress();
        PaymentInfo payment = cart.getPaymentInfo();
        
        if (items == null || items.isEmpty()) {
            return false;
        }
        
        for (CartItem item : items) {
            if (item.getQuantity() <= 0) {
                return false;
            }
            if (item.getPrice() <= 0) {
                return false;
            }
        }
        
        if (shippingAddress == null) {
            return false;
        }
        if (shippingAddress.getStreet() == null || shippingAddress.getStreet().isEmpty()) {
            return false;
        }
        if (shippingAddress.getCity() == null || shippingAddress.getCity().isEmpty()) {
            return false;
        }
        
        if (payment == null) {
            return false;
        }
        if (payment.getCardNumber() == null) {
            return false;
        }
        
        return subtotal > 0;
    }
}"""
    },
    {
        "id": 27,
        "expected": "FeatureEnvy",
        "description": "Report builder using employee data",
        "code": """
public class PerformanceReportBuilder {
    public String buildReport(Employee employee) {
        String name = employee.getFullName();
        String department = employee.getDepartment();
        int tasksCompleted = employee.getTasksCompleted();
        int tasksFailed = employee.getTasksFailed();
        double hoursWorked = employee.getHoursWorked();
        Date startDate = employee.getStartDate();
        double salary = employee.getSalary();
        List<String> skills = employee.getSkills();
        
        double successRate = (double) tasksCompleted / (tasksCompleted + tasksFailed) * 100;
        double productivity = tasksCompleted / hoursWorked;
        long daysEmployed = Duration.between(startDate.toInstant(), Instant.now()).toDays();
        double costPerTask = salary / tasksCompleted;
        
        StringBuilder report = new StringBuilder();
        report.append("Performance Report for: ").append(name).append("\\n");
        report.append("Department: ").append(department).append("\\n");
        report.append("Success Rate: ").append(String.format("%.1f", successRate)).append("%\\n");
        report.append("Productivity: ").append(String.format("%.2f", productivity)).append(" tasks/hour\\n");
        report.append("Days Employed: ").append(daysEmployed).append("\\n");
        report.append("Cost Per Task: $").append(String.format("%.2f", costPerTask)).append("\\n");
        report.append("Skills: ").append(String.join(", ", skills)).append("\\n");
        
        return report.toString();
    }
}"""
    },
    {
        "id": 28,
        "expected": "FeatureEnvy",
        "description": "Shipping calculator using package data",
        "code": """
public class ShippingCalculator {
    public double calculateShipping(Package pkg) {
        double weight = pkg.getWeight();
        double length = pkg.getLength();
        double width = pkg.getWidth();
        double height = pkg.getHeight();
        String destination = pkg.getDestinationZone();
        boolean isFragile = pkg.isFragile();
        boolean isUrgent = pkg.isUrgent();
        
        double volume = length * width * height;
        double dimensionalWeight = volume / 139;
        double billableWeight = Math.max(weight, dimensionalWeight);
        
        double baseRate;
        if (destination.equals("LOCAL")) {
            baseRate = 5.99;
        } else if (destination.equals("REGIONAL")) {
            baseRate = 9.99;
        } else if (destination.equals("NATIONAL")) {
            baseRate = 14.99;
        } else {
            baseRate = 29.99;
        }
        
        double weightCharge = billableWeight * 0.50;
        double total = baseRate + weightCharge;
        
        if (isFragile) {
            total += 5.00;
        }
        if (isUrgent) {
            total *= 1.5;
        }
        
        return total;
    }
}"""
    },
    {
        "id": 29,
        "expected": "FeatureEnvy",
        "description": "Discount applier using product data",
        "code": """
public class DiscountApplier {
    public double applyDiscount(Product product) {
        double price = product.getPrice();
        String category = product.getCategory();
        boolean isClearance = product.isClearance();
        boolean isSeasonalItem = product.isSeasonalItem();
        int stockLevel = product.getStockLevel();
        Date addedDate = product.getAddedDate();
        
        double discount = 0;
        
        if (category.equals("ELECTRONICS")) {
            discount = price * 0.10;
        } else if (category.equals("CLOTHING")) {
            discount = price * 0.20;
        } else if (category.equals("FURNITURE")) {
            discount = price * 0.15;
        }
        
        if (isClearance) {
            discount += price * 0.25;
        }
        
        if (isSeasonalItem) {
            discount += price * 0.10;
        }
        
        if (stockLevel > 100) {
            discount += price * 0.05;
        }
        
        long daysInStock = Duration.between(addedDate.toInstant(), Instant.now()).toDays();
        if (daysInStock > 90) {
            discount += price * 0.10;
        }
        
        return price - discount;
    }
}"""
    },
    {
        "id": 30,
        "expected": "FeatureEnvy",
        "description": "Loan eligibility checker",
        "code": """
public class LoanEligibilityChecker {
    public boolean checkEligibility(Applicant applicant) {
        double income = applicant.getAnnualIncome();
        double existingDebt = applicant.getExistingDebt();
        int creditScore = applicant.getCreditScore();
        int yearsEmployed = applicant.getYearsEmployed();
        boolean hasCollateral = applicant.hasCollateral();
        double requestedAmount = applicant.getRequestedLoanAmount();
        
        double debtToIncomeRatio = existingDebt / income;
        if (debtToIncomeRatio > 0.43) {
            return false;
        }
        
        if (creditScore < 620) {
            return false;
        }
        
        if (yearsEmployed < 2) {
            return false;
        }
        
        double maxLoan = income * 4;
        if (creditScore >= 750) {
            maxLoan = income * 5;
        }
        if (hasCollateral) {
            maxLoan *= 1.2;
        }
        
        if (requestedAmount > maxLoan) {
            return false;
        }
        
        return true;
    }
}"""
    },
    {
        "id": 31,
        "expected": "FeatureEnvy",
        "description": "Tax calculator using citizen data",
        "code": """
public class TaxCalculator {
    public double calculateTax(Citizen citizen) {
        double grossIncome = citizen.getGrossIncome();
        int dependents = citizen.getNumberOfDependents();
        boolean isMarried = citizen.isMarried();
        double charitableDonations = citizen.getCharitableDonations();
        double mortgageInterest = citizen.getMortgageInterest();
        double medicalExpenses = citizen.getMedicalExpenses();
        boolean isHomeowner = citizen.isHomeowner();
        
        double deductions = 0;
        deductions += dependents * 2000;
        if (isMarried) {
            deductions += 5000;
        }
        deductions += charitableDonations;
        deductions += mortgageInterest;
        if (medicalExpenses > grossIncome * 0.075) {
            deductions += medicalExpenses - (grossIncome * 0.075);
        }
        if (isHomeowner) {
            deductions += 3000;
        }
        
        double taxableIncome = Math.max(0, grossIncome - deductions);
        
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
        
        return tax;
    }
}"""
    },
    {
        "id": 32,
        "expected": "FeatureEnvy",
        "description": "Grade calculator using student data",
        "code": """
public class GradeCalculator {
    public String calculateFinalGrade(Student student) {
        List<Double> testScores = student.getTestScores();
        List<Double> quizScores = student.getQuizScores();
        double homeworkAverage = student.getHomeworkAverage();
        double projectScore = student.getProjectScore();
        int attendancePercentage = student.getAttendancePercentage();
        boolean hasExtraCredit = student.hasExtraCredit();
        
        double testAverage = testScores.stream().mapToDouble(d -> d).average().orElse(0);
        double quizAverage = quizScores.stream().mapToDouble(d -> d).average().orElse(0);
        
        double weightedScore = 0;
        weightedScore += testAverage * 0.40;
        weightedScore += quizAverage * 0.20;
        weightedScore += homeworkAverage * 0.15;
        weightedScore += projectScore * 0.20;
        weightedScore += attendancePercentage * 0.05;
        
        if (hasExtraCredit) {
            weightedScore += 3;
        }
        
        if (attendancePercentage < 70) {
            weightedScore *= 0.9;
        }
        
        String grade;
        if (weightedScore >= 90) grade = "A";
        else if (weightedScore >= 80) grade = "B";
        else if (weightedScore >= 70) grade = "C";
        else if (weightedScore >= 60) grade = "D";
        else grade = "F";
        
        return grade;
    }
}"""
    },
    
    # ========================================================================
    # DEAD CODE SAMPLES (33-40)
    # ========================================================================
    {
        "id": 33,
        "expected": "DeadCode",
        "description": "Unused private methods in calculator",
        "code": """
public class AdvancedCalculator {
    private Logger logger = LoggerFactory.getLogger(this.getClass());
    
    public double add(double a, double b) {
        return a + b;
    }
    
    public double subtract(double a, double b) {
        return a - b;
    }
    
    // This method is never called anywhere
    private double oldMultiply(double a, double b) {
        logger.debug("Using old multiply");
        return a * b;
    }
    
    // This method is never called anywhere
    private double deprecatedDivide(double a, double b) {
        if (b == 0) return 0;
        return a / b;
    }
    
    // This is also never used
    private void logCalculation(String operation, double result) {
        System.out.println(operation + " = " + result);
    }
}"""
    },
    {
        "id": 34,
        "expected": "DeadCode",
        "description": "Commented out code blocks",
        "code": """
public class UserService {
    private UserRepository userRepo;
    
    public User findUser(Long id) {
        return userRepo.findById(id);
    }
    
    /*
    public void deleteUser(Long id) {
        User user = userRepo.findById(id);
        if (user != null) {
            userRepo.delete(user);
            notifyDeletion(user);
        }
    }
    
    private void notifyDeletion(User user) {
        emailService.send(user.getEmail(), "Account Deleted");
    }
    */
    
    // Old implementation - keeping for reference
    // public List<User> searchUsers(String query) {
    //     return userRepo.findByNameContaining(query);
    // }
    
    public void updateUser(User user) {
        userRepo.save(user);
    }
}"""
    },
    {
        "id": 35,
        "expected": "DeadCode",
        "description": "Empty catch blocks and unused exceptions",
        "code": """
public class FileProcessor {
    public void processFile(String path) {
        try {
            FileInputStream fis = new FileInputStream(path);
            BufferedReader reader = new BufferedReader(new InputStreamReader(fis));
            String line;
            while ((line = reader.readLine()) != null) {
                processLine(line);
            }
        } catch (FileNotFoundException e) {
            // TODO: handle this later
        } catch (IOException e) {
            // Intentionally empty
        } catch (Exception e) {
            // Swallowing exception for now
        }
    }
    
    private void processLine(String line) {
        try {
            // Process the line
            line.trim();
        } catch (NullPointerException e) {
            // ignore
        }
    }
}"""
    },
    {
        "id": 36,
        "expected": "DeadCode",
        "description": "Obsolete TODO comments and dead methods",
        "code": """
public class PaymentHandler {
    // TODO: Remove this after Q2 2020 - we no longer use PayPal v1
    private static final String PAYPAL_V1_KEY = "pk_old_12345";
    
    // FIXME: This was replaced by the new payment flow
    private void processLegacyPayment(Order order) {
        // Old payment logic that's no longer used
        double amount = order.getTotal();
        String result = legacyGateway.charge(amount);
    }
    
    public void processPayment(Order order) {
        // Current implementation
        paymentGateway.charge(order);
    }
    
    // TODO: Delete after migration is complete (was due Dec 2019)
    @Deprecated
    private void migrateOldTransactions() {
        List<Transaction> old = legacyRepo.findAll();
        for (Transaction t : old) {
            newRepo.save(convert(t));
        }
    }
}"""
    },
    {
        "id": 37,
        "expected": "DeadCode",
        "description": "Unused class fields",
        "code": """
public class OrderProcessor {
    private OrderRepository orderRepo;
    private PaymentService paymentService;
    
    // These fields are never used
    private EmailService emailService;
    private Logger logger;
    private String unusedConfig = "legacy";
    private int maxRetries = 3;
    private boolean debugMode = false;
    
    public OrderProcessor(OrderRepository orderRepo, PaymentService paymentService) {
        this.orderRepo = orderRepo;
        this.paymentService = paymentService;
    }
    
    public void process(Order order) {
        order.validate();
        paymentService.charge(order);
        orderRepo.save(order);
    }
}"""
    },
    {
        "id": 38,
        "expected": "DeadCode",
        "description": "Methods with only comments (stub methods)",
        "code": """
public class ReportGenerator {
    public String generateDailyReport() {
        // Collect data
        List<Record> records = repository.findToday();
        return formatReport(records);
    }
    
    // Reserved for future use
    public void generateWeeklyReport() {
        // TODO: Implement weekly report
        // Will aggregate daily reports
        // Need to discuss format with stakeholders
    }
    
    // Placeholder for quarterly reports
    public void generateQuarterlyReport() {
        // Implementation pending
        // Waiting for requirements
    }
    
    private String formatReport(List<Record> records) {
        StringBuilder sb = new StringBuilder();
        for (Record r : records) {
            sb.append(r.toString()).append("\\n");
        }
        return sb.toString();
    }
}"""
    },
    {
        "id": 39,
        "expected": "DeadCode",
        "description": "Unused imports and constants",
        "code": """
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.TreeMap;
import java.util.LinkedList;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Future;
import org.apache.commons.lang.StringUtils;
import com.google.common.collect.ImmutableList;

public class SimpleService {
    // These constants are never referenced
    private static final int MAX_SIZE = 1000;
    private static final String DEFAULT_NAME = "Unknown";
    private static final double TAX_RATE = 0.08;
    private static final String[] VALID_STATUSES = {"ACTIVE", "INACTIVE"};
    
    private List<String> items;
    
    public SimpleService() {
        this.items = new ArrayList<>();
    }
    
    public void addItem(String item) {
        items.add(item);
    }
    
    public List<String> getItems() {
        return items;
    }
}"""
    },
    {
        "id": 40,
        "expected": "DeadCode",
        "description": "Dead code paths with always-false conditions",
        "code": """
public class FeatureManager {
    private static final boolean LEGACY_MODE = false;
    private static final boolean DEBUG_ENABLED = false;
    
    public void executeFeature(String name) {
        // This block is never executed
        if (LEGACY_MODE) {
            executeLegacyFeature(name);
            logLegacyExecution(name);
            notifyLegacySystem(name);
        }
        
        // Normal execution
        Feature feature = featureRepo.find(name);
        feature.execute();
        
        // This is also dead code
        if (DEBUG_ENABLED && LEGACY_MODE) {
            System.out.println("Debug: " + name);
            dumpState();
        }
    }
    
    private void executeLegacyFeature(String name) { }
    private void logLegacyExecution(String name) { }
    private void notifyLegacySystem(String name) { }
    private void dumpState() { }
}"""
    },
    
    # ========================================================================
    # CLEAN CODE SAMPLES (41-50)
    # ========================================================================
    {
        "id": 41,
        "expected": "Clean",
        "description": "Well-designed repository pattern",
        "code": """
public class OrderRepository {
    private final JdbcTemplate jdbcTemplate;
    private final RowMapper<Order> orderMapper;
    
    public OrderRepository(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
        this.orderMapper = new OrderRowMapper();
    }
    
    public Order findById(Long id) {
        String sql = "SELECT * FROM orders WHERE id = ?";
        return jdbcTemplate.queryForObject(sql, orderMapper, id);
    }
    
    public List<Order> findByCustomerId(Long customerId) {
        String sql = "SELECT * FROM orders WHERE customer_id = ?";
        return jdbcTemplate.query(sql, orderMapper, customerId);
    }
    
    public void save(Order order) {
        if (order.getId() == null) {
            insert(order);
        } else {
            update(order);
        }
    }
    
    private void insert(Order order) {
        String sql = "INSERT INTO orders (customer_id, total, status) VALUES (?, ?, ?)";
        jdbcTemplate.update(sql, order.getCustomerId(), order.getTotal(), order.getStatus());
    }
    
    private void update(Order order) {
        String sql = "UPDATE orders SET total = ?, status = ? WHERE id = ?";
        jdbcTemplate.update(sql, order.getTotal(), order.getStatus(), order.getId());
    }
}"""
    },
    {
        "id": 42,
        "expected": "Clean",
        "description": "Focused service with single responsibility",
        "code": """
public class EmailNotificationService {
    private final EmailClient emailClient;
    private final TemplateEngine templateEngine;
    
    public EmailNotificationService(EmailClient emailClient, TemplateEngine templateEngine) {
        this.emailClient = emailClient;
        this.templateEngine = templateEngine;
    }
    
    public void sendWelcomeEmail(User user) {
        String content = templateEngine.render("welcome", Map.of("name", user.getName()));
        emailClient.send(user.getEmail(), "Welcome!", content);
    }
    
    public void sendPasswordResetEmail(User user, String resetToken) {
        String content = templateEngine.render("password-reset", Map.of("token", resetToken));
        emailClient.send(user.getEmail(), "Password Reset", content);
    }
    
    public void sendOrderConfirmation(User user, Order order) {
        String content = templateEngine.render("order-confirmation", Map.of("order", order));
        emailClient.send(user.getEmail(), "Order Confirmed", content);
    }
}"""
    },
    {
        "id": 43,
        "expected": "Clean",
        "description": "Strategy pattern implementation",
        "code": """
public interface PricingStrategy {
    double calculatePrice(Product product, int quantity);
}

public class RegularPricing implements PricingStrategy {
    @Override
    public double calculatePrice(Product product, int quantity) {
        return product.getBasePrice() * quantity;
    }
}

public class BulkDiscountPricing implements PricingStrategy {
    private final int bulkThreshold;
    private final double discountRate;
    
    public BulkDiscountPricing(int bulkThreshold, double discountRate) {
        this.bulkThreshold = bulkThreshold;
        this.discountRate = discountRate;
    }
    
    @Override
    public double calculatePrice(Product product, int quantity) {
        double baseTotal = product.getBasePrice() * quantity;
        if (quantity >= bulkThreshold) {
            return baseTotal * (1 - discountRate);
        }
        return baseTotal;
    }
}"""
    },
    {
        "id": 44,
        "expected": "Clean",
        "description": "Value object with proper encapsulation",
        "code": """
public final class Money {
    private final BigDecimal amount;
    private final Currency currency;
    
    public Money(BigDecimal amount, Currency currency) {
        if (amount == null) throw new IllegalArgumentException("Amount cannot be null");
        if (currency == null) throw new IllegalArgumentException("Currency cannot be null");
        this.amount = amount.setScale(2, RoundingMode.HALF_UP);
        this.currency = currency;
    }
    
    public Money add(Money other) {
        validateSameCurrency(other);
        return new Money(this.amount.add(other.amount), this.currency);
    }
    
    public Money subtract(Money other) {
        validateSameCurrency(other);
        return new Money(this.amount.subtract(other.amount), this.currency);
    }
    
    public Money multiply(int factor) {
        return new Money(this.amount.multiply(BigDecimal.valueOf(factor)), this.currency);
    }
    
    private void validateSameCurrency(Money other) {
        if (!this.currency.equals(other.currency)) {
            throw new IllegalArgumentException("Cannot operate on different currencies");
        }
    }
    
    public BigDecimal getAmount() { return amount; }
    public Currency getCurrency() { return currency; }
}"""
    },
    {
        "id": 45,
        "expected": "Clean",
        "description": "Builder pattern for complex object",
        "code": """
public class HttpRequest {
    private final String method;
    private final String url;
    private final Map<String, String> headers;
    private final String body;
    
    private HttpRequest(Builder builder) {
        this.method = builder.method;
        this.url = builder.url;
        this.headers = Collections.unmodifiableMap(builder.headers);
        this.body = builder.body;
    }
    
    public static class Builder {
        private String method = "GET";
        private String url;
        private Map<String, String> headers = new HashMap<>();
        private String body;
        
        public Builder url(String url) {
            this.url = url;
            return this;
        }
        
        public Builder method(String method) {
            this.method = method;
            return this;
        }
        
        public Builder header(String key, String value) {
            this.headers.put(key, value);
            return this;
        }
        
        public Builder body(String body) {
            this.body = body;
            return this;
        }
        
        public HttpRequest build() {
            if (url == null) throw new IllegalStateException("URL is required");
            return new HttpRequest(this);
        }
    }
}"""
    },
    {
        "id": 46,
        "expected": "Clean",
        "description": "Observer pattern implementation",
        "code": """
public interface OrderEventListener {
    void onOrderCreated(Order order);
    void onOrderShipped(Order order);
    void onOrderCancelled(Order order);
}

public class OrderEventPublisher {
    private final List<OrderEventListener> listeners = new ArrayList<>();
    
    public void subscribe(OrderEventListener listener) {
        listeners.add(listener);
    }
    
    public void unsubscribe(OrderEventListener listener) {
        listeners.remove(listener);
    }
    
    public void publishOrderCreated(Order order) {
        for (OrderEventListener listener : listeners) {
            listener.onOrderCreated(order);
        }
    }
    
    public void publishOrderShipped(Order order) {
        for (OrderEventListener listener : listeners) {
            listener.onOrderShipped(order);
        }
    }
    
    public void publishOrderCancelled(Order order) {
        for (OrderEventListener listener : listeners) {
            listener.onOrderCancelled(order);
        }
    }
}"""
    },
    {
        "id": 47,
        "expected": "Clean",
        "description": "Clean validation service",
        "code": """
public class InputValidator {
    private static final Pattern EMAIL_PATTERN = Pattern.compile("^[A-Za-z0-9+_.-]+@(.+)$");
    private static final Pattern PHONE_PATTERN = Pattern.compile("^\\\\+?[0-9]{10,15}$");
    
    public ValidationResult validateEmail(String email) {
        if (email == null || email.isEmpty()) {
            return ValidationResult.error("Email is required");
        }
        if (!EMAIL_PATTERN.matcher(email).matches()) {
            return ValidationResult.error("Invalid email format");
        }
        return ValidationResult.success();
    }
    
    public ValidationResult validatePhone(String phone) {
        if (phone == null || phone.isEmpty()) {
            return ValidationResult.success(); // Phone is optional
        }
        if (!PHONE_PATTERN.matcher(phone).matches()) {
            return ValidationResult.error("Invalid phone format");
        }
        return ValidationResult.success();
    }
    
    public ValidationResult validateRequired(String value, String fieldName) {
        if (value == null || value.trim().isEmpty()) {
            return ValidationResult.error(fieldName + " is required");
        }
        return ValidationResult.success();
    }
}"""
    },
    {
        "id": 48,
        "expected": "Clean",
        "description": "Well-structured factory class",
        "code": """
public class NotificationFactory {
    private final EmailService emailService;
    private final SmsService smsService;
    private final PushService pushService;
    
    public NotificationFactory(EmailService emailService, SmsService smsService, PushService pushService) {
        this.emailService = emailService;
        this.smsService = smsService;
        this.pushService = pushService;
    }
    
    public Notification create(NotificationType type, String recipient, String message) {
        switch (type) {
            case EMAIL:
                return new EmailNotification(emailService, recipient, message);
            case SMS:
                return new SmsNotification(smsService, recipient, message);
            case PUSH:
                return new PushNotification(pushService, recipient, message);
            default:
                throw new IllegalArgumentException("Unknown notification type: " + type);
        }
    }
}"""
    },
    {
        "id": 49,
        "expected": "Clean",
        "description": "Adapter pattern implementation",
        "code": """
public interface PaymentGateway {
    PaymentResult charge(String customerId, BigDecimal amount);
    PaymentResult refund(String transactionId, BigDecimal amount);
}

public class StripeAdapter implements PaymentGateway {
    private final StripeClient stripeClient;
    
    public StripeAdapter(StripeClient stripeClient) {
        this.stripeClient = stripeClient;
    }
    
    @Override
    public PaymentResult charge(String customerId, BigDecimal amount) {
        StripeCharge charge = stripeClient.createCharge(customerId, amount.intValue() * 100);
        return new PaymentResult(charge.getId(), charge.getStatus().equals("succeeded"));
    }
    
    @Override
    public PaymentResult refund(String transactionId, BigDecimal amount) {
        StripeRefund refund = stripeClient.createRefund(transactionId, amount.intValue() * 100);
        return new PaymentResult(refund.getId(), refund.getStatus().equals("succeeded"));
    }
}"""
    },
    {
        "id": 50,
        "expected": "Clean",
        "description": "Decorator pattern for caching",
        "code": """
public interface UserRepository {
    User findById(Long id);
    void save(User user);
}

public class CachingUserRepository implements UserRepository {
    private final UserRepository delegate;
    private final Cache<Long, User> cache;
    
    public CachingUserRepository(UserRepository delegate, Cache<Long, User> cache) {
        this.delegate = delegate;
        this.cache = cache;
    }
    
    @Override
    public User findById(Long id) {
        User cached = cache.get(id);
        if (cached != null) {
            return cached;
        }
        User user = delegate.findById(id);
        if (user != null) {
            cache.put(id, user);
        }
        return user;
    }
    
    @Override
    public void save(User user) {
        delegate.save(user);
        cache.put(user.getId(), user);
    }
}"""
    },
]

def run_tests():
    """Run all 50 test cases and report results."""
    print("\n" + "=" * 80)
    print("   🧪 RUNNING 50 NEW TEST CASES")
    print("=" * 80 + "\n")
    
    # Load models
    print("📂 Loading models...")
    try:
        models = ps.load_models()
        print("   ✅ Models loaded successfully!\n")
    except Exception as e:
        print(f"   ❌ Failed to load models: {e}")
        return
    
    results = {"correct": 0, "wrong": 0, "details": []}
    category_stats = {}
    incorrect = []
    
    print(f"{'#':>3} | {'Expected':^12} | {'Predicted':^12} | {'Conf':>5} | {'Result':^7} | Description")
    print("-" * 80)
    
    for sample in TEST_SAMPLES:
        expected = sample["expected"]
        code = sample["code"]
        desc = sample["description"][:30]
        
        # Get prediction
        try:
            result = ps.predict_smell_compat(code, models)
            predicted = result["prediction"]
            confidence = result["confidence"]
        except Exception as e:
            predicted = "ERROR"
            confidence = 0
        
        # Check if correct
        is_correct = predicted == expected
        status = "✓" if is_correct else "✗"
        
        if is_correct:
            results["correct"] += 1
        else:
            results["wrong"] += 1
            incorrect.append({
                "id": sample["id"],
                "expected": expected,
                "predicted": predicted,
                "confidence": confidence,
                "description": sample["description"]
            })
        
        # Track category stats
        if expected not in category_stats:
            category_stats[expected] = {"correct": 0, "total": 0}
        category_stats[expected]["total"] += 1
        if is_correct:
            category_stats[expected]["correct"] += 1
        
        print(f"{sample['id']:>3} | {expected:^12} | {predicted:^12} | {confidence:>4.0f}% | {status:^7} | {desc}")
    
    print("-" * 80)
    
    # Print summary
    total = len(TEST_SAMPLES)
    accuracy = (results["correct"] / total) * 100
    
    print("\n" + "=" * 80)
    print("   📊 TEST RESULTS SUMMARY")
    print("=" * 80)
    print(f"\n   Total Tests:    {total}")
    print(f"   ✓ Correct:      {results['correct']}")
    print(f"   ✗ Wrong:        {results['wrong']}")
    print(f"   📈 Accuracy:     {accuracy:.1f}%")
    
    print("\n   Category Breakdown:")
    print("   " + "-" * 50)
    for cat in ["GodClass", "DataClass", "LongMethod", "FeatureEnvy", "DeadCode", "Clean"]:
        if cat in category_stats:
            stats = category_stats[cat]
            cat_accuracy = (stats["correct"] / stats["total"]) * 100 if stats["total"] > 0 else 0
            print(f"   {cat:15} | {stats['correct']}/{stats['total']} correct | {cat_accuracy:5.1f}%")
    print("   " + "-" * 50)
    
    if incorrect:
        print(f"\n   ✗ INCORRECT PREDICTIONS ({len(incorrect)}):")
        print("   " + "-" * 70)
        for item in incorrect:
            print(f"   #{item['id']:>2}: Expected {item['expected']:12} → Got {item['predicted']:12} ({item['confidence']:.0f}%)")
            print(f"         {item['description']}")
        print("   " + "-" * 70)
    
    print("\n" + "=" * 80 + "\n")
    
    return results

if __name__ == "__main__":
    run_tests()
