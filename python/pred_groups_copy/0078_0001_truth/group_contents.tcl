# geodesic_groups_file 2.1

#
# Group Stuff
#

proc group_autoload {} {
  global gFilenames
  set grpdir $gFilenames(groups_dir)
  group_readProfiles {RAICA} [file join $grpdir {RAICA}]
  group_readProfiles {LPICA} [file join $grpdir {LPICA}]
  group_readProfiles {RSCA} [file join $grpdir {RSCA}]
  group_readProfiles {LVA} [file join $grpdir {LVA}]
  group_readProfiles {RPCA_branch1} [file join $grpdir {RPCA_branch1}]
  group_readProfiles {LPCA_branch} [file join $grpdir {LPCA_branch}]
  group_readProfiles {RPICA} [file join $grpdir {RPICA}]
  group_readProfiles {LPCA_all} [file join $grpdir {LPCA_all}]
  group_readProfiles {RVA} [file join $grpdir {RVA}]
  group_readProfiles {LAICA} [file join $grpdir {LAICA}]
  group_readProfiles {LSCA} [file join $grpdir {LSCA}]
  group_readProfiles {LPCA_branch_3} [file join $grpdir {LPCA_branch_3}]
  group_readProfiles {LPCA_branch2} [file join $grpdir {LPCA_branch2}]
}
