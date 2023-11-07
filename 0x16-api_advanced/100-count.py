#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""

import requests
import re
import json
import BeautifulSoup

def count_words(subreddit, word_list,
    url="https://www.reddit.com/r/{}/hot/",
    start=None, counter=None):
    """
    Prints counts of given words found in hot posts of a given subreddit.
    """
    if not start:
        start = 0
    if not counter:
        counter = {}
    for word in word_list:
        word = word.lower()
        counter[word] = counter.get(word, 0)

    response = requests.get(url.format(subreddit), headers={"User-agent": "100-main"})
    if response.status_code != 200:
        print("Failed to query Reddit API.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a", class_="SQnoC3ObvgnGjWt90zD_" if start == 0 else "")
    for link in links:
        if "?count=" in link["href"]:
            return
        title = link.get_text()
        if not title:
            continue
        title = re.sub(r"[\W_]+", " ", title)
        title = title.lower()
        title = re.sub(r"\b({})\b".format("|".join(word_list)), r"\1 ", title)
        title = re.sub(r"\s+", " ", title)
        for word in word_list:
            counter[word] += title.count(word)

    next_link = soup.find("a", rel="next")
    if next_link:
        next_url = "https://www.reddit.com" + next_link["href"]
        return count_words(subreddit, word_list,
			   url=next_url, start=start+25,
     			   counter=counter)

    results = [(k, v) for k, v in counter.items() if v > 0]
    results.sort(key=lambda x: (-x[1], x[0]))
    for keyword, count in results:
        print("{}: {}".format(keyword, count))
