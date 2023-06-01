# Ursa Major Expert AI

The Ursa Major Expert AI is a powerful tool that leverages OpenAI's GPT-3.5-turbo to simulate a chat with a fictional 'Director of Research Computing' character who is an expert in Google's Ursa Major platform. 

## Getting Started

To get started, you will need to clone this repository and install the required dependencies.

## Prerequisites

The primary dependencies for this project are:

- Python 3.7 or higher
- OpenAI API Python client

Use the following command to install the OpenAI client:

```
pip install openai
```

Ensure that you have the OpenAI API key. Set this key in your environment variables or in the `config.py` file. 

## How it Works

The script accepts a transcript as a command line argument. The transcript is fed to the `ursa_major_expert` function which leverages GPT-3.5-turbo model to generate a response. The generated response is treated as a script. The script is then saved to a file with the correct file extension and executed.

## Usage

You can run the script from the command line with the following command:

```
python3 Ursa_Major_Ask "your text here"
```

Replace "your text here" with your desired input.

The `ursa_major_expert` function initiates a conversation with GPT-3.5-turbo, where it plays the role of a 'Director of Research Computing'. The character is described as an expert in Ursa Major, a Google Cloud Platform offering.

The AI returns a chat completion based on the input transcript, which is then saved to a file and executed.

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

