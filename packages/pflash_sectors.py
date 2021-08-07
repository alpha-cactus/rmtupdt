from packages.types import pflash_sector_t

#pflash sector objects are used to create a virtual image of the controller
pf0_sectors = [ \
#    pflash_sector_t('0xA0000000', '0xA0003FFF', 0x03),\
    pflash_sector_t('0xA0004000', '0xA00040FF', 0x03),\
    pflash_sector_t('0xA01F0000', '0xA01FFFFF', 0x07)]



pf1_sectors = [ \
 #   pflash_sector_t('0xA0200000', '0xA0203FFF', 0x03),\
    pflash_sector_t('0xA0204000', '0xA0207FFF', 0x03),\
    pflash_sector_t('0xA03F0000', '0xA03FFFFF', 0x07)]



pf2_sectors = [ \
  #  pflash_sector_t('0xA0400000', '0xA0403FFF', 0x03),\
    pflash_sector_t('0xA0404000', '0xA0407FFF', 0x03),\
    pflash_sector_t('0xA05F0000', '0xA05FFFFF', 0x07)]

