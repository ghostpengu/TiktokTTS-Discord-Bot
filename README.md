Create engaging TikTok videos effortlessly with our Text-to-Speech Discord TikTok video Generator! This app combines the power of customizable text input with high-quality speech synthesis, allowing users to transform written content into lively, entertaining videos. Express yourself, tell stories, or showcase your creativity in a whole new way. Easily adjust voice styles, add background music, and share your unique content on TikTok. Elevate your video creation experience with the Text-to-Speech TikTok Generator—because every word deserves to be heard! 🚀🎶

# **How to use ⚒️**
### Install requirements:
```python
pip install moviepy
pip install pydub
pip install discord
pip install flask
```
To Run the bot go into ```bot.py``` and find bot token replace with your and same with tiktok session id.
To change background video replace ```1.mp4``` with your own.

## Get TikTok Session id 🍪
- Install [Cookie Editor extension](https://cookie-editor.cgagnier.ca) for your browser.
- Log in to [TikTok Web](https://tiktok.com)
- While on TikTok web, open the extension and look for ```sessionid```
- Copy the ```sessionid``` value. (It should be an alphanumeric value)

## Commands
```!generate``` - generates video if the video is smaller than 25MB it will upload to discord as video
```!generate_audio``` - generates audio file.
