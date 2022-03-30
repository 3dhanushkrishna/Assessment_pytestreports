import Program
import pytest

@pytest.mark.parametrize("a,b",[(153,True),(370,True),(371,False),(407,True)])
def test_Amstrong(a,b):
    result = Program.Amstrong(a)
    assert result == b

@pytest.mark.parametrize("a,b",[(8,True),(10,False),(88,True),(73,True)])
@pytest.mark.skip(reason = "no need")
def test_Divisible8(a,b):
    result = Program.Div_8(a)
    assert result == b

@pytest.mark.parametrize("a,b,c,d",[(2,1,4,1),(4,2,5,2),(15,10,14,10),(12,32,34,10),(13,8,6,17)])
@pytest.mark.xfail
def test_Smallest(a,b,c,d):
    result = Program.Smallest(a,b,c)
    assert result == d

@pytest.mark.parametrize("a, b",[(14,True),(17,False),(10,True)])
def test_Evenorodd(a,b):
    result = Program.Evenorodd(a)
    assert result == b

@pytest.mark.parametrize("a,b",[("121",True),("123",True),("1551",True),("120",False),("221",True)])
def test_Palindrome(a,b):
    result = Program.Palindrome(a)
    assert result == b