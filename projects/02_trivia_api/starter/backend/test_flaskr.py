import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category

DATABASE_NAME = "trivia_test"
DATABASE_PATH = "postgresql://postgres:postgres@127.0.0.1:5432/trivia_test"


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # load test data
        os.system(f'psql "{DATABASE_PATH}" {DATABASE_NAME} -c "DROP TABLE questions, categories;"')
        os.system(f'psql "{DATABASE_PATH}" {DATABASE_NAME} < ./trivia.psql')

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = DATABASE_NAME
        self.database_path = DATABASE_PATH
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_available_categories(self):
        response = self.client().get('/categories')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertEqual(len(data["categories"]), 6)
        self.assertEqual(data["categories"]["4"], "History")

    def test_list_questions(self):
        response = self.client().get('/questions')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertEqual(len(data["questions"]), 10)
        self.assertEqual(data["total_questions"], 19)

    def test_delete_question(self):
        pass

    def test_create_question(self):
        pass

    def test_search_questions(self):
        pass

    def test_category_questions(self):
        pass

    def test_quizzes(self):
        pass


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
