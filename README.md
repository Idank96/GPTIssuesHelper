# GPTIssuesHelper
GPTIssuesHelper is a Python script that uses GPT-3.5-turbo to help developers solve issues on GitHub.

##  Usage
1. Clone the repository
2. Install the requirements
```bash
pip install -r requirements.txt
```
3. Create openai api key in https://beta.openai.com/.
4. Create a .txt file and copy your openai api key and save it as `openai_api_key.txt`.
5. Replace `path_to_key` in connect_to_openai function with the path to your `openai_api_key.txt` file.
6. Select the issue you want to solve and copy the url of the issue.
7. Run the script and paste the url of the issue when asked.
8. Wait for the script to finish and copy the steps to solve the issue.

Star the repository if you found it useful :)