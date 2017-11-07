# geodesic_groups_file 2.1

#
# Group Stuff
#

proc group_autoload {} {
  global gFilenames
  set grpdir $gFilenames(groups_dir)
  group_readProfiles {aorta_final} [file join $grpdir {aorta_final}]
  group_readProfiles {rt_carotid_final} [file join $grpdir {rt_carotid_final}]
  group_readProfiles {subclavian_final} [file join $grpdir {subclavian_final}]
  group_readProfiles {btrunk_final} [file join $grpdir {btrunk_final}]
  group_readProfiles {carotid_final} [file join $grpdir {carotid_final}]
}
