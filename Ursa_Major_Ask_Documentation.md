# Ursa Major Ask: AI-Powered Research Computing Assistant

## 1. High-Level Overview

Ursa_Major_Ask is a command-line tool that leverages OpenAI's GPT-3.5-turbo model to simulate a conversation with a fictional "Director of Research Computing." This AI persona is designed to be an expert in Google's Ursa Major platform, a customized version of Google Cloud Platform (GCP) tailored for research, as well as related technologies like VertexAI, BigQuery, Google's HPC Toolkit, Slurm, Google Drive, GCS, and rclone.

The main purpose of Ursa_Major_Ask is to assist researchers and academics by:
*   Generating code and scripts for various research computing tasks.
*   Executing these generated scripts to provide immediate results.
*   Analyzing data from files.
*   Providing an accessible interface for these capabilities.

It aims to simplify complex computing tasks and make advanced AI-driven research tools more accessible.

## 2. What It Does (Capabilities)

Ursa_Major_Ask offers a range of functionalities to aid in research computing:

*   **Code Generation:**
    The tool can generate scripts in various languages based on natural language prompts from the user. Supported and exemplified languages include:
    *   Python
    *   Bash shell scripts
    *   Slurm submission scripts (for HPC job scheduling)
    *   Nextflow scripts (for bioinformatics workflow management)
    For example, a user can ask it to: `"Generate and run a Slurm script that runs a Python script called 'my_analysis.py' on a cluster with a partition named 'research'."`

*   **Script Execution:**
    Using the `-r` or `--run` command-line flag, Ursa_Major_Ask can immediately execute the scripts it generates. This provides real-time feedback and actionable results. For instance:
    `Ursa_Major_Ask -r write a Python script that prints Hello, World`
    This command will generate a Python script to print "Hello, World!" and then run it, displaying the output in the console.

*   **Data Analysis:**
    Ursa_Major_Ask can process and analyze data from various file types. Users can pass file content as part of their prompt, and the underlying GPT-3.5-turbo model will interpret the data based on the user's query. Examples include:
    *   Analyzing trends from CSV files: `Ursa_Major_Ask analyze the sales trend "$(cat sales_data.csv)"`
    *   Identifying critical errors in log files: `Ursa_Major_Ask find critical errors "$(cat server.log)"`
    *   Interpreting user behavior from JSON or XML data: `Ursa_Major_Ask interpret user behavior "$(cat user_data.json)"`

*   **Gradio Web Interface:**
    The tool provides an interactive web-based interface using Gradio. This is launched with the `-l` or `--live` flag:
    `Ursa_Major_Ask -l`
    This interface allows users to interact with Ursa_Major_Ask through a web browser, making it accessible from various devices, including mobile phones. It also facilitates easier sharing of work and collaboration.

## 3. How It Works (Workflow)

The Ursa_Major_Ask project follows a structured workflow to process user requests:

1.  **User Input:**
    *   **Command Line (CLI):** Users invoke `Ursa_Major_Ask` with their request as a text argument (the `transcript`). Flags like `-r` (run), `-w` (write), or `-l` (live/Gradio) dictate the desired action.
    *   **Gradio Interface:** When `-l` is used, a Gradio web UI starts. User input from this interface is passed to the backend.

2.  **OpenAI API Interaction (Script Generation):**
    *   The user's input (transcript) is sent to a function (e.g., `call_gpt`).
    *   This function constructs a prompt for the OpenAI GPT-3.5-turbo model. It uses the `director` prompt defined in `prompts.py`. The `director` prompt sets the AI's persona as the "Director of Research Computing," knowledgeable in Ursa Major, GCP, Slurm, VertexAI, BigQuery, etc. This ensures the AI's response is contextually relevant.
    *   The OpenAI API processes this combined prompt and returns a text response, which is expected to be the generated script or code.

3.  **Script Type Detection:**
    *   The generated text from the AI is then analyzed to determine its programming language or script type (e.g., Python, Bash).
    *   The `detect_script_type` function handles this. It sends the generated script content to the OpenAI API again, but this time using the `script_detector` prompt (also from `prompts.py`).
    *   The `script_detector` prompt instructs the AI to return only the two-character file extension (e.g., `py`, `sh`, `js`) corresponding to the script's content.

