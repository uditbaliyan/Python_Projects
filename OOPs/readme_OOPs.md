# 🧠 Python OOP Challenge Set – Refined Mastery Edition (50 Pure-Python Problems)

This curated collection of **50 high-difficulty exercises** is designed to master Python’s Object-Oriented Programming (OOP) principles using only the **Python standard library**. Each problem focuses on designing complex, self-contained classes to solve real-world scenarios, emphasizing encapsulation, inheritance, polymorphism, abstraction, and composition. With no external dependencies, this set ensures minimal setup and maximum focus on crafting robust, efficient, and maintainable OOP solutions.

---

## ✅ 1. Classes & Objects (Core Concepts)

**Level: Medium → Hard** – Master object creation, state management, and method design.

1. **PointND Geometric Operations**  
   - **Description**: Model an N-dimensional point with coordinates in a list.  
   - **Requirements**:  
     - Compute Euclidean, Manhattan, and Minkowski distances to another point.  
     - Support vector operations (addition, subtraction, scalar multiplication, dot product).  
     - Implement `__eq__` with configurable floating-point tolerance.  
     - Serialize to JSON using `json` module.  
   - **Constraints**: Validate dimension consistency; handle edge cases (e.g., zero vectors).

2. **Library Catalog System**  
   - **Description**: Manage a library with books and borrowing logic.  
   - **Requirements**:  
     - `Book` class with title, author, ISBN, year, and availability.  
     - `Library` class with case-insensitive search (using `re` for regex), borrow/return with due dates, and fine calculation.  
     - Export catalog to CSV using `csv` module.  
   - **Constraints**: Ensure unique ISBNs; handle invalid inputs.

3. **Student Academic Manager**  
   - **Description**: Track student records and academic performance.  
   - **Requirements**:  
     - Store name, ID, and courses (dict of grades, credits, semesters).  
     - Compute weighted GPA; validate grades (0–100).  
     - Generate transcripts as formatted strings.  
   - **Constraints**: Handle missing grades; enforce prerequisite rules.

4. **Polygon Geometry Engine**  
   - **Description**: Represent 2D polygons with `Point2D` vertices.  
   - **Requirements**:  
     - Compute area (shoelace formula), perimeter, and centroid.  
     - Test if a point lies inside (ray-casting algorithm).  
     - Detect intersections with another polygon.  
   - **Constraints**: Support convex/concave polygons; optimize for large vertex counts.

5. **Bank Account Manager**  
   - **Description**: Simulate bank accounts with transaction history.  
   - **Requirements**:  
     - Support deposit, withdraw, and transfer with private balance.  
     - Maintain a transaction log (list of dicts with timestamps via `datetime`).  
     - Export history to CSV using `csv`.  
   - **Constraints**: Prevent overdrafts; ensure non-negative balances.

---

## 🔄 2. Encapsulation & Property Decorators

**Level: Medium → Hard** – Emphasize data protection and computed properties.

6. **Temperature Controller**  
   - **Description**: Manage temperature conversions and validation.  
   - **Requirements**:  
     - Store temperature in Celsius with properties for Fahrenheit and Kelvin.  
     - Enforce a minimum of absolute zero (-273.15°C).  
     - Log temperature changes with timestamps.  
   - **Constraints**: Validate inputs; ensure precision in conversions.

7. **Secure Password Vault**  
   - **Description**: Securely manage user passwords.  
   - **Requirements**:  
     - Store passwords as SHA-256 hashes using `hashlib`.  
     - Use `@property` for strength validation (e.g., length ≥ 8, mixed characters).  
     - Require old password for updates; log failed attempts.  
   - **Constraints**: Minimize memory exposure; enforce secure updates.

8. **Inventory Stock Tracker**  
   - **Description**: Track inventory with automated alerts.  
   - **Requirements**:  
     - Private `_quantity` with `@property` for access and low-stock alerts.  
     - Validate non-negative quantities and threshold settings.  
     - Log restock events to a string buffer.  
   - **Constraints**: Ensure consistent state during updates.

