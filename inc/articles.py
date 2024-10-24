import os
import feedparser
from inc.email import send_email
from inc.parser import get_sent_articles, save_sent_article

RSS_FEED_URL = os.getenv('RSS_FEED_URL', '')

def check_new_articles():
    """Main function to check new articles and send emails."""
    feeds = RSS_FEED_URL.split(',')

    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        sent_articles = get_sent_articles()
        
        for entry in feed.entries:
            article_id = entry.id
            if article_id not in sent_articles:
                title = entry.title
                link = entry.link
                content = entry.summary if 'summary' in entry else entry.description

                email_body = f"Title: {title}\nLink: {link}\n\n{content}"

                # Send email
                send_email(f"New Article: {title}", email_body)

                # Save article as sent
                save_sent_article(article_id)