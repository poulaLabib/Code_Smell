"""
100 Java Code Samples to Test Extended Smell Detection Features
Each sample is designed to trigger specific smell types.
"""

EXTENDED_TEST_SAMPLES = [
    # ═══════════════════════════════════════════════════════════════════════════
    # MAGIC NUMBERS (Samples 1-10)
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": 1,
        "name": "MagicNumbersInCondition",
        "expected_smells": ["MagicNumbers"],
        "code": """
public class PriceCalculator {
    public double calculateDiscount(double price) {
        if (price > 999) {
            return price * 0.15;
        } else if (price > 499) {
            return price * 0.10;
        }
        return price * 0.05;
    }
}
"""
    },
    {
        "id": 2,
        "name": "MagicNumbersInLoop",
        "expected_smells": ["MagicNumbers"],
        "code": """
public class DataProcessor {
    public void process() {
        for (int i = 0; i < 42; i++) {
            System.out.println("Processing item " + i);
        }
        int timeout = 30000;
        int retries = 5;
    }
}
"""
    },
    {
        "id": 3,
        "name": "MagicNumbersInArray",
        "expected_smells": ["MagicNumbers"],
        "code": """
public class ArrayHandler {
    public void initBuffer() {
        byte[] buffer = new byte[8192];
        int[] sizes = {64, 128, 256, 512};
        double ratio = 3.14159;
    }
}
"""
    },
    {
        "id": 4,
        "name": "MagicNumbersInCalc",
        "expected_smells": ["MagicNumbers"],
        "code": """
public class TaxCalculator {
    public double calculate(double income) {
        if (income > 50000) {
            return income * 0.35 + 4500;
        }
        return income * 0.22 + 1200;
    }
}
"""
    },
    {
        "id": 5,
        "name": "MagicNumbersTimeout",
        "expected_smells": ["MagicNumbers"],
        "code": """
public class ConnectionManager {
    public void connect() {
        int timeout = 30000;
        int maxRetries = 7;
        int bufferSize = 16384;
        sleep(2500);
    }
}
"""
    },
    {
        "id": 6,
        "name": "MagicNumbersConfig",
        "expected_smells": ["MagicNumbers"],
        "code": """
public class ServerConfig {
    public void setup() {
        int port = 8080;
        int maxConnections = 250;
        int threadPoolSize = 32;
        long cacheExpiry = 86400;
    }
}
"""
    },
    {
        "id": 7,
        "name": "MagicNumbersConversion",
        "expected_smells": ["MagicNumbers"],
        "code": """
public class UnitConverter {
    public double milesToKm(double miles) {
        return miles * 1.60934;
    }
    public double celsiusToFahrenheit(double c) {
        return c * 1.8 + 32;
    }
}
"""
    },
    {
        "id": 8,
        "name": "MagicNumbersValidation",
        "expected_smells": ["MagicNumbers"],
        "code": """
public class InputValidator {
    public boolean validate(String s) {
        if (s.length() < 8 || s.length() > 256) {
            return false;
        }
        return s.matches("[a-z]{3,16}");
    }
}
"""
    },
    {
        "id": 9,
        "name": "MagicNumbersPagination",
        "expected_smells": ["MagicNumbers"],
        "code": """
public class Paginator {
    public int getMaxPage(int total) {
        return (total + 49) / 50;
    }
    public int getOffset(int page) {
        return (page - 1) * 50;
    }
}
"""
    },
    {
        "id": 10,
        "name": "MagicNumbersRateLimit",
        "expected_smells": ["MagicNumbers"],
        "code": """
public class RateLimiter {
    public boolean allow(long requests) {
        if (requests > 1000) return false;
        if (requests > 500) throttle(100);
        return true;
    }
}
"""
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # GLOBAL MUTABLE STATE (Samples 11-20)
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": 11,
        "name": "GlobalMutableCounter",
        "expected_smells": ["GlobalMutableState"],
        "code": """
public class Counter {
    public static int count = 0;
    public static String lastOperation = "";
    
    public void increment() {
        count++;
        lastOperation = "increment";
    }
}
"""
    },
    {
        "id": 12,
        "name": "GlobalMutableConfig",
        "expected_smells": ["GlobalMutableState"],
        "code": """
public class AppConfig {
    public static String dbHost = "localhost";
    public static int dbPort = 5432;
    public static String apiKey = "";
    
    public void update(String host) {
        dbHost = host;
    }
}
"""
    },
    {
        "id": 13,
        "name": "GlobalMutableCache",
        "expected_smells": ["GlobalMutableState", "RawCollections"],
        "code": """
public class Cache {
    public static Map cache = new HashMap();
    public static List keys = new ArrayList();
    
    public void put(String k, Object v) {
        cache.put(k, v);
        keys.add(k);
    }
}
"""
    },
    {
        "id": 14,
        "name": "GlobalMutableUser",
        "expected_smells": ["GlobalMutableState"],
        "code": """
public class Session {
    public static String currentUser = null;
    public static boolean isLoggedIn = false;
    public static long sessionStart = 0;
    
    public void login(String user) {
        currentUser = user;
        isLoggedIn = true;
    }
}
"""
    },
    {
        "id": 15,
        "name": "GlobalMutableSettings",
        "expected_smells": ["GlobalMutableState"],
        "code": """
public class Settings {
    public static int volume = 50;
    public static String theme = "dark";
    public static boolean notifications = true;
    
    public void reset() {
        volume = 50;
        theme = "dark";
    }
}
"""
    },
    {
        "id": 16,
        "name": "GlobalMutableLogger",
        "expected_smells": ["GlobalMutableState"],
        "code": """
public class LogConfig {
    public static String logLevel = "INFO";
    public static String logPath = "/var/log";
    public static int maxSize = 10;
    
    public void setDebug() {
        logLevel = "DEBUG";
    }
}
"""
    },
    {
        "id": 17,
        "name": "GlobalMutableConnection",
        "expected_smells": ["GlobalMutableState"],
        "code": """
public class DbConnection {
    public static Connection conn = null;
    public static boolean connected = false;
    public static int queryCount = 0;
    
    public void connect() {
        connected = true;
        queryCount = 0;
    }
}
"""
    },
    {
        "id": 18,
        "name": "GlobalMutableMetrics",
        "expected_smells": ["GlobalMutableState"],
        "code": """
public class Metrics {
    public static long requestCount = 0;
    public static double avgLatency = 0.0;
    public static String lastError = "";
    
    public void record(long latency) {
        requestCount++;
        avgLatency = (avgLatency + latency) / 2;
    }
}
"""
    },
    {
        "id": 19,
        "name": "GlobalMutableQueue",
        "expected_smells": ["GlobalMutableState", "RawCollections"],
        "code": """
public class TaskQueue {
    public static List tasks = new ArrayList();
    public static int processed = 0;
    
    public void add(Object task) {
        tasks.add(task);
    }
    public void process() {
        processed++;
    }
}
"""
    },
    {
        "id": 20,
        "name": "GlobalMutableFlags",
        "expected_smells": ["GlobalMutableState"],
        "code": """
public class FeatureFlags {
    public static boolean enableNewUI = false;
    public static boolean betaFeatures = false;
    public static String experimentGroup = "control";
    
    public void enableBeta() {
        betaFeatures = true;
        experimentGroup = "beta";
    }
}
"""
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # RAW COLLECTIONS (Samples 21-30)
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": 21,
        "name": "RawList",
        "expected_smells": ["RawCollections"],
        "code": """
public class DataStore {
    private List items = new ArrayList();
    
    public void add(Object item) {
        items.add(item);
    }
    public Object get(int i) {
        return items.get(i);
    }
}
"""
    },
    {
        "id": 22,
        "name": "RawMap",
        "expected_smells": ["RawCollections"],
        "code": """
public class Registry {
    private Map registry = new HashMap();
    
    public void register(Object key, Object value) {
        registry.put(key, value);
    }
    public Object lookup(Object key) {
        return registry.get(key);
    }
}
"""
    },
    {
        "id": 23,
        "name": "RawSet",
        "expected_smells": ["RawCollections"],
        "code": """
public class UniqueItems {
    private Set unique = new HashSet();
    
    public boolean add(Object item) {
        return unique.add(item);
    }
    public boolean contains(Object item) {
        return unique.contains(item);
    }
}
"""
    },
    {
        "id": 24,
        "name": "RawQueue",
        "expected_smells": ["RawCollections"],
        "code": """
public class JobQueue {
    private Queue jobs = new LinkedList();
    
    public void submit(Object job) {
        jobs.offer(job);
    }
    public Object next() {
        return jobs.poll();
    }
}
"""
    },
    {
        "id": 25,
        "name": "RawLinkedList",
        "expected_smells": ["RawCollections"],
        "code": """
public class History {
    private LinkedList history = new LinkedList();
    
    public void push(Object item) {
        history.addFirst(item);
    }
    public Object pop() {
        return history.removeFirst();
    }
}
"""
    },
    {
        "id": 26,
        "name": "RawTreeMap",
        "expected_smells": ["RawCollections"],
        "code": """
public class SortedRegistry {
    private TreeMap sorted = new TreeMap();
    
    public void put(Object k, Object v) {
        sorted.put(k, v);
    }
    public Object first() {
        return sorted.firstEntry();
    }
}
"""
    },
    {
        "id": 27,
        "name": "RawArrayList",
        "expected_smells": ["RawCollections"],
        "code": """
public class Buffer {
    private ArrayList buffer = new ArrayList();
    private Vector backup = new Vector();
    
    public void write(Object data) {
        buffer.add(data);
        backup.add(data);
    }
}
"""
    },
    {
        "id": 28,
        "name": "RawTreeSet",
        "expected_smells": ["RawCollections"],
        "code": """
public class SortedUnique {
    private TreeSet items = new TreeSet();
    
    public void add(Object item) {
        items.add(item);
    }
    public Object first() {
        return items.first();
    }
}
"""
    },
    {
        "id": 29,
        "name": "RawStack",
        "expected_smells": ["RawCollections"],
        "code": """
public class CallStack {
    private Stack stack = new Stack();
    
    public void push(Object frame) {
        stack.push(frame);
    }
    public Object pop() {
        return stack.pop();
    }
}
"""
    },
    {
        "id": 30,
        "name": "RawMultipleCollections",
        "expected_smells": ["RawCollections"],
        "code": """
public class MultiStore {
    private List list = new ArrayList();
    private Map map = new HashMap();
    private Set set = new HashSet();
    
    public void store(Object item) {
        list.add(item);
        set.add(item);
    }
}
"""
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # SWALLOWED EXCEPTIONS (Samples 31-40)
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": 31,
        "name": "SwallowedIOException",
        "expected_smells": ["SwallowedException"],
        "code": """
public class FileReader {
    public String read(String path) {
        try {
            return new String(Files.readAllBytes(Paths.get(path)));
        } catch (IOException e) {
            // ignore
        }
        return null;
    }
}
"""
    },
    {
        "id": 32,
        "name": "SwallowedSQLException",
        "expected_smells": ["SwallowedException"],
        "code": """
public class DbQuery {
    public void execute(String sql) {
        try {
            connection.executeQuery(sql);
        } catch (SQLException e) {
            // TODO: handle later
        }
    }
}
"""
    },
    {
        "id": 33,
        "name": "SwallowedParseException",
        "expected_smells": ["SwallowedException"],
        "code": """
public class DateParser {
    public Date parse(String s) {
        try {
            return new SimpleDateFormat("yyyy-MM-dd").parse(s);
        } catch (ParseException e) {
        }
        return null;
    }
}
"""
    },
    {
        "id": 34,
        "name": "SwallowedNumberFormat",
        "expected_smells": ["SwallowedException"],
        "code": """
public class NumberParser {
    public int parse(String s) {
        try {
            return Integer.parseInt(s);
        } catch (NumberFormatException e) {
            // silent fail
        }
        return 0;
    }
}
"""
    },
    {
        "id": 35,
        "name": "SwallowedConnection",
        "expected_smells": ["SwallowedException"],
        "code": """
public class NetworkClient {
    public void connect(String host) {
        try {
            socket = new Socket(host, 80);
        } catch (Exception e) {
            // network error
        }
    }
}
"""
    },
    {
        "id": 36,
        "name": "SwallowedReflection",
        "expected_smells": ["SwallowedException"],
        "code": """
public class Reflector {
    public Object create(String className) {
        try {
            return Class.forName(className).newInstance();
        } catch (Exception e) {
            // class not found
        }
        return null;
    }
}
"""
    },
    {
        "id": 37,
        "name": "SwallowedFile",
        "expected_smells": ["SwallowedException"],
        "code": """
public class FileWriter {
    public void write(String path, String content) {
        try {
            Files.write(Paths.get(path), content.getBytes());
        } catch (IOException e) {
            // write failed
        }
    }
}
"""
    },
    {
        "id": 38,
        "name": "SwallowedJSON",
        "expected_smells": ["SwallowedException"],
        "code": """
public class JsonParser {
    public Object parse(String json) {
        try {
            return new JSONObject(json);
        } catch (JSONException e) {
            // invalid json
        }
        return null;
    }
}
"""
    },
    {
        "id": 39,
        "name": "SwallowedThread",
        "expected_smells": ["SwallowedException"],
        "code": """
public class Sleeper {
    public void sleep(long ms) {
        try {
            Thread.sleep(ms);
        } catch (InterruptedException e) {
            // interrupted
        }
    }
}
"""
    },
    {
        "id": 40,
        "name": "SwallowedMultiple",
        "expected_smells": ["SwallowedException"],
        "code": """
public class MultiCatch {
    public void process() {
        try {
            riskyOperation1();
        } catch (Exception e) {
        }
        try {
            riskyOperation2();
        } catch (Exception e) {
            // oops
        }
    }
}
"""
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # DEAD CODE (Samples 41-50)
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": 41,
        "name": "DeadCodeIfFalse",
        "expected_smells": ["DeadCode"],
        "code": """
public class DeadBranch {
    public void process() {
        if (false) {
            System.out.println("This never runs");
        }
        doWork();
    }
}
"""
    },
    {
        "id": 42,
        "name": "DeadCodeIfTrue",
        "expected_smells": ["DeadCode"],
        "code": """
public class AlwaysTrue {
    public void process() {
        if (true) {
            doWork();
        }
        // The else branch could never run
    }
}
"""
    },
    {
        "id": 43,
        "name": "DeadCodeWhileFalse",
        "expected_smells": ["DeadCode"],
        "code": """
public class NeverLoop {
    public void process() {
        while (false) {
            System.out.println("Never executes");
        }
        doWork();
    }
}
"""
    },
    {
        "id": 44,
        "name": "DeadCodeAfterReturn",
        "expected_smells": ["DeadCode"],
        "code": """
public class UnreachableCode {
    public int getValue() {
        return 42;
        System.out.println("Unreachable");
        int x = 10;
    }
}
"""
    },
    {
        "id": 45,
        "name": "DeadCodeDebugFlag",
        "expected_smells": ["DeadCode"],
        "code": """
public class DebugCode {
    private static final boolean DEBUG = false;
    public void process() {
        if (false) {
            debugLog("Processing started");
        }
    }
}
"""
    },
    {
        "id": 46,
        "name": "DeadCodeCommentedLogic",
        "expected_smells": ["DeadCode"],
        "code": """
public class OldCode {
    public void process() {
        if (false) {
            oldImplementation();
            legacyMethod();
        }
        newImplementation();
    }
}
"""
    },
    {
        "id": 47,
        "name": "DeadCodeTestSkip",
        "expected_smells": ["DeadCode"],
        "code": """
public class TestSkipper {
    public void runTests() {
        if (false) {
            runSlowTests();
        }
        runFastTests();
    }
}
"""
    },
    {
        "id": 48,
        "name": "DeadCodeFeatureToggle",
        "expected_smells": ["DeadCode"],
        "code": """
public class FeatureToggle {
    public void showUI() {
        if (false) {
            showNewUI();
        } else {
            showOldUI();
        }
    }
}
"""
    },
    {
        "id": 49,
        "name": "DeadCodeUnusedCondition",
        "expected_smells": ["DeadCode"],
        "code": """
public class UnusedPath {
    public void route(int code) {
        if (false) {
            handleError();
            logError();
            cleanup();
        }
    }
}
"""
    },
    {
        "id": 50,
        "name": "DeadCodeMultiple",
        "expected_smells": ["DeadCode"],
        "code": """
public class MultiDead {
    public void process() {
        if (false) {
            step1();
        }
        doWork();
        if (false) {
            step2();
        }
    }
}
"""
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # DUPLICATE CODE (Samples 51-60)
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": 51,
        "name": "DuplicateMethodCalls",
        "expected_smells": ["DuplicateCode"],
        "code": """
public class Repeater {
    public void process() {
        validate();
        validate();
        validate();
        doWork();
    }
}
"""
    },
    {
        "id": 52,
        "name": "DuplicatePrintStatements",
        "expected_smells": ["DuplicateCode"],
        "code": """
public class Logger {
    public void log() {
        System.out.println("Starting");
        System.out.println("Starting");
        System.out.println("Starting");
        process();
    }
}
"""
    },
    {
        "id": 53,
        "name": "DuplicateAssignments",
        "expected_smells": ["DuplicateCode"],
        "code": """
public class Initializer {
    public void init() {
        x = 0;
        x = 0;
        x = 0;
        startProcess();
    }
}
"""
    },
    {
        "id": 54,
        "name": "DuplicateAddCalls",
        "expected_smells": ["DuplicateCode"],
        "code": """
public class ListBuilder {
    public List build() {
        List<String> list = new ArrayList<>();
        list.add("item");
        list.add("item");
        list.add("item");
        return list;
    }
}
"""
    },
    {
        "id": 55,
        "name": "DuplicateIncrement",
        "expected_smells": ["DuplicateCode"],
        "code": """
public class Counter {
    public void count() {
        counter++;
        counter++;
        counter++;
        counter++;
        save();
    }
}
"""
    },
    {
        "id": 56,
        "name": "DuplicateServiceCalls",
        "expected_smells": ["DuplicateCode"],
        "code": """
public class ServiceCaller {
    public void notify() {
        service.notify();
        service.notify();
        service.notify();
    }
}
"""
    },
    {
        "id": 57,
        "name": "DuplicateSetCalls",
        "expected_smells": ["DuplicateCode"],
        "code": """
public class Setter {
    public void configure() {
        config.set("key", "value");
        config.set("key", "value");
        config.set("key", "value");
    }
}
"""
    },
    {
        "id": 58,
        "name": "DuplicateAppend",
        "expected_smells": ["DuplicateCode"],
        "code": """
public class Builder {
    public String build() {
        sb.append("data");
        sb.append("data");
        sb.append("data");
        return sb.toString();
    }
}
"""
    },
    {
        "id": 59,
        "name": "DuplicateRemove",
        "expected_smells": ["DuplicateCode"],
        "code": """
public class Cleaner {
    public void clean() {
        cache.remove("key");
        cache.remove("key");
        cache.remove("key");
    }
}
"""
    },
    {
        "id": 60,
        "name": "DuplicateSave",
        "expected_smells": ["DuplicateCode"],
        "code": """
public class Saver {
    public void persist() {
        repository.save(entity);
        repository.save(entity);
        repository.save(entity);
    }
}
"""
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # POINTLESS LOOPS (Samples 61-70)
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": 61,
        "name": "PointlessIncrementDecrement",
        "expected_smells": ["PointlessLoop"],
        "code": """
public class PointlessCounter {
    public void count() {
        for (int i = 0; i < 100; i++) {
            x = x + 1;
            x = x - 1;
        }
    }
}
"""
    },
    {
        "id": 62,
        "name": "PointlessAddSubtract",
        "expected_smells": ["PointlessLoop"],
        "code": """
public class UselessMath {
    public void calculate() {
        while (condition) {
            value += 10;
            value -= 10;
        }
    }
}
"""
    },
    {
        "id": 63,
        "name": "PointlessMultiplyDivide",
        "expected_smells": ["PointlessLoop"],
        "code": """
public class NullOperation {
    public void process() {
        for (int i = 0; i < n; i++) {
            x *= 2;
            x /= 2;
        }
    }
}
"""
    },
    {
        "id": 64,
        "name": "PointlessPlusMinus",
        "expected_smells": ["PointlessLoop"],
        "code": """
public class Oscillator {
    public void oscillate() {
        for (int i = 0; i < 50; i++) {
            counter = counter + 5;
            counter = counter - 5;
        }
    }
}
"""
    },
    {
        "id": 65,
        "name": "PointlessToggle",
        "expected_smells": ["PointlessLoop"],
        "code": """
public class Toggler {
    public void toggle() {
        for (int i = 0; i < 10; i++) {
            value = value + 1;
            value = value - 1;
            // Nothing changes
        }
    }
}
"""
    },
    {
        "id": 66,
        "name": "PointlessWhileLoop",
        "expected_smells": ["PointlessLoop"],
        "code": """
public class WhilePointless {
    public void run() {
        while (running) {
            offset = offset + 1;
            offset = offset - 1;
        }
    }
}
"""
    },
    {
        "id": 67,
        "name": "PointlessPositiveNegative",
        "expected_smells": ["PointlessLoop"],
        "code": """
public class SignChanger {
    public void flip() {
        for (int j = 0; j < count; j++) {
            num = num + 100;
            num = num - 100;
        }
    }
}
"""
    },
    {
        "id": 68,
        "name": "PointlessBalance",
        "expected_smells": ["PointlessLoop"],
        "code": """
public class Balancer {
    public void balance() {
        for (int k = 0; k < iterations; k++) {
            balance += amount;
            balance -= amount;
        }
    }
}
"""
    },
    {
        "id": 69,
        "name": "PointlessAccumulator",
        "expected_smells": ["PointlessLoop"],
        "code": """
public class Accumulator {
    public void accumulate() {
        for (int i = 0; i < 1000; i++) {
            sum = sum + delta;
            sum = sum - delta;
        }
    }
}
"""
    },
    {
        "id": 70,
        "name": "PointlessBidirectional",
        "expected_smells": ["PointlessLoop"],
        "code": """
public class Bidirectional {
    public void move() {
        while (active) {
            position = position + step;
            position = position - step;
            // Goes nowhere
        }
    }
}
"""
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # UNNECESSARY BOXING (Samples 71-80)
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": 71,
        "name": "UnnecessaryIntegerBoxing",
        "expected_smells": ["UnnecessaryBoxing"],
        "code": """
public class IntBoxer {
    public Integer box(int value) {
        return new Integer(value);
    }
}
"""
    },
    {
        "id": 72,
        "name": "UnnecessaryLongBoxing",
        "expected_smells": ["UnnecessaryBoxing"],
        "code": """
public class LongBoxer {
    public Long box(long value) {
        return new Long(value);
    }
}
"""
    },
    {
        "id": 73,
        "name": "UnnecessaryDoubleBoxing",
        "expected_smells": ["UnnecessaryBoxing"],
        "code": """
public class DoubleBoxer {
    public Double box(double value) {
        return new Double(value);
    }
}
"""
    },
    {
        "id": 74,
        "name": "UnnecessaryFloatBoxing",
        "expected_smells": ["UnnecessaryBoxing"],
        "code": """
public class FloatBoxer {
    public Float box(float value) {
        return new Float(value);
    }
}
"""
    },
    {
        "id": 75,
        "name": "UnnecessaryBooleanBoxing",
        "expected_smells": ["UnnecessaryBoxing"],
        "code": """
public class BoolBoxer {
    public Boolean box(boolean value) {
        return new Boolean(value);
    }
}
"""
    },
    {
        "id": 76,
        "name": "UnnecessaryCharBoxing",
        "expected_smells": ["UnnecessaryBoxing"],
        "code": """
public class CharBoxer {
    public Character box(char value) {
        return new Character(value);
    }
}
"""
    },
    {
        "id": 77,
        "name": "UnnecessaryShortBoxing",
        "expected_smells": ["UnnecessaryBoxing"],
        "code": """
public class ShortBoxer {
    public Short box(short value) {
        return new Short(value);
    }
}
"""
    },
    {
        "id": 78,
        "name": "UnnecessaryByteBoxing",
        "expected_smells": ["UnnecessaryBoxing"],
        "code": """
public class ByteBoxer {
    public Byte box(byte value) {
        return new Byte(value);
    }
}
"""
    },
    {
        "id": 79,
        "name": "UnnecessaryMultipleBoxing",
        "expected_smells": ["UnnecessaryBoxing"],
        "code": """
public class MultiBoxer {
    public void box() {
        Integer i = new Integer(10);
        Long l = new Long(20L);
        Double d = new Double(3.14);
    }
}
"""
    },
    {
        "id": 80,
        "name": "UnnecessaryBoxingInCollection",
        "expected_smells": ["UnnecessaryBoxing"],
        "code": """
public class CollectionBoxer {
    public void addToList(List<Integer> list, int value) {
        list.add(new Integer(value));
    }
}
"""
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # BAD NAMING (Samples 81-90)
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": 81,
        "name": "BadNamingSingleLetter",
        "expected_smells": ["BadNaming"],
        "code": """
public class X {
    private int a;
    private String b;
    public void c() {
        int d = 0;
        String e = "";
    }
}
"""
    },
    {
        "id": 82,
        "name": "BadNamingDoClass",
        "expected_smells": ["BadNaming"],
        "code": """
public class DoThings {
    public void doIt() {
        process();
    }
    public void doStuff() {
        handle();
    }
}
"""
    },
    {
        "id": 83,
        "name": "BadNamingGenericClass",
        "expected_smells": ["BadNaming"],
        "code": """
public class MyClass {
    public void myMethod() {
        int myVar = 0;
    }
}
"""
    },
    {
        "id": 84,
        "name": "BadNamingDataClass",
        "expected_smells": ["BadNaming"],
        "code": """
public class Data {
    public void process() {
        Object data = getData();
    }
}
"""
    },
    {
        "id": 85,
        "name": "BadNamingInfoClass",
        "expected_smells": ["BadNaming"],
        "code": """
public class Info {
    public void getInfo() {
        Object info = null;
    }
}
"""
    },
    {
        "id": 86,
        "name": "BadNamingMixedStyle",
        "expected_smells": ["BadNaming"],
        "code": """
public class Process {
    private int x;
    private int y;
    private int z;
    public void f() { x++; }
    public void g() { y++; }
}
"""
    },
    {
        "id": 87,
        "name": "BadNamingAbbreviations",
        "expected_smells": ["BadNaming"],
        "code": """
public class Mgr {
    public void proc() {
        int cnt = 0;
        String val = "";
    }
}
"""
    },
    {
        "id": 88,
        "name": "BadNamingTemp",
        "expected_smells": ["BadNaming"],
        "code": """
public class Handler {
    public void handle() {
        int tmp = 0;
        String temp = "";
        Object o = null;
    }
}
"""
    },
    {
        "id": 89,
        "name": "BadNamingLoopVars",
        "expected_smells": ["BadNaming"],
        "code": """
public class LoopHandler {
    public void process() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int k = 0; k < p; k++) {
                    data[i][j][k] = 0;
                }
            }
        }
    }
}
"""
    },
    {
        "id": 90,
        "name": "BadNamingResults",
        "expected_smells": ["BadNaming"],
        "code": """
public class Result {
    public Object get() {
        Object result = fetch();
        Object res = process(result);
        return res;
    }
}
"""
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # GOD METHOD (Samples 91-95)
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": 91,
        "name": "GodMethodDoesEverything",
        "expected_smells": ["GodMethod", "SwallowedException"],
        "code": """
public class GodProcessor {
    public void processEverything(String input) {
        System.out.println("Starting");
        File f = new File(input);
        try {
            Scanner s = new Scanner(f);
            while (s.hasNext()) {
                String line = s.nextLine();
                if (line.length() > 0) {
                    if (line.startsWith("#")) {
                        continue;
                    }
                }
            }
            for (int i = 0; i < 10; i++) {
                System.out.println(i);
            }
            Connection conn = getConnection();
            conn.execute("INSERT INTO log VALUES (?)");
        } catch (Exception e) {
        }
        System.out.println("Done");
    }
}
"""
    },
    {
        "id": 92,
        "name": "GodMethodMixedConcerns",
        "expected_smells": ["GodMethod", "SwallowedException"],
        "code": """
public class OrderProcessor {
    public void processOrder(Order order) {
        System.out.println("Processing order");
        File logFile = new File("orders.log");
        try {
            Writer w = new FileWriter(logFile);
            w.write(order.toString());
            w.close();
            if (order.getTotal() > 100) {
                if (order.isPremium()) {
                    applyDiscount();
                }
            }
            for (Item item : order.getItems()) {
                updateInventory(item);
            }
        } catch (Exception e) {
        }
        System.out.println("Order complete");
    }
}
"""
    },
    {
        "id": 93,
        "name": "GodMethodFullStack",
        "expected_smells": ["GodMethod", "SwallowedException"],
        "code": """
public class FullStackHandler {
    public String handleRequest(String request) {
        System.out.println("Handling: " + request);
        try {
            File config = new File("config.properties");
            Scanner scanner = new Scanner(config);
            String prop = scanner.nextLine();
            Connection conn = DriverManager.getConnection(prop);
            PreparedStatement ps = conn.prepareStatement("SELECT * FROM users");
            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                if (rs.getString(1).equals(request)) {
                    System.out.println("Found user");
                }
            }
            for (int i = 0; i < 5; i++) {
                System.out.println("Retry " + i);
            }
        } catch (Exception e) {
        }
        System.out.println("Done");
        return "OK";
    }
}
"""
    },
    {
        "id": 94,
        "name": "GodMethodReportGenerator",
        "expected_smells": ["GodMethod", "SwallowedException"],
        "code": """
public class ReportGenerator {
    public void generateReport(String type) {
        System.out.println("Generating " + type + " report");
        File output = new File("report.csv");
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(output));
            if (type.equals("sales")) {
                for (int i = 0; i < 100; i++) {
                    writer.write("sale," + i);
                }
            }
            if (type.equals("inventory")) {
                if (checkStock()) {
                    if (needsReorder()) {
                        writer.write("REORDER");
                    }
                }
            }
            writer.close();
        } catch (IOException e) {
        }
        System.out.println("Report complete");
    }
}
"""
    },
    {
        "id": 95,
        "name": "GodMethodDataSync",
        "expected_smells": ["GodMethod"],
        "code": """
public class DataSynchronizer {
    public void syncAll() {
        System.out.println("Starting sync");
        File source = new File("source.dat");
        Scanner reader = new Scanner(source);
        while (reader.hasNextLine()) {
            String line = reader.nextLine();
            if (line.isEmpty()) continue;
            if (line.startsWith("//")) continue;
        }
        for (int i = 0; i < retries; i++) {
            if (tryConnect()) break;
        }
        System.out.println("Sync complete");
        System.err.println("Check logs for details");
    }
}
"""
    },

    # ═══════════════════════════════════════════════════════════════════════════
    # COMBINED / COMPLEX (Samples 96-100)
    # ═══════════════════════════════════════════════════════════════════════════
    {
        "id": 96,
        "name": "CombinedMultipleSmells",
        "expected_smells": ["MagicNumbers", "RawCollections", "SwallowedException"],
        "code": """
public class MultiSmell {
    private List items = new ArrayList();
    
    public void process() {
        for (int i = 0; i < 1000; i++) {
            items.add(i * 42);
        }
        try {
            save();
        } catch (Exception e) {
        }
    }
}
"""
    },
    {
        "id": 97,
        "name": "CombinedBadPractices",
        "expected_smells": ["GlobalMutableState", "BadNaming", "MagicNumbers"],
        "code": """
public class X {
    public static int x = 0;
    public static String s = "";
    
    public void f() {
        x = 42;
        s = "data";
        int n = 12345;
    }
}
"""
    },
    {
        "id": 98,
        "name": "CombinedDeadAndDuplicate",
        "expected_smells": ["DeadCode", "DuplicateCode"],
        "code": """
public class DeadDuplicate {
    public void process() {
        doWork();
        doWork();
        doWork();
        if (false) {
            cleanup();
        }
    }
}
"""
    },
    {
        "id": 99,
        "name": "CombinedLoopIssues",
        "expected_smells": ["PointlessLoop", "MagicNumbers"],
        "code": """
public class LoopIssues {
    public void run() {
        for (int i = 0; i < 999; i++) {
            value = value + 50;
            value = value - 50;
        }
        timeout = 30000;
    }
}
"""
    },
    {
        "id": 100,
        "name": "CombinedAllIssues",
        "expected_smells": ["GlobalMutableState", "RawCollections", "MagicNumbers", "SwallowedException", "DeadCode", "BadNaming", "DuplicateCode"],
        "code": """
public class DoAllBad {
    public static int x = 0;
    public static List data = new ArrayList();
    
    public void f() {
        x = 42;
        x = 42;
        x = 42;
        try {
            process();
        } catch (Exception e) {
        }
        if (false) {
            cleanup();
        }
    }
}
"""
    },
]
