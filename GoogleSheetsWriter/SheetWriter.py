
"""

Simple script to write data to a Google Sheet.

Neil Stewart
https://github.com/nmyster
"""
from __future__ import print_function
import os

import httplib2

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPE = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Write To Google Sheet'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(
    	credential_dir,
       'sheets.googleapis.com-python-quickstart.json'
    )

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def update_sheet(values, sheet_name):

	try:
		request_body = {
		    "valueInputOption": "RAW",
		    "data": {
			  "range": "{}!A1".format(sheet_name),
			  # "majorDimension": enum(Dimension),
			  "values": values
			},
			"includeValuesInResponse": "false"
		}

		request = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body=request_body)
		response = request.execute()
		print("Write complete")
		return True
	except Exception as e:
		print(e)
		return False
	

def create_sheet(sheet_name=None, rows=1, columns=1):
	print("Attempting to create a sheet called {}".format(sheet_name))
	create_sheet = {
		"requests": [
		{
		  "addSheet": {
		    "properties": {
		      "title": sheet_name,
		      "gridProperties": {
		        "rowCount": rows,
		        "columnCount": coloumns
		      },
		      "tabColor": {
		        "red": 0.0,
		        "green": 1.0,
		        "blue": 1.0
		      }
		    }
		  }
		}
	    
		]
	}

	request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetId, body=create_sheet).execute()
	
	if 'addSheet' in request['replies'][0].keys():
		print("Sheet created")
		if 'sheetId' in request['replies'][0]['addSheet']['properties'].keys():
			print("Formatting")
			sheet_id = request['replies'][0]['addSheet']['properties']['sheetId']
			format_sheet = {
				"requests": [
				{
			      "updateDimensionProperties": {
			        "range": {
			          "sheetId": sheet_id,
			          "dimension": "COLUMNS",
			          "startIndex": 0,
			          "endIndex": coloumns
			        },
			        "properties": {
			          "pixelSize": 300
			        },
			        "fields": "pixelSize"
			      }
			    },
			    {
			      "updateDimensionProperties": {
			        "range": {
			          "sheetId": sheet_id,
			          "dimension": "ROWS",
			          "startIndex": 0,
			          "endIndex": 1
			        },
			        "properties": {
			          "pixelSize": 50
			        },
			        "fields": "pixelSize"
			      }
			    },
				{
				  "repeatCell": {
				    "range": {
				      "sheetId":sheet_id,
				      "startRowIndex": 0,
				      "endRowIndex": 1
				    },
				    "cell": {

				      "userEnteredFormat": {
				        "backgroundColor": {
				          "red": 0.0,
				          "green": 0.0,
				          "blue": 0.0
				        },
				        "horizontalAlignment" : "CENTER",
				        "textFormat": {
				          "foregroundColor": {
				            "red": 1.0,
				            "green": 1.0,
				            "blue": 1.0
				          },
				          "fontSize": 12,
				          "bold": True
				        }
				      }
				    },
				    "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)"
				  }
				}
				]
			}
			request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetId, body=format_sheet).execute()
			return True
		
	return False

credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                'version=v4')
service = discovery.build('sheets', 'v4', http=http,
                          discoveryServiceUrl=discoveryUrl)

# Change this to the ID of the spreadsheet you wish to write to. This can be found in the Sheet URL
# e.g https://docs.google.com/spreadsheets/u/1/d/<spreadsheetId>
spreadsheetId = '1tOZqax-oNvsXOVlQe1vn9FeqConRBgDkltd_P0zADsI'
try:
	spreadhseet = service.spreadsheets().get(spreadsheetId=spreadsheetId).execute()

	# Get available Sheet Names
	sheet_names = [sheet['properties']['title'] for sheet in spreadhseet['sheets']]
	sheet_to_update = "HelloWorld"

	if sheet_to_update not in sheet_names:
		# Attempt to create the sheet
		if create_sheet(sheet_name=sheet_to_update, rows=2, columns=3):
			print("Sheet created called {}".format(sheet_to_update))

	sheetFile = [
		['Column Title A', 'Column Title D', 'Column Title C'],
		['Value 1 for Column A','Value 1 for Column B','Value 1 for Column C'],
		['Value 2 for Column A','Value 2 for Column B','Value 2 for Column C'],
		['Value 3 for Column A','Value 3 for Column B','Value 3 for Column C'],
		['Value 4 for Column A','Value 4 for Column B','Value 4 for Column C']
	]

	# Update Sheet
	if update_sheet(sheetFile, sheet_to_update):
		print("Writing Complete")


except Exception as e:

	print("Error with Spreadsheet. {}".format(str(e)))


