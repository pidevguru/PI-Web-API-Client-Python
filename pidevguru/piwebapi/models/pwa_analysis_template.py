from pprint import pformat
from six import iteritems


class PWAAnalysisTemplate(object):
    swagger_types = {
        'analysis_rule_plug_in_name': 'str',
        'category_names': 'list[str]',
        'create_enabled': 'bool',
        'description': 'str',
        'group_id': 'int',
        'has_notification_template': 'bool',
        'has_target': 'bool',
        'id': 'str',
        'links': 'PWAAnalysisTemplateLinks',
        'name': 'str',
        'output_time': 'str',
        'path': 'str',
        'target_name': 'str',
        'time_rule_plug_in_name': 'str',
        'web_exception': 'PWAWebException',
        'web_id': 'str',
    }

    attribute_map = {
        'analysis_rule_plug_in_name': 'AnalysisRulePlugInName',
        'category_names': 'CategoryNames',
        'create_enabled': 'CreateEnabled',
        'description': 'Description',
        'group_id': 'GroupId',
        'has_notification_template': 'HasNotificationTemplate',
        'has_target': 'HasTarget',
        'id': 'Id',
        'links': 'Links',
        'name': 'Name',
        'output_time': 'OutputTime',
        'path': 'Path',
        'target_name': 'TargetName',
        'time_rule_plug_in_name': 'TimeRulePlugInName',
        'web_exception': 'WebException',
        'web_id': 'WebId',
    }

    def __init__(self, analysis_rule_plug_in_name=None, category_names=None, create_enabled=None, description=None, group_id=None, has_notification_template=None, has_target=None, id=None, links=None, name=None, output_time=None, path=None, target_name=None, time_rule_plug_in_name=None, web_exception=None, web_id=None):

        self._analysis_rule_plug_in_name = None
        self._category_names = None
        self._create_enabled = None
        self._description = None
        self._group_id = None
        self._has_notification_template = None
        self._has_target = None
        self._id = None
        self._links = None
        self._name = None
        self._output_time = None
        self._path = None
        self._target_name = None
        self._time_rule_plug_in_name = None
        self._web_exception = None
        self._web_id = None

        if analysis_rule_plug_in_name is not None:
            self.analysis_rule_plug_in_name = analysis_rule_plug_in_name
        if category_names is not None:
            self.category_names = category_names
        if create_enabled is not None:
            self.create_enabled = create_enabled
        if description is not None:
            self.description = description
        if group_id is not None:
            self.group_id = group_id
        if has_notification_template is not None:
            self.has_notification_template = has_notification_template
        if has_target is not None:
            self.has_target = has_target
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if output_time is not None:
            self.output_time = output_time
        if path is not None:
            self.path = path
        if target_name is not None:
            self.target_name = target_name
        if time_rule_plug_in_name is not None:
            self.time_rule_plug_in_name = time_rule_plug_in_name
        if web_exception is not None:
            self.web_exception = web_exception
        if web_id is not None:
            self.web_id = web_id

    @property
    def analysis_rule_plug_in_name(self):
        return self._analysis_rule_plug_in_name

    @analysis_rule_plug_in_name.setter
    def analysis_rule_plug_in_name(self, analysis_rule_plug_in_name):
        self._analysis_rule_plug_in_name = analysis_rule_plug_in_name

    @property
    def category_names(self):
        return self._category_names

    @category_names.setter
    def category_names(self, category_names):
        self._category_names = category_names

    @property
    def create_enabled(self):
        return self._create_enabled

    @create_enabled.setter
    def create_enabled(self, create_enabled):
        self._create_enabled = create_enabled

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        self._group_id = group_id

    @property
    def has_notification_template(self):
        return self._has_notification_template

    @has_notification_template.setter
    def has_notification_template(self, has_notification_template):
        self._has_notification_template = has_notification_template

    @property
    def has_target(self):
        return self._has_target

    @has_target.setter
    def has_target(self, has_target):
        self._has_target = has_target

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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
    def output_time(self):
        return self._output_time

    @output_time.setter
    def output_time(self, output_time):
        self._output_time = output_time

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def target_name(self):
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        self._target_name = target_name

    @property
    def time_rule_plug_in_name(self):
        return self._time_rule_plug_in_name

    @time_rule_plug_in_name.setter
    def time_rule_plug_in_name(self, time_rule_plug_in_name):
        self._time_rule_plug_in_name = time_rule_plug_in_name

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
        if not isinstance(other, PWAAnalysisTemplate):
            return False
        return self.__dict__ == other.__dict__

