import requests
import markdown
from datetime import datetime
import os
import json

def fetch_top_questions(tag='python', page_size=100):
    """
    Fetches the most voted questions for a specific tag from Stack Overflow
    """
    base_url = 'https://api.stackexchange.com/2.3'
    
    # Question parameters
    question_params = {
        'site': 'stackoverflow',
        'tagged': tag,
        'sort': 'votes',
        'order': 'desc',
        'pagesize': page_size,
        'filter': '!9Z(-wwYGT'  # Using a simpler filter
    }
    
    try:
        # Fetch questions
        response = requests.get(f'{base_url}/questions', params=question_params)
        response.raise_for_status()  # Check for HTTP errors
        questions = response.json()
        
        if 'items' not in questions:
            print("'items' not found in API response")
            return []
            
        return questions['items']
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        return []

def create_markdown_document(questions, output_file='stackoverflow_top_python.md'):
    """
    Creates a markdown document from questions and answers
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            # Title and description
            f.write(f'# Most Voted Python Questions on Stack Overflow\n\n')
            f.write(f'*Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
            
            for i, question in enumerate(questions, 1):
                # Question title
                f.write(f'## {i}. {question.get("title", "Title not found")}\n\n')
                
                # Question details
                f.write(f'**Vote count:** {question.get("score", 0)}\n')
                f.write(f'**Views:** {question.get("view_count", 0)}\n')
                f.write(f'**Question link:** [Stack Overflow]({question.get("link", "#")})\n\n')
                
                # Question content
                if "body" in question:
                    f.write('### Question\n\n')
                    f.write(f'{question["body"]}\n\n')
                
                # Answers
                if "answers" in question and question["answers"]:
                    # Get the most voted answer
                    best_answer = sorted(question["answers"], key=lambda x: x.get("score", 0), reverse=True)[0]
                    
                    f.write('### Best Answer\n\n')
                    f.write(f'**Vote count:** {best_answer.get("score", 0)}\n\n')
                    if "body" in best_answer:
                        f.write(f'{best_answer["body"]}\n\n')
                
                f.write('---\n\n')  # Separator line
        
        print(f'Markdown file successfully created: {output_file}')
    except Exception as e:
        print(f"Error while creating file: {e}")

def main():
    # Fetch the most voted Python questions
    questions = fetch_top_questions(tag='python', page_size=10)
    
    if questions:
        # Create markdown document
        output_file = 'stackoverflow_top_python.md'
        create_markdown_document(questions, output_file)
    else:
        print("Could not fetch questions or no questions found.")

if __name__ == '__main__':
    main()
