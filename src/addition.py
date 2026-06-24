# app.py
# This is a test commit
# Another test commit
# A 3rd test commit to trigger GitHub Actions workflows
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
