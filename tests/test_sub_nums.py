
import pytest
from src.sub_nums import sub_nums

@pytest.fixture(params=[
    (3, 2, 1),  
    (9, 5, 4),   
    (25, 15, 10)
])
def data(request):
    return request.param

def test_sub_nums(data):
    num1, num2, expected = data
    assert sub_nums(num1, num2) == expected