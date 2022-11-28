from flask import jsonify, redirect, url_for
from Backend.dao.user import UsersDAO


class UserController:

    def build_usr_dict(self,row):
        result = {}
        result['user_email'] = row[0]
        result['user_password'] = row[1]
        result['user_name'] = row[2]
        result['user_lastname'] = row[3]
        return result

    def get_all_users(self):
        dao = UsersDAO()
        list = dao.get_all_users()
        list = []
        for row in list:
            result = self.build_usr_dict(row)
            list.append(result)
        return jsonify(users=list), 201

    def insert(self, form):
        email = form['user_email']
        password = form['user_password']
        name = form['first_name']
        last_name = form['last_name']

        if email and password and name and last_name:
            dao = UsersDAO()
            added = dao.insert(email,password,name,last_name)
            if added:
                result = {}
                result['user_email'] = email
                result['user_password'] = password
                result['first_name'] = name
                result['last_name'] = last_name
                return jsonify(users=email + " has been addded"),201
            else:
                return jsonify("User has already been added."),404

        else:
            return jsonify("Input is incomplete1")


    def valid_login(self, form):
        if form and len(form) == 2:
            user_email = form['user_email']
            user_password = form['user_password']
            dao = UsersDAO()
            db_password = dao.get_user_password(user_email)
            if db_password:
                if db_password == user_password:
                    return jsonify(Users="Entered."), 201
                else:
                    return jsonify(Error="Wrong password or email1"), 404
            else:
                return jsonify(Error = "Wrong password or email2"), 404
        else:
            return jsonify(Error = "Wrong password or email3"), 404


