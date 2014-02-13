import os
import time
from subprocess import Popen
devnull = open(os.devnull, 'wb')

CSI="\x1B["
reset=CSI+"m"

print CSI+"31;40m"
print  "                           ...----...."
print  "                         ..-::..         ..:-.."
print  "                      .-.                      .-."
print  "                    ..              .     .       .."
print  "                  ..   .          .    .      .    ...."
print  "                ..  .    .       .   .   .     .   . ..:."
print  "              .. .   . .  .       .   .   ..  .   . ....::."
print  "           .: .   .   ..   .    .     . . .. . ... ....:.:VHA."
print  "           ...  .  .. .   .       .  . .. . .. . .....:.::IHHB."
print  "          .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM."
print  "         .:.... .   . .::::... .   .  . .:.:.:II;,. .. ..:IHIMMA"
print  "         .:.:..  ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM"
print  "        .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM"
print  "       .:.:V.:IVHHHHHHHMHMHHH::..:: .:HIHHHHHHHHHHHHHMHHA. .VMMM."
print  "       :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI"
print  "       ::V..:VIHHHHHHMMMHHHHHH. .   .I::IIMHHMMHHHHHHHHHHHAPI:WMM"
print  "       :::. .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:.:H:WM"
print  "       :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:.. .IHWW"
print  "       ..  ..:..:.:IHHHHHMMHV: .AVMHMA.:..VHMMMMHHHHHV:. .  :IHWV"
print  "        :.  .:...::.:.:TPP:   .AVMMHMMA.:. :VMMHHHP.:... .. :IVAI"
print  "       .:.   .... .::.   .   ..HMMMHMMMA::. .:VHHI:::....  .:IHW."
print  "       ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM"
print  "     : .   ..:. .:.V:. .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::..P:HM."
print  "     :.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV::T::I::.:.:IHIMA"
print  "     .V:.. .. . .. .  .  .   .VMMV..VMMV :....:V:.:..:....::IHHHMH"
print  "       :IHH:.II:.. .:. .  . . . : :HB:: . . ..PI:.::.:::..:IHHMMV:"
print  "        :IP::HHII:.  .  .    . . ..V:. . . ..:IH:.:.::IHIHHMMMMM:"
print  "        :..VIHIHMMMI...::.,:.,:!:I:!:I!:I!:V:AI:VAMMMMMMHMMMMMM."
print  "        .:.:HIHIMHHA::!!:I.:AXXXVVXXXXXXXA:.:HPHIMMMMHHMHMMMMMV"
print  "          V:H:I:MA:W.I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM"
print  "            .I::IVA ASSSSXSSSSBBSBMBSSSSSSBBMMMBS.VVMMHIMM.:."
print  "             I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI"
print  "            .I::. :H:XIIXBBMMMMMMMMMMMMMMMMMBXIXXMMPHIIMM."
print  "            :::I.  .:XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM"
print  "            :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM"
print  "            ::.I:.  .::SSSSSSSISISSXIIXSSSSBMMB:AHI:..MMM."
print  "            ::.I:. . ..::BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI"
print  "            :..::.  . ..::::BBBBBSSBBBMMMB:MMMMHHII::IHHMI"
print  "            .:.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV:"
print  "              :V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP."
print  "               .:. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM:"
print  "                 :::....::.:::..:..::IIIIIHHHHMMMHHMV:"
print  "                   :::.::.. .. .  ...:::IIHHMMMMHMV:"
print  "                     :V::... . .I::IHHMMV:."
print  "                       .:VHVHHHAHHHHMMV::."
print CSI + "0m"
print "... SINCRONICX SITE SHRINK v.0.1 ... type enter to continue "
raw_input()
str1=raw_input("TYPE THE SITE URL TO SHRINK >>>> ")
start_date=os.system("date")

print ""
print "SHRINK URL ",str1 
print ""
print str(os.system("date")) 
print "relax and drink a cofee! "

import subprocess
p = subprocess.Popen(["wget", "-r", "-p","-U","Mozilla",str1], stdout=subprocess.PIPE)
output, err = p.communicate()
print  output

if str1 == "":
 print "please type the url and try again ..."
 import sys
 sys.exit()
 print "Good bye!"


