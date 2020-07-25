# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentTerminalLocation:

    swagger_types = {
    
        'contact_address': 'PaymentTerminalContactAddress',
        'default_configuration': 'PaymentTerminalConfiguration',
        'delivery_address': 'PaymentTerminalAddress',
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'state': 'PaymentTerminalLocationState',
        'version': 'int',
    }

    attribute_map = {
        'contact_address': 'contactAddress','default_configuration': 'defaultConfiguration','delivery_address': 'deliveryAddress','id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','planned_purge_date': 'plannedPurgeDate','state': 'state','version': 'version',
    }

    
    _contact_address = None
    _default_configuration = None
    _delivery_address = None
    _id = None
    _linked_space_id = None
    _name = None
    _planned_purge_date = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.contact_address = kwargs.get('contact_address', None)
        self.default_configuration = kwargs.get('default_configuration', None)
        self.delivery_address = kwargs.get('delivery_address', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def contact_address(self):
        """Gets the contact_address of this PaymentTerminalLocation.

            

        :return: The contact_address of this PaymentTerminalLocation.
        :rtype: PaymentTerminalContactAddress
        """
        return self._contact_address

    @contact_address.setter
    def contact_address(self, contact_address):
        """Sets the contact_address of this PaymentTerminalLocation.

            

        :param contact_address: The contact_address of this PaymentTerminalLocation.
        :type: PaymentTerminalContactAddress
        """

        self._contact_address = contact_address
    
    @property
    def default_configuration(self):
        """Gets the default_configuration of this PaymentTerminalLocation.

            

        :return: The default_configuration of this PaymentTerminalLocation.
        :rtype: PaymentTerminalConfiguration
        """
        return self._default_configuration

    @default_configuration.setter
    def default_configuration(self, default_configuration):
        """Sets the default_configuration of this PaymentTerminalLocation.

            

        :param default_configuration: The default_configuration of this PaymentTerminalLocation.
        :type: PaymentTerminalConfiguration
        """

        self._default_configuration = default_configuration
    
    @property
    def delivery_address(self):
        """Gets the delivery_address of this PaymentTerminalLocation.

            

        :return: The delivery_address of this PaymentTerminalLocation.
        :rtype: PaymentTerminalAddress
        """
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, delivery_address):
        """Sets the delivery_address of this PaymentTerminalLocation.

            

        :param delivery_address: The delivery_address of this PaymentTerminalLocation.
        :type: PaymentTerminalAddress
        """

        self._delivery_address = delivery_address
    
    @property
    def id(self):
        """Gets the id of this PaymentTerminalLocation.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentTerminalLocation.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentTerminalLocation.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentTerminalLocation.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentTerminalLocation.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this PaymentTerminalLocation.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentTerminalLocation.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this PaymentTerminalLocation.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this PaymentTerminalLocation.

            The terminal location name is used internally to identify the terminal in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this PaymentTerminalLocation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentTerminalLocation.

            The terminal location name is used internally to identify the terminal in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this PaymentTerminalLocation.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this PaymentTerminalLocation.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this PaymentTerminalLocation.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this PaymentTerminalLocation.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this PaymentTerminalLocation.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this PaymentTerminalLocation.

            

        :return: The state of this PaymentTerminalLocation.
        :rtype: PaymentTerminalLocationState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentTerminalLocation.

            

        :param state: The state of this PaymentTerminalLocation.
        :type: PaymentTerminalLocationState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this PaymentTerminalLocation.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentTerminalLocation.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentTerminalLocation.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentTerminalLocation.
        :type: int
        """

        self._version = version
    

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
            elif isinstance(value, Enum):
                result[attr] = value.value
            else:
                result[attr] = value
        if issubclass(PaymentTerminalLocation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentTerminalLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
