from flask import Flask, render_template, request, jsonify
from .api.RecEngine import rec_engine

# Static_folder: static resource, like css
# template_folder: template resource, like index.html
# static_url_path: Other resource
app = Flask(
    __name__,
    static_folder="./static",
    static_url_path="/",
    template_folder="./static")

@app.route('/')
def index():
    '''
        When browser visit the page, render index.html files in the dist folder.
    '''
    return render_template("index.html")

# Get message from user and return 
@app.route('/api/send_msg', methods=['POST'])
def sned_msg():

    # An example to show how to use the Class.
    recommend_list = rec_engine.get_list_by_genre('pop', [], 10)
    
    return_data = { # data return to FE
        "response": f"This is my response",
        "recommend_list": recommend_list
    }
    return jsonify(return_data)


if __name__ == '__main__':
    app.run()