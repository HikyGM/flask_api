from flask import request, jsonify
from config import application
from static.database import db_session
import static.database.__all_models as model


@application.route('/posts/<int:id_post>', methods=['GET'])
def get_one_post(id_post):
    db_sess = db_session.create_session()
    post = db_sess.query(model.Blog.Blog).get(id_post)
    if not post:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'provider': post.to_dict(only=(
                'id_post', 'title_post', 'author_post', 'data_time_post', 'path_im_post'))
        }
    )


@application.route('/posts', methods=['GET'])
def get_posts():
    db_sess = db_session.create_session()
    return jsonify(
        {
            'posts':
                [item.to_dict(only=('id_post', 'title_post', 'author_post', 'data_time_post', 'text_post'))
                 for item in db_sess.query(model.Blog.Blog).all()]
        }
    )


@application.route('/posts', methods=['POST'])
def post_posts():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['title_post', 'author_post', 'data_time_post', 'path_im_post',
                  'text_post']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    post = model.Blog.Blog(
        title_post=request.json['title_post'],
        author_post=request.json['author_post'],
        data_time_post=request.json['data_time_post'],
        path_im_post=request.json['path_im_post'],
        text_post=request.json['text_post']
    )
    db_sess.add(post)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@application.route('/posts/<int:id_post>', methods=['PUT'])
def put_posts(id_post):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['title_post', 'author_post', 'data_time_post', 'path_im_post',
                  'text_post']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    post = db_sess.query(model.Blog.Blog).get(id_post)
    if post:
        post.title_post = request.json['title_post']
        post.author_post = request.json['author_post']
        post.data_time_post = request.json['data_time_post']
        post.path_im_post = request.json['path_im_post']
        post.text_post = request.json['text_post']
        db_sess.merge(post)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'Not found'})


@application.route('/posts/<int:id_post>', methods=['DELETE'])
def delete_posts(id_post):
    db_sess = db_session.create_session()
    post = db_sess.query(model.Blog.Blog).get(id_post)
    if post:
        db_sess.delete(post)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'Not found'})
