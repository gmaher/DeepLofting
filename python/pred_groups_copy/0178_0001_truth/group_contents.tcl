# geodesic_groups_file 2.1

#
# Group Stuff
#

proc group_autoload {} {
  global gFilenames
  set grpdir $gFilenames(groups_dir)
  group_readProfiles {C_right} [file join $grpdir {C_right}]
  group_readProfiles {R_vtrbl} [file join $grpdir {R_vtrbl}]
  group_readProfiles {L_incrd} [file join $grpdir {L_incrd}]
  group_readProfiles {aneurysm_1} [file join $grpdir {aneurysm_1}]
  group_readProfiles {C_left} [file join $grpdir {C_left}]
  group_readProfiles {aneurysm_2} [file join $grpdir {aneurysm_2}]
  group_readProfiles {L_ant} [file join $grpdir {L_ant}]
  group_readProfiles {L_vtrbl_s} [file join $grpdir {L_vtrbl_s}]
  group_readProfiles {R_incrd} [file join $grpdir {R_incrd}]
  group_readProfiles {R_ant} [file join $grpdir {R_ant}]
  group_readProfiles {C_ant} [file join $grpdir {C_ant}]
  group_readProfiles {L_vtrbl_i} [file join $grpdir {L_vtrbl_i}]
}
