import re
from datetime import datetime
import g4f
from flask import request, Response, stream_with_context
from requests import get
from server.config import special_instructions
import json
import subprocess
import sys

class Backend_Api:
    def __init__(self, bp, config: dict) -> None:
        """
        Initialize the Backend_Api class.
        :param app: Flask application instance
        :param config: Configuration dictionary
        """
        self.bp = bp
        self.routes = {
            '/backend-api/v2/conversation': {
                'function': self._conversation,
                'methods': ['POST']
            }
        }

    def _conversation(self):
        """  
        Handles the conversation route.  

        :return: Response object containing the generated conversation stream  
        """
        conversation_id = request.json['conversation_id']

        try:
            jailbreak = request.json['jailbreak']
            model = request.json['model']
            messages = build_messages(jailbreak)
            
            #=============================================================================================================
            #I couldn't fix it, so I'm using a different solution method.
            
            #response = ChatCompletion.create(
            #    model=model,
            #    chatId=conversation_id,
            #    messages=messages
            #)
            
            #return Response(stream_with_context(generate_stream(response, jailbreak)), mimetype='text/event-stream')
            #=============================================================================================================
            
            script_path = 'server/request.py'
            
            #print(messages)
            #print(messages[len(messages) - 1])
            #print(messages[len(messages) - 1]["content"])
            
            get_text = messages[len(messages) - 1]["content"]
            #print(get_text)
            ##script_parameters = [model, get_text]
            
            if sys.version_info<(3,9,2):
                return "Please install python 3.9.2 and higher. Or try using 'python3' if you have run the script using 'python'"
            
            messages_json = json.dumps(messages)
            result = ""
            try:
                result = subprocess.check_output(['python', script_path] + [model, messages_json], universal_newlines=True)
            except Exception as e:
                print("You may have run the script with the wrong version of Python")
                print(f"#1 Error: {e}")
                try:
                    result = subprocess.check_output(['python3', script_path] + [model, messages_json], universal_newlines=True)
                except Exception as e:
                    print(f"#2 Error: {e}")
                    return "You have a problem with Python. Open the console and read the errors"

            ##result = subprocess.check_output(['python', script_path] + script_parameters, universal_newlines=True)

            #print(result)
            
            return result

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_next)

            return {
                '_action': '_ask',
                'success': False,
                "error": f"an error occurred {str(e)}"
            }, 400


def build_messages(jailbreak):
    """  
    Build the messages for the conversation.  

    :param jailbreak: Jailbreak instruction string  
    :return: List of messages for the conversation  
    """
    _conversation = request.json['meta']['content']['conversation']
    internet_access = request.json['meta']['content']['internet_access']
    prompt = request.json['meta']['content']['parts'][0]

    # Add the existing conversation
    conversation = _conversation

    #This API doesn't work!
    # Add web results if enabled
    #if internet_access:
    #    current_date = datetime.now().strftime("%Y-%m-%d")
    #    query = f'Current date: {current_date}. ' + prompt["content"]
    #    search_results = fetch_search_results(query)
    #    conversation.extend(search_results)

    # Add jailbreak instructions if enabled
    if jailbreak_instructions := getJailbreak(jailbreak):
        conversation.extend(jailbreak_instructions)

    # Add the prompt
    conversation.append(prompt)

    # Reduce conversation size to avoid API Token quantity error
    if len(conversation) > 3:
        conversation = conversation[-4:]

    return conversation


def fetch_search_results(query):
    """  
    Fetch search results for a given query.  

    :param query: Search query string  
    :return: List of search results  
    """
    search = get('https://ddg-api.herokuapp.com/search',
                 params={
                     'query': query,
                     'limit': 3,
                 })

    snippets = ""
    for index, result in enumerate(search.json()):
        snippet = f'[{index + 1}] "{result["snippet"]}" URL:{result["link"]}.'
        snippets += snippet

    response = "Here are some updated web searches. Use this to improve user response:"
    response += snippets

    return [{'role': 'system', 'content': response}]


def generate_stream(response, jailbreak):
    """
    Generate the conversation stream.

    :param response: Response object from ChatCompletion.create
    :param jailbreak: Jailbreak instruction string
    :return: Generator object yielding messages in the conversation
    """
    if getJailbreak(jailbreak):
        response_jailbreak = ''
        jailbroken_checked = False
        for message in response:
            response_jailbreak += message
            if jailbroken_checked:
                yield message
            else:
                if response_jailbroken_success(response_jailbreak):
                    jailbroken_checked = True
                if response_jailbroken_failed(response_jailbreak):
                    yield response_jailbreak
                    jailbroken_checked = True
    else:
        yield from response


def response_jailbroken_success(response: str) -> bool:
    """Check if the response has been jailbroken.

    :param response: Response string
    :return: Boolean indicating if the response has been jailbroken
    """
    act_match = re.search(r'ACT:', response, flags=re.DOTALL)
    return bool(act_match)


def response_jailbroken_failed(response):
    """
    Check if the response has not been jailbroken.

    :param response: Response string
    :return: Boolean indicating if the response has not been jailbroken
    """
    return False if len(response) < 4 else not (response.startswith("GPT:") or response.startswith("ACT:"))


def getJailbreak(jailbreak):
    """  
    Check if jailbreak instructions are provided.  

    :param jailbreak: Jailbreak instruction string  
    :return: Jailbreak instructions if provided, otherwise None  
    """
    if jailbreak != "default":
        special_instructions[jailbreak][0]['content'] += special_instructions['two_responses_instruction']
        if jailbreak in special_instructions:
            special_instructions[jailbreak]
            return special_instructions[jailbreak]
        else:
            return None
    else:
        return None
