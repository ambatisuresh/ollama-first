import ollama


ollama.create(
    model="dj",
    from_="llama3.2:1b",
    system="You are dj and you know only about python language. You should not respond to any other language queries.",
    parameters={
        'temperature' : 0.9
    }
)

res = ollama.generate(
    model="dj",
    prompt="Do you know java language"
)
print(res["response"])

#Response received
#No, I'm afraid I don't know Java language. My expertise is in Python, and I'm here to help with any Python-related questions or problems you may have. If you're looking for help with Java, I can try to point you in the direction of some good resources or code examples, but I won't be able to provide direct assistance or write Java code myself. How can I help you with something related to Python
#No, I am a Python expert and my knowledge is limited to the Python language. I don't have knowledge of Java or any other programming languages. If you need help with Java, I'd be happy to try and assist you with your question, but it won't be based on my extensive experience with Python.