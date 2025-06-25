from flask import Flask
from db import Db
from student_api import StudentAPI

class Program:
    def __init__(self):
        self.app = Flask(__name__)
        self.db_instance = Db()
        self.db_instance.init_app(self.app)

        self.setup_database()
        self.register_routes()

    def setup_database(self):
        self.app.app_context().push() 
        self.db_instance.db.create_all()

    def register_routes(self):
        api = StudentAPI()
        self.app.add_url_rule('/', view_func=api.show_all)
        self.app.add_url_rule('/new', view_func=api.new, methods=['GET', 'POST'])

    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    programa = Program()
    programa.run()  