import base64
import datetime
import hashlib
import io
import os
import time
import openai
import keyboard
import requests
import sounddevice as sd
from scipy.io.wavfile import write
from ..config import config_path, current_dir_path, load_api_keys
from openai import OpenAI

# 设置录音参数
fs = 44100  # 采样率

if not os.path.exists(os.path.join(current_dir_path, "record")):
    os.makedirs(os.path.join(current_dir_path, "record"))

# 录音函数
def record_audio():
    print("开始录音...")
    recording = sd.rec(int(fs * 10), samplerate=fs, channels=2)
    sd.wait()  # 等待录音结束
    return recording

# 保存录音文件
def save_recording(recording, file_path):
    write(file_path, fs, recording)  # 直接保存为wav文件
    print(f"录音已保存到：{file_path}")




class listen_audio:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "press_key":(["shift","space","ctrl","alt","tab"], {
                    "default": "shift",
                }),
            },
        }

    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("audio",)

    FUNCTION = "listen"

    #OUTPUT_NODE = True

    CATEGORY = "大模型派对（llm_party）/函数（function）"

    def listen(self,press_key="shift"):
        print(f"请按下{press_key}键开始录音，松开后录音结束。")
        while True:  # 持续监听键盘
            try:
                if keyboard.is_pressed(press_key):  # 如果按下空格键
                    audio_data = record_audio()
                    break  # 录音结束后退出循环
            except Exception as e:
                print(e)
                break
        # 获得当前时间戳
        timestamp = str(int(round(time.time() * 1000)))
        # 保存录音文件的路径
        full_audio_path = os.path.join(current_dir_path, "record", f"{timestamp}.wav")
        save_recording(audio_data, full_audio_path)
        return (full_audio_path,)
    
    @classmethod
    def IS_CHANGED(s):
        #生成当前时间的哈希值
        hash_value = hashlib.md5(str(datetime.datetime.now()).encode()).hexdigest()
        return hash_value
    

class openai_whisper:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "is_enable": ("BOOLEAN", {"default": True}),
                "audio": ("AUDIO", {}),
            },
            "optional": {
                "base_url": (
                    "STRING",
                    {
                        "default": "https://api.openai.com/v1/",
                    },
                ),
                "api_key": (
                    "STRING",
                    {
                        "default": "sk-XXXXX",
                    },
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    FUNCTION = "whisper"

    # OUTPUT_NODE = False

    CATEGORY = "大模型派对（llm_party）/函数（function）"

    def whisper(self, is_enable=True,audio="",base_url=None,api_key=None):
        if is_enable == False:
            return (None,)
        
        api_keys = load_api_keys(config_path)
        if api_key != "":
            openai.api_key = api_key
        elif api_keys.get("openai_api_key") != "":
            openai.api_key = api_keys.get("openai_api_key")
        else:
            openai.api_key = os.environ.get("OPENAI_API_KEY")
        if base_url != "":
            #如果以/结尾
            if base_url[-1] == "/":
                openai.base_url = base_url
            else:
                openai.base_url = base_url + "/"
        elif api_keys.get("base_url") != "":
            openai.base_url = api_keys.get("base_url")
        else:
            openai.base_url = os.environ.get("OPENAI_API_BASE")
        if openai.api_key == "":
            return ("请输入API_KEY",)

        if audio!="":
            client = OpenAI(api_key=openai.api_key,base_url=openai.base_url)
            audio_file= open(audio, "rb")
            transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
            )
            out =transcription.text
        else:
            out = None

        return (out,)