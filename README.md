<p align="right">
   <a href="./README_ZH.md">中文</a> |  <strong>English</strong>
</p>

## Latest Updates
1. Added LLM tools to send messages to Work_wechat, DingTalk, and Feishu, as well as external functions to call.

# **COMFYUI LLM PARTY—A Node Library for LLM Workflow Development in ComfyUI**

## Introduction
[comfyui](https://github.com/comfyanonymous/ComfyUI) is an extremely minimalist UI interface, primarily used for AI drawing and other workflows based on the SD model. This project aims to develop a complete set of nodes for LLM workflow construction based on comfyui. It allows users to quickly and conveniently build their own LLM workflows and easily integrate them into their existing SD workflows.The picture shows a workflow of LLM implementing multi-tool calling, for more workflows please refer to the [workflow](workflow) folder.

![图片](img/多工具调用.png)

## User Guide
1. [Building a Modular AI with ComfyUI×LLM: A Step-by-Step Tutorial (Super Easy!)](https://www.bilibili.com/video/BV1JZ421v7Tw/?vd_source=f229e378448918b84afab7c430c6a75b)

2. [[ComfyUI Black Technology] Teach you GPT-4o access to comfyui | Make workflow call another workflow | Make LLM a tool](https://www.bilibili.com/video/BV1JJ4m1A789/?spm_id_from=333.999.0.0&vd_source=f229e378448918b84afab7c430c6a75b)

## Features
1. You can right-click in the comfyui interface, select `llm` from the context menu, and you will find the nodes for this project. [how to use nodes](how_to_use_nodes.md)
2. Supports API integration or local large model integration. Modular implementation for tool invocation.When entering the base_url, please use a URL that ends with `/v1/`.You can use [ollama](https://github.com/ollama/ollama) to manage your model. Then, enter `http://localhost:11434/v1/` for the base_url, `ollama` for the api_key, and your model name for the model_name, such as: llama3. If the call fails with a 503 error, you can try turning off the proxy server.
3. Local knowledge base integration with RAG support.
4. Ability to invoke code interpreters.
5. Enables online queries, including Google search support.
6. Implement conditional statements within ComfyUI to categorize user queries and provide targeted responses.
7. Supports looping links for large models, allowing two large models to engage in debates.
8. Attach any persona mask, customize prompt templates.
9. Supports various tool invocations, including weather lookup, time lookup, knowledge base, code execution, web search, and single-page search.
10. Use LLM as a tool node.
11. Rapidly develop your own web applications using API + Streamlit.The picture below is an example of a drawing application.
12. Added a dangerous omnipotent interpreter node that allows the large model to perform any task.
13. It is recommended to use the `show_text` node under the `function` submenu of the right-click menu as the display output for the LLM node.
14. Supported the visual features of GPT-4O!
15. A new workflow intermediary has been added, which allows your workflow to call other workflows!
16. Adapted to all models with an interface similar to OpenAI, such as: Tongyi Qianwen/QWEN, Zhigu Qingyan/GLM, DeepSeek, Kimi/Moonshot. Please fill in the base_url, api_key, and model_name of these models into the LLM node to call them.
17. Added an LVM loader, now you can call the LVM model locally, support [lava-llama-3-8b-v1_1-gguf](https://huggingface.co/xtuner/llava-llama-3-8b-v1_1-gguf) model, other LVM models should theoretically run if they are GUFF format.The example workflow can be found here: [start_with_LVM.json](workflow/start_with_LVM.json).
18. I wrote a `fastapi.py` file, and if you run it directly, you’ll get an OpenAI interface on `http://127.0.0.1:8817/v1/`. Any application that can call GPT can now invoke your comfyui workflow! I will create a tutorial to demonstrate the details on how to do this.
19. I’ve separated the LLM loader and the LLM chain, dividing the model loading and model configuration. This allows for sharing models across different LLM nodes!
20. macOS and mps devices are now supported! Thanks to [bigcat88](https://github.com/bigcat88) for their contribution!

![图片](img/画画应用.png)

## Download
Install using one of the following methods:
### Method 1:
1. Search for comfyui_LLM_party in the [comfyui manager](https://github.com/ltdrdata/ComfyUI-Manager) and install it with one click.
2. Restart comfyui.

### Method 2:
1. Navigate to the `custom_nodes` subfolder under the ComfyUI root folder.
2. Clone this repository with `git clone https://github.com/heshengtao/comfyui_LLM_party.git`.

### Method 3:
1. Click `CODE` in the upper right corner.
2. Click `download zip`.
3. Unzip the downloaded package into the `custom_nodes` subfolder under the ComfyUI root folder.

## Environment Deployment
1. Navigate to the `comfyui_LLM_party` project folder.
2. Enter `pip install -r requirements.txt` in the terminal to deploy the third-party libraries required by the project into the comfyui environment. Please ensure you are installing within the comfyui environment and pay attention to any `pip` errors in the terminal.
3. If you are using the comfyui launcher, you need to enter `path_in_launcher_configuration\python_embeded\python.exe path_in_launcher_configuration\python_embeded\Scripts\pip.exe install -r requirements.txt` in the terminal to install. The `python_embeded` folder is usually at the same level as your `ComfyUI` folder.

## Configuration
Configure the APIKEY using one of the following methods:
### Method One:
1. Open the `config.ini` file in the `comfyui_LLM_party` project folder.
2. Enter your `openai_api_key` and `base_url` in `config.ini`.
3. If you want to use the Google search tool, enter your `google_api_key` and `cse_id` in `config.ini`.

### Method Two:
1. Open the comfyui interface.
2. Create a new Large Language Model (LLM) node and directly enter your `openai_api_key` and `base_url` in the node.
3. Create a new Google Search Tool (google_tool) node and directly enter your `google_api_key` and `cse_id` in the node.

## Next Steps Plan:
1. More model adaptations, at least covering the API interfaces of mainstream large models and local calls of mainstream open-source models, as well as more LVM model adaptations. Currently, I have only adapted the visual function calls of GPT-4;
2. More ways to build agents. The work I have completed in this area includes importing an LLM as a tool to another LLM, achieving radial construction of LLM workflows, and importing one workflow as a node into another workflow. I might develop some cooler functions in this area in the future.
3. More automation features. In the future, I will introduce more nodes that automatically push images, text, videos, and audio to other applications, as well as listening nodes that implement automatic replies to mainstream social software and forums.
4. More knowledge base management functions. The project already supports local file search and web search. In the future, I will introduce knowledge graph search and long-term memory search. This will allow agents to think logically about professional knowledge and always remember certain key information when conversing with users.
5. More tools, more persona. This part is the easiest to do but also requires the most accumulation. I hope that in the future, this project can have as many custom nodes as comfyui, with a multitude of tools and persona.

## Disclaimer:
This open-source project and its contents (hereinafter referred to as "Project") are provided for reference purposes only and do not imply any form of warranty, either expressed or implied. The contributors of the Project shall not be held responsible for the completeness, accuracy, reliability, or suitability of the Project. Any reliance you place on the Project is strictly at your own risk. In no event shall the contributors of the Project be liable for any indirect, special, or consequential damages or any damages whatsoever resulting from the use of the Project.

## If my work has brought value to your day, consider fueling it with a coffee! Your support not only energizes the project but also warms the heart of the creator. ☕💖 Every cup makes a difference!
<div style="display:flex; justify-content:space-between;">
    <img src="img/zhifubao.jpg" style="width: 48%;" />
    <img src="img/wechat.jpg" style="width: 48%;" />
</div>
