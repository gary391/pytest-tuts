# Unit Testing in Python with pytest

### Unit Testing in Python with pytest | Getting Started (Part-1)

---
### Unit Testing in Python with pytest | Asserting Expected Exceptions (Part-2)

- How to validate if the expected exception is being raised or not?
    

- What is `with` statement?

    The `with` statement in Python is used to wrap the execution of a block with methods defined by a context manager. 
    A context manager is an object that defines the runtime context to be established when the with statement is executed.
    It is designed to simplify the setup and teardown actions that need to be executed around a block of code. 
    The with statement ensures that resources are acquired and released properly, and it provides a cleaner syntax for 
    try-finally blocks.
    
    In the context of testing with pytest, the with statement is often used in conjunction with pytest. Raises to test 
    that a block of code raises an expected exception. `pytest.raises` is a context manager that checks if the code inside
    its block raises a specific exception and fails the test if the exception is not raised.

---
### Unit Testing in Python with pytest | Introduction to Markers (Part-3)

- Allows you easily set metadata on your test function.
---