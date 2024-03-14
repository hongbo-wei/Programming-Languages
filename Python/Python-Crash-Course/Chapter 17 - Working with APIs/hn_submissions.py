# 17-2 Active Discussions

from operator import itemgetter
import plotly.express as px

import requests

# Make anm API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
print(submission_ids)

submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a new APIcall for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"{submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comment': response_dict['descendants']
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comment'),
                          reverse=True)

news, comments, news_links, hover_texts = [], [], [], []

for submission_dict in submission_dicts:
    news_title = submission_dict['title']
    news_url = submission_dict['hn_link']

    news_link = f"<a href='{news_url}'>{news_title}</a>"
    news_links.append(news_link)

    comments.append(submission_dict['comment'])

title = f"Most Commented News on Hacker News"
labels = {'x': 'News', 'y': 'Comments'}

fig = px.bar(x=news_links, y=comments, title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()
