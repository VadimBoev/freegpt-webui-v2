# FreeGPT WebUI v2
<img src="https://github.com/VadimBoev/freegpt-webui-v2/blob/main/webui-gpt.png" width="1000" />

## GPT 3.5/4

<strong>NOT REQUIRE ANY API KEY</strong> ❌🔑 

This project features a WebUI utilizing the [G4F API](https://github.com/xtekky/gpt4free). <br>
Experience the power of ChatGPT with a user-friendly interface, enhanced jailbreaks, and completely free.  

**Important!** Don't be afraid to ask a question or write about any problem in the "issue".  
We will solve a question or a problem together! 🌍  

You can [buy me coffee](https://boosty.to/vadimboev/donate) here ☕🤎

## Known bugs 🚧
- Stream mode not working properly.
- At the moment, only gpt 3.5 turbo works, but I think I will fix it in the future
- Docker is missing (possibly temporarily)
- Operation timed out after 30000 milliseconds
- ChatGPT does not remember the dialog.  
This problem is related to the fact that I use a different solution method so that our Web UI can access g4f. This is fixable, not critical and not scary
- Web Access is not working.  
Because the API that was used earlier in the "freegpt-webui" repository from ramonvc stopped working. This will be fixed later

## Features v2 📢
- Updated g4f
- Fixes to make everything work

## Project Hosting and Demonstration 🌐🚀
The project is hosted on multiple platforms to be tested and modified.
|Platform|Status|API Key|Free|Repo|Demo|
|--|--|--|--|--|--|
|[My site](http://vadimboev.ru:1338/)|![Active](https://img.shields.io/badge/Active-brightgreen)|◼️|☑️|[FreeGPT WebUI](https://github.com/VadimBoev/freegpt-webui-v2)|[Chat](http://vadimboev.ru:1338/)

## Table of Contents  
- [To-Do List](#to-do-list-%EF%B8%8F)  
- [Getting Started](#getting-started-white_check_mark)  
  - [Cloning the Repository](#cloning-the-repository-inbox_tray)  
  - [Install Dependencies](#install-dependencies-wrench)  
- [Running the Application](#running-the-application-rocket)  
- [Incorporated Projects](#incorporated-projects-busts_in_silhouette)
  - [WebUI](#webui) 
  - [API FreeGPT](#api-g4f)
- [Star History](#star-history)
- [Legal Notice](#legal-notice) 

## Getting Started :white_check_mark:  
To get started with this project, you'll need to clone the repository and have [Python](https://www.python.org/downloads/) installed on your system.  
(Version 3.10+ is recommended. It also works for me on 3.9.2 in debian 11).
  
### Cloning the Repository :inbox_tray:
Run the following command to clone the repository:  

```
git clone https://github.com/VadimBoev/freegpt-webui-v2.git
```

### Install Dependencies :wrench: 
Navigate to the project directory:
```
cd freegpt-webui-v2
```

Install the dependencies:
```
pip install -r requirements.txt
```
## Running the Application :rocket:
To run the application, run the following command:
```
python run.py
```

Access the application in your browser using the URL:
```
http://127.0.0.1:1338
```
or
```
http://localhost:1338
```

## Incorporated Projects :busts_in_silhouette:
I highly recommend visiting and supporting both projects.

### WebUI
The application interface was incorporated from the [chatgpt-clone](https://github.com/xtekky/chatgpt-clone) repository.

### API G4F
The free GPT-4 API was incorporated from the [GPT4Free](https://github.com/xtekky/gpt4free) repository.

<br>

## Star History
[![Star History Chart](https://api.star-history.com/svg?repos=VadimBoev/freegpt-webui-v2&type=Timeline)](https://star-history.com/#VadimBoev/freegpt-webui-v2&Timeline)

<br>

## Legal Notice
This repository is _not_ associated with or endorsed by providers of the APIs contained in this GitHub repository. This
project is intended **for educational purposes only**. This is just a little personal project. Sites may contact me to
improve their security or request the removal of their site from this repository.

Please note the following:

1. **Disclaimer**: The APIs, services, and trademarks mentioned in this repository belong to their respective owners.
   This project is _not_ claiming any right over them nor is it affiliated with or endorsed by any of the providers
   mentioned.

2. **Responsibility**: The author of this repository is _not_ responsible for any consequences, damages, or losses
   arising from the use or misuse of this repository or the content provided by the third-party APIs. Users are solely
   responsible for their actions and any repercussions that may follow. We strongly recommend the users to follow the
   TOS of the each Website.

3. **Educational Purposes Only**: This repository and its content are provided strictly for educational purposes. By
   using the information and code provided, users acknowledge that they are using the APIs and models at their own risk
   and agree to comply with any applicable laws and regulations.

4. **Copyright**: All content in this repository, including but not limited to code, images, and documentation, is the
   intellectual property of the repository author, unless otherwise stated. Unauthorized copying, distribution, or use
   of any content in this repository is strictly prohibited without the express written consent of the repository
   author.

5. **Indemnification**: Users agree to indemnify, defend, and hold harmless the author of this repository from and
   against any and all claims, liabilities, damages, losses, or expenses, including legal fees and costs, arising out of
   or in any way connected with their use or misuse of this repository, its content, or related third-party APIs.

6. **Updates and Changes**: The author reserves the right to modify, update, or remove any content, information, or
   features in this repository at any time without prior notice. Users are responsible for regularly reviewing the
   content and any changes made to this repository.

By using this repository or any code related to it, you agree to these terms. The author is not responsible for any
copies, forks, or reuploads made by other users. This is the author's only account and repository. To prevent
impersonation or irresponsible actions, you may comply with the GNU GPL license this Repository uses.
