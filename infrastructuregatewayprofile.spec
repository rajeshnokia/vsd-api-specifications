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
            "description": "If set, this represents the security key for the Gateway to communicate with the NTP server (a VSC).",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": 32,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "NTPServerKey",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "NTP Key"
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
            "description": "Corresponds to the key ID on the NTP server that matches the NTPServerKey value.  Valid values are from 1 to 255 as specified by SR-OS and when value 0 is entered, it means that the NTP Key is not used (VSD/NSG only).",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": 255,
            "min_length": null,
            "min_value": 0,
            "name": "NTPServerKeyID",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "NTP Key Identifier"
        },
        {
            "allowed_chars": "255",
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "P7DT0H0M",
            "deprecated": false,
            "description": "Duration for a controller-less local operation (in ISO-duration format).",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "controllerLessDuration",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Controllerless Local Duration"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": true,
            "description": "Flag to enable controller-less operations",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "controllerLessEnabled",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": true,
            "type": "boolean",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Controllerless"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "DISABLED",
                "LOCAL_AND_REMOTE",
                "LOCAL_ONLY"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "DISABLED",
            "deprecated": false,
            "description": "The forwarding mode to use for controllerLess operations",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "controllerLessForwardingMode",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Controllerless Forwarding Mode"
        },
        {
            "allowed_chars": "255",
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "P3DT0H0M",
            "deprecated": false,
            "description": "Duration for a controller-less remote operation (in ISO-duration format).",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "controllerLessRemoteDuration",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Controllerless Remote Duration"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "1000",
            "deprecated": false,
            "description": "Datapath flows sync-time-interval specified in milliseconds",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": 60000,
            "min_length": null,
            "min_value": 1000,
            "name": "datapathSyncTimeout",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "long",
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "OpenFlow Datapath Synchronization Timeout"
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
            "description": "ISO 8601 format duration: **PnYnMnD T nHnMnS**. **P** represents the period field and **T** the time field. Period field: **Y** = year, **M** = month, **D** = day. Time field: **H** = hours, **M** = minutes, **S** = seconds. **n** is the value of each field. Because the years and month are units that vary in length, for the time being those are not supported yet.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": 255,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "deadTimer",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Enable Automatic Quarantine"
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
            "description": "Flag to enable the functionlity where VSD will automatically place an NSG into a quarantine state if it is no longer being reported by VSC nodes for a specified period.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "deadTimerEnabled",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Automatic Quarantine"
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
            "description": "A description of the Profile instance created.",
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
            "default_value": "false",
            "deprecated": false,
            "description": "Enables underlay tests during gateway activation. Underlay tests will cause the bootstrapping operation to be about two minutes longer.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "enableUnderlayTestsDuringActivation",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Underlay Tests During Activation"
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
            "description": "Enterprise/Organisation associated with this Profile instance.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "enterpriseID",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Enterprise ID"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "2500",
            "deprecated": true,
            "description": "Number of flows at which eviction from kernel flow table will be triggered (default: 2500)",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": 200000,
            "min_length": null,
            "min_value": 100,
            "name": "flowEvictionThreshold",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "long",
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "OpenFlow Eviction Threshold"
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
            "description": "Usually the synchronization will span across 1 hour window after the defined synchronization time. Forcing an immediate synchronization can overload the system and can have a negative impact on the system.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "forceImmediateSystemSync",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Force Immediate Synchronization"
        },
        {
            "allowed_chars": "URL",
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Path/URL to retrieve the NSG Upgrade information meta data files.  From that meta data, the NSG will be able to retrieve the upgrade package files and perform some validations.  It is expected that the meta data file is in JSON format.  RFC 2616 states that there are no 'official' maximum length for a URL but different browsers and servers have limits.  Our friendly Internet Explorer has a maximum of 'around' 2048 characters, we shall use this as a limit here.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": 2048,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "metadataUpgradePath",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Upgrade Metadata URL"
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
            "description": "Name of the Infrastructure Profile",
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
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": true,
            "uniqueScope": null,
            "userlabel": "Name"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "180",
            "deprecated": false,
            "description": "Openflow audit timer in seconds. Upon the expiry of this timer a set of cleanup operations will be performed",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": 1800,
            "min_length": null,
            "min_value": 180,
            "name": "openFlowAuditTimer",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": "long",
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "OpenFlow Audit Timer"
        },
        {
            "allowed_chars": "URL",
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Proxy DNS Name :  DNS Name of the system acting as a proxy between the NSG instances and the VSD.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "proxyDNSName",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "VSD Proxy FQDN"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "DISABLED",
                "RSYSLOG"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "DISABLED",
            "deprecated": false,
            "description": "Type of Log Server for system logs generated by Gateways associated with this Infrastructure Profile.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "remoteLogMode",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Log Export"
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
            "description": "Primary Log Server for system logs generated by Gateways associated with this Infrastructure Profile.  Can be an IP address or a URL.  This field is optional.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "remoteLogServerAddress",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Server Address"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "514",
            "deprecated": false,
            "description": "Port to be used to access the Remote Syslog server.  By default, this is port 514.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": 65535,
            "min_length": null,
            "min_value": 1,
            "name": "remoteLogServerPort",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Port"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "true",
            "deprecated": false,
            "description": "Run the underlay bandwidth test during activation. Will only have an effect if the Underlay tests at bootstrap are enabled.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "runUnderlayBandwidthTest",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Bandwidth"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "true",
            "deprecated": false,
            "description": "Run the underlay connectivity test during activation. Will only have an effect if the Underlay tests at bootstrap are enabled.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "runUnderlayConnectivityTest",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Connectivity"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "true",
            "deprecated": false,
            "description": "Run the underlay MTU discovery test during activation. Will only have an effect if the Underlay tests at bootstrap are enabled.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "runUnderlayMTUDiscoveryTest",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "MTU Discovery"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "39090",
            "deprecated": false,
            "description": "The port to open by the proxy for the statistics collector to use.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": 65535,
            "min_length": null,
            "min_value": 1024,
            "name": "statsCollectorPort",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Statistics Collector Port"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "0 0 * * *",
            "deprecated": false,
            "description": "Time, in a Cron format, when configuration updates are being applied on the Gateway (NSG).  This property is linked to systemSyncWindow.  Default value is every midnight (0 0 * * *).  Format:  Minutes Hours DayOfMonth Month DayOfWeek",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": 64,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "systemSyncScheduler",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Synchronize Configuration"
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
            "description": "Underlay Test Server (FQDN or IP Address). Required when the Underlay test at bootstrap feature is enabled or to allow On-Demand tests to be run.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "underlayTestServer",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Underlay Test Server"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "ALL_UPLINKS",
                "BOOTSTRAP_UPLINK"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "BOOTSTRAP_UPLINK",
            "deprecated": false,
            "description": "Enumerator to describe which uplinks to run underlay tests on during bootstrap",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "underlayTestUplinkMode",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Underlay Test Uplink Mode"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "DOWNLOAD_AND_UPGRADE_AT_WINDOW",
                "DOWNLOAD_AND_UPGRADE_NOW",
                "DOWNLOAD_ONLY",
                "NONE",
                "UPGRADE_AT_BOOTSTRAPPING",
                "UPGRADE_NOW"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "NONE",
            "deprecated": false,
            "description": "Upgrade action for NSG associated with this Infrastructure Gateway Profile instance.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "upgradeAction",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Upgrade Policy"
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
            "description": "Use Two Factor :  When set to true, the use of two independent authentication factors will be used to secure the installed NSG.  When set to false, there is an assumption that the NSG is being installed in a secure environment and the installer is also trusted.  The defaut value is true, using 2-factor.",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "useTwoFactor",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "boolean",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Two-Factor Authentication"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "8080",
            "deprecated": false,
            "description": "The port to be opened by the proxy for webfilter update database",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": 65535,
            "min_length": null,
            "min_value": 1024,
            "name": "webFilterDownloadPort",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Web Filter Download Port"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "9090",
            "deprecated": false,
            "description": "The port to be opened by the proxy for webfilter category query request",
            "exposed": true,
            "filterable": false,
            "format": null,
            "max_length": null,
            "max_value": 65535,
            "min_length": null,
            "min_value": 1024,
            "name": "webFilterQueryPort",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Web Filter Query Port"
        }
    ],
    "children": [],
    "model": {
        "allowed_job_commands": null,
        "create": false,
        "delete": true,
        "description": "Infrastructure Gateway Profiles are gateway-level platform attributes inherited by gateways as they are instantiated, connecting them to Nuage management infrastructure.",
        "entity_name": "InfrastructureGatewayProfile",
        "extends": [
            "@audited",
            "@base",
            "@metadata",
            "@permission"
        ],
        "get": true,
        "package": "infrastructure",
        "resource_name": "infrastructuregatewayprofiles",
        "rest_name": "infrastructuregatewayprofile",
        "root": false,
        "template": false,
        "update": true,
        "userlabel": "Infrastructure Gateway Profile"
    }
}