from pprint import pformat
from six import iteritems


class PWAAttributeTrait(object):
    swagger_types = {
        'abbreviation': 'str',
        'allow_child_attributes': 'bool',
        'allow_duplicates': 'bool',
        'is_allowed_on_root_attribute': 'bool',
        'is_type_inherited': 'bool',
        'is_u_o_m_inherited': 'bool',
        'links': 'PWAAttributeTraitLinks',
        'name': 'str',
        'require_numeric': 'bool',
        'require_string': 'bool',
        'web_exception': 'PWAWebException',
    }

    attribute_map = {
        'abbreviation': 'Abbreviation',
        'allow_child_attributes': 'AllowChildAttributes',
        'allow_duplicates': 'AllowDuplicates',
        'is_allowed_on_root_attribute': 'IsAllowedOnRootAttribute',
        'is_type_inherited': 'IsTypeInherited',
        'is_u_o_m_inherited': 'IsUOMInherited',
        'links': 'Links',
        'name': 'Name',
        'require_numeric': 'RequireNumeric',
        'require_string': 'RequireString',
        'web_exception': 'WebException',
    }

    def __init__(self, abbreviation=None, allow_child_attributes=None, allow_duplicates=None, is_allowed_on_root_attribute=None, is_type_inherited=None, is_u_o_m_inherited=None, links=None, name=None, require_numeric=None, require_string=None, web_exception=None):

        self._abbreviation = None
        self._allow_child_attributes = None
        self._allow_duplicates = None
        self._is_allowed_on_root_attribute = None
        self._is_type_inherited = None
        self._is_u_o_m_inherited = None
        self._links = None
        self._name = None
        self._require_numeric = None
        self._require_string = None
        self._web_exception = None

        if abbreviation is not None:
            self.abbreviation = abbreviation
        if allow_child_attributes is not None:
            self.allow_child_attributes = allow_child_attributes
        if allow_duplicates is not None:
            self.allow_duplicates = allow_duplicates
        if is_allowed_on_root_attribute is not None:
            self.is_allowed_on_root_attribute = is_allowed_on_root_attribute
        if is_type_inherited is not None:
            self.is_type_inherited = is_type_inherited
        if is_u_o_m_inherited is not None:
            self.is_u_o_m_inherited = is_u_o_m_inherited
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if require_numeric is not None:
            self.require_numeric = require_numeric
        if require_string is not None:
            self.require_string = require_string
        if web_exception is not None:
            self.web_exception = web_exception

    @property
    def abbreviation(self):
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        self._abbreviation = abbreviation

    @property
    def allow_child_attributes(self):
        return self._allow_child_attributes

    @allow_child_attributes.setter
    def allow_child_attributes(self, allow_child_attributes):
        self._allow_child_attributes = allow_child_attributes

    @property
    def allow_duplicates(self):
        return self._allow_duplicates

    @allow_duplicates.setter
    def allow_duplicates(self, allow_duplicates):
        self._allow_duplicates = allow_duplicates

    @property
    def is_allowed_on_root_attribute(self):
        return self._is_allowed_on_root_attribute

    @is_allowed_on_root_attribute.setter
    def is_allowed_on_root_attribute(self, is_allowed_on_root_attribute):
        self._is_allowed_on_root_attribute = is_allowed_on_root_attribute

    @property
    def is_type_inherited(self):
        return self._is_type_inherited

    @is_type_inherited.setter
    def is_type_inherited(self, is_type_inherited):
        self._is_type_inherited = is_type_inherited

    @property
    def is_u_o_m_inherited(self):
        return self._is_u_o_m_inherited

    @is_u_o_m_inherited.setter
    def is_u_o_m_inherited(self, is_u_o_m_inherited):
        self._is_u_o_m_inherited = is_u_o_m_inherited

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
    def require_numeric(self):
        return self._require_numeric

    @require_numeric.setter
    def require_numeric(self, require_numeric):
        self._require_numeric = require_numeric

    @property
    def require_string(self):
        return self._require_string

    @require_string.setter
    def require_string(self, require_string):
        self._require_string = require_string

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
        if not isinstance(other, PWAAttributeTrait):
            return False
        return self.__dict__ == other.__dict__

