from netmiko import Netmiko
import subprocess
from pathlib import Path
from datetime import datetime
import json
import difflib

INVENTORY=Path(__file__).resolve().parent.parent.joinpath("Ansible/Inventory/Inventory.yaml")
Backup_dir=Path(__file__).resolve().parent.parent.joinpath("Backup_files")


def get_inventory():

    Inventory_result=subprocess.run(
        ["ansible-inventory","-i",INVENTORY,"--list"],
        capture_output= True,
        text= True,
        check=True
    )
    
    return json.loads(Inventory_result.stdout)


def get_routers(Inventory):
    hostvars=Inventory.get("_meta",{}).get("hostvars",{})
    routers=[]
    for hostname,variables in hostvars.items():
        if "ansible_host" not in variables:
            continue
        routers.append(
            {
              "hostname": hostname,
              "host": variables["ansible_host"],
              "username": variables.get("ansible_user"),
              "password": variables.get("ansible_password")
            }
        )
    return routers

def backup(router):

    device={"device_type":"cisco_ios",
            "host":router["host"],
            "username":router["username"],
            "password":router["password"]
            }
    device_access=Netmiko(**device)
    print(f"Connected to the {router["hostname"] } successfully ")
    running_config=device_access.send_command("show running-config")
    timestamp=datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    router_dir=Backup_dir / router["hostname"]
    router_dir.mkdir(parents=True,exist_ok=True)
    diff=check_and_update(router_dir,running_config)
    if diff:
        print(f"Config has changed for {router["hostname"]}")
        print("\n".join(diff))
        backup_file=router_dir / f"{timestamp}.cfg"
        backup_file.write_text(running_config)
        print(f"Backup file for {router["hostname"]} saved successfully under {backup_file}!!!!")
    else:
        print(f"Config has not changed for {router["hostname"]}")



def check_and_update(router_dir,current_config):
    files= [f for f in router_dir.iterdir() if f.is_file()]
    latest_file=max(files,key=lambda f: f.stat().st_ctime)
    with open(latest_file) as file:
        previous_config=file.read()
    diff=list(difflib.unified_diff(
        previous_config.splitlines(),
        current_config.splitlines(),
        fromfile="previous",
        tofile="current",
        lineterm=""
    ))
    return diff
    



def main():
    Inventory=get_inventory()
    routers=get_routers(Inventory)
    for router in routers:
        backup(router)

if __name__=="__main__":
    main()