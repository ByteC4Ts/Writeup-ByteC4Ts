from flask import Flask, render_template, request
from ldap3 import Server, Connection, ALL

app = Flask(__name__)

ADMIN_PASSWORD = "STYE0P8dg55WGLAkFobiwMSJKix1QqpH"


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        server = Server('localhost', port=389, get_info=ALL)

        conn = Connection(server, 
                          user=f'cn=admin,dc=bts,dc=ctf',
                          password=ADMIN_PASSWORD,
                          auto_bind=True)
        
        if not conn.bind():
            return 'Failed to connect to LDAP server', 500

        conn.search('ou=people,dc=bts,dc=ctf', f'(&(employeeType=active)(uid={username})(userPassword={password}))', attributes=['uid'])

        if not conn.entries:
            return 'Invalid credentials', 401

        return render_template('index.html', username=username)
    
    return render_template('login.html')
