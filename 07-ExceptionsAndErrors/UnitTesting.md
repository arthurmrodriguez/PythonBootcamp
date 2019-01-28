# Unit Testing: pylint and unittest

Tests provide useful information about the health of our code when it starts to grow larger while working with teammates on big projects. We're gonna focus in two **testing tools**:

- **pylint**: library that looks at our code and reports/check possible issues. ```pip install pylint``` will install this tool in case you don't have it.
- **unittest**: built-in library that tests our program and check if we're getting desired outputs.


## Pylint

We'll use an example script called **simple1.py** with a slight error of typing. We can check how *pylint* work afterwards. Actual output of running ```pylint simple1.py``` is:

```E:  4, 6: Undefined variable 'B' (undefined-variable)```
