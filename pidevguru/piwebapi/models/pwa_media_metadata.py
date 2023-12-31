from pprint import pformat
from six import iteritems


class PWAMediaMetadata(object):
    swagger_types = {
        'author': 'str',
        'change_date': 'str',
        'description': 'str',
        'links': 'PWAMediaMetadataLinks',
        'name': 'str',
        'size': 'float',
        'web_exception': 'PWAWebException',
    }

    attribute_map = {
        'author': 'Author',
        'change_date': 'ChangeDate',
        'description': 'Description',
        'links': 'Links',
        'name': 'Name',
        'size': 'Size',
        'web_exception': 'WebException',
    }

    def __init__(self, author=None, change_date=None, description=None, links=None, name=None, size=None, web_exception=None):

        self._author = None
        self._change_date = None
        self._description = None
        self._links = None
        self._name = None
        self._size = None
        self._web_exception = None

        if author is not None:
            self.author = author
        if change_date is not None:
            self.change_date = change_date
        if description is not None:
            self.description = description
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if web_exception is not None:
            self.web_exception = web_exception

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def change_date(self):
        return self._change_date

    @change_date.setter
    def change_date(self, change_date):
        self._change_date = change_date

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

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
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

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
        if not isinstance(other, PWAMediaMetadata):
            return False
        return self.__dict__ == other.__dict__

