{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "75",
            "deprecated": false,
            "description": "Threshold for CPU usage",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 100,
            "min_length": null,
            "min_value": 1,
            "name": "CPUThreshold",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": " C P U Threshold"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "NONE",
                "RESET",
                "SHUTOFF"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "NONE",
            "deprecated": false,
            "description": "Action to be taken on threshold crossover",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "action",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Action"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "75",
            "deprecated": false,
            "description": "Threshold for memory usage",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 100,
            "min_length": null,
            "min_value": 1,
            "name": "memoryThreshold",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Memory Threshold"
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
            "description": "Number of restart retries before shutdown",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "retries",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Retries"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "75",
            "deprecated": false,
            "description": "Threshold for storage usage",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 100,
            "min_length": null,
            "min_value": 1,
            "name": "storageThreshold",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Storage Threshold"
        }
    ],
    "children": [],
    "model": {
        "create": null,
        "delete": true,
        "description": "This represents VNF agent policy",
        "entity_name": "VNFAgentPolicy",
        "extends": [],
        "get": true,
        "package": "vnf",
        "resource_name": "vnfagentpolicies",
        "rest_name": "vnfagentpolicy",
        "root": null,
        "update": true
    }
}