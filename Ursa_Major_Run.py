#!/usr/bin/env python3

import openai
import config
import subprocess
import argparse

openai.api_key = config.OPENAI_API_KEY


def ursa_major_expert(transcript):

    messages = [{"role": "system", "content": 'You are a Director of Research Computing at the University of California, Riverside. Ursa Major is a branded verion of Googles GCP platfor that uses the Google HPC Toolkit github site and google gcp researcher researouces for help and informatiom and support. Slurm is the default cluster scheduler and it doesnt need walltime delarationas and the default queue is names debug. Ursa Major uses Google Drive and GCS buckets for research storage and uses rclone to mount these to linux clusters. Respond to all input in as an expert and gives examples where ever possiable. Respond to code requests with only the code dont explain anything or use markdown or identify the code but do use the shebang as the first line'}]
    messages.append({"role": "user", "content": transcript})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    system_message = response["choices"][0]["message"]["content"]
    return system_message

import openai
import config

# Set OpenAI API Key
openai.api_key = config.OPENAI_API_KEY

def detect_script_type(script_text):
    # Initiate a conversation with GPT-3.5-turbo
    messages = [
        {"role": "system", "content": "You are a skilled AI capable of identifying the type of a given script. Your task is to determine the type of the script based on its content. Only return the name of the file extention for the type of script it is, do not include any extra text at all no explaination or example what so ever , just the file extention of the type of script it is."},
        {"role": "user", "content": script_text}
    ]

    # Send the conversation to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extract the AI's message from the response
    ai_message = response["choices"][0]["message"]["content"]

    # Only return the type of script
    # If the AI's message doesn't follow the expected format, return the whole message
    try:
        script_type = ai_message.split(':')[1].strip()
    except IndexError:
        script_type = ai_message

    return script_type

def save_to_file(result1, fileextention):
    file_name = f"run.{fileextention}"
    with open(file_name, 'w') as f:
        f.write(result1)

def strip_triple_backticks(result1):
    stripped_result1 = result1.strip('`')
    return stripped_result1

import subprocess
import os

def run_script(filename):
    try:
        # Change the file permissions to make it executable
        subprocess.run(['chmod', '+x', filename], check=True)

        # Run the script
        script_path = os.path.join('./', filename)
        result = subprocess.run(script_path, capture_output=True, text=True, check=True)

        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print("Script execution failed with error: ", e.returncode)
        print("Error message: ", e.stderr)

def strip_dot(fileextention):
    return fileextention.lstrip('.')


def remove_blank_first_line(result1):
    # Split the text by lines
    lines = result1.split('\n')

    # Remove the first line if it's blank
    if lines[0].strip() == '':
        lines = lines[1:]

    # Join the lines back together and return the result
    return '\n'.join(lines)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("transcript", nargs='*', type=str, help="Transcript of the conversation")
    args = parser.parse_args()

    transcript = '\n'.join(args.transcript)


    import textwrap

    result1 = ursa_major_expert(transcript)
    stripped_result1 = strip_triple_backticks(result1)
    fileextention = detect_script_type(stripped_result1)
    stripped_fileextention = strip_dot(fileextention)
    stripped2_result1 = remove_blank_first_line(stripped_result1)
    save_to_file(stripped2_result1, stripped_fileextention)
    file_name = f"run.{stripped_fileextention}"
    run_script(file_name)

    #print("---------")
    #print(result1)
    #print("---------")

    #print(detect_script_type(result1))