9. **Circle Geometry**  
   - **Description**: Model circles with computed properties.  
   - **Requirements**:  
     - Store radius; provide `@property` for diameter, area, and circumference.  
     - Enforce positive radius; compare circles by radius.  
     - Format as string (e.g., "Circle(radius=5)").  
   - **Constraints**: Optimize property calculations; handle edge cases.

10. **Email Address Validator**  
    - **Description**: Validate and manage email addresses.  
    - **Requirements**:  
      - Use `@property` to validate email format (using `re`).  
      - Extract domain and username; provide readable string output.  
      - Track creation timestamp via `datetime`.  
    - **Constraints**: Handle invalid formats with custom exceptions.

---

## 🔁 3. Inheritance & Polymorphism

**Level: Hard** – Design class hierarchies with dynamic behavior.

11. **Shape Hierarchy**  
    - **Description**: Model geometric shapes with polymorphic methods.  
    - **Requirements**:  
      - Abstract `Shape` class (using `abc`) with `area()` and `perimeter()`.  
      - Subclasses: `Circle`, `Rectangle`, `Triangle` with unique calculations.  
      - Implement `__str__` for readable output.  
    - **Constraints**: Validate geometric constraints (e.g., positive dimensions).

12. **Employee Role System**  
    - **Description**: Manage employees with role-specific logic.  
    - **Requirements**:  
      - Base `Employee` with `calculate_salary()` and `promote()`.  
      - Subclasses: `Manager`, `Developer`, `Intern` with unique salary rules.  
      - Track promotions in a history list.  
    - **Constraints**: Ensure salary calculations are consistent.

13. **Vehicle Family**  
    - **Description**: Model vehicles with type-specific behaviors.  
    - **Requirements**:  
      - Base `Vehicle` with `start_engine()` and `fuel_efficiency()`.  
      - Subclasses: `Car`, `Bike`, `Truck` with distinct implementations.  
      - Simulate travel distance based on fuel.  
    - **Constraints**: Handle invalid states (e.g., no fuel).

14. **Animal Behavior Simulator**  
    - **Description**: Simulate animals with unique behaviors.  
    - **Requirements**:  
      - Base `Animal` with `make_sound()` and `move()`.  
      - Subclasses: `Dog`, `Cat`, `Bird` with specific behaviors.  
      - Create a `Zoo` to iterate over animals.  
    - **Constraints**: Ensure realistic behavior modeling.

15. **Payment Processor**  
    - **Description**: Process payments with different methods.  
    - **Requirements**:  
      - Abstract `PaymentMethod` with `process_payment()` and `refund()`.  
      - Subclasses: `CreditCard`, `MobileWallet`, `BankTransfer`.  
      - Log transactions with timestamps.  
    - **Constraints**: Validate payment amounts; handle failures.

---

## 🧩 4. Abstraction & Interfaces

**Level: Hard** – Enforce strict contracts with abstract base classes.

16. **Drawable Interface**  
    - **Description**: Define shapes for rendering.  
    - **Requirements**:  
      - Abstract `Drawable` (using `abc`) with `draw()` method.  
      - Subclasses: `Line`, `Circle`, `Text` with ASCII-based rendering.  
      - Support scaling transformations.  
    - **Constraints**: Ensure consistent rendering output.

17. **Serializable Interface**  
    - **Description**: Enable object serialization.  
    - **Requirements**:  
      - Abstract `Serializable` with `to_dict()` and `from_dict()`.  
      - Implement for `User` (name, ID) and `Product` (name, price).  
      - Validate deserialized data.  
    - **Constraints**: Handle malformed data gracefully.

18. **Logger Interface**  
    - **Description**: Log messages to different outputs.  
    - **Requirements**:  
      - Abstract `Logger` with `log()` method.  
      - Subclasses: `ConsoleLogger`, `FileLogger` (using `io.StringIO`).  
      - Support log levels (INFO, ERROR).  
    - **Constraints**: Ensure thread-safe logging.

19. **Database Connection Interface**  
    - **Description**: Simulate database connections.  
    - **Requirements**:  
      - Abstract `DatabaseConnection` with `connect()` and `query()`.  
      - Subclasses: `InMemoryDB` (using dict), `FileDB` (using `json`).  
      - Handle connection errors.  
    - **Constraints**: Simulate latency and failures.

