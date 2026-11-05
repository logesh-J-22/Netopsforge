# Validation Engine (Pre-Flight Guardrails)

The **Validation** engine protects production network devices from incorrect configurations, syntax bugs, and conflicting VLAN assignments. It acts as an automated gatekeeper between human YAML files and switch hardware.

---

## How It Works

The engine runs a two-stage evaluation process before allowing any configuration to be deployed:

```
[ Input YAML Files ]
         │
         ▼
┌────────────────────────────────────────────────────────┐
│ Stage 1: Schema & Data Model Validation (models.py)   │
│ - Uses Pydantic to ensure all fields have correct data │
│ - Checks 802.1Q VLAN ranges (1 to 4094)                │
│ - Rejects Cisco legacy reserved VLANs (1002 - 1005)   │
│ - Enforces access vs trunk mode rules                 │
└────────────────────────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────────────────────────┐
│ Stage 2: Network State & Logic Checks                  │
│ (VLAN_and_Interface_validation.py)                    │
│ - Detects duplicate VLAN IDs or names within a switch │
│ - Identifies naming conflicts with existing live VLANs│
│ - Checks physical interface existence on the switch   │
│ - Verifies access/trunk VLAN references are valid     │
└────────────────────────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────────────────────────┐
│ Report Generation (orchestrator.py)                    │
│ - Severity categorization: ERROR, CONFLICT, WARNING,   │
│   CHANGE, OK                                           │
│ - Blocking rule: Any ERROR or CONFLICT halts deployment│
└────────────────────────────────────────────────────────┘
```

---

## File Breakdown

| File | Purpose |
| :--- | :--- |
| [`orchestrator.py`](file:///home/logee/Netopsforge/Validation/orchestrator.py) | **Main CLI coordinator.** Loads YAMLs, triggers Stage 1 & 2 validation, prints the formatted report, and either passes control to Ansible or aborts execution. |
| [`models.py`](file:///home/logee/Netopsforge/Validation/models.py) | **Pydantic models.** Defines `Vlan_structure` and `Vlan_interface_structure` with custom field validators for VLAN ranges and port modes. |
| [`VLAN_and_Interface_validation.py`](file:///home/logee/Netopsforge/Validation/VLAN_and_Interface_validation.py) | **Business logic checks.** Contains the validation functions that cross-examine input intent against normalized device states. |
| [`device_state_parser.py`](file:///home/logee/Netopsforge/Validation/device_state_parser.py) | **State normalizer.** Flattens raw device information from live switches or mock files into fast O(1) dictionary maps (`All_devices_VLAN_details`, `All_devices_Interface_Summary`). |
| [`validator.py`](file:///home/logee/Netopsforge/Validation/validator.py) | **Netmiko collector.** Gathers live operational state directly from switches via SSH (`show ip interface brief`, `show vlan brief`) when needed. |
| [`exception.py`](file:///home/logee/Netopsforge/Validation/exception.py) | **Custom error definitions.** Provides explicit errors like `ReservedVLANError` and `InvalidVLANError`. |

---

## Severity Levels

Issues found during validation are tagged with one of five severity levels:

1. **`ERROR`** *(Blocking)*: Critical syntax or data invalidity (e.g. non-numeric VLAN ID, VLAN out of range 1-4094, using reserved VLANs 1002-1005, or missing required fields).
2. **`CONFLICT`** *(Blocking)*: Logical collision (e.g. assigning the same VLAN ID twice with different names, or renaming an existing live VLAN).
3. **`WARNING`** *(Non-blocking)*: Potential operational concerns that do not strictly break execution (e.g. interface already configured with target parameters).
4. **`CHANGE`** *(Informational)*: Highlights net-new additions that will be applied to the device.
5. **`OK`** *(Informational)*: Verified checks that passed cleanly.

> [!IMPORTANT]
> If a report contains **any** `ERROR` or `CONFLICT`, `orchestrator.py` exits with status `1` and prevents Ansible from executing.

---

## CLI Usage

### Standalone Dry Run (Simulation)
Inspect configurations without running Ansible:
```bash
python3 Validation/orchestrator.py --dry-run
```

### Validate a Specific Inventory Folder
Test against different test suites (such as known bug scenarios):
```bash
python3 Validation/orchestrator.py --dry-run --vlan-dir Input/test_inventories/with_issues
```

### Custom File Paths
Specify custom individual YAML files:
```bash
python3 Validation/orchestrator.py --dry-run \
  -v Input/VLAN/VLANs.yaml \
  -i Input/VLAN/VLAN_interfaces.yaml
```

### Full Execution (Validate & Deploy)
Run pre-flight validation and automatically kick off the Ansible playbook if all checks pass:
```bash
python3 Validation/orchestrator.py
```
