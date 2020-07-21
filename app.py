from prediction import Prediction, Preprocessing
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text as sa_text
from database import db_session, init_db
from models import Triplete

app = Flask(__name__)

@app.route('/')
def index():
    session = init_db()
    tripletes = session.query(Triplete).filter(Triplete.predicate == 'title')
    return render_template('index.html', tripletes=tripletes)

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        search = request.form['search']
        # Preprocesar entrada de texto
        result = Prediction
        search = Preprocessing.pre_process(search)
        p = result.predicty(search)
        print(p)
        tripletes = []
        session = init_db()
        for i in p[0] :
            i = i.replace('__label__', '')
            i = i.replace('-', ' ')
            i += '?show=full'
            aux = session.query(Triplete).filter(Triplete.predicate == 'title')
            print(aux)
            for a in aux :
                if a.subject == i :
                    tripletes.append(a)
            print(i)
    return render_template('index.html', tripletes=tripletes)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    print('Database session removed')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()