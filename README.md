# Stack Overflow Python Questions Scraper

A Python tool that fetches the most upvoted Python questions from Stack Overflow and creates a beautifully formatted document in both Markdown and HTML formats.

## Features

- Fetches top Python questions from Stack Overflow using the Stack Exchange API
- Converts content to well-formatted Markdown
- Generates a responsive HTML version with modern styling
- Creates a shareable ZIP package containing both formats
- Mobile-friendly and print-ready output
- Note: Don't forget to change page size to get more data.
## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/stackoverflow-python-scraper.git
cd stackoverflow-python-scraper
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

1. To fetch questions and create Markdown:
```bash
python stackoverflow_scraper.py
```

2. To view the content in a formatted HTML:
```bash
python md_viewer.py
```

3. To create a shareable package (includes both MD and HTML):
```bash
python export_stackoverflow.py
```

### Output Files

- `stackoverflow_top_python.md`: Raw Markdown file containing the questions
- `stackoverflow_python_questions.html`: Formatted HTML version
- `stackoverflow_python_export.zip`: Shareable package containing both formats

## File Structure

- `stackoverflow_scraper.py`: Main script for fetching Stack Overflow questions
- `md_viewer.py`: Script for viewing Markdown as HTML
- `export_stackoverflow.py`: Script for creating shareable packages
- `requirements.txt`: Python dependencies

## Dependencies

- Python 3.x
- requests
- markdown

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
