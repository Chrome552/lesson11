from functions import salary,hello_who

assert hello_who('Max') == 'Hello, Max', 'Max error'
assert hello_who('Leo') == 'Hello, Leo', 'Leo error'
assert hello_who('Nikita') == 'Hello, Nikita', 'Nikita error'
assert salary(2, 1) == 4, 'Salary error 1'
assert salary(2, 2) == 8

# AssertionError: Salary error 1