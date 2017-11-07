# geodesic_groups_file 2.1
            #
            # Group Stuff
            #

            proc group_autoload {} {
            global gFilenames
            set grpdir $gFilenames(groups_dir)
   group_readProfiles {r_renal_final} [file join $grpdir {r_renal_final}]
   group_readProfiles {SMA_final} [file join $grpdir {SMA_final}]
   group_readProfiles {l_renal_final} [file join $grpdir {l_renal_final}]
   group_readProfiles {IMA} [file join $grpdir {IMA}]
   group_readProfiles {celiac_final} [file join $grpdir {celiac_final}]
   group_readProfiles {l_illiac_final} [file join $grpdir {l_illiac_final}]
   group_readProfiles {r_in_illiac} [file join $grpdir {r_in_illiac}]
   group_readProfiles {aorta_final} [file join $grpdir {aorta_final}]
   group_readProfiles {l_in_illiac} [file join $grpdir {l_in_illiac}]
   group_readProfiles {celiac_hepatic} [file join $grpdir {celiac_hepatic}]
}