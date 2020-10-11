

class BinarySearch(object):
    '''Does a binary search.

        To determine if the search item was found, use the `was_found`
        method. If the item was found then use `index` to get the
        location it was found at. If the item was not found use `index`
        to get the location that the item should be inserted in order
        to keep the data in sorted order.

        Note: `was_found` should always be called before accessing
        `index` to determine if it is the found location, or the
        insertion location.

        Properties:
            index (int): The index the search item was found if it was,
                otherwise the index in which to insert the item to keep
                the data in sorted order.

        Methods:
            was_found() -> bool: Return if the search item was found
                       
    '''


    def __init__(self,
                data,
                search,
                data_key = lambda x: x,
                search_key = lambda x: x) -> None:
        '''Preform the search and store the index calculated.
            Args:
                data: The data to be searched.
                search: The item being searched for.
                data_key (function): The key to access the value from
                    the current item in data to be compared.
                search_key (function): They key to access the value from
                    the search item to be compared.

            Returns:
                None:
        '''
        self.__index = self.__search(data, search, data_key, search_key)


    @property
    def index(self) -> int:
        '''The index the search item was found if it was,
            otherwise the index in which to insert the item to keep
            the data in sorted order.

            `was_found` should always be called before accessing index.

            Returns:
                int: The index the item was found, or should be inserted
                    at.
        '''
        # Return the index if it is positive (element was found), if
        # it is negitive, then the index is the location in which the
        # element should be inserted. To cover if the item should be
        # inserted at index 0, since a positve 0 and negative 0 do not
        # exist, the insertion index was shifted in the negative
        # direction by 1, the 1 is now being added here to shift it
        # back up so that the insertion index is correct once the
        # absolute value is taken.
        return self.__index if self.__index >= 0 else abs(self.__index + 1)


    def was_found(self) -> bool:
        '''Return if the search item was found in the data.

            Returns:
                bool: If the item was found or not.
        '''
        return self.__index >= 0


    @staticmethod
    def __search(data, search, data_key, search_key) -> int:
        '''Does a binary search.

            Args:
                data: The data to be searched.
                search: The item being searched for.
                data_key (function): The key to access the value from
                    the current item in data to be compared.
                search_key (function): They key to access the value from
                    the search item to be compared.

            Returns:
                int: The index in which the search item is located in
                    data if found, or the negative value of where
                    the item should be inserted -1 to keep the data in
                    order if not found.

            Raises:
                TypeError: if the `search` term is None
        '''
        if data is None:
            return -1
        if search is None:
            raise TypeError("`search` must not be None")

        left: int = 0
        right: int = len(data)
        while(left != right):

            mid: int = left + (right - left) // 2
            # Get the search term to compare from the search key.
            s = search_key(search)
            # Get the data term to compare from the data key.
            d = data_key(data[mid])

            if s < d   : right = mid
            elif s > d : left  = mid + 1
            else       : return  mid  

        # Return the location the element should be inserted to keep
        # the data in order. This can be done, because at this point
        # the right and left values are the same. The 1 is subtracted
        # from the negative left value to cover if the item should be
        # inserted at index 0, since a positve 0 and negative 0 do not
        # exist, every index needs to be shifted in the negative
        # direction by 1 for the insertion index. This is later shifted
        # back when getting the index. 
        return (-left) - 1


    def __str__(self) -> str:
        return "BinarySearch('{}')".format(str(self.__index)) 
