<p align="right">
   <a href="./README_ZH.md">中文</a> |  <strong>English</strong> 
</p>

## Latest Updates
1. Supports GPT-4’s visual features, can read images in ComfyUI, but requires the free image hosting service imgbb to implement this feature.
2. Added persona nodes, you can quickly enable your set system prompts, or use custom persona to quickly adjust prompt word templates.
3. Implemented conditional statements in ComfyUI, allowing the large model to output to different interfaces after judgment.
4. Added more example workflows, welcome everyone to use directly!

# **COMFYUI LLM PARTY—A Node Library for LLM Workflow Development in ComfyUI** 

## Introduction
[comfyui](https://github.com/comfyanonymous/ComfyUI) is an extremely minimalist UI interface, primarily used for AI drawing and other workflows based on the SD model. This project aims to develop a complete set of nodes for LLM workflow construction based on comfyui. It allows users to quickly and conveniently build their own LLM workflows and easily integrate them into their existing SD workflows.(The image shows the intelligent customer service workflow built by the nodes of this project.For more example workflows, please check the [workflow](workflow/) folder.)

![图片](img/智能助手.png)

# User Guide
[Building a Modular AI with ComfyUI×LLM: A Step-by-Step Tutorial (Super Easy!)](https://www.bilibili.com/video/BV1JZ421v7Tw/?vd_source=f229e378448918b84afab7c430c6a75b)

## Features
1. You can right-click in the comfyui interface, select `llm` from the context menu, and you will find the nodes for this project. [how to use nodes](how_to_use_nodes.md)
2. Supports OpenAI API driving and custom base_url, allowing the use of a proxy API to drive LLM nodes.If you are using other large model interfaces, you can convert them to the OpenAI API format using [openai-style-api](https://github.com/tian-minghui/openai-style-api). Please select the LLM_local node for local deployment. Currently, both GLM and LLAMA have been adapted, but LLAMA cannot be used for tool invocations because the native LLAMA does not include this functionality.
1. Local knowledge base access, supports RAG.
2. Can invoke a code interpreter.
3. Can perform online queries, supports Google search.
4. Can implement conditional statements in comfyui, can classify user questions and then provide targeted responses.
5. Supports loopback links for large models, allowing two large models to have a debate.
6. Supports attaching any personality mask, can customize prompt word templates.
7. Supports multiple tool invocations; currently developed tools include weather check, time check, knowledge base, code execution, online search, search on a single webpage, and more tools are under development.
8. It is recommended to use the show_text node from [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts) in conjunction with the LLM node for output display.

## Download
[Baidu Cloud Download](https://pan.baidu.com/s/13ogn1np6bHgxOJhS--QJmg?pwd=jppj) (Recommended! Includes a compressed package of comfyui with the environment setup completed, and a folder for this project. After downloading the former, there’s no need for further environment configuration!)

Or install using one of the following methods:
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
### Method 1:
1. Open the `config.ini` file in the `comfyui_LLM_party` project folder.
2. Enter your `openai_api_key` and `base_url` in `config.ini`.
3. If you want to use the Google search tool, enter your `google_api_key` and `cse_id` in `config.ini`.

### Method 2:
1. Open the comfyui interface.
2. Create a new Large Language Model (LLM) node and directly enter your `openai_api_key` and `base_url` in the node.
3. Create a new Google Search Tool (google_tool) node and directly enter your `google_api_key` and `cse_id` in the node.

## Next Steps Plan:
1. More common utility nodes, such as: code interpreters, text-to-speech output, recognition of text information in images, etc.
2. Allow LLM to internally call an LLM that is subsidiary to it, giving the assistant its own assistant.
3. New nodes that can connect with the numerous SD nodes in comfyui, expanding the possibilities for LLM and SD, and providing related workflows.

## If my work has brought value to your day, consider fueling it with a coffee! Your support not only energizes the project but also warms the heart of the creator. ☕💖 Every cup makes a difference!
<div style="display:flex; justify-content:space-between;">
    <img src="img/zhifubao.jpg" style="width: 48%;" />
    <img src="img/wechat.jpg" style="width: 48%;" />
</div>
