# app.py
# This is a test commit
def add(a, b):
    return a + b
#test one
def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
