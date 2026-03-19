import ollama
from rich import print_json

#list all the avaliable models using ollama API
# response = ollama.list()
# print(response)

#list all the running models using ollama API. Add mode='json' to convert all the dates to string and print
response = ollama.ps()
print_json(data=response.model_dump(mode='json'))