20. **Authenticator Interface**  
    - **Description**: Authenticate users with different methods.  
    - **Requirements**:  
      - Abstract `Authenticator` with `authenticate()` and `revoke()`.  
      - Subclasses: `PasswordAuth`, `TokenAuth` with custom exceptions.  
      - Track authentication attempts.  
    - **Constraints**: Prevent brute-force attacks.

---

## 🎮 5. Magic Methods & Operator Overloading

**Level: Hard** – Customize object behavior with advanced overloading.

21. **Fraction Arithmetic**  
    - **Description**: Model fractions with exact arithmetic.  
    - **Requirements**:  
      - Overload `+`, `-`, `*`, `/`, `==`, `<`, `>`; reduce using GCD (via `math.gcd`).  
      - Implement `__str__` and `__float__`.  
      - Support mixed-type operations (e.g., int).  
    - **Constraints**: Prevent division by zero; optimize GCD.

22. **Vector2D Operations**  
    - **Description**: Manage 2D vectors with operator overloading.  
    - **Requirements**:  
      - Overload `+`, `-`, `*` (dot/scalar), `/`, `==`.  
      - Compute magnitude, normalization, and angle between vectors.  
      - Format as readable string.  
    - **Constraints**: Handle floating-point precision.

23. **Matrix Operations**  
    - **Description**: Perform matrix arithmetic with nested lists.  
    - **Requirements**:  
      - Support addition, multiplication, transpose, and scalar multiplication.  
      - Implement `__str__` for grid output; validate dimensions.  
      - Compute determinant (2x2, 3x3).  
    - **Constraints**: Handle dimension mismatches; optimize multiplication.

24. **Time Duration**  
    - **Description**: Represent time durations.  
    - **Requirements**:  
      - Overload `+`, `-`, `==`, `<`, `>`; format as "HH:MM:SS".  
      - Support conversion between units (seconds, minutes).  
      - Validate non-negative durations.  
    - **Constraints**: Ensure consistent arithmetic.

25. **Custom List Implementation**  
    - **Description**: Mimic Python’s list behavior.  
    - **Requirements**:  
      - Support `__getitem__`, `__setitem__`, `__len__`, `__iter__`, `__contains__`.  
      - Implement append, remove, and slicing.  
      - Overload `+` for concatenation.  
    - **Constraints**: Optimize for large lists; handle edge cases.

---

## 🧱 6. Composition & Aggregation

**Level: Hard** – Build modular systems with composed objects.

26. **Car and Engine System**  
    - **Description**: Model a car with an engine component.  
    - **Requirements**:  
      - `Car` composed of `Engine` (horsepower, fuel type).  
      - Methods to start/stop engine and report specs.  
      - Validate engine compatibility.  
    - **Constraints**: Ensure state consistency (e.g., engine off when stopped).

27. **Playlist and Songs**  
    - **Description**: Manage music playlists.  
    - **Requirements**:  
      - `Playlist` composed of `Song` objects (title, artist, duration).  
      - Support add, remove, shuffle (using `random.shuffle`), and total duration.  
      - Format playlist as string.  
    - **Constraints**: Handle empty playlists; optimize shuffling.

28. **Computer Configuration**  
    - **Description**: Simulate a computer system.  
    - **Requirements**:  
      - `Computer` composed of `CPU`, `RAM`, `Storage`.  
      - Check compatibility (e.g., RAM capacity); report specs.  
      - Simulate boot-up sequence.  
    - **Constraints**: Validate component specs.

29. **E-commerce Order System**  
    - **Description**: Manage shopping orders.  
    - **Requirements**:  
      - `Order` composed of `Item` objects (name, quantity, price).  
      - Calculate total cost; apply discounts.  
      - Export order summary to string.  
    - **Constraints**: Handle invalid quantities; ensure accurate totals.

30. **Sports Team Manager**  
    - **Description**: Manage a sports team.  
    - **Requirements**:  
      - `Team` composed of `Player` objects (name, position, stats).  
      - Compute team stats (average score); find players by position.  
      - Support substitutions.  
    - **Constraints**: Validate player data; handle roster limits.

---

## 🧠 7. Advanced OOP Concepts

