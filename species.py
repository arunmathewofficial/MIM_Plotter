"""
Species_info.py
"""
# Author: Arun Mathew
# Created: 08-03-2023


# LABELS
HYDROGEN_LABELS = [r"$H$", r"$H^{1+}$"]
HELIUM_LABELS = [r"$He$", r"$He^{1+}$", r"$He^{2+}$"]
CARBON_LABELS = [r"$C$", r"$C^{1+}$", r"$C^{2+}$", r"$C^{3+}$", r"$C^{4+}$", r"$C^{5+}$", r"$C^{6+}$"]
NITROGEN_LABELS = [r"$N$", r"$N^{1+}$", r"$N^{2+}$", r"$N^{3+}$", r"$N^{4+}$", r"$N^{5+}$", r"$N^{6+}$",
                     r"$N^{7+}$"]
OXYGEN_LABELS = [r"$O$", r"$O^{1+}$", r"$O^{2+}$", r"$O^{3+}$", r"$O^{4+}$", r"$O^{5+}$", r"$O^{6+}$",
                     r"$O^{7+}$", r"$O^{7+}$"]
NEON_LABELS = [r"$Ne$", r"$Ne^{1+}$", r"$Ne^{2+}$", r"$Ne^{3+}$", r"$Ne^{4+}$", r"$Ne^{5+}$", r"$Ne^{6+}$",
                r"$Ne^{7+}$", r"$Ne^{8+}$", r"$Ne^{9+}$", r"$Ne^{10+}$"]
SILICON_LABELS = [r"$Si$", r"$Si^{1+}$", r"$Si^{2+}$", r"$Si^{3+}$", r"$Si^{4+}$", r"$Si^{5+}$", r"$Si^{6+}$",
                r"$Si^{7+}$", r"$Si^{8+}$", r"$Si^{9+}$", r"$Si^{10+}$", r"$Si^{11+}$", r"$Si^{12+}$", r"$Si^{13+}$",
                r"$Si^{14+}$"]
SULFUR_LABELS = [r"$S$", r"$S^{1+}$", r"$S^{2+}$", r"$S^{3+}$", r"$S^{4+}$", r"$S^{5+}$", r"$S^{6+}$", r"$S^{7+}$",
                r"$S^{8+}$", r"$S^{9+}$", r"$S^{10+}$", r"$S^{11+}$", r"$S^{12+}$", r"$S^{13+}$", r"$S^{14+}$",
                r"$S^{15+}$", r"$S^{16+}$"]
IRON_LABELS = [r"$Fe$", r"$Fe^{1+}$", r"$Fe^{2+}$", r"$Fe^{3+}$", r"$Fe^{4+}$", r"$Fe^{5+}$", r"$Fe^{6+}$",
                r"$Fe^{7+}$", r"$Fe^{8+}$", r"$Fe^{9+}$", r"$Fe^{10+}$", r"$Fe^{11+}$", r"$Fe^{12+}$",
                r"$Fe^{13+}$", r"$Fe^{14+}$", r"$Fe^{15+}$", r"$Fe^{16+}$", r"$Fe^{17+}$", r"$Fe^{18+}$",
                r"$Fe^{19+}$", r"$Fe^{20+}$", r"$Fe^{21+}$", r"$Fe^{22+}$", r"$Fe^{23+}$", r"$Fe^{24+}$",
                r"$Fe^{25+}$", r"$Fe^{26+}$"]

# CIE LABELS
HYDROGEN_CIE_LABELS = [r"$\textrm{I}$", r"$\textrm{II}$"]

HELIUM_CIE_LABELS = [r"$He$", r"$\textrm{II}$", r"$\textrm{III}$"]
CARBON_CIE_LABELS = [r"$\textrm{I}$", r"$\textrm{II}$", r"$\textrm{III}$", r"$\textrm{IV}$", r"$\textrm{V}$",
                     r"$\textrm{VI}$", r"$\textrm{VII}$"]
