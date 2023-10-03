from flask import Flask, jsonify, request
from app import app
from app.openai.openai_api_call import generate_blog_post

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/generate-blog', methods=['POST'])
def generate_blog():
    try:
        data = request.get_json()
        articles = data.get('articles', [])
        keywords = data.get('keywords',[])  # Replace with your default prompt
        blogResult = generate_blog_post(articles,keywords)
        
        # Return the generated article as JSON
        return jsonify({'blog': blogResult})
    except Exception as e:
        return jsonify({'error': str(e)}), 500