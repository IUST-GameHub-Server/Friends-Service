from ..Logic_Layer.FriendPanelLogic import friend_panel_logic
from flask import Flask

app = Flask(__name__)
config=""

@app.route('/Create_Friend_Panel')
def Create_Friend_Panel(email):
    return "Not Implemented"

@app.route('/Add_Friend')
def Add_Friend(friend_username):
        return "Not implimented"


@app.route('/Remove_Friend')
def Remove_Friend(friend_username):
        return "Not implimented"

@app.route('/Gift')
def Gift(friend_username):
        return "Not implimented"

@app.route('/invitation_To_Play')
def invitation_To_Play(friend_username):
        return "Not implimented"

@app.route('/ Games_History')
def Games_History():
        return "Not implimented"  

@app.route('/ Gifts_History')
def Gifts_History():
        return "Not implimented"  