from website import create_app

app = create_app()

if __name__ == '__main__':
    # Todo: set this in an environment variable or command line option, not in code
    app.run(debug=True)
