import sys
import os

print('+++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ ')
print()
print("PATH-variable for local folder added")
directory_of_this_file = os.path.dirname(os.path.realpath(__file__))
tempPathModules = os.path.abspath(os.path.join(directory_of_this_file,   'pytm1'))
print(tempPathModules)
sys.path.append(tempPathModules)
#print(sys.path)
print()
print('+++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ +++++ ')
print()

import tm1_loading
tm1l = tm1_loading.tm1_loading
import tm1_structure
tm1s = tm1_structure.tm1_structure

tm1Base = 'https://localhost:8015/api/v1/'
tm1AdminName = 'admin'
tm1AdminPW = ''
#deleteBefore = False
debugLevel = 0

# initialize tm1-script
tm1l=tm1l(tm1Base, tm1AdminName, tm1AdminPW, debugLevel)
tm1s=tm1s(tm1Base, tm1AdminName, tm1AdminPW, debugLevel)

print(tm1l.getListOf_Processes())
print(tm1s.getListOf_Dimensions())

sProcessProlog = "cDimName='date12'; \
If(DimensionExists(cDimName)=1); \
DimensionDestroy(cDimName); \
EndIf; \
DimensionCreate(cDimName);"

tm1l.createProcess("Test23", sProcessProlog)
tm1l.executeProcess("Test23")
#tm1.deleteProcess("Test2")