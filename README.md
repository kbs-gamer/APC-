# Advanced Python Computing (APC) - Semester 5

This repository contains comprehensive Python implementations and laboratory assignments for the **Advanced Python Computing (APC)** course.

---

## 📁 Repository Structure

```
APC-/
├── Array1/                      # Array Manipulation & Operations (13 programs)
├── First/                       # String Problem Statements (30 programs)
├── Function/Function/           # Functions, Recursion & Lambda Expressions (52 programs)
├── Regular Expression/          # Regex Patterns & Text Processing (26 programs)
├── Dictionary/                  # Dictionary Problem Statements & Real-World Use Cases (35 programs)
├── q01_... to q16_...py         # Pandas DataFrames, Series & CSV Data Analysis (16 programs)
├── *.csv                        # Datasets (students.csv, employees.csv, patients.csv, weather.csv)
└── *.docx                       # Original Assignment Specification Documents
```

---

## 📚 Topics & Modules

### 1. Dictionary Operations (`Dictionary/`)
Contains **35 comprehensive programs** solving dictionary operations and practical systems:
- Key-value creation, insertion, updating, deletion, and search
- Character and word frequency counters
- Dictionary merging, common keys, and common values
- Duplicate value handling and sorting by keys
- Dictionary comprehensions (squares, cubes, filtered even numbers)
- Practical systems: Student CRUD Management, Employee Salary Analyzer, Inventory Tracker, Phonebook Manager, and Library Book System
- Two Sum problem using hash maps, first unique character, first duplicate character, and word length distribution

### 2. Functions, Recursion & Lambda (`Function/Function/`)
Contains **52 programs** covering:
- Mathematical & algorithmic functions: Factorial, prime check, power, Fibonacci series, second largest number
- Recursive implementations: Decimal to binary conversion, recursive palindrome checker, binary search
- Higher-order functions: Passing functions as arguments to a unified `calculate()` dispatcher
- Real-world modular systems: Banking transaction simulator, Library management, Electricity bill calculator, Patient hospital billing system, Retail invoice generator
- Lambda Functions & Functional Programming: `map()`, `filter()`, `sorted()`, list comprehensions, sorting records, filtering high earners, and processing product catalogs

### 3. Regular Expressions (`Regular Expression/`)
Contains **26 programs** solving pattern matching tasks:
- Digits, vowels, uppercase letters extraction
- Whitespace and punctuation normalization
- Validations: 10-digit Indian mobile numbers, email addresses, password strength, Indian vehicle registration plates (e.g. `MH12AB1234`), and product codes (`ABC-1234-XY`)
- Information extraction: Six-digit Indian PIN codes, dates (`DD-MM-YYYY`), website URLs, hashtags (`#topic`), file extensions, invoice numbers and monetary amounts
- Academic extraction: Parsing student records from paragraphs, research reference extraction (DOIs, publication years, emails, URLs)
- Python comment detection and discussion of regex parsing limitations

### 4. String Manipulation (`First/`)
Contains **30 programs** for fundamental and advanced string algorithms:
- String length calculation without `len()`
- Vowel, consonant, digit, and special character counters
- String reversal and palindrome verification
- Longest, shortest, and word count extraction
- Duplicate character detection and character frequencies
- Anagram testing, substring search, Caesar Cipher encoder/decoder
- Run-Length Encoding (RLE) and compression

### 5. Pandas Data Analysis (`q01_...` to `q16_...`)
Contains **16 data analysis scripts** and datasets:
- **DataFrame Analysis**:
  - `q01_student_marks.py`: Student academic performance, total, average, and 75% cutoff
  - `q02_employees.py`: Employee department filtering, salary statistics, and experience
  - `q03_products.py`: Product revenue, quantity, and top-selling product
  - `q04_patients.py`: Patient medical charges and senior citizen demographics
  - `q05_orders.py`: E-commerce orders, discount calculation, and high-value orders
  - `q06_attendance.py`: Class attendance percentage and defaulter lists
  - `q07_retail_shop.py`: Retail store total sales and statistics
- **Series Analysis**:
  - `q08_series_student_marks.py` to `q12_series_attendance.py`: Pandas Series manipulation, min/max, indexing, and filtering
- **CSV Ingestion & Processing**:
  - `q13_students_csv.py`: Multi-subject analysis from `students.csv`
  - `q14_employees_csv.py`: Departmental payroll analytics from `employees.csv`
  - `q15_patients_csv.py`: Disease frequencies and hospital bills from `patients.csv`
  - `q16_weather_csv.py`: City-wise temperature and rainfall analytics from `weather.csv`

---

## 🚀 How to Run

Ensure Python 3.8+ and pandas are installed:
```bash
pip install pandas
```

Run any script individually:
```bash
python Dictionary/01_student_details.py
python "Function/Function/ex31.py"
python "Regular Expression/q15.py"
python q01_student_marks.py
```
