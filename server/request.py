import g4f
import sys
import platform
import json

import asyncio

#its fix for Windows
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
messages_json = sys.argv[2]
messages = json.loads(messages_json)

response = g4f.ChatCompletion.create(
    #model=sys.argv[1],
    model="gpt-3.5-turbo",
    messages=messages,
    #messages=[{"role": "user", "content": sys.argv[2]}],
)

print(response)
