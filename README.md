# Sherlock Web App

This is a web-based interface for Sherlock, a tool to find usernames across social networks. The web app is built using Streamlit and provides a user-friendly interface to search for usernames across various social media platforms.

## Features

- Simple and intuitive web interface
- Real-time username search across multiple social networks
- Results displayed in a clean, sortable table
- Option to download results as CSV
- Configurable request timeout
- Progress tracking during searches

## Installation

1. Clone this repository:
```bash
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Web App

To start the web app, run:
```bash
streamlit run app.py
```

The app will open in your default web browser. If it doesn't, you can access it at http://localhost:8501

## Usage

1. Enter a username in the search box
2. Adjust the timeout if needed (default is 60 seconds)
3. Click "Search" to begin the search
4. View the results in the table below
5. Optionally download the results as a CSV file

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Original Sherlock project: https://github.com/sherlock-project/sherlock
- Built with Streamlit: https://streamlit.io/
- Created By Pranav Manglani
