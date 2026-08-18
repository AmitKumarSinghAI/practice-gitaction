from src.math_operation import mul

def test_mul():
    assert mul(2,3) == 6
    assert mul(2,50) == 100
    assert mul(2,2) == 4
    assert mul(2,1) == 6
    assert mul(2,0) == 0