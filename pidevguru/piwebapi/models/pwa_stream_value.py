from pprint import pformat
from six import iteritems


class PWAStreamValue(object):
    swagger_types = {
        'links': 'PWAStreamValueLinks',
        'name': 'str',
        'path': 'str',
        'value': 'PWATimedValue',
        'web_exception': 'PWAWebException',
        'web_id': 'str',
    }

    attribute_map = {
        'links': 'Links',
        'name': 'Name',
        'path': 'Path',
        'value': 'Value',
        'web_exception': 'WebException',
        'web_id': 'WebId',
    }

    def __init__(self, links=None, name=None, path=None, value=None, web_exception=None, web_id=None):

        self._links = None
        self._name = None
        self._path = None
        self._value = None
        self._web_exception = None
        self._web_id = None

        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if value is not None:
            self.value = value
        if web_exception is not None:
            self.web_exception = web_exception
        if web_id is not None:
            self.web_id = web_id

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, links):
        self._links = links

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def web_exception(self):
        return self._web_exception

    @web_exception.setter
    def web_exception(self, web_exception):
        self._web_exception = web_exception

    @property
    def web_id(self):
        return self._web_id

    @web_id.setter
    def web_id(self, web_id):
        self._web_id = web_id

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
        if not isinstance(other, PWAStreamValue):
            return False
        return self.__dict__ == other.__dict__

