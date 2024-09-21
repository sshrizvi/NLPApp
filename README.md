<h1 align="center">NLPApp 🚀</h1>

<div align="center">

  ![NLP](https://img.shields.io/badge/NLP-Cloud%20API-blue.svg)
  ![Python](https://img.shields.io/badge/Python-3.8+-brightgreen.svg)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>


Welcome to **NLPApp**, a Python-based application that allows users to register, login, and utilize various Natural Language Processing (NLP) functionalities like Named Entity Recognition (NER), Language Detection, and Sentiment Analysis. The app interacts with the NLP Cloud API to perform these advanced tasks.


## 📋 Features
- **User Registration & Login**: Securely register and login using an email and password.
- **Named Entity Recognition (NER)**: Extract entities such as people, organizations, or locations from text.
- **Language Detection**: Detect the language of any given paragraph.
- **Sentiment Analysis**: Analyze the sentiment (positive, negative, neutral) of a given comment or text.


## 🛠️ Installation

To run this application, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/sshrizvi/NLPApp.git
    cd NLPApp
    ```

2. **Create a virtual environment (optional but recommended)**:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Get your API Key**:
    - Register on [NLP Cloud](https://nlpcloud.io/) and get your API key.
    - Paste your API key in the `API_KEY` variable inside the `NLPApp` class.


## 🖥️ Usage

### To run the application, simply execute:

```bash
python main.py
```

### Once started, you will be presented with a menu:
- **Login**: Existing users can log in with their credentials.
- **Register**: New users can sign up.
- **Exit**: Exit the application.

### After logging in, users can:
- **NER (Named Entity Recognition)**: Enter a paragraph and extract specific entities.
- **Language Detection**: Detect the language of a provided paragraph.
- **Sentiment Analysis**: Analyze the sentiment of a comment or paragraph.


## 📚 Example

Here’s how the NER function works in the app:

```
NER
---------------------------------------------------
Enter paragraph: John Doe works at Google in California.
Which entity do you want to search in the paragraph: Organization

+-------------+-------------+
| entity      | type        |
+-------------+-------------+
| Google      | Organization|
+-------------+-------------+
```


## 📦 Dependencies
This project requires the following dependencies:
- `nlpcloud`
- `pandas`

You can install all dependencies using the provided `requirements.txt`.


## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/sshrizvi/NLPApp/issues).


## 📝 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## 🌐 Connect with Me
- GitHub: [sshrizvi](https://github.com/sshrizvi)
- LinkedIn: [sshrizvi](https://www.linkedin.com/in/sshrizvi)