**Level: Hard → Expert** – Leverage advanced Python features.

31. **Singleton Configuration**  
    - **Description**: Ensure a single configuration instance.  
    - **Requirements**:  
      - Use a metaclass to enforce singleton behavior.  
      - Store key-value settings; support thread-safe access (via `threading.Lock`).  
      - Provide update and query methods.  
    - **Constraints**: Prevent race conditions; ensure immutability for settings.

32. **Validator Descriptor**  
    - **Description**: Validate attributes dynamically.  
    - **Requirements**:  
      - Create a `PositiveNumber` descriptor for attributes like price or quantity.  
      - Apply to a `Product` class; raise custom exceptions on invalid values.  
      - Support type checking.  
    - **Constraints**: Ensure descriptor reusability.

33. **Cached Property Decorator**  
    - **Description**: Cache expensive property computations.  
    - **Requirements**:  
      - Implement a `@cached_property` decorator storing results.  
      - Demonstrate with a class computing factorials.  
      - Allow cache invalidation.  
    - **Constraints**: Optimize memory usage; ensure thread-safety.

34. **Custom Enum Implementation**  
    - **Description**: Model an enumeration for weekdays.  
    - **Requirements**:  
      - Create a `Day` enum with methods for weekend/weekday checks.  
      - Support iteration and string formatting.  
      - Validate enum values.  
    - **Constraints**: Ensure immutability; handle invalid inputs.

35. **File Handler Context Manager**  
    - **Description**: Manage file operations safely.  
    - **Requirements**:  
      - Implement a `FileHandler` with `__enter__` and `__exit__`.  
      - Support read/write modes; handle file errors.  
      - Log operations to a string buffer.  
    - **Constraints**: Ensure proper resource cleanup.

---

## 🕸 8. Complex System Design

**Level: Hard → Expert** – Model real-world systems with intricate relationships.

36. **ATM Simulator**  
    - **Description**: Simulate an ATM system.  
    - **Requirements**:  
      - Classes: `User`, `Account`, `Transaction`.  
      - Support PIN authentication, deposit, withdrawal, and balance inquiry.  
      - Log transactions with timestamps.  
    - **Constraints**: Prevent unauthorized access; handle insufficient funds.

37. **Library Management System**  
    - **Description**: Manage books and borrowers.  
    - **Requirements**:  
      - Classes: `Book`, `Member`, `Loan`.  
      - Support borrowing, returning, and fine calculation.  
      - Implement reservation queues.  
    - **Constraints**: Ensure unique loans; handle overdue logic.

38. **Hospital Record System**  
    - **Description**: Track patient records.  
    - **Requirements**:  
      - Classes: `Patient`, `Doctor`, `Appointment`.  
      - Manage schedules; enforce patient privacy (private attributes).  
      - Generate appointment summaries.  
    - **Constraints**: Validate appointment conflicts.

39. **E-commerce Shopping Cart**  
    - **Description**: Simulate an online store.  
    - **Requirements**:  
      - Classes: `Product`, `Cart`, `Order`.  
      - Add/remove items; calculate totals with tax/discounts.  
      - Export order details to string.  
    - **Constraints**: Handle stock limits; ensure accurate calculations.

40. **Course Registration System**  
    - **Description**: Manage university course registrations.  
    - **Requirements**:  
      - Classes: `Student`, `Course`, `Registration`.  
      - Enforce course capacity and prerequisites.  
      - Generate student schedules.  
    - **Constraints**: Prevent over-registration; validate prerequisites.

---

## 🧪 9. Testing & Exception Handling

**Level: Hard** – Ensure robustness with custom exceptions and tests.

41. **Robust Calculator**  
    - **Description**: Build a calculator with error handling.  
    - **Requirements**:  
      - Support basic arithmetic with custom exceptions (e.g., `DivisionByZeroError`).  
      - Write `unittest` tests for valid/invalid inputs.  
      - Log operations to a string buffer.  
    - **Constraints**: Ensure comprehensive error handling.

