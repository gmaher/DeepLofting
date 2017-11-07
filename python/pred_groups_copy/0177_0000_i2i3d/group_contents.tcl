# geodesic_groups_file 2.1
            #
            # Group Stuff
            #

            proc group_autoload {} {
            global gFilenames
            set grpdir $gFilenames(groups_dir)
   group_readProfiles {RCCA} [file join $grpdir {RCCA}]
   group_readProfiles {renal_left} [file join $grpdir {renal_left}]
   group_readProfiles {dc_4} [file join $grpdir {dc_4}]
   group_readProfiles {IMA} [file join $grpdir {IMA}]
   group_readProfiles {ext_iliac_left} [file join $grpdir {ext_iliac_left}]
   group_readProfiles {renal_right} [file join $grpdir {renal_right}]
   group_readProfiles {RSA} [file join $grpdir {RSA}]
   group_readProfiles {aorta} [file join $grpdir {aorta}]
   group_readProfiles {in_iliac_right} [file join $grpdir {in_iliac_right}]
   group_readProfiles {dc_2} [file join $grpdir {dc_2}]
   group_readProfiles {LSA} [file join $grpdir {LSA}]
   group_readProfiles {in_iliac_left} [file join $grpdir {in_iliac_left}]
   group_readProfiles {LCCA} [file join $grpdir {LCCA}]
   group_readProfiles {celiac_splenic} [file join $grpdir {celiac_splenic}]
   group_readProfiles {dc_5} [file join $grpdir {dc_5}]
   group_readProfiles {celiac_hepatic} [file join $grpdir {celiac_hepatic}]
   group_readProfiles {dc_3} [file join $grpdir {dc_3}]
   group_readProfiles {SMA} [file join $grpdir {SMA}]
   group_readProfiles {dc_1} [file join $grpdir {dc_1}]
   group_readProfiles {disection} [file join $grpdir {disection}]
}