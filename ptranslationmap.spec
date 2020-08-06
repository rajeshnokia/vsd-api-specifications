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
            "description": "The list of provider source IPs to be SPAT'd.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "SPATSourceList",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "string",
            "transient": false,
            "type": "list",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "SPAT Source List"
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
            "description": "associated domain for this",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedDomainID",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": true,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Domain"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "NAT",
                "PAT"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": true,
            "default_order": true,
            "default_value": null,
            "deprecated": false,
            "description": "1:1 NATmapping, or *:1 PAT mappings",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "mappingType",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Mapping Type"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": true,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Provider public IP in Customer Domain",
            "exposed": true,
            "filterable": false,
            "format": "cidr",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "providerAliasIP",
            "orderable": false,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Provider Alias IP"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": true,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Provider private IP in Provider Domain.",
            "exposed": true,
            "filterable": false,
            "format": "cidr",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "providerIP",
            "orderable": false,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Provider IP"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": null,
        "delete": true,
        "description": "1:1 mappings of private IPs in provider domain to the provider  alias (public) IPs in customer domain and N:1 mappings of a collection of provider private IPs to a provider alias IP into the customer domain.",
        "entity_name": "PTranslationMap",
        "extends": [
            "@audited",
            "@base",
            "@metadata",
            "@permission"
        ],
        "get": true,
        "package": null,
        "resource_name": "ptranslationmaps",
        "rest_name": "ptranslationmap",
        "root": null,
        "template": false,
        "update": true,
        "userlabel": "Provider Translational Map"
    }
}