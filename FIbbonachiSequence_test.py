import FIbbonachiSequence

def test_FIbbonachiSequence():
    assert FIbbonachiSequence.generate_fibonacci_sequence(0) == []
    assert FIbbonachiSequence.generate_fibonacci_sequence(1) == [0]
    assert FIbbonachiSequence.generate_fibonacci_sequence(2) == [0, 1]
    assert FIbbonachiSequence.generate_fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    assert FIbbonachiSequence.generate_fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert FIbbonachiSequence.generate_fibonacci_sequence(15) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    assert FIbbonachiSequence.generate_fibonacci_sequence(-5) == []  # Negative input should return an empty list
    assert FIbbonachiSequence.generate_fibonacci_sequence(1) == [0]  # The sequence with a single element