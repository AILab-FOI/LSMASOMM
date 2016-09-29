#!/bin/sh
# Unix AToM3 startup script (for convenience sake)
#
# Provide an argument such as ClassDiagramsV3_META to start AToM3 with the
# formalism "ClassDiagramsV3". Except for truly old formalisms, give the name
# of the *_META file for this argument.
#
# NOTE: the atom3NoSplash.py file can also start AToM3, the old difference
#       is that it doesn't show the logo for 2 seconds on startup...


sn=`dirname $0`
python $sn/atom3.py $1


