from pprint import pformat
from six import iteritems


class PWAPointAttributeLinks(object):
    swagger_types = {
        'point': 'str',
    }

    attribute_map = {
        'point': 'Point',
    }

    def __init__(self, point=None):

        self._point = None

        if point is not None:
            self.point = point

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, point):
        self._point = point

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
        if not isinstance(other, PWAPointAttributeLinks):
            return False
        return self.__dict__ == other.__dict__

