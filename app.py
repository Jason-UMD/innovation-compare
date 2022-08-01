import db_helpers as db
import api_helpers as api
import psycopg2
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, url_for, flash, redirect, Response
from werkzeug.exceptions import abort
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

min_sup = 1

token = 'Your Elsevier InstToken'
key = 'Your Elsevier API Key'
epoch = 2000

@app.route("/")
def index():
    topics = db.get_topic(-1)
    return render_template('index.html', topics=topics)

def plot_png(topic_id):
    keywords = db.get_keywords(topic_id)
    title = db.get_topic(topic_id)[2]
    
    usa = []
    china = []
    x = range(epoch,2022)
    
    for year in x:
        print(year)
        usa.append(api.fetch_papers(keywords, token, key, year, 'United States'))
        china.append(api.fetch_papers(keywords, token, key, year, 'China'))
                
    fig, ax = plt.subplots()
    ax.plot(x, usa, color='blue', label='United States')
    ax.plot(x, china, color='red', label='China')
    ax.set_ylabel("Papers Published")
    ax.set_title(title)
    ax.legend()
    
    plt.savefig("static/" + str(topic_id) + ".png")

@app.route('/<int:topic_id>', methods=('GET', 'POST'))
def topic(topic_id):
    topic = db.get_topic(topic_id)
    if topic is None:
        abort(404)
    seeds_str = db.to_str(db.get_seeds(topic[0]))
    keywords_str = db.to_str(db.get_keywords(topic[0]))
    
    if request.method == 'POST':
        if request.form['button'] == 'save':
            title = request.form['title']
            seed_papers = request.form['seed_papers'].splitlines()
            keywords = request.form['keywords'].splitlines()

            if not title:
                flash('Title is required!')
            else:
                new_id = db.update_topic(topic_id, title, seed_papers, keywords)
                return redirect(url_for('topic', topic_id=topic_id))
                
        elif request.form['button'] == 'fetch_keywords':
            seeds = db.get_seeds(topic_id)
            keywords = api.fetch_keywords(seeds, min_sup, token, key)
            db.delete_keywords(topic_id)
            db.insert_keywords(topic_id, keywords)
            return redirect(url_for('topic', topic_id=topic_id))
        elif request.form['button'] == 'gen_graph':
            plot_png(topic_id)

    return render_template('edit.html', topic=topic, seeds=seeds_str, keywords=keywords_str)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        seed_papers = request.form['seed_papers'].split('\n')

        if not title:
            flash('Title is required!')
        else:
            db.create_topic(title, seed_papers, [])
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/settings', methods=('GET', 'POST'))
def settings():
    global min_sup
    global token
    global key
    if request.method == 'POST':
        min_sup = int(request.form['min_sup'])
        token = request.form['token']
        key = request.form['key']
    return render_template('settings.html', min_sup=min_sup, token=token, key=key)

@app.route('/<int:topic_id>/delete', methods=('POST',))
def delete(topic_id):
    topic = db.get_topic(topic_id)
    db.delete_topic(topic_id)
    flash('"{}" was successfully deleted!'.format(topic[2]))
    return redirect(url_for('index'))

