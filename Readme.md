# python-django-react-sample-app

Sample BigCommerce App using Python, Django, and React

𝐇𝐨𝐰 𝐭𝐨 𝐫𝐮𝐧 𝐢𝐭 𝐢𝐧 𝐋𝐨𝐜𝐚𝐥 𝐦𝐚𝐜𝐡𝐢𝐧𝐞 ?

Open terminal frst.
You have to follow these points

1.Download anaconda

https://www.anaconda.com/products/individual

2. Open terminal.

3.create a virtual environment with python 3.8 using this commond "conda create --name py38 python=3.8"

4.Then activate virtua environment using this commond "conda activate py38"

5.Then run this commond "pip install -r requirements.txt"

6.Then run this commond to run project in local machine "python manage.py runserver 8054"

𝐅𝐎𝐫 𝐍𝐠𝐫𝐨𝐤 :
In .env file use http instead of https for callBackURL for ngrok.

---

𝐒𝐭𝐞𝐩𝐬 𝐭𝐨 𝐟𝐨𝐥𝐥𝐨𝐰 𝐭𝐨 𝐢𝐧𝐬𝐭𝐚𝐥𝐥 𝐭𝐡𝐞 𝐚𝐩𝐩 𝐨𝐧 𝐁𝐢𝐠𝐂𝐨𝐦𝐦𝐞𝐫𝐜𝐞𝐬𝐭𝐨𝐫𝐞.

𝗪𝗲 𝘄𝗶𝗹𝗹 𝗵𝗶𝗴𝗵𝗹𝘆 𝗿𝗲𝗰𝗼𝗺𝗺𝗲𝗻𝗱 𝘄𝗮𝘁𝗰𝗵𝗶𝗻𝗴 𝘃𝗶𝗱𝗲𝗼 𝗱𝘂𝗿𝗶𝗻𝗴 𝗶𝗻𝘀𝘁𝗮𝗹𝗹𝗮𝘁𝗶𝗼𝗻 𝗮𝗽𝗽 𝗼𝗻 𝘁𝗵𝗲 𝘀𝘁𝗼𝗿𝗲.
Here is installation video
https://youtu.be/FKf5pOBC3z0

1.Open Url https://login.bigcommerce.com/

2.login your account

3.from side menue go to Advance Setting > API Accounts

4.Click Create API Account then Create V2/V3 API Token

5.Fill Name of API

6.Select All Higer level Permissions

7.Open Url https://devtools.bigcommerce.com/my/apps

8.Create an App

9.Click View Client ID and Note down Client ID Client Secret

10.Open URL https://dashboard.heroku.com/apps

11.Create a new App

12.Select Deployment Method Github

13.Enable Automatic Deployment

14.go to setting tab

15.Click Reveal Config Variable and Add following Variables

appClientId = elfctt4r8cai3u6cw4yg70lamxroke8

appClientSecret = ee074094318cdbd56bba82dd7e1ba9df2f5794b51fdeb27c0e8ac0f88a95f904

16.callBackURL = https://inventroman.herokuapp.com/cb/auth

17.DISABLE_COLLECTSTATIC=1

18.DEBUG_COLLECTSTATIC = 1

19.From Deploy Tab Click Deploy Branch

20.Open Url https://devtools.bigcommerce.com/my/apps

21.Click Edit App and Go to Technical Tab of APP and Fill the following fields

22.Auth Callback URL (add /auth at the end of heroku app url)

23.Load Callback URL

24.Uninstall Callback URL

25.Click Update

26.Go to URl Open Url https://login.bigcommerce.com/

27.from side Menue Apps > My Apps

Note: To run React at development run "yarn run" and to compile Reactjs code run "yarn build" at root level folder.
