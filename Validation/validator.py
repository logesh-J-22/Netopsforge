from pathlib import Path
from orchestrator import load_yaml
from pprint import pprint
from netmiko import Netmiko
import subprocess
import json

INVENTORY_VALIDATOR=Path(__file__).resolve().parent.parent.joinpath("Ansible/Inventory/Inventory.yaml")
INVENTORY_VLAN=Path(__file__).resolve().parent.parent.joinpath("Ansible/Inventory/group_vars/VLAN/VLANs.yaml")

def get_device_list_from_INVENTORY():
    router_list=[]
    Inventory_details=subprocess.run(
        ["ansible-inventory","-i",INVENTORY_VALIDATOR,"--list"],
        capture_output=True,
        check=True
    )
    Inventory_details=json.loads(Inventory_details.stdout)
    # pprint(Inventory_details)
    if Inventory_details.get("_meta",{}).get("hostvars",{}) != None:
        for hostname,variables in Inventory_details.get("_meta",{}).get("hostvars",{}).items():
            router_list.append(
                {
                    "hostname": hostname,
                    "host": variables["ansible_host"],
                    "username": variables.get("ansible_user"),
                    "password": variables.get("ansible_password")
                }
            )
    # print(router_list)
    return router_list
    
    

def Required_device_details():
    print("Gathering the device info")
    router_list=get_device_list_from_INVENTORY()
    # print(router_list)
    for router in router_list:
        device={
                "device_type":"cisco_ios",
                "host":router["host"],
                "username":router["username"],
                "password":router["password"]
                }
        device_access=Netmiko(**device)
        print(f"Connected to the device {router["host"]}")
        device_interfaces_details=device_access.send_command("show ip interface brief",use_genie=True)
        device_vlan_details=device_access.send_command("show vlan brief",use_textfsm=True)

        device_interfaces=list(device_interfaces_details.get("interface").keys())
        device_VLAN_and_interface_detail={
            item["vlan_id"]: {item["vlan_name"]:item["interfaces"]}
            for item in device_vlan_details
        }
        # pprint(device_interfaces) # has the interfaces in the router
        # pprint(device_VLAN_and_interface_detail) # vlans and the respective interfaces that are configured in it.
        return device_interfaces, device_VLAN_and_interface_detail
        


def vlan_exist(device_VLAN_and_interface_detail):
    VLAN_YAML_Contents=load_yaml(INVENTORY_VLAN)
    # pprint(VLAN_YAML_Contents)
    existing_VLAN=[]
    for router in VLAN_YAML_Contents['VLANS'].values():
        for vlan in router:
                # print(str(vlan['id']))
                if str(vlan['id']) in list(VLAN_YAML_Contents['VLANS'].values())[0]:
                    
                    existing_VLAN.append(vlan)
                    continue
                else: 
                    print(f"{vlan['id']} is not yet created")
                    print(f"{vlan['id']} is getting skipped without being exceuted....")
    print(existing_VLAN)
   
    # print(VLAN_YAML_Contents['VLANS'].keys())
    
    



def main():
    device_interfaces, device_VLAN_and_interface_detail=Required_device_details()
    vlan_exist(device_VLAN_and_interface_detail)
    

if __name__=="__main__":
    main()
