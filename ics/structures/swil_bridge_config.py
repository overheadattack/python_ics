# This file was auto generated; Do not modify, if you value your sanity!
import ctypes
import enum



class config(ctypes.Structure):
    _pack_ = 2
    _fields_ = [
        ('can_id', ctypes.c_uint, 29),
        ('can_id_isExtended', ctypes.c_uint, 1),
        ('tcp_port', ctypes.c_uint16),
        ('manager_onboard_external', ctypes.c_uint, 1),
        ('reserved', ctypes.c_uint, 18),
    ]



class swil_bridge_config(ctypes.Union):
    _pack_ = 2
    _fields_ = [
        ('dword', ctypes.c_uint64),
        ('config', config),
    ]


SWILBridgeConfig = swil_bridge_config

