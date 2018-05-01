# coding: utf-8
import json
from flask import Flask, jsonify, request, redirect, url_for, flash
from flask import render_template
from db import REDIS
import datetime
import time


app = Flask(__name__)


@app.route('/')
def index():
    todolist = [(id.decode('utf8'), json.loads(value))
                 for id, value in REDIS.hgetall('todolist').items()]
    return render_template('index.html', todolist=todolist)


@app.route('/del_todo', methods=['DELETE'])
def del_todo():
    if request.method == 'DELETE':
        todo_id = request.args.get('todo_id', None)
        if todo_id:
            REDIS.hdel('todolist',todo_id)
    return jsonify({"status": True})

@app.route('/add-todo/', methods=['POST'])
def add_todo():
    if request.method == 'POST':
        if request.form['id'] != '':
            todo = {}
            todo_id = request.form['id']
            todo['title'] = request.form['title']
            todo['descript'] = request.form['descript']
            todo['create'] = datetime.datetime.today().strftime('%Y/%m/%d %H:%M:%S')
            todo['due'] = request.form['due']
            todo['status'] = request.form['status']

            REDIS.hset('todolist',todo_id,json.dumps(todo))


    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
