from flask import Flask, render_template, redirect, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import false
app = Flask(__name__)
author = "Sang ah Park 70309"
fruits = ["apple", "banana", "cherry", "peach", "melon", "mango"]
cars = ["Tesla", "Toyota", "Volvo", "Jeep", "Ford", "Audi"]

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.today())

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route("/")
def index():   
    return render_template('index.html', author=author)

@app.route('/todo', methods=['POST', 'GET'])
def todo():
    if request.method == 'POST' :
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/todo')
        except:
            return 'There was an issue adding your task'     
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('todo.html', tasks=tasks, author=author)   

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/todo')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/todo')
        except:
            return 'There was an issue updating your task'
    else: 
        return render_template('update.html', task=task, author=author)

@app.route('/about')
def about():
    return render_template('/about.html', author=author)

@app.route('/calculator')
def help():
    return render_template('/calculator.html', author=author)

@app.route("/forloop")
def valuefunction():
    return render_template("forloop.html", fruits = fruits, cars = cars)

if __name__ == "__main__":
    app.run(debug=True)
