# Ansible Automation & Playbooks

This directory contains the Ansible playbooks, inventory configuration, and custom filter plugins used to deploy VLAN and interface configurations to Cisco IOS devices.

---

## Key Files

* **[`Playbook/VLAN.yaml`](file:///home/logee/Netopsforge/Ansible/Playbook/VLAN.yaml)**: The core deployment playbook.
  * **Pre-flight Check**: Runs `Validation/orchestrator.py --dry-run` as a `pre_task`. If validation detects blocking errors, the playbook fails immediately before touching any switches.
  * **VLAN Creation**: Uses `cisco.ios.ios_vlans` in `merged` mode.
  * **Access Ports**: Uses `cisco.ios.ios_l2_interfaces` to assign access VLANs.
  * **Trunk Ports**: Configures native and allowed VLANs on trunk interfaces.
  * **Interface Descriptions**: Uses `cisco.ios.ios_interfaces` to set port descriptions and admin status (`enabled: true/false`).
  * **Post-check Verification**: Parses `show vlan brief` using Network Text FSM (`ansible.netcommon.ntc_templates`) to display active VLAN state.

* **[`Inventory/Inventory.yaml`](file:///home/logee/Netopsforge/Ansible/Inventory/Inventory.yaml)**: Defines switch hosts, IP addresses, credentials, and connection types (`network_cli` for Cisco IOS).

* **[`filter_plugins/expand_interfaces.py`](file:///home/logee/Netopsforge/Ansible/filter_plugins/expand_interfaces.py)**:
  * A custom Ansible filter plugin.
  * Takes comma-separated interface strings (e.g. `'Gi1/0/1, Gi1/0/2'`) and expands them into individual entries in the loop.
  * Avoids repetitive YAML blocks for multiple ports sharing the same configuration.

---

## How to Run

### Direct Playbook Execution
Run the playbook against your inventory:
```bash
ansible-playbook -i Ansible/Inventory/Inventory.yaml Ansible/Playbook/VLAN.yaml
```

### Passing a Custom Input Directory
To run the playbook using a specific inventory directory:
```bash
ansible-playbook -i Ansible/Inventory/Inventory.yaml Ansible/Playbook/VLAN.yaml \
  -e "vlan_dir=$(pwd)/Input/test_inventories/resolved"
```

