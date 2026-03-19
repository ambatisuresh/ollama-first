import ollama
from rich import print_json

res = ollama.chat(
    model="llama3.2:1b",
    messages = [
        {"role":"user",
        "content":"Who is ambati suresh"}
    ],
#    stream=True
)

#It is very difficult to read the res directly so using rich library to format the chat response
print_json(data=res.model_dump())

#If you want to stream=True, then you will not be getting model_dump
#Iterate the response chunks
# for chunk in res:
#     print_json(data=chunk.model_dump(mode='json'))