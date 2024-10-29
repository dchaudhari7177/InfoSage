from flask import Flask, request, render_template, redirect, url_for, flash
from transformers import pipeline
from database import init_db, insert_qa_pair, fetch_qa_history
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

question_answering = pipeline("question-answering", model="t5-base")

@app.route('/')
def home():
    qa_history = fetch_qa_history() 
    return render_template('index.html', qa_history=qa_history)

@app.route('/answer', methods=['POST'])
@app.route('/answer', methods=['POST'])
def answer():
    context = request.form['context']
    question = request.form['question']
    
    answer = question_answering(question=question, context=context)

    if answer and 'answer' in answer:
        response_answer = answer['answer']
    else:
        response_answer = "I'm sorry, I couldn't find an answer."

    insert_qa_pair(question, response_answer)

    qa_history = fetch_qa_history()  
    return render_template('index.html', answer=response_answer, qa_history=qa_history)


if __name__ == "__main__":
    init_db()  
    app.run(debug=True)