NITROGEN_CIE_LABELS = [r"$\textrm{I}$", r"$\textrm{II}$", r"$\textrm{III}$", r"$\textrm{IV}$", r"$\textrm{V}$",
                     r"$\textrm{VI}$", r"$\textrm{VII}$", r"$\textrm{VIII}$"]
OXYGEN_CIE_LABELS = [r"$O$", r"$O^{1+}$", r"$O^{2+}$", r"$O^{3+}$", r"$\textrm{V}$", r"$\textrm{VI}$", r"$\textrm{VII}$",
                     r"$\textrm{VIII}$", r"$\textrm{IX}$"]
NEON_CIE_LABELS = [r"$Ne$", r"$Ne^{1+}$", r"$Ne^{2+}$", r"$Ne^{3+}$", r"$Ne^{4+}$", r"$Ne^{5+}$", r"$Ne^{6+}$",
                r"$Ne^{7+}$", r"$Ne^{8+}$", r"$Ne^{9+}$", r"$Ne^{10+}$"]
SILICON_CIE_LABELS = [r"$Si$", r"$Si^{1+}$", r"$Si^{2+}$", r"$Si^{3+}$", r"$Si^{4+}$", r"$Si^{5+}$", r"$Si^{6+}$",
                r"$Si^{7+}$", r"$Si^{8+}$", r"$Si^{9+}$", r"$Si^{10+}$", r"$Si^{11+}$", r"$Si^{12+}$", r"$Si^{13+}$",
                r"$Si^{14+}$"]
SULFUR_CIE_LABELS = [r"$S$", r"$S^{1+}$", r"$S^{2+}$", r"$S^{3+}$", r"$S^{4+}$", r"$S^{5+}$", r"$S^{6+}$", r"$S^{7+}$",
                r"$S^{8+}$", r"$S^{9+}$", r"$S^{10+}$", r"$S^{11+}$", r"$S^{12+}$", r"$S^{13+}$", r"$S^{14+}$",
                r"$S^{15+}$", r"$S^{16+}$"]
IRON_CIE_LABELS = [r"$Fe$", r"$Fe^{1+}$", r"$Fe^{2+}$", r"$Fe^{3+}$", r"$Fe^{4+}$", r"$Fe^{5+}$", r"$Fe^{6+}$",
                r"$Fe^{7+}$", r"$Fe^{8+}$", r"$Fe^{9+}$", r"$Fe^{10+}$", r"$Fe^{11+}$", r"$Fe^{12+}$",
                r"$Fe^{13+}$", r"$Fe^{14+}$", r"$Fe^{15+}$", r"$Fe^{16+}$", r"$Fe^{17+}$", r"$Fe^{18+}$",
                r"$Fe^{19+}$", r"$Fe^{20+}$", r"$Fe^{21+}$", r"$Fe^{22+}$", r"$Fe^{23+}$", r"$Fe^{24+}$",
                r"$Fe^{25+}$", r"$Fe^{26+}$"]




