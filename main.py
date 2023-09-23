from bs4 import BeautifulSoup
import requests
import openai


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
    You will be provided with a GitHub issue. Your task is to write instructions and steps on how to solve the issue, based on the information given in the issue
    Use the following format for your response:

    Start by providing an initial overview of the problem to a Python-competent computer science student who is new to the issue.
    Explain any technical jargon that you use.
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
    model = "gpt-3.5-turbo"
    return model


def get_steps_to_solve(model: str, pre_prompt: str, issue_text: str) -> str:
    messages = [{'role': 'user',
                 'content': pre_prompt+issue_text}]

    response = openai.ChatCompletion.create(model=model,
                                            messages=messages,
                                            max_tokens=1000,
                                            temperature=0)
    generated_text = response['choices'][0]['message']['content']

    return generated_text


def display_steps(steps_to_solve: str):
    print("The steps to solve the issue are: ")
    # Display the text in a window with each line in a separate line.
    # Split by \n:
    steps_to_solve_seperated = steps_to_solve.split("\n")
    for step in steps_to_solve_seperated:
        print(step)


def main():
    url = get_url()
    issue_text = extract_issue_text(url)
    pre_prompt = create_prompt()
    connect_to_openai()
    model = init_model()
    steps_to_solve = get_steps_to_solve(model, pre_prompt, issue_text)
    display_steps(steps_to_solve)


if __name__ == '__main__':
    main()

