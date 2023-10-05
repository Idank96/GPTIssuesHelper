# GPTIssuesHelper
GPTIssuesHelper is a Python script that uses GPT to help developers solve issues on GitHub.

## Options
You can use either OpenAI API with gpt-3.5-turbo or g4f with gpt-4 or g4f with Bing-GPT4:
1. Using OpenAI API with gpt-3.5-turbo: set `using_openai = True` at the beginning of the script.
2. Using g4f with gpt-4: set `using_openai = False` at the beginning of the script. 

##  Usage
1. Clone the repository
2. Install the requirements
```bash
pip install -r requirements.txt
```
3. Select the issue you want to solve and copy the url of the issue.
4. Run the script and paste the url of the issue when asked.
5. Wait for the script to finish and copy the steps to solve the issue.

optional (using OpenAI API with gpt-3.5-turbo) 
* Create openai api key in https://beta.openai.com/. 
* Create a .txt file and copy your openai api key and save it as `openai_api_key.txt`. 
* Replace `path_to_key` in connect_to_openai function with the path to your `openai_api_key.txt` file.__


## Output Example

Enter the url of the issue you want to solve: https://github.com/pytorch/pytorch/issues/107006#

**Overview of the Issue:**
This GitHub issue pertains to the optimization of PyTorch's NAdam and Adagrad optimizers. Currently, these optimizers compile to more than 5 kernels, which is less efficient. The goal is to make them fully fuse for better performance. The issue mentions that there might be problems due to mutation in the code, and it suggests looking into the `scheduler.py` file.

**Technical Jargon and Terms:**
- **NAdam**: An optimizer used in deep learning, specifically in PyTorch, for optimizing neural network models.
- **Adagrad**: Another optimizer commonly used in deep learning for gradient-based optimization.
- **Kernels**: Small computational units or functions that are part of the optimization process.
- **Mutation**: Changes in the code that affect its behavior.
- **`scheduler.py`**: A Python script file, likely responsible for scheduling or controlling aspects of the optimization process.

**Steps to Solve the Issue:**
1. **Understand the Problem**: Familiarize yourself with the issue description and the context provided. Make sure you understand the goal, which is to make NAdam and Adagrad optimizers fully fuse for better efficiency.

2. **Clone the Repository**: If you haven't already, clone the PyTorch repository to your local machine. You can do this by running the following command in your terminal:
   ```bash
   git clone <repository_url>
   ```

3. **Locate `scheduler.py`**: Navigate to the `pytorch/torch/_inductor/` directory in the cloned repository. In this directory, you will find the `scheduler.py` file mentioned in the issue.

4. **Examine `scheduler.py`**: Open the `scheduler.py` file in a code editor. Look for the `can_fuse` function, which is referred to in the issue. This function likely contains logic related to fusion.

5. **Analyze the `can_fuse` Function**: Study the code within the `can_fuse` function. Try to understand how fusion decisions are made and how they can be modified to allow NAdam and Adagrad to fully fuse.

6. **Contact @mlazos for Details**: The issue suggests contacting the user @mlazos for more details. If you have questions or need clarification on specific aspects of the code or problem, reach out to them via GitHub.

7. **Propose Modifications**: Based on your analysis, propose modifications to the `can_fuse` function or other relevant parts of the code that would enable full fusion for NAdam and Adagrad optimizers. Ensure that any changes you make are in line with the coding standards of the project.

8. **Create a Pull Request**: Once you've made the necessary code modifications, create a new branch in your cloned repository and commit your changes. Then, create a pull request to submit your changes for review. Be sure to reference this GitHub issue in your pull request.

9. **Seek Feedback**: Be prepared to engage in discussions and address any feedback or comments provided by the project maintainers or other contributors. Collaboration is key to resolving the issue effectively.

10. **Test Your Changes**: Before finalizing your contribution, test your modifications to ensure they don't introduce new issues and that NAdam and Adagrad optimizers now fully fuse as intended.

11. **Document Your Work**: Update any relevant documentation or comments in the code to explain your changes and how they improve fusion for NAdam and Adagrad.

12. **Finalize and Merge**: Once your changes have been reviewed and approved, they can be merged into the PyTorch repository, and the issue can be closed.

**Good luck!**


Star the repository if you found it useful :)


Copyright (c) 2023 [Idan Kogan]
This software is licensed under the GNU General Public License v3.0. You can find a copy of the license at:
https://www.gnu.org/licenses/gpl-3.0.txt