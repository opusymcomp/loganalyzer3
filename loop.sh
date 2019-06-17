#!/bin/bash

FILE=$1
DIR=`dirname $0`

TMP_FILENAME="rcglist.txt"

startcycle=0
endcycle=6000
opt=""

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
			opt="${opt} -s l"
			;;

		-r)
			opt="${opt} -s r"
			;;

		--side)
			if [ $# -lt 3 ]; then
				usage
				exit 1
			fi
			opt="${opt} -s ${3}"
			shift 1
			;;

		--team)
			if [ $# -lt 3 ]; then
				usage
				exit 1
			fi
			opt="${opt} -t ${3}"
			shift 1
			;;

		--each-cycle)
			opt="${opt} --each-cycle"
			;;

		--start-cycle)
			if [ $# -lt 3 ]; then
				usage
				exit 1
			fi
			opt="${opt} --start-cycle ${3}"
			shift 1
			;;

		--end-cycle)
			if [ $# -lt 3 ]; then
				usage
				exit 1
			fi
			opt="${opt} --end-cycle ${3}"
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
		python ${DIR}/main.py ${log} ${opt}
	else
		python ${DIR}/main.py ${log} ${opt} "--without-index"
	fi
	count=$(($count+1))
done

rm ${TMP_FILENAME}
