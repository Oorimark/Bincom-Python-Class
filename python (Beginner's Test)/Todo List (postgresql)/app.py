from django.shortcuts import redirect
from flask import Flask, render_template, request

from pathlib import Path
import sys

app = Flask(__name__)

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

try:
    from config.config import DB_REQUEST
    
    @app.route("/", methods=['POST'])
    def Index():
        res = DB_REQUEST.LoadList()
        return render_template('todo.html', props = res)

    @app.route("/insert", methods=['POST'])
    def Insert():
        DB_REQUEST.Insert(request.form['list'])
        return redirect("/")

    @app.route("/post/<id>")
    def Delete(id):
        DB_REQUEST.Delete(id)
        return redirect("/")
    
except Exception as e:
    @app.route("/")
    def someFun():
        return "<h3>Please connect the database using the sql command in the config.sql file</h3>"
    

if __name__ == "__main__":
    app.run(debug=True)