from pprint import pformat
from six import iteritems


class PWASecurityMappingLinks(object):
    swagger_types = {
        'asset_server': 'str',
        'security': 'str',
        'security_entries': 'str',
        'security_identity': 'str',
    }

    attribute_map = {
        'asset_server': 'AssetServer',
        'security': 'Security',
        'security_entries': 'SecurityEntries',
        'security_identity': 'SecurityIdentity',
    }

    def __init__(self, asset_server=None, security=None, security_entries=None, security_identity=None):

        self._asset_server = None
        self._security = None
        self._security_entries = None
        self._security_identity = None

        if asset_server is not None:
            self.asset_server = asset_server
        if security is not None:
            self.security = security
        if security_entries is not None:
            self.security_entries = security_entries
        if security_identity is not None:
            self.security_identity = security_identity

    @property
    def asset_server(self):
        return self._asset_server

    @asset_server.setter
    def asset_server(self, asset_server):
        self._asset_server = asset_server

    @property
    def security(self):
        return self._security

    @security.setter
    def security(self, security):
        self._security = security

    @property
    def security_entries(self):
        return self._security_entries

    @security_entries.setter
    def security_entries(self, security_entries):
        self._security_entries = security_entries

    @property
    def security_identity(self):
        return self._security_identity

    @security_identity.setter
    def security_identity(self, security_identity):
        self._security_identity = security_identity

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
        if not isinstance(other, PWASecurityMappingLinks):
            return False
        return self.__dict__ == other.__dict__

