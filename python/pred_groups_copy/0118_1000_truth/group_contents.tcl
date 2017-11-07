# geodesic_groups_file 2.1

#
# Group Stuff
#

proc group_autoload {} {
  global gFilenames
  set grpdir $gFilenames(groups_dir)
  group_readProfiles {RPA_006} [file join $grpdir {RPA_006}]
  group_readProfiles {RPA_007} [file join $grpdir {RPA_007}]
  group_readProfiles {RPA_008} [file join $grpdir {RPA_008}]
  group_readProfiles {RPA_0081} [file join $grpdir {RPA_0081}]
  group_readProfiles {RPA} [file join $grpdir {RPA}]
  group_readProfiles {RPA_009} [file join $grpdir {RPA_009}]
  group_readProfiles {RPA_010} [file join $grpdir {RPA_010}]
  group_readProfiles {RPA_0082} [file join $grpdir {RPA_0082}]
  group_readProfiles {RPA_011} [file join $grpdir {RPA_011}]
  group_readProfiles {RPA_0083} [file join $grpdir {RPA_0083}]
  group_readProfiles {LPA_001} [file join $grpdir {LPA_001}]
  group_readProfiles {RPA_012} [file join $grpdir {RPA_012}]
  group_readProfiles {RPA_013} [file join $grpdir {RPA_013}]
  group_readProfiles {LPA_002} [file join $grpdir {LPA_002}]
  group_readProfiles {LPA_003} [file join $grpdir {LPA_003}]
  group_readProfiles {RPA_014} [file join $grpdir {RPA_014}]
  group_readProfiles {LPA2} [file join $grpdir {LPA2}]
  group_readProfiles {LPA_004} [file join $grpdir {LPA_004}]
  group_readProfiles {RPA_015} [file join $grpdir {RPA_015}]
  group_readProfiles {LPA_005} [file join $grpdir {LPA_005}]
  group_readProfiles {RPA_016} [file join $grpdir {RPA_016}]
  group_readProfiles {LPA_006} [file join $grpdir {LPA_006}]
  group_readProfiles {RPA_017} [file join $grpdir {RPA_017}]
  group_readProfiles {LPA_007} [file join $grpdir {LPA_007}]
  group_readProfiles {RPA_001} [file join $grpdir {RPA_001}]
  group_readProfiles {LPA_008} [file join $grpdir {LPA_008}]
  group_readProfiles {RPA_002} [file join $grpdir {RPA_002}]
  group_readProfiles {LPA_010} [file join $grpdir {LPA_010}]
  group_readProfiles {LPA_009} [file join $grpdir {LPA_009}]
  group_readProfiles {LPA} [file join $grpdir {LPA}]
  group_readProfiles {RPA_003} [file join $grpdir {RPA_003}]
  group_readProfiles {LPA_011} [file join $grpdir {LPA_011}]
  group_readProfiles {RPA_004} [file join $grpdir {RPA_004}]
  group_readProfiles {LPA_012} [file join $grpdir {LPA_012}]
  group_readProfiles {RPA_005} [file join $grpdir {RPA_005}]
}
