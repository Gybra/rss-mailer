docker run -d --name rss-mailer-container \
  -e RSS_FEED_URL="https://tuo-feed-rss.com/feed/" \
  -e TO_EMAIL="destinatario@example.com" \
  -e SMTP_SERVER="smtp-server" \
  -e SMTP_PORT="smtp-port" \
  -e EMAIL="smtp-server" \
  -e PASSWORD="smtp-server" \
  rss_mailer