'''
# Shock LABELS
HYDROGEN_SHOCK_LABELS = [r"$\textrm{I}$", r"$\textbf{\huge\textrm{II}}$"]

HELIUM_SHOCK_LABELS = [r"$\textbf{\textrm{I}}$", r"$\textrm{II}$", r"$\textrm{III}$"]
CARBON_SHOCK_LABELS = [r"$\textrm{I}$", r"$\textrm{II}$", r"$\textrm{III}$", r"$\textrm{IV}$", r"$\textrm{V}$",
                     r"$\textrm{VI}$", r"$\textrm{VII}$"]
NITROGEN_SHOCK_LABELS = [r"$\textrm{I}$", r"$\textrm{II}$", r"$\textrm{III}$", r"$\textrm{IV}$", r"$\textrm{V}$",
                     r"$\textrm{VI}$", r"$\textrm{VII}$", r"$\textrm{VIII}$"]
OXYGEN_SHOCK_LABELS = [r"$\textrm{I}$", r"$\textrm{II}$", r"$\textrm{III}$", r"$\textrm{IV}$", r"$\textrm{V}$", r"$\textrm{VI}$", r"$\textrm{VII}$",
                     r"$\textrm{VIII}$", r"$\textrm{IX}$"]
NEON_SHOCK_LABELS = [r"$\textrm{I}$", r"$\textrm{II}$", r"$\textrm{III}$", r"$\textrm{IV}$", r"$\textrm{V}$", r"$\textrm{VI}$", r"$\textrm{VII}$",
                     r"$\textrm{VIII}$", r"$\textrm{IX}$", r"$\textrm{X}$", r"$\textrm{XI}$"]
SILICON_SHOCK_LABELS = [r"$Si$", r"$Si^{1+}$", r"$Si^{2+}$", r"$Si^{3+}$", r"$Si^{4+}$", r"$Si^{5+}$", r"$Si^{6+}$",
                r"$Si^{7+}$", r"$Si^{8+}$", r"$Si^{9+}$", r"$Si^{10+}$", r"$Si^{11+}$", r"$Si^{12+}$", r"$Si^{13+}$",
                r"$Si^{14+}$"]
SULFUR_SHOCK_LABELS = [r"$S$", r"$S^{1+}$", r"$S^{2+}$", r"$S^{3+}$", r"$S^{4+}$", r"$S^{5+}$", r"$S^{6+}$", r"$S^{7+}$",
                r"$S^{8+}$", r"$S^{9+}$", r"$S^{10+}$", r"$S^{11+}$", r"$S^{12+}$", r"$S^{13+}$", r"$S^{14+}$",
                r"$S^{15+}$", r"$S^{16+}$"]
IRON_SHOCK_LABELS = [r"$Fe$", r"$Fe^{1+}$", r"$Fe^{2+}$", r"$Fe^{3+}$", r"$Fe^{4+}$", r"$Fe^{5+}$", r"$Fe^{6+}$",
                r"$Fe^{7+}$", r"$Fe^{8+}$", r"$Fe^{9+}$", r"$Fe^{10+}$", r"$Fe^{11+}$", r"$Fe^{12+}$",
                r"$Fe^{13+}$", r"$Fe^{14+}$", r"$Fe^{15+}$", r"$Fe^{16+}$", r"$Fe^{17+}$", r"$Fe^{18+}$",
                r"$Fe^{19+}$", r"$Fe^{20+}$", r"$Fe^{21+}$", r"$Fe^{22+}$", r"$Fe^{23+}$", r"$Fe^{24+}$",
                r"$Fe^{25+}$", r"$Fe^{26+}$"]
'''

# Shock LABELS
HYDROGEN_SHOCK_LABELS = [r"$\textbf{\Large\textrm{I}}$", r"$\textbf{\Large\textrm{II}}$"]

HELIUM_SHOCK_LABELS = [r"$\textbf{\textrm{I}}$", r"$\textrm{II}$", r"$\textrm{III}$"]
CARBON_SHOCK_LABELS = [r"$\textrm{I}$", r"$\textrm{II}$", r"$\textrm{III}$", r"$\textrm{IV}$", r"$\textrm{V}$",
                     r"$\textrm{VI}$", r"$\textrm{VII}$"]
NITROGEN_SHOCK_LABELS = [r"$\textrm{I}$", r"$\textrm{II}$", r"$\textrm{III}$", r"$\textrm{IV}$", r"$\textrm{V}$",
                     r"$\textrm{VI}$", r"$\textrm{VII}$", r"$\textrm{VIII}$"]
OXYGEN_SHOCK_LABELS = [r"$\textrm{I}$", r"$\textrm{II}$", r"$\textrm{III}$", r"$\textrm{IV}$", r"$\textrm{V}$", r"$\textrm{VI}$", r"$\textrm{VII}$",
                     r"$\textrm{VIII}$", r"$\textrm{IX}$"]
