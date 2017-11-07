# geodesic_groups_file 2.1
        #
        # Group Stuff
        #

        proc group_autoload {} {
        global gFilenames
        set grpdir $gFilenames(groups_dir)
   group_readProfiles {L_crd} [file join $grpdir {L_crd}]
   group_readProfiles {A_com} [file join $grpdir {A_com}]
   group_readProfiles {L_ant} [file join $grpdir {L_ant}]
   group_readProfiles {R_vrt} [file join $grpdir {R_vrt}]
   group_readProfiles {R_com} [file join $grpdir {R_com}]
   group_readProfiles {L_vrt_s} [file join $grpdir {L_vrt_s}]
   group_readProfiles {L_vrt_i} [file join $grpdir {L_vrt_i}]
   group_readProfiles {R_crd} [file join $grpdir {R_crd}]
   group_readProfiles {L_com} [file join $grpdir {L_com}]
   group_readProfiles {R_ant} [file join $grpdir {R_ant}]
   group_readProfiles {aneurysm} [file join $grpdir {aneurysm}]
}