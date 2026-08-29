import yaml
from pathlib import Path
from pprint import pprint
from models import Vlan_interface_structure, Vlan_structure
from pydantic import ValidationError

def load_yaml(path):
    with open(path,'r') as f:
        return yaml.safe_load(f)



def main():

    Vlans_file_path=Path(__file__).resolve().parent.parent.joinpath("Ansible/Inventory/group_vars/VLAN/VLANs.yaml")
    Vlan_interface_file_path=Path(__file__).resolve().parent.parent.joinpath("Ansible/Inventory/group_vars/VLAN/VLAN_interfaces.yaml")




    vlans=load_yaml(Vlans_file_path)
    Vlans_interface= load_yaml(Vlan_interface_file_path)


    for each_vlan in vlans["VLANS"]["R1"]:
        # print(each_vlan)
        try: 
            validate_object=Vlan_structure(id=each_vlan["id"],
                                    name=each_vlan["name"])
        except ValidationError as e:
            number_of_error=1
            for error in e.errors():
                print(f"###########################  Error No.{number_of_error}   ###########################")
                print("Error Type:",error["type"])
                print("Error Feild:",error["loc"][0])
                print("Error Message:",error["msg"])
                print("###############################################################")
                number_of_error+=1
    for each_interface in Vlans_interface["interfaces"]["R1"]:
        try: 
            validate_object=Vlan_interface_structure(name=each_interface["name"],
                                        description=each_interface["description"],
                                        mode=each_interface["mode"],
                                        access_vlan=each_interface.get("access_vlan"),
                                        enable=each_interface["enable"],
                                        allowed_vlans=each_interface.get("allowed_vlans"),
                                        native_vlan=each_interface.get("native_vlan"))
        except ValidationError as e:
            number_of_error=1
            for error in e.errors():
                print(f"###########################  Error No.{number_of_error}   ###########################")
                print("Error Type:",error["type"])
                print("Error Feild:",error["loc"])
                print("Error Message:",error["msg"])
                print("Error occured at :", error.get("input"))
                number_of_error+=1


if __name__=="__main__":
    main()