NEON_SHOCK_LABELS = [r"$\textrm{I}$", r"$\textrm{II}$", r"$\textrm{III}$", r"$\textrm{IV}$", r"$\textrm{V}$", r"$\textrm{VI}$", r"$\textrm{VII}$",
                     r"$\textrm{VIII}$", r"$\textrm{IX}$", r"$\textrm{X}$", r"$\textrm{XI}$"]
SILICON_SHOCK_LABELS = [r"$Si$", r"$Si^{1+}$", r"$Si^{2+}$", r"$Si^{3+}$", r"$Si^{4+}$", r"$Si^{5+}$", r"$Si^{6+}$",
                r"$Si^{7+}$", r"$Si^{8+}$", r"$Si^{9+}$", r"$Si^{10+}$", r"$Si^{11+}$", r"$Si^{12+}$", r"$Si^{13+}$",
                r"$Si^{14+}$"]
SULFUR_SHOCK_LABELS = [r"$S$", r"$S^{1+}$", r"$S^{2+}$", r"$S^{3+}$", r"$S^{4+}$", r"$S^{5+}$", r"$S^{6+}$", r"$S^{7+}$",
                r"$S^{8+}$", r"$S^{9+}$", r"$S^{10+}$", r"$S^{11+}$", r"$S^{12+}$", r"$S^{13+}$", r"$S^{14+}$",
                r"$S^{15+}$", r"$S^{16+}$"]
IRON_SHOCK_LABELS = [r"$Fe$", r"$Fe^{1+}$", r"$Fe^{2+}$", r"$Fe^{3+}$", r"$Fe^{4+}$", r"$Fe^{5+}$", r"$Fe^{6+}$",
                r"$Fe^{7+}$", r"$Fe^{8+}$", r"$Fe^{9+}$", r"$Fe^{10+}$", r"$Fe^{11+}$", r"$Fe^{12+}$",
                r"$Fe^{13+}$", r"$Fe^{14+}$", r"$Fe^{15+}$", r"$Fe^{16+}$", r"$Fe^{17+}$", r"$Fe^{18+}$",
                r"$Fe^{19+}$", r"$Fe^{20+}$", r"$Fe^{21+}$", r"$Fe^{22+}$", r"$Fe^{23+}$", r"$Fe^{24+}$",
                r"$Fe^{25+}$", r"$Fe^{26+}$"]







# CIE ASPLUND 2009 ==========================================================================================
HYDROGEN_CIE_ASPLUND2009 = ["Tr000_X_H", "Tr009_H1p"]
HELIUM_CIE_ASPLUND2009 = ["Tr001_X_He", "Tr010_He1p", "Tr011_He2p"]
CARBON_CIE_ASPLUND2009 = ["Tr002_X_C", "Tr012_C1p", "Tr013_C2p", "Tr014_C3p", "Tr015_C4p", "Tr016_C5p", "Tr017_C6p"]
NITROGEN_CIE_ASPLUND2009 = ["Tr003_X_N", "Tr018_N1p", "Tr019_N2p", "Tr020_N3p", "Tr021_N4p", "Tr022_N5p", "Tr023_N6p",
                 "Tr024_N7p"]
OXYGEN_CIE_ASPLUND2009 = ["Tr004_X_O", "Tr025_O1p", "Tr026_O2p", "Tr027_O3p", "Tr028_O4p", "Tr029_O5p", "Tr030_O6p",
                 "Tr031_O7p", "Tr032_O8p"]

NEON_CIE_ASPLUND2009 = ["Tr005_X_Ne", "Tr033_Ne1p", "Tr034_Ne2p", "Tr035_Ne3p", "Tr036_Ne4p", "Tr037_Ne5p", "Tr038_Ne6p",
           "Tr039_Ne7p", "Tr040_Ne8p", "Tr041_Ne9p", "Tr042_Ne10p"]

