# PySNMP SMI module. Autogenerated from smidump -f python PYSNMP-USM-MIB
# by libsmi2pysnmp-0.0.7-alpha at Thu Nov 16 16:12:46 2006,
# Python version (2, 4, 3, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( pysnmpModuleIDs, ) = mibBuilder.importSymbols("PYSNMP-MIB", "pysnmpModuleIDs")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( usmUserEntry, ) = mibBuilder.importSymbols("SNMP-USER-BASED-SM-MIB", "usmUserEntry")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( RowStatus, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus")

# Objects

pysnmpUsmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1)).setRevisions(("2005-05-14 00:00",))
pysnmpUsmMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1))
pysnmpUsmCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 1))
pysnmpUsmDiscoverable = MibScalar((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 1, 1), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,0,)).subtype(namedValues=namedval.NamedValues(("notDiscoverable", 0), ("discoverable", 1), )).clone(1)).setMaxAccess("readwrite")
pysnmpUsmDiscovery = MibScalar((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,0,)).subtype(namedValues=namedval.NamedValues(("doNotDiscover", 0), ("doDiscover", 1), )).clone(1)).setMaxAccess("readwrite")
pysnmpUsmSecretTable = MibTable((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 2))
pysnmpUsmSecretEntry = MibTableRow((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 2, 1)).setIndexNames((1, "PYSNMP-USM-MIB", "pysnmpUsmSecretUserName"))
pysnmpUsmSecretUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
pysnmpUsmSecretAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 65535))).setMaxAccess("noaccess")
pysnmpUsmSecretPrivKey = MibTableColumn((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 65535))).setMaxAccess("noaccess")
pysnmpUsmSecretStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
pysnmpUsmUser = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 3))
pysnmpUsmKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 3, 1))
pysnmpUsmKeyAuthLocalized = MibTableColumn((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 32))).setMaxAccess("noaccess")
pysnmpUsmKeyPrivLocalized = MibTableColumn((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 32))).setMaxAccess("noaccess")
pysnmpUsmKeyAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 32))).setMaxAccess("noaccess")
pysnmpUsmKeyPriv = MibTableColumn((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 1, 3, 1, 4), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(8, 32))).setMaxAccess("noaccess")
pysnmpUsmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 2))
pysnmpUsmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 2, 1))
pysnmpUsmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1, 1, 2, 2))

# Augmentions
usmUserEntry, = mibBuilder.importSymbols("SNMP-USER-BASED-SM-MIB", "usmUserEntry")
usmUserEntry.registerAugmentions(("PYSNMP-USM-MIB", "pysnmpUsmKeyEntry"))
apply(pysnmpUsmKeyEntry.setIndexNames, usmUserEntry.getIndexNames())

# Exports

# Module identity
mibBuilder.exportSymbols("PYSNMP-USM-MIB", PYSNMP_MODULE_ID=pysnmpUsmMIB)

# Objects
mibBuilder.exportSymbols("PYSNMP-USM-MIB", pysnmpUsmMIB=pysnmpUsmMIB, pysnmpUsmMIBObjects=pysnmpUsmMIBObjects, pysnmpUsmCfg=pysnmpUsmCfg, pysnmpUsmDiscoverable=pysnmpUsmDiscoverable, pysnmpUsmDiscovery=pysnmpUsmDiscovery, pysnmpUsmSecretTable=pysnmpUsmSecretTable, pysnmpUsmSecretEntry=pysnmpUsmSecretEntry, pysnmpUsmSecretUserName=pysnmpUsmSecretUserName, pysnmpUsmSecretAuthKey=pysnmpUsmSecretAuthKey, pysnmpUsmSecretPrivKey=pysnmpUsmSecretPrivKey, pysnmpUsmSecretStatus=pysnmpUsmSecretStatus, pysnmpUsmUser=pysnmpUsmUser, pysnmpUsmKeyEntry=pysnmpUsmKeyEntry, pysnmpUsmKeyAuthLocalized=pysnmpUsmKeyAuthLocalized, pysnmpUsmKeyPrivLocalized=pysnmpUsmKeyPrivLocalized, pysnmpUsmKeyAuth=pysnmpUsmKeyAuth, pysnmpUsmKeyPriv=pysnmpUsmKeyPriv, pysnmpUsmMIBConformance=pysnmpUsmMIBConformance, pysnmpUsmMIBCompliances=pysnmpUsmMIBCompliances, pysnmpUsmMIBGroups=pysnmpUsmMIBGroups)

