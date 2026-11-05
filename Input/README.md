# Input Specifications & Data Models

This directory contains declarative network intent defined in YAML. These files describe what the network *should* look like, which is then parsed by the validation engine and applied by Ansible.

---

## Directory Layout

* **`VLAN/`**: Production/active configuration files.
  * `VLANs.yaml`: VLAN IDs and names per switch.
  * `VLAN_interfaces.yaml`: Interface mode, port assignments, native VLANs, and descriptions.
* **`test_inventories/`**: Test datasets used to verify the validation pipeline:
  * `with_issues/`: Sample inventories with known syntax errors, duplicate IDs, and reserved VLANs.
  * `resolved/`: Cleaned versions of test inventories with all issues fixed.

---

## Schema Examples

### `VLANs.yaml`
```yaml
VLANS:
  R1:
    - id: 10
      name: Devops
    - id: 20
      name: Security
    - id: 30
      name: Netops
```

### `VLAN_interfaces.yaml`
Supports both single interfaces and comma-separated interface lists:

```yaml
interfaces:
  R1:
    # Access Port Example (multiple ports)
    - name: "Gi1/0/1, Gi1/0/2"
      description: "Devops Access Ports"
      mode: "access"
      access_vlan: 10
      enable: true

    # Trunk Port Example
    - name: "Gi1/0/24"
      description: "Uplink to Core"
      mode: "trunk"
      native_vlan: 99
      allowed_vlans: [10, 20, 30]
      enable: true
```

---

## Field Rules & Constraints
* **`id`**: Must be an integer between `1` and `4094`. Reserved VLANs `1002 - 1005` are rejected.
* **`mode`**: Must be either `access` or `trunk`.
* **Access Mode Rules**:
  * `access_vlan` is required.
  * `allowed_vlans` and `native_vlan` must NOT be specified.
* **Trunk Mode Rules**:
  * `allowed_vlans` and `native_vlan` are required.
  * `access_vlan` must NOT be specified.

