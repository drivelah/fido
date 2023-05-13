import requests

def get_answer(question):
  url = "https://api.duckduckgo.com/?q=" + question
  response = requests.get(url)
  answer = response.json()["results"][0]["text"]
  return answer
