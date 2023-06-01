#!/usr/bin/env python3
# The above shebang line ensures that the script runs with python3 interpreter

# Importing necessary libraries
# openai - an API to connect to OpenAI's language model
# config - a module containing configurations such as API keys
# subprocess - a module for running system commands
# argparse - a module for parsing command line arguments
import openai
import config
import subprocess
import argparse
import os

# Setting the API key for OpenAI's API
openai.api_key = config.OPENAI_API_KEY

# Defining the function ursa_major_expert which takes a transcript as input and simulates a chat with a fictional 'Director of Research Computing' character.
def ursa_major_expert(transcript):

    # Defining an initial system message which sets the context and character's role.
    messages = [{"role": "system", "content": 'You are a Director of Research Computing at the University of California, Riverside. Ursa Major is a branded version of Google\'s GCP platform that uses the Google HPC Toolkit github site and google gcp researcher resources for help, information, and support. Slurm is the default cluster scheduler and it doesn\'t need walltime declarations and the default queue is named debug. Ursa Major uses Google Drive and GCS buckets for research storage and uses rclone to mount these to linux clusters. Respond to all input as an expert and give examples wherever possible. Respond to code requests with only the code don\'t explain anything or use markdown or identify the code but do use the shebang as the first line'}]
    
    # Adding user's transcript to the messages.
    messages.append({"role": "user", "content": transcript})

    # Making a request to OpenAI API to generate a chat completion based on the messages
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    # Extracting the system's message from the API response
    system_message = response["choices"][0]["message"]["content"]
    
    # Returning the system's message
    return system_message


# Defining function to detect the script type. This function takes in a script text, sends it to OpenAI API, and returns the type of script.
def detect_script_type(script_text):
    # Initiating a conversation with GPT-3.5-turbo
    messages = [
        {"role": "system", "content": "You are a skilled AI capable of identifying the type of a given script. Your task is to determine the type of the script based on its content. Only return the name of the file extension for the type of script it is, do not include any extra text at all no explanation or example whatsoever , just the file extension of the type of script it is."},
        {"role": "user", "content": script_text}
    ]

    # Sending the conversation to the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Extracting the AI's message from the response
    ai_message = response["choices"][0]["message"]["content"]

    # Only returning the type of script
    # If the AI's message doesn't follow the expected format, return the whole message
    try:
        script_type = ai_message.split(':')[1].strip()
    except IndexError:
        script_type = ai_message

    return script_type

# Defining function to save a string (result1) to a file with a given file extension
def save_to_file(result1, file_extension):
    file_name = f"run.{file_extension}"
    with open(file_name, 'w') as f:
        f.write(result1)

# Defining function to strip triple backticks from a string (result1)
def strip_triple_backticks(result1):
    stripped_result1 = result1.strip('`')
    return stripped_result1

# Defining function to execute a script given a filename. It first makes the script executable then runs it.
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

# Defining function to strip leading dot from a string (file_extension)
def strip_dot(file_extension):
    return file_extension.lstrip('.')

# Defining function to remove blank first line from a string (result1)
def remove_blank_first_line(result1):
    # Split the text by lines
    lines = result1.split('\n')

    # Remove the first line if it's blank
    if lines[0].strip() == '':
        lines = lines[1:]

    # Join the lines back together and return the result
    return '\n'.join(lines)

# Ensuring that the following code only runs when this script is run directly (and not when it is imported as a module)
if __name__ == "__main__":

    # Creating an ArgumentParser object
    parser = argparse.ArgumentParser()
    
    # Adding an argument for the transcript
    parser.add_argument("transcript", nargs='*', type=str, help="Transcript of the conversation")
    
    # Parsing the command line arguments
    args = parser.parse_args()

    # Joining the transcript arguments with newline characters in between
    transcript = '\n'.join(args.transcript)

    # Getting the expert's response to the transcript
    result1 = ursa_major_expert(transcript)
    
    # Removing triple backticks from the response
    stripped_result1 = strip_triple_backticks(result1)
    
    # Detecting the script type
    file_extension = detect_script_type(stripped_result1)
    
    # Removing leading dot from the file extension
    stripped_file_extension = strip_dot(file_extension)
    
    # Removing blank first line from the response
    stripped2_result1 = remove_blank_first_line(stripped_result1)
    
    # Saving the script to a file
    save_to_file(stripped2_result1, stripped_file_extension)
    
    # Constructing the filename
    file_name = f"run.{stripped_file_extension}"
    
    # Running the saved script
    run_script(file_name)

