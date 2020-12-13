Python 3.8 is required for thsi App

Open Url https://login.bigcommerce.com/
login your account
from side menue go to Advance Setting > API Accounts
Click Create API Account then Create V2/V3 API Token
Fill Name of API
Select All Higer level Permissions

Open Url https://devtools.bigcommerce.com/my/apps
Create an App
Click View Client ID and Note down Client ID Client Secret

Open URL https://dashboard.heroku.com/apps
Create a new App
Select Deployment Method Github
Enable Automatic Deployment
go to setting tab
Click Reveal Config Variable and Add following Variables

apiToken = dwvhv8miusl07noqz7ax5crh9iox7l4
apiStoreHash = 4zjutairi8
appClientId = elfctt4r8cai3u6cw4yg70lamxroke8
appClientSecret = ee074094318cdbd56bba82dd7e1ba9df2f5794b51fdeb27c0e8ac0f88a95f904
callBackURL = https://inventroman.herokuapp.com/cb/auth
DISABLE_COLLECTSTATIC=1
DEBUG_COLLECTSTATIC = 1

From Deploy Tab Click Deploy Branch

Open Url https://devtools.bigcommerce.com/my/apps
Click Edit App and Go to Technical Tab of APP and Fill the following fields
Auth Callback URL (add cb/auth athe the end of heroku app url)
Load Callback URL
Uninstall Callback URL
Click Update

Go to URl Open Url https://login.bigcommerce.com/
from side Menue Apps > My Apps
go to My Draft Apps Tab and Install the App
