from binary_search import BinarySearch


'''
    Test searching
'''

def test_null_list():
    bin_search = BinarySearch(None, 0)
    assert not bin_search.was_found()
    assert bin_search.index == 0

    bin_search = BinarySearch(None, 15)
    assert not bin_search.was_found()
    assert bin_search.index == 0


def test_empty_list():
    data = []
    bin_search = BinarySearch(data, 0)
    assert not bin_search.was_found()
    assert bin_search.index == 0

    data = []
    bin_search = BinarySearch(data, 15)
    assert not bin_search.was_found()
    assert bin_search.index == 0


def test_one_element():
    data = [0]
    bin_search = BinarySearch(data, 0)
    assert bin_search.was_found
    assert bin_search.index == 0


def test_two_elements():
    data = [0, 1]
    # Found first element
    bin_search = BinarySearch(data, 0)
    assert bin_search.was_found
    assert bin_search.index == 0
    # Found second element
    bin_search = BinarySearch(data, 1)
    assert bin_search.was_found
    assert bin_search.index == 1


def test_short_length_even():
    data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    # Ensure the search finds every element in the list of test data.
    for i in range(len(data)):
        bin_search = BinarySearch(data, data[i])
        assert bin_search.was_found
        assert bin_search.index == i


def test_short_length_odd():
    data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    # Ensure the search finds every element in the list of test data.
    for i in range(len(data)):
        bin_search = BinarySearch(data, data[i])
        assert bin_search.was_found
        assert bin_search.index == i


def test_long_length_even():
    data = [i*2 for i in range(10000)]
    # Ensure the search finds every element in the list of test data.
    for i in range(len(data)):
        bin_search = BinarySearch(data, data[i])
        assert bin_search.was_found
        assert bin_search.index == i


def test_long_length_odd():
    data = [i*2 for i in range(10001)]
    # Ensure the search finds every element in the list of test data.
    for i in range(len(data)):
        bin_search = BinarySearch(data, data[i])
        assert bin_search.was_found
        assert bin_search.index == i


def test_negative():
    data = [i-200 for i in range(100)]
    # Ensure the search finds every element in the list of test data.
    for i in range(len(data)):
        bin_search = BinarySearch(data, data[i])
        assert bin_search.was_found()
        assert bin_search.index == i


def test_negative_positive():
    data = [i-100 for i in range(200)]
    # Ensure the search finds every element in the list of test data.
    for i in range(len(data)):
        bin_search = BinarySearch(data, data[i])
        assert bin_search.was_found()
        assert bin_search.index == i


def test_find_other_type():
    data = ['A', 'C', 'F', 'X', 'Z', 'a', 'b', 'i', 'k', 'm', 'q', 'r', 'u', 'v']
    for i in range(len(data)):
        bin_search = BinarySearch(data, data[i])
        assert bin_search.was_found()
        assert bin_search.index == i


'''
    Test not found
'''

def test_not_found_long_length():
    data = [i*2 for i in range(10000)]
    # Ensure the search doesn't find an element in the list of test data.
    for i in range(len(data)):
        bin_search = BinarySearch(data, data[i]+1)
        assert not bin_search.was_found()


def test_not_found_even_edges():
    data = [i+10 for i in range(1, 100)]
    # Ensure one less than lowest element was not found.
    bin_search = BinarySearch(data, 10)
    assert not bin_search.was_found()
    # Ensure one more than highest element was not found.
    bin_search = BinarySearch(data, 110)
    assert not bin_search.was_found()


def test_not_found_odd_edges():
    data = [i+10 for i in range(101)]
    # Ensure one less than lowest element was not found.
    bin_search = BinarySearch(data, 9)
    assert not bin_search.was_found()
    # Ensure one more than highest element was not found.
    bin_search = BinarySearch(data, 111)
    assert not bin_search.was_found()


'''
    Test insert indicies
'''

def test_correct_insert_index():
    data = []
    input_data = [4, 1, 3, 7, 8, 6, 2, 0, 9]
    # Ensure the input items are not found, then insert them.
    for item in input_data:
        bin_search = BinarySearch(data, item)
        assert not bin_search.was_found()
        data.insert(bin_search.index, item)
    
    expected_data = [0, 1, 2, 3, 4, 6, 7, 8, 9]
    # Ensure the inserted data matches the expected data.
    assert len(data) == len(expected_data)
    for i in range(len(expected_data)):
        assert data[i] == expected_data[i]


def test_correct_partial_insert_index():
    data = [2, 4, 6, 8, 10, 12]
    input_data = [3, 5, 7, 9, 11, 13]
    # Ensure the input items are not found, then insert them.
    for item in input_data:
        bin_search = BinarySearch(data, item)
        assert not bin_search.was_found()
        data.insert(bin_search.index, item)
    
    expected_data = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # Ensure the inserted data matches the expected data.
    assert len(data) == len(expected_data)
    for i in range(len(expected_data)):
        assert data[i] == expected_data[i]

    
def test_insert_other_type():
    data = []
    input_data = ['i', 'A', 'm', 'F', 'u', 'r', 'Z', 'a', 'C', 'k', 'X', 'q', 'b', 'v']
    # Ensure the input items are not found, then insert them.
    for item in input_data:
        bin_search = BinarySearch(data, item)
        assert not bin_search.was_found()
        data.insert(bin_search.index, item)

    expected_data = ['A', 'C', 'F', 'X', 'Z', 'a', 'b', 'i', 'k', 'm', 'q', 'r', 'u', 'v']
    # Ensure the inserted data matches the expected data.
    assert len(data) == len(expected_data)
    for i in range(len(expected_data)):
        assert data[i] == expected_data[i]


'''
    Test data and search keys
'''

class BasicObject:
    '''A basic object to be used by the following tests. '''

    def __init__(self, value: int):
        self.value: int = value
    
    def operate(self) -> int:
        return self.value + 5


def test_search_data_key():
    # Create a test list and a search list to test the data key.
    data = [BasicObject(i*2) for i in range(1000)]
    search = [(i*2)+5 for i in range(1000)]
    # Ensure the search item is found in the data after the data key is
    # applied.
    for i in range(len(data)):
        bin_search = BinarySearch(data,
                                  search[i],
                                  data_key=lambda x: x.operate())
        assert bin_search.was_found
        assert bin_search.index == i


def test_search_search_key():
    # Create a test list and a search list to test the search key.
    data = [(i*2)+5 for i in range(1000)]
    search = [BasicObject(i*2) for i in range(1000)]
    # Ensure the search item is found in the data after the search key
    # is applied.
    for i in range(len(data)):
        bin_search = BinarySearch(data,
                                  search[i],
                                  search_key=lambda x: x.operate())
        assert bin_search.was_found
        assert bin_search.index == i


def test_search_both_key():
    # Create a test list and a search list to test the keys.
    data = [BasicObject(i*2) for i in range(1000)]
    search = [BasicObject(i*2) for i in range(1000)]
    # Ensure the search item is found in the data after the both keys
    # are applied.
    for i in range(len(data)):
        bin_search = BinarySearch(data,
                                  search[i],
                                  data_key=lambda x: x.operate(),
                                  search_key=lambda x: x.operate())
        assert bin_search.was_found
        assert bin_search.index == i
