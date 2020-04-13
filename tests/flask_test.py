#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kanban.db'
db = SQLAlchemy(app)

#app = Flask(__name__)
#app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///kanban.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

class Todo(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
#    def __repr__(self):
#        return '<Task %r>' % self.id


#@app.route('/', methods=['POST','GET'])
#def index():
#    return render_template('Kanban_example.html')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('Kanban_example.html', tasks=tasks)



if __name__ == "__main__":
    app.run(debug=True)

