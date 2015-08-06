#!/bin/bash

sh run_tool_shed.sh --bootstrap_from_tool_shed null &

while [ `tail -qn 1 tool_shed_webapp.log 2> /dev/null | grep -qs "serving on" ; echo $?` -ne 0 ]; do
	sleep 5
done
echo "now serving"
api_key=`curl -s --user toolshed@galaxy.org:toolshed http://192.168.59.103:9009/api/authenticate/baseauth/ | sed 's/.\+api_key[^0-9a-f]\+\([0-9a-f]\+\).\+/\1/'`

python ./setup_basic_toolshed.py -a $api_key -u devteam,iuc,rnateam
python lib/tool_shed/scripts/api/create_categories.py -a $api_key -f 'https://toolshed.g2.bx.psu.edu/' -t 'http://192.168.59.103:9009/'

echo "Shutting down toolshed"
python ./scripts/paster.py serve tool_shed_wsgi.ini --pid-file=tool_shed_webapp.pid --log-file=tool_shed_webapp.log --stop-daemon
echo "Toolshed shutdown, exiting.."
exit 0
