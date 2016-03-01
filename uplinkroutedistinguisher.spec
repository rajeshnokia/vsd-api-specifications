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
            "description": "The uplink route distinguisher value is used to identify which route packets should be flowing through with regards to having multiple network ports on the VRS/NSG.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "routeDistinguisher",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "RD_PRIMARY1",
                "RD_PRIMARY2",
                "RD_SECONDARY1",
                "RD_SECONDARY2"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "RD_PRIMARY1",
            "deprecated": false,
            "description": "Indicates the uplink type associated with the instance of Uplink Route Distinguisher.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "uplinkType",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null
        }
    ],
    "children": [],
    "model": {
        "create": false,
        "delete": false,
        "description": "Represents a network port uplink route distinguisher value.",
        "entity_name": "UplinkRD",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "network",
        "resource_name": "uplinkroutedistinguishers",
        "rest_name": "uplinkroutedistinguisher",
        "root": false,
        "update": false
    }
}
