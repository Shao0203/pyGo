from module.name_function import get_formatted_name


def test_first_last_name():
    '''test a name like Tom Green'''
    formatted_name = get_formatted_name('tom', 'green')
    assert formatted_name == 'Tom Green'


def test_first_last_middle_name():
    '''deal with middle name'''
    formatted_name = get_formatted_name('tom', 'green', 'middle')
    assert formatted_name == 'Tom Middle Green'
