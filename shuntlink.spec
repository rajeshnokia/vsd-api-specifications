{
    "attributes": [
        {
            "allowed_chars": "UUID supported characters",
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The ID of the shunted VLAN from the first NSG of the redundant gateway group.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "VLANPeer1ID",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "VLAN Peer 1"
        },
        {
            "allowed_chars": "UUID supported characters.",
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The ID of the shunted VLAN from the second NSG of the redundant gateway group.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "VLANPeer2ID",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "VLAN Peer 2"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "null",
            "deprecated": false,
            "description": "Extra information entered by the operator to define the Shunt Link.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "description",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Description"
        },
        {
            "allowed_chars": "UUID supported characters.",
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "null",
            "deprecated": false,
            "description": "The ID of the first NSG of the redundant gateway group part of this Shunt Link.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "gatewayPeer1ID",
            "orderable": true,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Gateway Peer 1"
        },
        {
            "allowed_chars": "UUID supported characters.",
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "null",
            "deprecated": false,
            "description": "The ID of the second NSG of the redundant gateway group part of this Shunt Link.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "gatewayPeer2ID",
            "orderable": true,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Gateway Peer 2"
        },
        {
            "allowed_chars": "Almost everything",
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "null",
            "deprecated": false,
            "description": "The name auto-generated by VSD and given to a newly created Shunt Link.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "name",
            "orderable": true,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Name"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The IP address of the first peer of the Shunt Link.",
            "exposed": true,
            "filterable": false,
            "format": "ipv4",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "peer1IPAddress",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": true,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Peer 1 IP Address"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The subnet given to the first peer of the Shunt Link.",
            "exposed": true,
            "filterable": false,
            "format": "ipv4",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "peer1Subnet",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": true,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Peer 1 Subnet"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The IP address of the second peer of the Shunt Link.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "peer2IPAddress",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": true,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Peer 2 IP Address"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The subnet on the second peer of the Shunt Link.",
            "exposed": true,
            "filterable": false,
            "format": "ipv4",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "peer2Subnet",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": true,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Peer 2 Subnet"
        }
    ],
    "children": [
        {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": true,
            "delete": false,
            "deprecated": null,
            "get": true,
            "relationship": "child",
            "rest_name": "alarm",
            "update": false
        }
    ],
    "model": {
        "allowed_job_commands": null,
        "create": null,
        "delete": true,
        "description": "A shunt link represents an alliance of uplink interface resources between two NSGs belonging to a Redundant Group.  An operator specifies which network port-VLAN from each NSG peers to be considered as shunted together so that control uplinks from each NSG may be used by the other.",
        "entity_name": "ShuntLink",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "nsg",
        "resource_name": "shuntlinks",
        "rest_name": "shuntlink",
        "root": null,
        "template": null,
        "update": true,
        "userlabel": "Shunt Links"
    }
}