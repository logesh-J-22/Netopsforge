def expand_interfaces(interface_list):
    """
    Expands comma-separated interface names in a list of interface dictionaries
    into individual interface entries.

    Example:
      Input:  [{'name': 'Gi1/0/1, Gi1/0/2', 'mode': 'access', 'access_vlan': 10}]
      Output: [{'name': 'Gi1/0/1', 'mode': 'access', 'access_vlan': 10},
               {'name': 'Gi1/0/2', 'mode': 'access', 'access_vlan': 10}]
    """
    print(interface_list)
    if not interface_list or not isinstance(interface_list, list):
        return []

    result = []
    for item in interface_list:
        if not isinstance(item, dict):
            result.append(item)
            continue

        raw_name = item.get("name")
        if not raw_name:
            result.append(item)
            continue

        # Split comma-separated interface names
        names = [n.strip() for n in str(raw_name).split(",") if n.strip()]
        if not names:
            result.append(item)
            continue

        for name in names:
            new_item = dict(item)
            new_item["name"] = name
            result.append(new_item)

    return result


class FilterModule(object):
    def filters(self):
        return {
            "expand_interfaces": expand_interfaces
        }
