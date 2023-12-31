from pprint import pformat
from six import iteritems


class PWASystemLanding(object):
    swagger_types = {
        'links': 'PWASystemLandingLinks',
        'product_title': 'str',
        'product_version': 'str',
        'web_exception': 'PWAWebException',
    }

    attribute_map = {
        'links': 'Links',
        'product_title': 'ProductTitle',
        'product_version': 'ProductVersion',
        'web_exception': 'WebException',
    }

    def __init__(self, links=None, product_title=None, product_version=None, web_exception=None):

        self._links = None
        self._product_title = None
        self._product_version = None
        self._web_exception = None

        if links is not None:
            self.links = links
        if product_title is not None:
            self.product_title = product_title
        if product_version is not None:
            self.product_version = product_version
        if web_exception is not None:
            self.web_exception = web_exception

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, links):
        self._links = links

    @property
    def product_title(self):
        return self._product_title

    @product_title.setter
    def product_title(self, product_title):
        self._product_title = product_title

    @property
    def product_version(self):
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        self._product_version = product_version

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
        if not isinstance(other, PWASystemLanding):
            return False
        return self.__dict__ == other.__dict__

