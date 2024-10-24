import os

SENT_ARTICLES_FILE = 'sent_articles.txt'

def get_sent_articles():
    """Function to retrieve the list of articles already sent."""
    if not os.path.exists(SENT_ARTICLES_FILE):
        return []
    with open(SENT_ARTICLES_FILE, 'r') as f:
        return f.read().splitlines()

def save_sent_article(article_id):
    """Function to save an article as already sent."""
    with open(SENT_ARTICLES_FILE, 'a') as f:
        f.write(article_id + '\n')