42. **File Reader with Context**  
    - **Description**: Read files safely with context management.  
    - **Requirements**:  
      - Implement a `FileReader` context manager for reading text.  
      - Handle file errors (e.g., `FileNotFoundError`).  
      - Test with `unittest` for various scenarios.  
    - **Constraints**: Ensure proper resource cleanup.

43. **URL Validator**  
    - **Description**: Validate URLs with custom exceptions.  
    - **Requirements**:  
      - Create a `URL` class with regex-based validation (using `re`).  
      - Raise `InvalidURLError` for malformed URLs.  
      - Test with valid/invalid cases using `unittest`.  
    - **Constraints**: Support common URL formats.

44. **Bank Transfer System**  
    - **Description**: Simulate account transfers with rollback.  
    - **Requirements**:  
      - Implement `Account` with transfer method; rollback on failure.  
      - Raise `InsufficientFundsError` or `InvalidAccountError`.  
      - Test atomicity with `unittest`.  
    - **Constraints**: Ensure transactional integrity.

45. **Configuration Loader**  
    - **Description**: Load and validate configurations.  
    - **Requirements**:  
      - Parse JSON configs using `json`; provide defaults.  
      - Raise `ConfigError` for invalid formats.  
      - Test with `unittest` for various cases.  
    - **Constraints**: Handle malformed configs gracefully.

---

## 🔗 10. Performance & Optimization

**Level: Hard → Expert** – Optimize efficiency with pure Python.

46. **Memoized Fibonacci Calculator**  
    - **Description**: Compute Fibonacci numbers efficiently.  
    - **Requirements**:  
      - Implement a `Fibonacci` class with memoization using a dictionary.  
      - Compare with naive recursion via `time.perf_counter`.  
      - Support large indices (e.g., 1000).  
    - **Constraints**: Minimize memory usage; handle overflow.

47. **Efficient Sorting Algorithms**  
    - **Description**: Implement and compare sorting algorithms.  
    - **Requirements**:  
      - Create a `Sorter` class with bubble, quicksort, and mergesort methods.  
      - Measure performance using `time.perf_counter`.  
      - Sort lists of custom objects (e.g., `Point2D`).  
    - **Constraints**: Optimize for large datasets.

48. **Lazy Data Loader**  
    - **Description**: Load data lazily to save memory.  
    - **Requirements**:  
      - Implement a `LazyLoader` class using generators for large datasets.  
      - Support iteration and filtering.  
      - Compare memory usage with eager loading.  
    - **Constraints**: Handle large datasets efficiently.

49. **Thread-Safe Counter**  
    - **Description**: Manage a counter in concurrent environments.  
    - **Requirements**:  
      - Create a `Counter` class with thread-safe increment/decrement (using `threading.Lock`).  
      - Simulate concurrent access with `threading.Thread`.  
      - Test correctness with `unittest`.  
    - **Constraints**: Prevent race conditions.

50. **Optimized Matrix Multiplier**  
    - **Description**: Optimize matrix multiplication.  
    - **Requirements**:  
      - Implement a `Matrix` class with standard and divide-and-conquer multiplication.  
      - Compare performance using `time.perf_counter`.  
      - Support sparse matrix optimization.  
    - **Constraints**: Handle large matrices; validate dimensions.

---

## 🚀 Additional Notes

- **Testing**: Each problem should include `unittest` tests covering edge cases (e.g., empty inputs, invalid values). Use `unittest.mock` for simulating I/O.
- **Performance**: Optimize for time and space complexity; use `time.perf_counter` for profiling.
- **Concurrency**: Use `threading` or `multiprocessing` where applicable, ensuring thread-safety with locks.
- **Documentation**: Include docstrings and type hints for clarity and IDE support.
- **Best Practices**: Follow PEP 8; validate inputs; handle exceptions robustly.

This **Refined Mastery Edition** ensures you master Python OOP by focusing on intricate class design and real-world problem-solving with minimal setup. All problems are self-contained, leveraging only Python’s standard library (`math`, `json`, `csv`, `datetime`, `re`, `random`, `threading`, `io`, `abc`, `unittest`).

Let me know if you want:
- Starter code for any problem (e.g., in Python with comments).
- Test cases using `unittest`.
- A structured GitHub repository layout.
- A PDF version of this challenge set.
- Detailed solutions for specific problems.