SILICON_CIE_ASPLUND2009 = ["Tr006_X_Si", "Tr043_Si1p", "Tr044_Si2p", "Tr045_Si3p", "Tr046_Si4p", "Tr047_Si5p", "Tr048_Si6p",
           "Tr049_Si7p", "Tr050_Si8p", "Tr051_Si9p", "Tr052_Si10p", "Tr053_Si11p", "Tr054_Si12p", "Tr055_Si13p",
           "Tr056_Si14p"]

SULFUR_CIE_ASPLUND2009 = ["Tr007_X_S", "Tr057_S1p", "Tr058_S2p", "Tr059_S3p", "Tr060_S4p", "Tr061_S5p", "Tr062_S6p", "Tr063_S7p",
           "Tr064_S8p", "Tr065_S9p", "Tr066_S10p", "Tr067_S11p", "Tr068_S12p", "Tr069_S13p", "Tr070_S14p",
           "Tr071_S15p", "Tr072_S16p"]

IRON_CIE_ASPLUND2009 = ["Tr008_X_Fe", "Tr073_Fe1p", "Tr074_Fe2p", "Tr075_Fe3p", "Tr076_Fe4p", "Tr077_Fe5p", "Tr078_Fe6p",
           "Tr079_Fe7p", "Tr080_Fe8p", "Tr081_Fe9p", "Tr082_Fe10p", "Tr083_Fe11p", "Tr084_Fe12p", "Tr085_Fe13p",
           "Tr086_Fe14p", "Tr087_Fe15p", "Tr088_Fe16p", "Tr089_Fe17p", "Tr090_Fe18p", "Tr091_Fe19p", "Tr092_Fe20p",
           "Tr093_Fe21p", "Tr094_Fe22p", "Tr095_Fe23p", "Tr096_Fe24p", "Tr097_Fe25p", "Tr098_Fe26p"]



# CIE EATSON 2022

HELIUM_CIE_EATSON2022 = ["Tr000_X_He", "Tr007_He1p", "Tr008_He2p"]
CARBON_CIE_EATSON2022 = ["Tr001_X_C", "Tr009_C1p", "Tr010_C2p", "Tr011_C3p", "Tr012_C4p", "Tr013_C5p", "Tr014_C6p"]
OXYGEN_CIE_EATSON2022 = ["Tr002_X_O", "Tr015_O1p", "Tr016_O2p", "Tr017_O3p", "Tr018_O4p", "Tr019_O5p", "Tr020_O6p",
                 "Tr021_O7p", "Tr022_O8p"]

NEON_CIE_EATSON2022 = ["Tr003_X_Ne", "Tr023_Ne1p", "Tr024_Ne2p", "Tr025_Ne3p", "Tr026_Ne4p", "Tr027_Ne5p", "Tr028_Ne6p",
           "Tr029_Ne7p", "Tr030_Ne8p", "Tr031_Ne9p", "Tr032_Ne10p"]

SILICON_CIE_EATSON2022 = ["Tr004_X_Si", "Tr033_Si1p", "Tr034_Si2p", "Tr035_Si3p", "Tr036_Si4p", "Tr037_Si5p", "Tr038_Si6p",
           "Tr039_Si7p", "Tr040_Si8p", "Tr041_Si9p", "Tr042_Si10p", "Tr043_Si11p", "Tr044_Si12p", "Tr045_Si13p",
           "Tr046_Si14p"]

SULFUR_CIE_EATSON2022 = ["Tr005_X_S", "Tr047_S1p", "Tr048_S2p", "Tr049_S3p", "Tr050_S4p", "Tr051_S5p", "Tr052_S6p", "Tr053_S7p",
           "Tr054_S8p", "Tr055_S9p", "Tr056_S10p", "Tr057_S11p", "Tr058_S12p", "Tr059_S13p", "Tr060_S14p",
           "Tr061_S15p", "Tr062_S16p"]

