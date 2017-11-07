# geodesic_groups_file 2.1

#
# Group Stuff
#

proc group_autoload {} {
  global gFilenames
  set grpdir $gFilenames(groups_dir)
  group_readProfiles {LSA} [file join $grpdir {LSA}]
  group_readProfiles {RCCA} [file join $grpdir {RCCA}]
  group_readProfiles {RSA} [file join $grpdir {RSA}]
  group_readProfiles {aorta} [file join $grpdir {aorta}]
  group_readProfiles {LCCA} [file join $grpdir {LCCA}]
}
