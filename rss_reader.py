import time
from inc.articles import check_new_articles

if __name__ == "__main__":
    while True:
        check_new_articles()
        
        time.sleep(12 * 60 * 60)
