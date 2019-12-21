from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()

app = Flask(__name__)
mysql.init_app(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'test 1'

print(app)

@app.route("/")
def hello():
    cur = mysql.connection.cursor()
    cur.execute('select * from user')
    result = cur.fetchall()
    print(result)
    return 'success'

if __name__ == "__main__":
    app.run()




