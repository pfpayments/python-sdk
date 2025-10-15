# coding: utf-8
from enum import Enum, unique


@unique
class SubscriptionChargeType(Enum):
    
    MANUAL = "MANUAL"
    AUTOMATIC = "AUTOMATIC"

