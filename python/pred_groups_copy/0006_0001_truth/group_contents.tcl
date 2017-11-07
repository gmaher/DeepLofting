# geodesic_groups_file 2.1

#
# Group Stuff
#

proc group_autoload {} {
  global gFilenames
  set grpdir $gFilenames(groups_dir)
  group_readProfiles {celiac_trunk} [file join $grpdir {celiac_trunk}]
  group_readProfiles {renal_left} [file join $grpdir {renal_left}]
  group_readProfiles {left_internal_iliac} [file join $grpdir {left_internal_iliac}]
  group_readProfiles {celiac_branch} [file join $grpdir {celiac_branch}]
  group_readProfiles {superior_mesentaric} [file join $grpdir {superior_mesentaric}]
  group_readProfiles {renal_right} [file join $grpdir {renal_right}]
  group_readProfiles {right_iliac} [file join $grpdir {right_iliac}]
  group_readProfiles {aorta} [file join $grpdir {aorta}]
  group_readProfiles {right_internal_iliac} [file join $grpdir {right_internal_iliac}]
}
