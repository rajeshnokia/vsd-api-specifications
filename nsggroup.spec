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
            "description": "Description of the NSG Group",
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
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Name of the NSG Group",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "name",
            "orderable": true,
            "read_only": false,
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
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The NSG Group 12 bit identifier.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "nsgGroupId",
            "orderable": true,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": true,
            "uniqueScope": null,
            "userlabel": "NSG Group ID"
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
            "rest_name": "ducgroupbinding",
            "update": false
        },
        {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": false,
            "delete": false,
            "deprecated": null,
            "get": true,
            "relationship": "member",
            "rest_name": "nsgateway",
            "update": true
        }
    ],
    "model": {
        "allowed_job_commands": null,
        "create": null,
        "delete": true,
        "description": "A logical group of NSG and NSG-BR instances that can be used to assign NSG-UBRs to all NSGs in the group, to provide connectivity to NSGs in disjoint underlays.",
        "entity_name": "NSGGroup",
        "extends": [
            "@audited",
            "@base",
            "@metadata",
            "@permission"
        ],
        "get": true,
        "package": null,
        "resource_name": "nsggroups",
        "rest_name": "nsggroup",
        "root": null,
        "template": false,
        "update": true,
        "userlabel": "NSG Group"
    }
}