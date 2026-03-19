import requests
import json

url = "http://localhost:11434/api/generate"
data = {
    "model" : "llama3.2:1b",
    "prompt": "tell me about Ambati Suresh"
}

response = requests.post(url, json=data, stream=True)

#check the response status
if response.status_code == 200:
    print("Generated text: ", end=" ", flush=True)
    #Iterate over the streaming response
    for line in response.iter_lines():
        if line:
            #decode the line and parse the json
            decoded_line = line.decode("utf-8")
            result = json.loads(decoded_line)

            #Get the text from the response
            generated_text = result.get("response", "")
            print(generated_text, end="", flush=True)
else:
    print("Error:", response.status_code, response.text)


#Response
"""Generated text:  Ambati Suresh is an Indian medical researcher and scientist who has made significant contributions to the field of neuroscience. Here's a brief overview of his life and work:

Early Life and Education:
Ambati Suresh was born on August 3, 1957, in Hyderabad, India. He received his Bachelor's degree in Biochemistry from Osmania University, Hyderabad.
"""

"""
Generated text:  Ambati Suresh is an Indian cricketer who has played for the Indian national team. He was born on July 16, 1988, in Hyderabad, Telangana, India.

Suresh made his international debut in 2006 and has since become one of the most successful batsmen in Indian cricket history. He is known for his aggressive batting style and ability to score big runs.

Some of his notable achievements include:

* 34 Test centuries, which is a record for the Indian team
* 23 One-Day International (ODI) centuries, making him the second-highest scorer in Indian ODI history
* The highest run-scorer in ODIs by an Indian batsman with 9,378 runs
* A member of the Indian Team that won the 2007 ICC World Twenty20

Suresh has also played for the Hyderabad City Runners and is a part-owner of the Deccan Chargers in the Indian Premier League (IPL).% 
"""