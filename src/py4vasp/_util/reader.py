import py4vasp.exceptions as exception
import numpy as np


class Reader:
    "Helper class to deal with error handling of the array reading."

    def __init__(self, array):
        self._array = array
        self.shape = np.shape(array)

    def error_message(self, key, err):
        "We can overload this message in a subclass to make it more specific"
        return (
            "Error reading from the array, please check that the shape of the "
            "array is consistent with the access key."
        )

    def __getitem__(self, key):
        try:
            return self._array[key]
        except (ValueError, IndexError, TypeError) as err:
            raise exception.IncorrectUsage(self.error_message(key, err)) from err

    def __len__(self):
        return len(self._array)