# File we are going to run when wanting to start the website.

from website import create_app


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
 