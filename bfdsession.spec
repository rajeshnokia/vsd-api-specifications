{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Destination IP Address used for Bidirectional Forwarding Detection.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 64,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "BFDDestinationIP",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "BFD Destination IP"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "IPV4",
                "IPV6"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Destination IP Type of Bidirectional Forwarding Detection",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "BFDDestinationIPType",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "BFD Destination IP Type"
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
            "description": null,
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "BFDDestinationIPv6",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "B F D Destination I Pv6"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "3",
            "deprecated": false,
            "description": "Multiplier used for Bidirectional Forwarding Detection Timer.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": 20,
            "min_length": null,
            "min_value": 2,
            "name": "BFDMultiplier",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "BFD Multiplier"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "500",
            "deprecated": false,
            "description": "Timer for Bidirectional Forwarding Detection in milliseconds.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": 100000,
            "min_length": null,
            "min_value": 10,
            "name": "BFDTimer",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "BFD Timer"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "false",
            "deprecated": false,
            "description": "Boolean flag to indicate whether the BFD Session has single hop or multi hop capability.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "multiHopEnabled",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Multi Hop Enabled"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": null,
        "delete": true,
        "description": "Represents the Bidirectional Forwarding Detection session that can be configured on an uplink/BR connection.",
        "entity_name": "BFDSession",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": null,
        "resource_name": "bfdsessions",
        "rest_name": "bfdsession",
        "root": null,
        "template": false,
        "update": true,
        "userlabel": "BFD Session"
    }
}