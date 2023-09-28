import g4f
import sys

#this is for the future
#import json

#import asyncio

#its fix for Windows
#asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    #messages=script_parameters,
    messages=[{"role": "user", "content": sys.argv[1]}],
)

print(response)
