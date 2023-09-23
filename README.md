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

## Example
```bash
Enter the url of the issue you want to solve: https://github.com/pytorch/pytorch/issues/107006#
The steps to solve the issue are: 
Overview:
The issue is related to the fusion of NAdam and Adagrad optimizers in PyTorch. Currently, these optimizers are not fully fusing, resulting in multiple kernels being compiled. The presence of mutation is likely causing the issue. The goal is to modify the fusion rules to allow these optimizers to fuse fully.

To solve this issue, follow these steps:

1. Start by understanding the concept of fusion in PyTorch. Fusion refers to the process of combining multiple operations into a single kernel, which can improve performance by reducing memory transfers and overhead.

2. Familiarize yourself with the NAdam and Adagrad optimizers in PyTorch. These optimizers are used for updating the parameters of a neural network during training.

3. Review the code in the `test_compiled_optimizers.py` file located in the `pytorch/test/inductor/` directory. This file contains tests for the compiled optimizers and can provide insights into the current kernel counts.

4. Open the `scheduler.py` file located in the `pytorch/torch/_inductor/` directory. This file contains the implementation of the scheduler, including the `can_fuse` function.

5. Locate the `can_fuse` function in the `scheduler.py` file. This function determines whether two operations can be fused together. Understanding this function is crucial for modifying the fusion rules.

6. Contact @mlazos for more details on the issue. They can provide additional information and guidance on how to modify the fusion rules to allow full fusion of NAdam and Adagrad optimizers.

7. Consider alternative approaches if modifying the fusion rules proves to be challenging. Discuss with the relevant stakeholders and team members to explore other potential solutions.

8. Keep the relevant team members and stakeholders informed about your progress and any potential solutions you come up with.

Good luck!


Star the repository if you found it useful :)