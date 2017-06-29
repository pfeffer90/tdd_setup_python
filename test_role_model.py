def add(x,y):
    pass

def test_add_adds_two_numbers():
    # Arrange
    first_summand = 2
    second_summand = 3
    expected_sum = 5
    # Act
    actual_sum = add(first_summand, second_summand)
    # Assert
    assert expected_sum == actual_sum
