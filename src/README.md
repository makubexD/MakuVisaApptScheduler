# US VISA (ais.usvisa-info.com) appointment rescheduler for Canada

## Prerequisites
- Having a US VISA appointment scheduled already
- Google Chrome installed (to be controlled by the script)
- Python v3 installed (for running the script)
  
## How to Setup Telegram Notification
### Get your Telegram Bot token
1. Open the Telegram App and search for @BotFather and open it
2. Click on start to get detailed information and commands for creating bot, deleting the bot and etc …
3. Type or select /newbot to create a bot
4. Now it will send you a message, that to choose a name for your bot and type your own bot name (Eg: chat,chitti,Alex)
5. Now it will ask you to enter the username for your bot with the given condition like Alex_bot or Chat_bot or AlexBot. If the username is already take try it using different name but it should satisfy the condition
6. When it accepts your username it will send you a API token key like
   `142523231:AEX************`
7. In that message at top, you will see a link like t.me/AlexBot this will redirect to your bot chat, then click on /start to start chat with the bot
8. Add the token ID you received in previous step in `config.ini`
### Get your User ID
1. Look for @userinfobot on the Telegram
2. Press /start.
3. It will provide you with a User ID. Add it to `config.ini`

## Initial Setup
- Add your required information in the `config.ini` file. 
  > The SHOW_GUI should be False if you are using script in a remote terminal (e.g. Amazon EC2) which can not have GUI elements. 
- Install the required python packages: `pip3 install -r requirements.txt`

## Executing the script
- Simply run `python3 visa1.py`
  > If running on a remote terminal that does not have GUI (e.g. Amazon EC2), use `screen` command first to run it on a separate screen. Press `CTRL+a` and then `d` to detach from the screen, once the script is running. The script will keep running in the background. Use `screen -ls` to get your screen number. You can go back to screen by using `screen -r 12345` (replace 12345 with your actual screen number).
- That's it!

## Acknowledgement
Thanks to @yaojialyu & @cejaramillof for creating the initial versions to adapt.
