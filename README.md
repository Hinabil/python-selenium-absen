# Python Selenium Absen

This project automates the attendance process for students using Selenium WebDriver. It logs into the specified website, marks attendance, and takes screenshots of each action for verification.

## Project Structure

```
python-selenium-absen
├── src
│   ├── absen.py          # Main logic for logging in and taking attendance
│   └── utils
│       └── screenshot.py  # Utility functions for taking screenshots
├── .github
│   └── workflows
│       └── windows-ci.yml # GitHub Actions workflow for CI on Windows
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/python-selenium-absen.git
   cd python-selenium-absen
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure ChromeDriver:**
   Download ChromeDriver and place it in a suitable directory. Update the path in `src/absen.py` to point to your ChromeDriver executable.

4. **Fill in User Data:**
   Open `src/absen.py` and manually fill in the user data in the `users` list.

## Usage

To run the attendance script, execute the following command:
```bash
python src/absen.py
```

The script will log in with the provided user credentials, mark attendance, and take screenshots of each step.

## GitHub Actions

This project includes a GitHub Actions workflow configured to run on Windows. The workflow is defined in `.github/workflows/windows-ci.yml` and will automatically execute the attendance script on each push to the repository.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.