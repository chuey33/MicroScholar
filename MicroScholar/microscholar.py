# import wikipedia
import requests
# from bs4 import BeautifulSoup

def wiki_url(keyword):
    response = requests.get('http://localhost:1995/get_url/' + keyword)
    print(response.text)


def youtube_url(keyword):
    response = requests.get('http://localhost:8888/get_video/' + keyword)
    print(response.text)


if __name__ == '__main__':
    print("Welcome to MicroScholar - a tiny, wonderful source of knowledge. What is your name? ")
    name = input()
    print("Nice to meet you,  " + name + "!")
    keyword = input("What topic would you like to learn about today? ")
    results = wiki_url(keyword)
    print(results)
    print("Thank you for using MicroScholar! Here is a link to a Youtube video to learn more about " + keyword)
    you_url = youtube_url(keyword)
    print("Hope you enjoyed the video. Isn't learning wonderful? Enjoy your learning journey and we hope you use our program again soon!")






