import pytest
from src.add_nums import add_nums

@pytest.fixture(params=[
    (1, 2, 3),  
    (4, 5, 9),  
    (10, 15, 25)
])
def data(request):
    return request.param

def test_add_nums(data):
    num1, num2, expected = data
    assert add_nums(num1, num2) == expected