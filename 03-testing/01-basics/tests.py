from intervals import overlapping_intervals


def test_overlapping_intervals():
    # true
    assert overlapping_intervals((1, 5), (3, 6))

    # false
    assert not overlapping_intervals((2, 5), (7, 10))
    assert not overlapping_intervals((0, 0), (0, 1))