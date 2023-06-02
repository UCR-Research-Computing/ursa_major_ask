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
usage: Ursa_Major_Ask [-h] [-r] [-l] [-w] [transcript ...]

positional arguments:
  transcript   Transcript of the conversation

options:
  -h, --help   show this help message and exit
  -r, --run    Run the generated script
  -l, --live   Run using a gradio interface
  -w, --write  Write the generated script

example:
Ursa_Major_Ask your text here
```

Replace "your text here" with your desired questions.

# Running Generated Scripts with Ursa_Major_Ask

One of the truly unique and powerful features of Ursa_Major_Ask is the `-r` or `--run` option. This option gives you the incredible ability not only to have the AI generate code based on your requests, but also to execute the created script, providing you with immediate, actionable results.

## Real-Time Code Execution

Imagine having a conversation with an AI that not only understands your coding needs but also executes them in real time. With the `-r` or `--run` option, that's precisely what you get. No longer do you just get the code; you can execute it within the same environment.

```bash
Ursa_Major_Ask -r write a Python script that prints Hello, World
```
The command above generates a Python script that prints 'Hello, World!' and immediately executes it, outputting 'Hello, World!' to the console.

```bash
Ursa_Major_Ask -r write a script that prints fibonacci numbers up to 10000
```
```
Fibonacci Series up to 10000:
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765

completed running: run.sh
```
Here are a few examples that involve high performance computing (HPC) with Slurm and genomics research pipelines:

1. **Running a Job on a Slurm Managed HPC Cluster**

   Let's assume you want to submit a job that runs a Python script on your HPC cluster. You could use Ursa_Major_Ask to generate and execute a Slurm script for you:

   ```bash
   Ursa_Major_Ask -r "Generate and run a Slurm script that runs a Python script called 'my_analysis.py' on a cluster with a partition named 'research'."
   ```

   Ursa_Major_Ask will generate a Slurm script to submit a job that runs 'my_analysis.py' on the 'research' partition of your cluster, and then it will execute the script to submit the job.

2. **Automating a Genomics Pipeline**

   Imagine you are conducting genomics research and you need to automate a pipeline that involves multiple tools such as FastQC, Trimmomatic, and HISAT2. You could request:

   ```bash
   Ursa_Major_Ask -r "Generate and run a Bash script that runs FastQC on 'sample.fastq', trims the adapters using Trimmomatic, and then aligns the reads to the 'reference.fa' genome using HISAT2."
   ```

   Ursa_Major_Ask will generate a Bash script that runs FastQC on 'sample.fastq', trims the adapters using Trimmomatic, and aligns the reads to 'reference.fa' using HISAT2. It will then run this script for you.

3. **Creating and Running a Bioinformatics Workflow with Nextflow**

   If you need to create and run a bioinformatics workflow with Nextflow, you could ask Ursa_Major_Ask something like:

   ```bash
   Ursa_Major_Ask -r "Generate and run a Nextflow script that takes as input 'reads.fastq', runs FastQC for quality control, uses Trimmomatic for trimming, aligns with BWA, and finally calls variants with FreeBayes."
   ```

   Ursa_Major_Ask would create a Nextflow script that performs the specified workflow and then execute this script to start the workflow.

These examples show how Ursa_Major_Ask can be used in a scientific research setting, helping to automate tasks related to HPC and genomics research. The possibilities are endless, and Ursa_Major_Ask's utility extends as far as your needs and creativity can take it.

## Unleashing Endless Possibilities

This ability is more than a convenience—it's a game-changer. Whether you're creating a Python script, a Bash shell script, or even a complex data analysis pipeline, Ursa_Major_Ask can generate and execute it for you. You can leverage the full power of the OpenAI model, GPT-3.5-turbo, to analyze data, automate tasks, or even write software—all within a single command.

Moreover, since Ursa_Major_Ask can take any text file as an input, the possibilities are virtually limitless. You could feed it a data file and ask it to perform data analysis, input a requirements document and ask it to write the corresponding code, or provide a bug report and ask it to debug and fix the code for you.

With Ursa_Major_Ask, you are not just talking about code—you are bringing it to life, turning ideas into actions and solutions in a matter of seconds. Code generation and execution have never been so accessible and intuitive. It's not just a coding tool; it's your AI-powered coding assistant that understands your needs and acts on them in real time.

Unlock the full potential of your programming prowess with the power of Ursa_Major_Ask.

### Access Ursa_Major_Ask Anywhere with the Gradio Interface

With the Gradio Interface, Ursa_Major_Ask can be accessed in any web browser, including on your phone, acting like a mobile app. Simply run the command:

```bash
Ursa_Major_Ask -l 
```

![image](https://github.com/UCR-Research-Computing/ursa_major_ask/assets/54458298/2baebdd4-21a7-41aa-884c-3bfd4e3ad5bb)

This allows you to use Ursa_Major_Ask anytime, anywhere. Whether you're commuting, in between meetings, or just on-the-go, you can execute scripts, analyze data, and bring your coding ideas to life right at your fingertips.

The Gradio interface also allows for easy sharing of your work, making collaboration simple and efficient. Experience the convenience and power of Ursa_Major_Ask on any device with the Gradio interface.


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

For any queries, please reach out to us at research-computing@ucr.edu.



