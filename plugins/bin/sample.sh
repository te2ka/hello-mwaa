#!/bin/sh
set -e

usage() {
    cat <<EOF
    Usage:
        $(dirname $0) --date <value>
EOF
    exit 1
}

opts=$(getopt -o d: -l date: -- $@)
set -- $opts

while :
do
    case "$1" in
        -d | --date) _date=$2; shift;;
        --) shift; break;;
        *) echo "Unknown parameter: $1";;
    esac
    shift
done

echo $_date
echo "Other params: $@"

echo 'Sample script done.'
