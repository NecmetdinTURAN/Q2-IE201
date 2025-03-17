import getpermutations
def pytest_test(txt=str):
    assert get_permutations("abc")==['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
