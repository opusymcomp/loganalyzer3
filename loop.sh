#!/bin/bash

FILE=$1
DIR=`dirname $0`

TMP_FILENAME="rcglist.txt"

startcycle=0
endcycle=6000

usage()
{
	(echo "Usage: $0 dirname [options]"
	 echo "Available options:"
	 echo "  --help           prints this"
	 echo "  -l|--side l      analyzes left team"
	 echo "  -r|--side r      analyzes right team"
	 echo "  --team TEAMNAME  analyzes TEAMNAME team"
	 echo "  --each-cycle     outputs results for each cycle"
	 echo "  --start-cycle    sets start cycle"
	 echo "  --end-cycle      sets end cycle"
	)
}


if [ ! -d $1 ]; then
	usage
	exit 1
fi

while [ $# -gt 0 ]
do
	case $2 in

		--help)
			usage
			exit 0
			;;

		-l)
			side="l"
			;;

		-r)
			side="r"
			;;

		--side)
			if [ $# -lt 3 ]; then
				usage
				exit 1
			fi
			side="${3}"
			shift 1
			;;

		--team)
			if [ $# -lt 3 ]; then
				usage
				exit 1
			fi
			team="true"
			teamname="${3}"
			shift 1
			;;

		--each-cycle)
			eachcycle="true"
			;;

		--start-cycle)
			if [ $# -lt 3 ]; then
				usage
				exit 1
			fi
			startcycle=$3
			shift 1
			;;

		--end-cycle)
			if [ $# -lt 3 ]; then
				usage
				exit 1
			fi
			endcycle=$3
			shift 1
			;;

	esac

	shift 1
done

ls ${FILE}*.rcg > ${TMP_FILENAME}
count=0

cat ${TMP_FILENAME} | while read log; do
	echo ${log}
	if [ $count -eq 0 ]; then
		python ${DIR}/main.py ${log} -s ${side} --start-cycle ${startcycle} --end-cycle ${endcycle}
	else
		python ${DIR}/main.py ${log} -s ${side} --without-index --start-cycle ${startcycle} --end-cycle ${endcycle}
	fi
	count=$(($count+1))
done

rm ${TMP_FILENAME}
