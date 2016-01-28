{
    "attributes": {
        "assocClusterId": {
            "description": "The ID of the cluster to which this host is attached",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "hypervisorIP": {
            "description": "IP Address of the Hypervisor",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "string"
        },
        "networkList": {
            "description": "The available network list",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "orderable": true,
            "type": "list"
        }
    },
    "model": {
        "delete": true,
        "entity_name": "AutoDiscoverHypervisorFromCluster",
        "get": true,
        "resource_name": "autodiscoveredhypervisors",
        "rest_name": "autodiscoveredhypervisor",
        "update": true
    }
}