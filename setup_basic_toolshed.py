import sys
import argparse
sys.path.append('/galaxy-central/lib/tool_shed/scripts/api/')
from common import submit

def main( options ):
	api_key = options.api
	url = 'http://192.168.59.103:9009/api/categories'
	data = dict ( name='A Test Category', description='Drop tests repositories here' )
	try:
		response = submit( url, data, api_key )
	except Exception, e:
		response = str( e )
		print "Error attempting to create category using URL: ", url, " exception: ", str( e )
	
	for username in options.users.split(","):
		email = '%s@test.org' % username
		password = 'testuser'
		data = dict( email=email,
		             password=password,
		             username=username )
		url = 'http://192.168.59.103:9009/api/users'
		try:
		    response = submit( url, data, api_key )
		except Exception, e:
		    response = str( e )
		    print "Error attempting to create user using URL: ", url, " exception: ", str( e )


if __name__ == '__main__':
	parser = argparse.ArgumentParser( description='add default cat' )
	parser.add_argument("-a", "--api", dest="api", required=True, help="API key" )
	parser.add_argument("-u", "--users", type=str, dest="users", required=False, help="Create users")
	options = parser.parse_args()
	main( options )
