# geodesic_groups_file 2.1
            #
            # Group Stuff
            #

            proc group_autoload {} {
            global gFilenames
            set grpdir $gFilenames(groups_dir)
   group_readProfiles {renal_right} [file join $grpdir {renal_right}]
   group_readProfiles {SMA} [file join $grpdir {SMA}]
   group_readProfiles {int_iliac_left} [file join $grpdir {int_iliac_left}]
   group_readProfiles {IMA} [file join $grpdir {IMA}]
   group_readProfiles {int_iliac_right} [file join $grpdir {int_iliac_right}]
   group_readProfiles {renal_left} [file join $grpdir {renal_left}]
   group_readProfiles {celiac_splenic} [file join $grpdir {celiac_splenic}]
   group_readProfiles {ext_iliac_left} [file join $grpdir {ext_iliac_left}]
   group_readProfiles {aorta} [file join $grpdir {aorta}]
   group_readProfiles {celiac_hepatic} [file join $grpdir {celiac_hepatic}]
}