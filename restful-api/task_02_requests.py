#!/usr/bin/python3
"""Module that fetches and processes posts from JSONPlaceholder API."""
import csv
import requests


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print status and titles."""
    res = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(res.status_code))
    if res.status_code == 200:
        posts = res.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and save them to posts.csv."""
    res = requests.get('https://jsonplaceholder.typicode.com/posts')
    if res.status_code == 200:
        posts = res.json()
        data = [
            {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            }
            for post in posts
        ]
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data)
