# File we are going to run when wanting to start the website.

from website import create_app
# Imports | Initially from __init__
from website.views import views
from website.auth import auth

app = create_app()

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

if __name__ == '__main__':
    """
    - Only when this file is run, not import, this line is executed.
    Want this because if were to import main.py from another file it 
    would run this line which is the server. Want to run the web server
    from this file directly.
    - debug=True means any change to python code will automatically run
    the server
    """
    app.run(debug=True)
 