from flask import Flask, send_from_directory, request, render_template, render_template_string, redirect, url_for
import re

app = Flask(__name__)
app.config.from_pyfile('config.py')

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = "[**FLAG**]"

# secret is only number and lowercase
secret = "secret6_k24ey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query', None)
    if query == None:
        return render_template("search.html", query=None, result=None)
    if query == secret:
        return render_template("search.html", query=query, result=FLAG)

    if query != "" and query in secret:
        return render_template("search.html", query=query, result=(query in secret))
    return render_template("search.html", query=query, result=None)




# robots.txt
@app.route('/robots.txt')
def robot_to_root():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
