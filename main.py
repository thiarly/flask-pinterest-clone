from pinterest import app, database

with app.app_context():
    database.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=70, debug=True)