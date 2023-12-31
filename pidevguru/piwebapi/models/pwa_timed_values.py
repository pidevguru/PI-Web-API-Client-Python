from pprint import pformat
from six import iteritems


class PWATimedValues(object):
    swagger_types = {
        'items': 'list[PWATimedValue]',
        'units_abbreviation': 'str',
        'web_exception': 'PWAWebException',
    }

    attribute_map = {
        'items': 'Items',
        'units_abbreviation': 'UnitsAbbreviation',
        'web_exception': 'WebException',
    }

    def __init__(self, items=None, units_abbreviation=None, web_exception=None):

        self._items = None
        self._units_abbreviation = None
        self._web_exception = None

        if items is not None:
            self.items = items
        if units_abbreviation is not None:
            self.units_abbreviation = units_abbreviation
        if web_exception is not None:
            self.web_exception = web_exception

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    @property
    def units_abbreviation(self):
        return self._units_abbreviation

    @units_abbreviation.setter
    def units_abbreviation(self, units_abbreviation):
        self._units_abbreviation = units_abbreviation

    @property
    def web_exception(self):
        return self._web_exception

    @web_exception.setter
    def web_exception(self, web_exception):
        self._web_exception = web_exception

    def to_dict(self):
        result = {}
        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        return result

    def to_str(self):
        return pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __ne__(self, other):
        return not self == other

    def __eq__(self, other):
        if not isinstance(other, PWATimedValues):
            return False
        return self.__dict__ == other.__dict__

