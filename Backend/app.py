from flask import Flask,request,redirect,url_for
from flask_cors import CORS, cross_origin
from flask import jsonify
from Backend.controller.user import UserController
app = Flask(__name__)
CORS(app)



#Login for user
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        user = UserController()
        result = user.valid_login(request.form)
        return result

#Logout
@app.route('/logout')
def logout():
    return "Logged out successfully"

@app.route('/signup',methods=['POST'])
def signup():
    user = UserController()
    if request.method == 'POST':
        inserted = user.insert(request.form)
        return inserted




if __name__ == '__main__':
    app.run()

