from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()

# MySQL connection setup
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        correct_answers = 0
        questions = request.form.getlist('questions')
        for question_id in questions:
            selected_answer = request.form.get(f'answer_{question_id}')
            cursor.execute("SELECT correct_option FROM questions WHERE id = %s", (question_id,))
            result = cursor.fetchone()
            if result:
                correct_option = result[0]
                if selected_answer == correct_option:
                    correct_answers += 1
        user_name = request.form['user_name']
        cursor.execute("INSERT INTO quiz_results (user_name, score) VALUES (%s, %s)", (user_name, correct_answers))
        db.commit()
        return redirect(url_for('index'))
    return render_template('quiz.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        cursor.execute("INSERT INTO contact_messages (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
        db.commit()
        return redirect(url_for('index'))
    return render_template('contact.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        feedback_text = request.form['feedback']
        cursor.execute("INSERT INTO feedback (name, email, feedback) VALUES (%s, %s, %s)", (name, email, feedback_text))
        db.commit()
        return redirect(url_for('index'))
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)
