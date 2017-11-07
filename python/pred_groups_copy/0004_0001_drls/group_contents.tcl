# geodesic_groups_file 2.1
            #
            # Group Stuff
            #

            proc group_autoload {} {
            global gFilenames
            set grpdir $gFilenames(groups_dir)
   group_readProfiles {profunda_branch_left} [file join $grpdir {profunda_branch_left}]
   group_readProfiles {profunda_left} [file join $grpdir {profunda_left}]
   group_readProfiles {knee_right} [file join $grpdir {knee_right}]
   group_readProfiles {profunda_branch_right} [file join $grpdir {profunda_branch_right}]
   group_readProfiles {anterior_tibial_right} [file join $grpdir {anterior_tibial_right}]
   group_readProfiles {knee_left} [file join $grpdir {knee_left}]
   group_readProfiles {anterior_tibial_left} [file join $grpdir {anterior_tibial_left}]
   group_readProfiles {posterior_tibial_right} [file join $grpdir {posterior_tibial_right}]
   group_readProfiles {femoral_right} [file join $grpdir {femoral_right}]
   group_readProfiles {posterior_tibial_left} [file join $grpdir {posterior_tibial_left}]
   group_readProfiles {femoral_left} [file join $grpdir {femoral_left}]
   group_readProfiles {aorta_leg_right} [file join $grpdir {aorta_leg_right}]
   group_readProfiles {celiac} [file join $grpdir {celiac}]
   group_readProfiles {leg_left} [file join $grpdir {leg_left}]
   group_readProfiles {renal_right} [file join $grpdir {renal_right}]
   group_readProfiles {superior_mesenteric_artery} [file join $grpdir {superior_mesenteric_artery}]
   group_readProfiles {internal_iliac_right} [file join $grpdir {internal_iliac_right}]
   group_readProfiles {renal_left} [file join $grpdir {renal_left}]
   group_readProfiles {profunda_right} [file join $grpdir {profunda_right}]
   group_readProfiles {internal_iliac_left} [file join $grpdir {internal_iliac_left}]
}