# One hour challenge to take in two strings: one stale and
# one up to date, and a list of operations that the text
# editor conducted. The result would determine whether the
# list of operations would lead to the up to date string, 
# or if the list of operations was invalid in some way. 
# Test cases were provided by company, but have been removed
# to avoid being searchable if company still uses this challenge
# to vett potential candidates. 

import json

def isValid(stale, latest, otjson):
  parseResult = True
  opList = json.loads(otjson)
  cursorPosition = 0
  modifiedStale = stale

  for operation in opList:
    if operation['op'] == "skip":
      cursorPosition = int(cursorPosition + int(operation['count']))
      if cursorPosition > len(modifiedStale):
        parseResult = False
        break
    elif operation['op'] == "delete":
      deleteCounter = cursorPosition + operation['count']
      try:
        modifiedStale = "" + modifiedStale[0:cursorPosition] + modifiedStale[deleteCounter:]
      except:
        break
    elif operation['op'] == "insert":
      modifiedStale = "" + modifiedStale[0:cursorPosition] + operation['chars'] +  modifiedStale[cursorPosition:]
      cursorPosition += len(operation['chars'])

  if modifiedStale != latest:
    parseResult = False
  print(parseResult)
  return parseResult
