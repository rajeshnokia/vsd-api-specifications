{
    "attributes": {
        "IKEv2GatewayIdentifier": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "IKEv2GatewayIdentifierType": {
            "allowed_choices": [
                "ID_IPV4_ADDR", 
                "ID_FQDN", 
                "ID_RFC822_ADDR\n", 
                "ID_KEY_ID", 
                "ID_DER_ASN1_DN"
            ], 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "associatedEnterpriseID": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedIKEv2AuthenticationID": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedIKEv2AuthenticationType": {
            "allowed_choices": [
                "ikev2certificate", 
                "ikev2psk"
            ], 
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }, 
        "associatedIKEv2EncryptionProfileID": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "associatedIKEv2GatewayID": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "description": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "nsgRole": {
            "description": null, 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "model": {
        "delete": true, 
        "entity_name": "IKEv2GatewayProfile", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "resource_name": "ikev2gatewayprofiles", 
        "rest_name": "ikev2gatewayprofile", 
        "update": true
    }
}