4.  **Code Cleaning:**
    *   The AI-generated script undergoes a cleaning process by the `result_code_cleaning(result)` function. This involves several steps to improve usability:
        *   `remove_blank_first_line(result1)`: Removes any leading blank line.
        *   `remove_first_line_if_not_shebang(text)`: Removes the first line if it's not a valid shebang (e.g., `#!/bin/bash`), as LLMs often add introductory text.
        *   `strip_triple_backticks(result1)`: Removes triple backticks (```) that commonly enclose code blocks generated by LLMs.

5.  **Saving the Script (Optional but typical before execution):**
    *   The `save_to_file(result1, file_extension)` function takes the cleaned script and the detected file extension.
    *   It saves the script to a local file, typically named `run.<ext>` (e.g., `run.sh`, `run.py`).

6.  **Script Execution (Conditional):**
    *   If the user specified the `-r` (run) flag, or if execution is requested via the Gradio interface, the `run_script(filename)` function is called.
    *   This function uses Python's `subprocess.run` to execute the saved script file. The script's output is then usually displayed to the user.
    *   If the `-w` (write) flag is used, the script is saved but not executed.
    *   If neither `-r` nor `-w` is specified, the tool may simply print the AI's generated script to the console.

The main script (`Ursa_Major_Ask`) orchestrates these steps, with the `go_live_gradio` function specifically managing the workflow for the Gradio interface.

## 4. How to Run It

### Installation

1.  **Prerequisites:**
    *   Python 3.7 or higher.
    *   OpenAI API Python library version 0.27.2 or newer (`openai>=0.27.2`).
    *   Gradio (`gradio`).
    *   An active OpenAI API key.

2.  **Cloning the Repository (Implied First Step):**
    You'll need the project files. If you don't have them, clone the repository:
    ```bash
    # Replace <repository_url> with the actual Git repository URL
    git clone <repository_url>
    cd ursa_major_ask # Or the name of the directory created by git clone
    ```

3.  **Using the `install.sh` script (Recommended Method):**
    The project includes an `install.sh` script to automate setup.
    *   **Quick Install (downloads and runs the script):**
        ```bash
        curl -L https://raw.githubusercontent.com/UCR-Research-Computing/ursa_major_ask/main/install.sh | bash
        ```
    *   **Manual Execution (after cloning):**
        Navigate to the cloned repository directory.
        ```bash
        chmod +x install.sh
        ./install.sh
        ```
    *   **What `install.sh` does:**
        1.  Creates a `~/bin` folder in your home directory if it doesn't exist.
        2.  Copies the main `Ursa_Major_Ask` script into `~/bin`.
        3.  Sets execute permissions (755) for the script in `~/bin`.
        4.  Adds `~/bin` to your system's PATH environment variable (you may need to reload your shell configuration, e.g., `source ~/.bashrc`, or open a new terminal).
        5.  Installs required Python packages from `requirements.txt` using `pip`.

4.  **Manual Dependency Installation:**
    If you prefer or if `install.sh` has issues with dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    The `requirements.txt` file specifies:
    ```
    openai>=0.27.2
    gradio
    ```

5.  **Configuring the OpenAI API Key:**
    *   Create a file named `config.py` inside your `~/bin` directory (i.e., `$HOME/bin/config.py`).
    *   Add your OpenAI API key to this file as follows:
        ```python
        # ~/bin/config.py
        openai_key = "your-openai-api-key"
        ```
        Replace `"your-openai-api-key"` with your actual key.
    *   The script can also potentially pick up the key from an environment variable, but `config.py` is the explicitly documented method.

### Usage

1.  **Command-Line Interface (CLI):**
    Once installed and `~/bin` is in your PATH, you can use `Ursa_Major_Ask` from any terminal location.
    *   **General Syntax:**
        ```bash
        Ursa_Major_Ask [options] [transcript ...]
        ```
    *   `transcript ...`: Your question or instruction for the AI.
        *   **Example:**
            ```bash
            Ursa_Major_Ask "Write a Python script to list files in the current directory."
            ```
    *   **Options:**
        *   `-h, --help`: Display help message and exit.
        *   `-r, --run`: Generate and then immediately execute the script.
            ```bash
            Ursa_Major_Ask -r "write a script that prints fibonacci numbers up to 100"
            ```
        *   `-w, --write`: Generate and write the script to a file (e.g., `run.py`, `run.sh`) without executing.
            ```bash
            Ursa_Major_Ask -w "Create a bash script to check disk space."
            ```
        *   `-l, --live`: Launch the Gradio web interface.
            ```bash
            Ursa_Major_Ask -l
            ```

2.  **Gradio Web Interface:**
    *   Start by running:
        ```bash
        Ursa_Major_Ask -l
        ```
    *   This will output a local URL (e.g., `http://127.0.0.1:7860`). Open this URL in a web browser.
    *   The interface allows for interactive querying and can be accessed from other devices on the same network if firewall configurations permit.

3.  **Analyzing File Content:**
    You can pass file contents directly into the prompt using command substitution:
    ```bash
    Ursa_Major_Ask "Summarize this log file: $(cat server.log)"
    Ursa_Major_Ask "What are the key trends in this data? $(cat data.csv)"
    ```

This document provides a comprehensive guide to understanding, installing, and using the Ursa_Major_Ask tool, based on the information present in `README.md` and `prompts.py`.
