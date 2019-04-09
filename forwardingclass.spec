{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Class of service to be used.Service classes in order of priority are A, B, C, D, E, F, G, and H.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "forwardingClass",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Forwarding Class"
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
            "description": "Indicates whether the Service Class is used to used for load balancing in the forwarding path.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "loadBalancing",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Load Balancing"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": false,
        "delete": false,
        "description": "Contains the Forwarding Class and its usage for load balancing.",
        "entity_name": "ForwardingClass",
        "extends": [],
        "get": true,
        "package": null,
        "resource_name": null,
        "rest_name": null,
        "root": null,
        "template": null,
        "update": true,
        "userlabel": "Forwarding Class"
    }
}