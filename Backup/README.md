# Backup & State Archival

This directory provides automated collection, comparison, and timestamped archiving of Cisco switch configurations.

---

## How It Works

1. **Inventory Discovery**: [`main.py`](file:///home/logee/Netopsforge/Backup/main.py) reads switch connection details directly from `Ansible/Inventory/Inventory.yaml` using `ansible-inventory --list`.
2. **SSH Connection**: Uses **Netmiko** to connect to each switch (`cisco_ios`) and runs `show running-config`.
3. **Change Detection (Diffing)**:
   * Looks for the most recent backup file in `Backup_files/<hostname>/`.
   * Compares the current live configuration against the previous backup using Python's `difflib.unified_diff`.
4. **Smart Saving**:
   * **First time backup**: Saves the full running configuration.
   * **If changed**: Prints the exact line-by-line diff and saves a new timestamped file (`DD-MM-YYYY_HH-MM-SS.cfg`).
   * **If unchanged**: Skips saving to avoid cluttering the repository with duplicate copies.

---

## How to Run

Execute the backup script directly from the project root:
```bash
python3 Backup/main.py
```

The archived configuration files will be stored under:
```text
Backup_files/<hostname>/<timestamp>.cfg
```

