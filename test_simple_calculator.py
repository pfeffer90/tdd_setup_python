class Calculator():
    @staticmethod
    def add(x,y):
        pass
    def __init__(self):
        pass

def test_calculator_adds_two_numbers():
    # Arrange
    calculator = Calculator()
    first_summand = 2
    second_summand = 3
    expected_sum = 5
    # Act
    actual_sum = calculator.add(first_summand, second_summand)
    # Assert
    assert expected_sum == actual_sum
