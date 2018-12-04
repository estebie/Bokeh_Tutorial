#flask app

from flask import Flask, render_template
from BasicLine import js, div, cdn_css, cdn_js
from bokeh.embed import server_session
from bokeh.util import session_id

#instantiate the flask app
app = Flask(__name__)

#create index page function
@app.route("/")
def index():
    server_script = server_session(None, session_id=session_id.generate_session_id(), url="http://localhost:5006/slider")
    return render_template("index.html", graphname="Sliders", server_script=server_script)

#run the app
if __name__ == "__main__":
    app.run(debug=True)
