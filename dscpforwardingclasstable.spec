{
    "attributes": {
        "description": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "A description of the dscp-fc mapping table.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "name": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "A unique name of the dscp-fc mapping table.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        }
    },
    "children": {
        "dscpforwardingclassmapping": {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": true,
            "delete": false,
            "deprecated": false,
            "get": true,
            "relationship": "child",
            "update": false
        }
    },
    "model": {
        "create": false,
        "delete": true,
        "description": "Provides the definition of a table that holds multiple DSCP -> Forwarding class mappings. Used in QoS policies.",
        "entity_name": "DSCPForwardingClassTable",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "policy",
        "resource_name": "dscpforwardingclasstables",
        "rest_name": "dscpforwardingclasstable",
        "root": false,
        "update": true
    }
}