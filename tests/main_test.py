from src.main import test_func


def test_main_function_will_return_hello_world():
    assert test_func() == "Hello world"
