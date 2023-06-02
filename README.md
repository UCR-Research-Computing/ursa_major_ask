# Ursa Major Ask

The Ursa Major Ask is a powerful tool that leverages OpenAI's GPT-3.5-turbo to simulate a chat with a fictional 'Director of Research Computing' character who is an expert in Google's Ursa Major platform. 

## Getting Started

To get started, you will need to clone this repository and install the required dependencies.

## Prerequisites

The primary dependencies for this project are:

- Python 3.7 or higher
- OpenAI API Python client

Use the following command to install the OpenAI client:

```
pip install -r requirements.txt
```

Ensure that you have the OpenAI API key. Set this key in your environment variables or in the `config.py` file. 

## How it Works

The script accepts a transcript as a command line argument. The transcript is fed to the `ursa_major_expert` function which leverages GPT-3.5-turbo model to generate a response. The generated response is treated as a script. The script is then saved to a file with the correct file extension and executed.

## Usage

You can run the script from the command line with the following command:

```bash
Ursa_Major_Ask "your text here"
```

Replace "your text here" with your desired questions.

# Running Generated Scripts with Ursa_Major_Ask

One of the truly unique and powerful features of Ursa_Major_Ask is the `-r` or `--run` option. This option gives you the incredible ability not only to have the AI generate code based on your requests, but also to execute the created script, providing you with immediate, actionable results.

## Real-Time Code Execution

Imagine having a conversation with an AI that not only understands your coding needs but also executes them in real time. With the `-r` or `--run` option, that's precisely what you get. No longer do you just get the code; you can execute it within the same environment.

```bash
Ursa_Major_Ask -r "Generate and run a Python script that prints 'Hello, World!'"
```

The command above generates a Python script that prints 'Hello, World!' and immediately executes it, outputting 'Hello, World!' to the console.

## Unleashing Endless Possibilities

This ability is more than a convenience—it's a game-changer. Whether you're creating a Python script, a Bash shell script, or even a complex data analysis pipeline, Ursa_Major_Ask can generate and execute it for you. You can leverage the full power of the OpenAI model, GPT-3.5-turbo, to analyze data, automate tasks, or even write software—all within a single command.

Moreover, since Ursa_Major_Ask can take any text file as an input, the possibilities are virtually limitless. You could feed it a data file and ask it to perform data analysis, input a requirements document and ask it to write the corresponding code, or provide a bug report and ask it to debug and fix the code for you.

With Ursa_Major_Ask, you are not just talking about code—you are bringing it to life, turning ideas into actions and solutions in a matter of seconds. Code generation and execution have never been so accessible and intuitive. It's not just a coding tool; it's your AI-powered coding assistant that understands your needs and acts on them in real time.

Unlock the full potential of your programming prowess with the power of Ursa_Major_Ask.

### Gradio interface

```bash
Ursa_Major_Ask -l 
```

![image](https://github.com/UCR-Research-Computing/ursa_major_ask/assets/54458298/2baebdd4-21a7-41aa-884c-3bfd4e3ad5bb)

The `ursa_major_expert` function initiates a conversation with GPT-3.5-turbo, where it plays the role of a 'Director of Research Computing'. The character is described as an expert in Ursa Major, a Google Cloud Platform offering.

The AI returns a chat completion based on the input transcript, which is then saved to a file and executed.

---

## Powerful File Input and Data Analysis

`Ursa_Major_Ask` isn't just designed to accept file input – it's built to harness the full potential of OpenAI's GPT-3 model, enabling sophisticated analysis and interpretation of the data you feed into it. This elevates `Ursa_Major_Ask` from a mere command-line tool to a versatile solution for a wide range of data processing tasks.

Whether you are dealing with scripts, structured text files, or raw data, `Ursa_Major_Ask` can process it, and utilize the language understanding capabilities of GPT-3 to provide meaningful insights.

The power of this approach lies in its versatility. You are not limited to scripts or programming languages; you can feed in any type of text file and let the model analyze it based on the question you ask.

### Examples

1. **Analyzing a CSV data file**: If you have a CSV file, `sales_data.csv`, containing sales data for a period, you could ask:

    ```
    Ursa_Major_Ask analyze the sales trend "$(cat sales_data.csv)"
    ```
    `Ursa_Major_Ask` will provide you with an interpretation of the sales trend based on the data in the file.

2. **Understanding Log Files**: You have a log file, `server.log`, and you want to know about any critical errors. You can ask:

    ```
    Ursa_Major_Ask find critical errors "$(cat server.log)"
    ```
    The command-line tool will provide a summary of the critical errors found in the log file.

3. **Interpreting Complex XML or JSON data**: You can even feed complex XML or JSON files. For instance, with a complex JSON data file `user_data.json`, you might want to understand the user behavior it signifies:

    ```
    Ursa_Major_Ask interpret user behavior "$(cat user_data.json)"
    ```
    `Ursa_Major_Ask` will then provide an interpretation of the user behavior based on the data.

Remember, `Ursa_Major_Ask` is as powerful and versatile as the questions you ask and the data you feed. It leverages the robustness of OpenAI's GPT-3 model to analyze, understand, and provide insights on a wide array of data. 

---

Please note that the file paths in these examples are relative. If your files are in different directories, be sure to include the correct paths. Also, ensure the data or text you're feeding into `Ursa_Major_Ask` does not contain sensitive or personal information, as it will be processed by an external AI model.
Gradio interface


## Note

This script is for educational and research purposes. It is not meant for production use.

## License

This project is licensed under the terms of the MIT license.

## Contributions

We welcome contributions to improve this project. Please feel free to create an issue or pull request.

## Contact

For any queries, please reach out to us at (your email here).

---

This README is a basic starting point for your project. You may want to further customize it to suit the specific needs of your project and provide more detailed instructions or explanations as needed.

