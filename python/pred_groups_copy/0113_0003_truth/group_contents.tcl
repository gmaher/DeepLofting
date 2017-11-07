# geodesic_groups_file 2.1

#
# Group Stuff
#

proc group_autoload {} {
  global gFilenames
  set grpdir $gFilenames(groups_dir)
  group_readProfiles {RSA_b1} [file join $grpdir {RSA_b1}]
  group_readProfiles {RCCA} [file join $grpdir {RCCA}]
  group_readProfiles {RSA_b2} [file join $grpdir {RSA_b2}]
  group_readProfiles {LSA} [file join $grpdir {LSA}]
  group_readProfiles {LCA} [file join $grpdir {LCA}]
  group_readProfiles {N_LCA5} [file join $grpdir {N_LCA5}]
  group_readProfiles {LSA_b1} [file join $grpdir {LSA_b1}]
  group_readProfiles {LCA2} [file join $grpdir {LCA2}]
  group_readProfiles {LSA_b2} [file join $grpdir {LSA_b2}]
  group_readProfiles {LIMA} [file join $grpdir {LIMA}]
  group_readProfiles {LCCA} [file join $grpdir {LCCA}]
  group_readProfiles {LSA_b3} [file join $grpdir {LSA_b3}]
  group_readProfiles {LSA_b4} [file join $grpdir {LSA_b4}]
  group_readProfiles {N_LCA} [file join $grpdir {N_LCA}]
  group_readProfiles {RSA} [file join $grpdir {RSA}]
  group_readProfiles {RCA} [file join $grpdir {RCA}]
  group_readProfiles {LSA_b5} [file join $grpdir {LSA_b5}]
  group_readProfiles {aorta} [file join $grpdir {aorta}]
}
