'''API User Route tests'''
import unittest 
import json
from flask import Flask
from app.models import Users, Businesses
from app import app, db

class UserTestcase(unittest.TestCase):
    '''Test for class user'''
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres17!@localhost/weconnect_test'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
        self.app = app.test_client 
        db.init_app(app)
        with app.app_context():
            db.drop_all()
            db.create_all()            

        self.app().post("/api/v2/auth/register",
                    data=json.dumps(dict(email="nina@live",username="nina",
                                password="12345678")), content_type="application/json")      
            
    def test_create_user(self):
        response = self.app().post("/api/v2/auth/register",
                    data=json.dumps(dict(email="nesh@live",username="nesh",
                                password="12345678")), content_type="application/json")

        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response_msg,"Account successfully registered. Log In to access.")      

    def test_existing_username(self):
        response = self.app().post("/api/v2/auth/register",
                    data=json.dumps(dict(email="kmunene@live",username="nina",
                                password="12345678")), content_type="application/json")

        self.assertEqual(response.status_code, 409)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response_msg,"Username Taken!")       

    def test_existing_email(self):
        response = self.app().post("/api/v2/auth/register",
                    data=json.dumps(dict(email="nina@live",username="kmunene",
                                password="12345678")), content_type="application/json")

        self.assertEqual(response.status_code, 409)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response_msg,"Email Already Exists!")
    def test_login(self):
        response = self.app().post("/api/v2/auth/login",
                        data=json.dumps(dict(username="nina",password="12345678")),
                                         content_type="application/json")

        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response_msg["message"],"Welcome nina. Log In Succesful!")
        self.assertTrue(response_msg['token'])
    def test_wrong_password(self):
        response = self.app().post("/api/v2/auth/login",
                        data=json.dumps(dict(username="nina",password="1234")),
                                         content_type="application/json")

        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response_msg,"Invalid Password!")

    def test_non_existent_user(self):
        response = self.app().post("/api/v2/auth/login",
                        data=json.dumps(dict(username="anin",password="1234")),
                                         content_type="application/json")

        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual(response_msg,"Non-Existent User!")
        
         
        