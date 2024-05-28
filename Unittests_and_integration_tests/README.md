Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls. 

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with

```bash
$ python -m unittest path/to/test_file.py
```

## Resources

**Read or watch:**

- [unittest — Unit testing framework](https://intranet.atlasschool.com/rltoken/ug8beURP6GPP7yJtQ4I1Jw)
- [unittest.mock — mock object library](https://intranet.atlasschool.com/rltoken/cCjj8L1q_NaYxvFfqFfYPA)
- [How to mock a readonly property with mock?](https://intranet.atlasschool.com/rltoken/y8OnTBcqkL_Rmr2I3peRSQ)
- [parameterized](https://intranet.atlasschool.com/rltoken/Z6XhDNPKVcd7BW6163H0_Q)
- [Memoization](https://intranet.atlasschool.com/rltoken/7xU6wdKJpB8L2S8vtkxpjw)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.atlasschool.com/rltoken/AiD51mZh2lZ8stCrg3CjGQ), **without the help of Google**:

- The difference between unit and integration tests.
- Common testing patterns such as mocking, parametrizations and fixtures

## What is a unittest?

A unit test is a type of software test that focuses on verifying the correctness of individual units of code, typically functions or methods, to ensure they perform as expected. The main purpose of unit tests is to isolate each part of the program and show that the individual parts are correct. A unit is the smallest testable part of an application, which could be a function, method, procedure, module, or object.

### Here are key points about unit tests:

1. **Isolation**: Each unit test should test a single part of the code in isolation from the rest. This means it doesn't interact with external dependencies like databases, file systems, or network resources.
2. **Automation**: Unit tests are usually automated. This allows them to be run quickly and frequently, providing immediate feedback to developers.
3. **Consistency**: They help ensure that code changes do not break existing functionality. By running unit tests after every change, developers can quickly identify and fix issues.
4. **Documentation**: Unit tests can serve as documentation for the code. They describe how the code is supposed to work and what it is supposed to do.
5. **Regression Testing**: When new features are added or changes are made, running unit tests ensures that existing functionality still works as intended.

The `[unittest](https://docs.python.org/3/library/unittest.html#module-unittest)` module provides a rich set of tools for constructing and running tests.  This section demonstrates that a small subset of the tools suffice to meet the needs of most users.

Here is a short script to test three string methods:

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

The crux of each test is a call to `[assertEqual()](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)` to check for an expected result; `[assertTrue()](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue)` or `[assertFalse()](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse)` to verify a condition; or `[assertRaises()](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises)` to verify that a specific exception gets raised.  These methods are used instead of the `[assert](https://docs.python.org/3/reference/simple_stmts.html#assert)` statement so the test runner can accumulate all test results and produce a report.

## What is unittest.mock?

`[unittest.mock](https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock)` is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used. Mock objects are used to simulate the behavior of real objects in a controlled way, which is particularly useful for isolating the unit of code being tested by eliminating dependencies on external systems or components.

### Key Concepts and Uses of `unittest.mock`

1. **Mock Objects**:
Mock objects can simulate the methods and properties of real objects. You can define their behavior and specify return values, side effects, and expected calls.
2. **Patching**:
Patching is a technique used to replace real objects in your code with mock objects during a test. This is typically done using decorators or context managers.
3. **Assertions**:
`unittest.mock` provides various assertion methods to verify that mock objects are used correctly, such as checking if certain methods were called with specific arguments.

### Key Components of `unittest.mock`

1. **Mock Class**:
The basic mock object. You can configure it to return specific values or raise exceptions.
2. **MagicMock Class**:
A subclass of Mock with default implementations of most of the magic methods (like `__getitem__`, `__setitem__`, `__call__`, etc.), making it suitable for mocking more complex objects.
3. **patch Function**:
A function used to replace objects in your code with mocks. It can be used as a decorator, context manager, or manually.

### Basic Mock Object

```python
from unittest.mock import Mock

# Create a mock object
mock = Mock()

# Configure the mock to return a specific value
mock.return_value = 'mocked value'

# Call the mock and check its return value
result = mock()
print(result)  # Output: 'mocked value'
```

### Patching with `patch` as a Decorator

```python
import unittest
from unittest.mock import patch

# Function to be tested
def fetch_data():
    # Simulate fetching data from an external source
    return "real data"

# Function that uses fetch_data
def process_data():
    data = fetch_data()
    return data.upper()

class TestProcessData(unittest.TestCase):

    @patch('__main__.fetch_data', return_value="mocked data")
    def test_process_data(self, mock_fetch):
        result = process_data()
        self.assertEqual(result, "MOCKED DATA")
        mock_fetch.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```

### **Using `MagicMock` for Complex Mocks**

```python
from unittest.mock import MagicMock

# Create a MagicMock object
magic_mock = MagicMock()

# Configure the magic mock
magic_mock.__getitem__.return_value = 'mocked item'

# Use the magic mock
print(magic_mock['key'])  # Output: 'mocked item'
```

### Benefits of Using `unittest.mock`

- **Isolation**: Tests can focus on the code being tested without relying on external systems or dependencies.
- **Control**: You can precisely control the behavior of mocks, making it easier to test various scenarios.
- **Verification**: Easily verify that interactions with mocks are as expected, ensuring your code behaves correctly under different conditions.

## What is the difference between unit and integration tests?

### Key Differences

- **Focus**: Unit tests focus on individual components in isolation, while integration tests focus on interactions between components.
- **Dependencies**: Unit tests typically mock external dependencies; integration tests often use real instances of these dependencies.
- **Execution Time**: Unit tests are faster and can be run more frequently; integration tests are slower and might be run less often.
- **Complexity**: Unit tests are simpler and more granular; integration tests are more complex and involve multiple components.

## Common testing patterns

- **Mocking**: Used to isolate the unit of code being tested by replacing dependencies with mock objects. This allows you to simulate different scenarios and behaviors of those dependencies.
- **Parametrization**: Allows running the same test with multiple sets of input values, increasing test coverage and ensuring the code handles various inputs correctly.
- **Fixtures**: Provide a way to set up and tear down the test environment, ensuring that each test runs in a consistent and controlled context, reducing code duplication and improving test reliability.
