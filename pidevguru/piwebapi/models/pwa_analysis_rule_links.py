from pprint import pformat
from six import iteritems


class PWAAnalysisRuleLinks(object):
    swagger_types = {
        'analysis': 'str',
        'analysis_rules': 'str',
        'analysis_template': 'str',
        'parent': 'str',
        'plug_in': 'str',
    }

    attribute_map = {
        'analysis': 'Analysis',
        'analysis_rules': 'AnalysisRules',
        'analysis_template': 'AnalysisTemplate',
        'parent': 'Parent',
        'plug_in': 'PlugIn',
    }

    def __init__(self, analysis=None, analysis_rules=None, analysis_template=None, parent=None, plug_in=None):

        self._analysis = None
        self._analysis_rules = None
        self._analysis_template = None
        self._parent = None
        self._plug_in = None

        if analysis is not None:
            self.analysis = analysis
        if analysis_rules is not None:
            self.analysis_rules = analysis_rules
        if analysis_template is not None:
            self.analysis_template = analysis_template
        if parent is not None:
            self.parent = parent
        if plug_in is not None:
            self.plug_in = plug_in

    @property
    def analysis(self):
        return self._analysis

    @analysis.setter
    def analysis(self, analysis):
        self._analysis = analysis

    @property
    def analysis_rules(self):
        return self._analysis_rules

    @analysis_rules.setter
    def analysis_rules(self, analysis_rules):
        self._analysis_rules = analysis_rules

    @property
    def analysis_template(self):
        return self._analysis_template

    @analysis_template.setter
    def analysis_template(self, analysis_template):
        self._analysis_template = analysis_template

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def plug_in(self):
        return self._plug_in

    @plug_in.setter
    def plug_in(self, plug_in):
        self._plug_in = plug_in

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
        if not isinstance(other, PWAAnalysisRuleLinks):
            return False
        return self.__dict__ == other.__dict__

