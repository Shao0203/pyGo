import pytest


# ==================== Fixtures ====================

@pytest.fixture(scope="function")
def func_fixture():
    print("\n[func_fixture] setup")
    return {"type": "function"}


@pytest.fixture(scope="module")
def module_fixture():
    print("\n[module_fixture] setup")
    return {"type": "module"}


@pytest.fixture(scope="session")
def session_fixture():
    print("\n[session_fixture] setup")
    return {"type": "session"}


# ==================== Tests ====================

def test_one(func_fixture, module_fixture, session_fixture):
    print("Running test_111")
    assert func_fixture["type"] == "function"
    assert module_fixture["type"] == "module"
    assert session_fixture["type"] == "session"


def test_two(func_fixture, module_fixture, session_fixture):
    print("Running test_222")
    assert func_fixture["type"] == "function"
    assert module_fixture["type"] == "module"
    assert session_fixture["type"] == "session"


def test_three(func_fixture, module_fixture, session_fixture):
    print("Running test_333")
    assert func_fixture["type"] == "function"
    assert module_fixture["type"] == "module"
    assert session_fixture["type"] == "session"
