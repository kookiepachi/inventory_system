# Lab 5 – Static Code Analysis
**Student:** Khushee P Kiran  
**Course:** Software Engineering – Lab 5  
**File Analyzed:** inventory_system.py  

---

## Overview
This lab focused on performing static code analysis using **Pylint**, **Flake8**, and **Bandit** to detect and correct style, logic, and security issues in the `inventory_system.py` program.  
The objective was to understand how automated tools help identify vulnerabilities, enforce coding standards, and improve overall software quality.

---

## Tools Used
1. **Pylint** – Checked for logical errors, naming conventions, and missing documentation.  
2. **Flake8** – Enforced PEP8 style and formatting rules.  
3. **Bandit** – Scanned for potential security issues such as the use of unsafe functions.

---

## Issues and Fixes

| No. | Issue (Tool / Code) | Severity | Description | Fix Applied | Status |
|-----|----------------------|-----------|--------------|--------------|---------|
| 1 | `B307: Use of eval()` (Bandit) | High | The `eval()` function can execute arbitrary code, posing a severe security risk. | Removed the `eval()` line completely and replaced it with a safe demo function. | Fixed |
| 2 | `B110: try/except/pass` (Bandit) | High | The bare `except:` block ignored all errors, hiding runtime issues. | Replaced with `except KeyError:` and added a logging warning. | Fixed |
| 3 | `W0102: Dangerous default value []` (Pylint) | Medium | Mutable default argument caused shared-state bugs between function calls. | Changed the argument to `logs=None` and initialized inside the function. | Fixed |
| 4 | `W1514/R1732: open() without encoding or with` (Pylint/Bandit) | Medium | Files were opened without a context manager or explicit encoding. | Used `with open(..., encoding="utf-8")` for both reading and writing. | Fixed |
| 5 | `C0103: Function names not in snake_case` (Pylint) | Low | Function names were written in camelCase instead of snake_case. | Renamed all functions to follow PEP8 naming conventions. | Fixed |
| 6 | `W0611: Unused import logging` (Flake8/Pylint) | Low | The `logging` module was imported but never used. | Configured logging and added appropriate log messages. | Fixed |
| 7 | `C0116: Missing function docstring` (Pylint) | Low | Functions lacked documentation strings describing their purpose. | Added clear and concise docstrings for every function. | Fixed |
| 8 | `C0209: Consider using f-string` (Pylint) | Low | Old-style string formatting was used instead of f-strings. | Replaced all with f-strings for clarity and efficiency. | Fixed |
| 9 | `E302/E305: Missing blank lines` (Flake8) | Low | Functions were not separated by two blank lines as per PEP8. | Added proper spacing between all function definitions. | Fixed |

---

## Results Summary

| Tool | Before | After | Key Improvements |
|------|---------|--------|------------------|
| **Pylint** | 4.80 / 10 | 9.50 / 10 | Improved naming, documentation, and logic |
| **Flake8** | 10+ warnings | 0 warnings | Fully PEP8 compliant |
| **Bandit** | 2 issues (B110, B307) | 0 issues | Security vulnerabilities resolved |

---

## Key Improvements
- Implemented **input validation** to ensure correct data types and values.  
- Used **logging** for better traceability instead of print statements.  
- Introduced **context managers** for safe file handling with encoding.  
- Removed insecure code (`eval()`) and replaced it with safe functions.  
- Added **docstrings** and standardized function naming conventions.  
- Achieved a consistent and professional coding style following PEP8 and PEP257.

---

## Reflection

### Major Issues Identified
- Insecure use of the `eval()` function.  
- Bare `except:` block hiding real errors.  
- Mutable default arguments.  
- Missing `with open()` statements for file safety.  
- Poor naming and lack of documentation.

### Fixes Implemented
- Removed `eval()` and replaced with a safe demo function.  
- Used specific exception handling (`KeyError`) instead of bare `except:`.  
- Replaced mutable defaults with `None` and initialized locally.  
- Applied context managers with UTF-8 encoding for file operations.  
- Added detailed docstrings, logging, and PEP8-compliant naming.

### Improvements Observed

| Tool | Before | After |
|------|---------|--------|
| **Pylint** | 4.80 / 10 | 9.50 / 10 |
| **Flake8** | 10+ warnings | 0 warnings |
| **Bandit** | 2 security issues | 0 issues |

### Learnings from the Lab
- Static analysis helps identify potential issues **without executing the code**.  
- Even small changes such as proper exception handling and naming greatly improve readability.  
- Security issues like `eval()` and improper exception blocks can be caught early using tools like Bandit.  
- Following **PEP8** and **PEP257** improves maintainability and collaboration.

### Future Applications
- Integrate these tools into **CI/CD pipelines** for automated quality checks.  
- Use **pre-commit hooks** to enforce linting before commits.  
- Maintain a **minimum Pylint score of 9/10** in all projects.  
- Apply static code analysis to machine learning, backend, and automation projects to ensure safety and clarity.

---

## Conclusion
This lab demonstrated the importance of static code analysis in improving code quality, security, and readability.  
By analyzing and refactoring the code iteratively, all logical, stylistic, and security issues were resolved.  
The final version of the `inventory_system.py` script is secure, maintainable, and compliant with modern Python coding standards.
