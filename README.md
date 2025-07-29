# Zootopia-API

This project generates a simple animal information website using data fetched from the [API Ninjas Animals API](https://api-ninjas.com/api/animals).  
The user can input the name of an animal, and the program will create an HTML page showing details like its diet, location, and type.  
If the animal does not exist, the website will display a friendly error message.

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/kristina-krauberger/zootopia-api.git
   cd zootopia-api
   ```

2. Create and activate a virtual environment (recommended):

    ```bash
    python -m venv .venv
    source .venv/bin/activate   # on macOS/Linux
    .venv\Scripts\activate      # on Windows
   ```

3. Install the dependencies:

    ```bash
   pip install -r requirements.txt
   ```

4. Create a .env file in the project root and add your API key:

    ```bash
   API_KEY=your_api_key_here
   ```


## Usage

To run the program, execute the following command:

```bash
python animals_web_generator.py
```

## Project Structure

```
zootopia-api/
│
├── animals_web_generator.py   # Main program logic
├── data_fetcher.py            # Handles API requests
├── animals_template.html      # HTML template for the output
├── animals.html               # Generated output file
├── requirements.txt           # Dependencies
├── .env                       # Stores API key (not committed)
└── README.md                  # Project documentation
```

## Contributing

Contributions are welcome!  
If you'd like to contribute, please fork the repository and create a pull request.  
For larger changes, please open an issue first to discuss what you would like to change.

---
