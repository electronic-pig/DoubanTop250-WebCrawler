import sqlite3

from flask import Flask, render_template, request
from flask_paginate import Pagination

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def home():
    # return render_template('index.html')
    return index()


@app.route('/movie', methods=['GET'])
def movie():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    con = sqlite3.connect('movieTop250.db')
    cur = con.cursor()
    sql = 'select * from movie250'
    data = cur.execute(sql).fetchall()  # 获取所有数据
    cur.close()
    con.close()

    paginated_data = paginate_data(data, page, per_page)

    pagination = Pagination(page=page, total=len(data), per_page=per_page)
    print(pagination.total)
    print(pagination.per_page)
    print(pagination.pages)
    return render_template('movie.html', movies=paginated_data, pagination=pagination)

def paginate_data(data, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    paginated_data = data[start:end]
    return paginated_data

@app.route('/score')
def score():
    scores = []  # 评分
    count = []  # 每个评分的电影数量
    con = sqlite3.connect('movieTop250.db')
    cur = con.cursor()
    sql = 'select score,count(score) from movie250 group by score'
    data = cur.execute(sql)
    for item in data:
        scores.append(str(item[0]) + '分')
        count.append(item[1])
    cur.close()
    con.close()
    return render_template('score.html', scores=scores, count=count)


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/word')
def word():
    return render_template('word.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
