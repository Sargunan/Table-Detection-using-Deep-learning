# -*- encoding: utf-8 -*-

from webapp import app
#from cocoapp.cocomodel import *  # clunky for now - needs to be this path for unpickling model

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config['DEBUG'], port=app.config['PORT'], use_reloader=False)
