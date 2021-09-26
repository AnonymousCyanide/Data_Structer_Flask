from datetime import datetime
from flask import Flask , request , jsonify
from sqlite3 import Connection as SQLite3Connection 
from sqlalchemy import event
from sqlalchemy.engine import Engine
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import linkedlist
#app
app = Flask(__name__)
#app config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlitedb.file'
app.config['SQL_TRACK_MODIFICATION'] = 0
# configure sqlite3 to enforce foreign key constraints
@event.listens_for(Engine, 'connect')
def _set_sqlite_pragma(db_apiconnection, connection_record):
    if isinstance(db_apiconnection, SQLite3Connection):
        cursor = db_apiconnection.cursor()
        cursor.execute("PRAGMA foreign_key = ON;")
        cursor.close()
db = SQLAlchemy(app)
now = datetime.now()

# Models
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(70))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    posts = db.relationship("BlogPost")
    
class BlogPost(db.Model):
    __tablename__ = 'blog_post'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(500))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

# Routes
@app.route('/user',methods=['POST'])
def create_user():
    data = request.get_json()
    
    new_user = User(
        name = data['name'],
        email = data['email'],
        address = data['address'],
        phone = data['phone'],
        
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message':'user created'}), 200

@app.route('/user/descending_id',methods=['GET'])
def get_all_users_descending():
    users = User.query.all()
    ll = linkedlist.LinkedList()
    for user in users:
        ll.insert_beginning(
            {
                'id':user.id,
                'name':user.name,
                'email':user.email,
                'phone':user.phone,
                'address':user.address,
            }
        )
    return jsonify(ll.to_array())


@app.route('/user/ascending_id',methods=['GET'])
def get_all_users_ascending():
    pass


@app.route('/user/<user_id>',methods=['GETT'])
def  get_one_user(user_id):
    pass


@app.route('/user/descending_id',methods=['DELETE'])
def delete_user(user_id):
    pass


@app.route('/blog_post/<user_id>',methods=['POST'])
def create_blog_post(user_id):
    pass


@app.route('/blog_post/<blog_post_id>',methods=['GET'])
def get_one_blog_post(blog_post_id):
    pass

@app.route('/blog_post/<user_id>',methods=['GET'])
def get_all_blog_post(user_id):
    pass

@app.route('/blog_post/<blog_post_id>',methods=['GET'])
def delete_one_blog_post(blog_post_id):
    pass

if __name__ == '__main__':
    app.run(debug=True)