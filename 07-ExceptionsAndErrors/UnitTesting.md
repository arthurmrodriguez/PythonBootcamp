# Unit Testing: pylint and unittest

Tests provide useful information about the health of our code when it starts to grow larger while working with teammates on big projects. We're gonna focus in two **testing tools**:

- **pylint**: library that looks at our code and reports/check possible issues. ```pip install pylint``` will install this tool in case you don't have it.
- **unittest**: built-in library that tests our program and check if we're getting desired outputs.


## pylint

We'll use an example script called **simple1.py** with a slight error of typing. We can check how *pylint* work afterwards. Actual output of running ```pylint simple1.py``` is:

```
E:  4, 6: Undefined variable 'B' (undefined-variable)
```

## unittest

In order to use unittest we create a script called **test_cap.py** where we create a class that inherits from *unittest.TestCase*.

Then we need to create a set of methods called **test methods** that will simply execute the functions or features we want to test.

Afterwards, the last line of the **test method** has to be something that actually tests the output of the function we are testing. This last line has the following syntax:

```
self.assertEqual(current_result,expected_result)
```

Finally to make the test script execute, we need to add at the end the last line:

```
if __name__ == '__main__'
    unittest.main()
```

And now we can test our code as we want!
