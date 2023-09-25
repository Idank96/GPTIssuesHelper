from bs4 import BeautifulSoup
import requests
import openai
import g4f

using_openai = False


def get_url() -> str:
    url = input("Enter the url of the issue you want to solve: ")
    return url


def extract_issue_text(url: str) -> str:
    # Fetch the web page content from the URL

    response = requests.get(url)

    # Check the status code
    if response.status_code == 200:
        # Create a soup object from the web page content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the element that contains the issue text
        issue_element = soup.find("td", class_="d-block comment-body markdown-body js-comment-body")

        # Get the issue text as a string
        issue_text = issue_element.text.strip()

        # Remove the \n characters
        issue_text = issue_text.replace("\n", " ")

        # Remove the \t characters
        issue_text = issue_text.replace("\t", " ")

    else:
        # Handle the error
        print(f"Error: {response.status_code}")

    return issue_text


def create_prompt() -> str:
    pre_prompt = """
    You will be provided with a GitHub issue. 
    Your task is to write instructions and steps on how to solve the issue, based on the information given in the issue.
    Use the following format for your response:
    Start by providing an initial overview of the problem to a Python-competent computer science student who is new to the issue and new to github.
    Write a list of any technical jargon, technical terms that you use and explain each of the terms.
    List the steps in bullet points, using numbers for each step.
    Use clear and concise language.
    Provide code snippets or commands when necessary, using triple backticks to enclose them.
    Write at the end of your message "Good luck!".
    The issue is:
    """
    return pre_prompt


def connect_to_openai():
    path_to_key = "..\keys\openai_key.txt"
    # open file with key
    with open(path_to_key, "r") as file:
        my_key = file.read()

    openai.api_key = my_key


def init_model() -> str:
    if using_openai:
        model = "gpt-3.5-turbo"
    else:
        model = g4f.models.gpt_4
    return model


def get_steps_to_solve_openai(model: str, pre_prompt: str, issue_text: str) -> str:
    messages = [{'role': 'user',
                 'content': pre_prompt+issue_text}]

    response = openai.ChatCompletion.create(model=model,
                                            messages=messages,
                                            max_tokens=1000,
                                            temperature=0)
    generated_text = response['choices'][0]['message']['content']

    return generated_text


def display_steps(steps_to_solve: str):
    # Split by \n:
    steps_to_solve_seperated = steps_to_solve.split("\n")
    # Display the text beautifully:
    for step in steps_to_solve_seperated:
        print(step)


def get_steps_to_solve_g4f(model, pre_prompt, issue_text):
    messages = [{'role': 'user',
                 'content': pre_prompt + issue_text}]
    response = g4f.ChatCompletion.create(
        model=model,
        messages=messages,
    )
    return response


def write_to_file(steps_to_solve: str, issue_id: str):
    # Write to file:
    with open(issue_id + ' Guide' + '.md', "w") as file:
        file.write(steps_to_solve)


def main():
    url = get_url()
    issue_text = extract_issue_text(url)
    pre_prompt = create_prompt()
    model = init_model()
    print('Generating steps to solve the issue...')
    if using_openai:
        connect_to_openai()
        steps_to_solve = get_steps_to_solve_openai(model, pre_prompt, issue_text)
    else:
        steps_to_solve = get_steps_to_solve_g4f(model, pre_prompt, issue_text)
    display_steps(steps_to_solve)
    write_to_file(steps_to_solve, url[-7:])


if __name__ == '__main__':
    main()