IRON_CIE_EATSON2022 = ["Tr006_X_Fe", "Tr063_Fe1p", "Tr064_Fe2p", "Tr065_Fe3p", "Tr066_Fe4p", "Tr067_Fe5p", "Tr068_Fe6p",
           "Tr069_Fe7p", "Tr070_Fe8p", "Tr071_Fe9p", "Tr072_Fe10p", "Tr073_Fe11p", "Tr074_Fe12p", "Tr075_Fe13p",
           "Tr076_Fe14p", "Tr077_Fe15p", "Tr078_Fe16p", "Tr079_Fe17p", "Tr080_Fe18p", "Tr081_Fe19p", "Tr082_Fe20p",
           "Tr083_Fe21p", "Tr084_Fe22p", "Tr085_Fe23p", "Tr086_Fe24p", "Tr087_Fe25p", "Tr088_Fe26p"]




# RAYMOND SHOCK TEST  ==========================================================================================
HYDROGEN_SHOCK_RAY79E = ["Tr000_X_H", "Tr009_H1p"]
HELIUM_SHOCK_RAY79E = ["Tr001_X_He", "Tr010_He1p", "Tr011_He2p"]
CARBON_SHOCK_RAY79E = ["Tr002_X_C", "Tr012_C1p", "Tr013_C2p", "Tr014_C3p", "Tr015_C4p", "Tr016_C5p", "Tr017_C6p"]
NITROGEN_SHOCK_RAY79E = ["Tr003_X_N", "Tr018_N1p", "Tr019_N2p", "Tr020_N3p", "Tr021_N4p", "Tr022_N5p", "Tr023_N6p",
                 "Tr024_N7p"]
OXYGEN_SHOCK_RAY79E = ["Tr004_X_O", "Tr025_O1p", "Tr026_O2p", "Tr027_O3p", "Tr028_O4p", "Tr029_O5p", "Tr030_O6p",
                 "Tr031_O7p", "Tr032_O8p"]
NEON_SHOCK_RAY79E = ["Tr005_X_Ne", "Tr033_Ne1p", "Tr034_Ne2p", "Tr035_Ne3p", "Tr036_Ne4p", "Tr037_Ne5p", "Tr038_Ne6p",
           "Tr039_Ne7p", "Tr040_Ne8p", "Tr041_Ne9p", "Tr042_Ne10p"]
SILICON_SHOCK_RAY79E = ["Tr006_X_Si", "Tr043_Si1p", "Tr044_Si2p", "Tr045_Si3p", "Tr046_Si4p", "Tr047_Si5p", "Tr048_Si6p",
           "Tr049_Si7p", "Tr050_Si8p", "Tr051_Si9p", "Tr052_Si10p", "Tr053_Si11p", "Tr054_Si12p", "Tr055_Si13p",
           "Tr056_Si14p"]
SULFUR_SHOCK_RAY79E = ["Tr007_X_S", "Tr057_S1p", "Tr058_S2p", "Tr059_S3p", "Tr060_S4p", "Tr061_S5p", "Tr062_S6p", "Tr063_S7p",
           "Tr064_S8p", "Tr065_S9p", "Tr066_S10p", "Tr067_S11p", "Tr068_S12p", "Tr069_S13p", "Tr070_S14p",
           "Tr071_S15p", "Tr072_S16p"]
IRON_SHOCK_RAY79E = ["Tr008_X_Fe", "Tr073_Fe1p", "Tr074_Fe2p", "Tr075_Fe3p", "Tr076_Fe4p", "Tr077_Fe5p", "Tr078_Fe6p",
           "Tr079_Fe7p", "Tr080_Fe8p", "Tr081_Fe9p", "Tr082_Fe10p", "Tr083_Fe11p", "Tr084_Fe12p", "Tr085_Fe13p",
           "Tr086_Fe14p", "Tr087_Fe15p", "Tr088_Fe16p", "Tr089_Fe17p", "Tr090_Fe18p", "Tr091_Fe19p", "Tr092_Fe20p",
           "Tr093_Fe21p", "Tr094_Fe22p", "Tr095_Fe23p", "Tr096_Fe24p", "Tr097_Fe25p", "Tr098_Fe26p"]



