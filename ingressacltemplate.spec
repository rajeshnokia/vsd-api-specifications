{
    "attributes": {
        "active": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "If enabled, it means that this ACL or QOS entry is active",
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
            "type": "boolean",
            "unique": false,
            "uniqueScope": "no"
        },
        "allowAddressSpoof": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "If enabled, it will disable the default anti-spoof ACL for this domain that essentially prevents any VM to send packets that do not originate from that particular VM",
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
            "type": "boolean",
            "unique": false,
            "uniqueScope": "no"
        },
        "assocAclTemplateId": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "ID of the ACL template associated with this ACL template",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "associatedLiveEntityID": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "In the draft mode, the ACL entry refers to this LiveEntity. In non-drafted mode, this is null.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "defaultAllowIP": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "If enabled a default ACL of Allow All is added as the last entry in the list of ACL entries",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": "no"
        },
        "defaultAllowNonIP": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "If enabled, non ip traffic will be dropped",
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
            "type": "boolean",
            "unique": false,
            "uniqueScope": "no"
        },
        "description": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "A description of the entity",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "orderable": false,
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
            "description": "The name of the entity",
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
        },
        "policyState": {
            "allowed_chars": null,
            "allowed_choices": [
                "DRAFT",
                "LIVE"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "",
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
            "type": "enum",
            "unique": false,
            "uniqueScope": "no"
        },
        "priority": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The priority of the ACL entry that determines the order of entries",
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
            "type": "integer",
            "unique": false,
            "uniqueScope": "no"
        },
        "priorityType": {
            "allowed_chars": null,
            "allowed_choices": [
                "BOTTOM",
                "NONE",
                "TOP"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "",
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
            "type": "enum",
            "unique": false,
            "uniqueScope": "no"
        }
    },
    "children": {
        "container": {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": false,
            "delete": false,
            "deprecated": null,
            "get": true,
            "relationship": "child",
            "update": false
        },
        "eventlog": {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": false,
            "delete": false,
            "deprecated": false,
            "get": true,
            "relationship": "child",
            "update": false
        },
        "ingressaclentrytemplate": {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": true,
            "delete": false,
            "deprecated": false,
            "get": true,
            "relationship": "child",
            "update": false
        },
        "job": {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": true,
            "delete": false,
            "deprecated": false,
            "get": false,
            "relationship": "child",
            "update": false
        },
        "vm": {
            "bulk_create": false,
            "bulk_delete": false,
            "bulk_update": false,
            "create": false,
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
        "description": "Defines the template for an Ingress ACL.",
        "entity_name": "IngressACLTemplate",
        "extends": [
            "@audited",
            "@base",
            "@metadata"
        ],
        "get": true,
        "package": "policy/acl",
        "resource_name": "ingressacltemplates",
        "rest_name": "ingressacltemplate",
        "root": false,
        "update": true
    }
}