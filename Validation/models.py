from pydantic import BaseModel, model_validator, field_validator
from enum import Enum
from exception import InvalidVLANError, ReservedVLANError


class Vlan_structure(BaseModel):
        id: int
        name: str
        @field_validator("id")
        @classmethod
        def validate_vlan_id(cls, vlan: int):
            if 1002 <= vlan <= 1005:
                raise ReservedVLANError("VLANs 1002 to 1005 are reserved for legacy purposre please use other VLANs")
            elif not (1 <= vlan <= 4094):
                raise InvalidVLANError(f"{vlan} is a invlaid VLAN and it's not in the range 1-4094")
            return vlan

class Vlan_modes(str,Enum):
    ACCESS= "access"
    TRUNK= "trunk"

class Vlan_interface_structure(BaseModel):
    name: str
    description: str
    mode: Vlan_modes
    access_vlan: int | None = None 
    allowed_vlans: list[int] | None = None
    native_vlan: int | None = None
    enable: bool

    

    @field_validator("access_vlan", "allowed_vlans")
    @classmethod
    def validate_vlan_range(cls, value):
        if value is None:
            return value
        vlans = value if isinstance(value, list) else [value]
        for vlan in vlans:
            if vlan is not None:
                if 1002 <= vlan <= 1005:
                    raise ReservedVLANError("VLANs 1002 to 1005 are reserved for legacy purposre please use other VLANs")
                elif not (1 <= vlan <= 4094):
                    raise InvalidVLANError(f"{vlan} is a invlaid VLAN and it's not in the range 1-4094")
        return value
        
    @model_validator(mode="after")
    def validate_mode_fields(self):
        if self.mode==Vlan_modes.ACCESS:
            if self.access_vlan== None:
                raise ValueError("Access Vlan detail is required for the mode access ")
            if self.allowed_vlans != None:
                raise ValueError("VLAN access mode doesn't have any allowed vlans feilds ")
            if self.native_vlan != None:
                raise ValueError("VLAN access mode doesn't allow native vlans ")
        else:
            if  self.allowed_vlans == None:
                raise ValueError("Allowed Vlans detail is required for the mode trunk ")
            if  self.native_vlan == None:
                raise ValueError("Native Vlans detail is required for the mode trunk ")
            if  self.access_vlan != None:
                raise ValueError("Trunk mode doesn't support access vlans ")
        return self

