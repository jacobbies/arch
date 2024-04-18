import json
import requests
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

targetUrl = 'https://books.toscrape.com/'
response = requests.get(targetUrl)
html_text = response.text

completion = client.chat.completions.create(
  model="gpt-4-1106-preview", # Feel free to change the model to gpt-3.5-turbo-1106
  messages=[
    {"role": "system", "content": "You are a master at scraping and parsing raw HTML."},
    {"role": "user", "content": html_text}
  ],
  tools=[
          {
            "type": "function",
            "function": {
              "name": "parse_data",
              "description": "Parse raw HTML data nicely",
              "parameters": {
                'type': 'object',
                'properties': {
                    'data': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'title': {'type': 'string'},
                                'rating': {'type': 'number'},
                                'price': {'type': 'number'}
                            }
                        }
                    }
                }
              }
          }
        }
    ],
   tool_choice={
       "type": "function",
       "function": {"name": "parse_data"}
   }
)

argument_str = completion.choices[0].message.tool_calls[0].function.arguments
arguments_dict = json.loads(argument_str)
data = arguments_dict['data']

for book in data:
    print(book['title'], book['rating'], book['price'])
