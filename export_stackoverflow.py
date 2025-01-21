import markdown
import webbrowser
import os
from datetime import datetime
import zipfile
import shutil

def convert_md_to_html(md_file, html_file):
    # Read the markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert markdown to HTML with extra features enabled
    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'codehilite', 'nl2br']
    )
    
    # Create HTML with embedded styling and meta tags
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Stack Overflow Python Questions</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.6;
                max-width: 900px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
                color: #2c3e50;
            }}
            .container {{
                background-color: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 2px solid #eee;
                padding-bottom: 10px;
                font-size: 2.2em;
            }}
            h2 {{
                color: #34495e;
                margin-top: 30px;
                font-size: 1.8em;
            }}
            h3 {{
                color: #16a085;
                font-size: 1.4em;
            }}
            code {{
                background-color: #f8f9fa;
                padding: 2px 4px;
                border-radius: 4px;
                font-family: Monaco, Consolas, monospace;
                font-size: 0.9em;
            }}
            pre {{
                background-color: #f8f9fa;
                padding: 15px;
                border-radius: 4px;
                overflow-x: auto;
                border: 1px solid #e9ecef;
            }}
            a {{
                color: #3498db;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
                color: #2980b9;
            }}
            hr {{
                border: none;
                border-top: 1px solid #eee;
                margin: 30px 0;
            }}
            .metadata {{
                color: #666;
                font-style: italic;
                margin-bottom: 20px;
            }}
            .question-stats {{
                background-color: #f8f9fa;
                padding: 10px;
                border-radius: 4px;
                margin: 10px 0;
                border: 1px solid #e9ecef;
            }}
            @media print {{
                body {{
                    background-color: white;
                }}
                .container {{
                    box-shadow: none;
                    padding: 0;
                }}
                a {{
                    color: #2c3e50;
                }}
            }}
            @media (max-width: 768px) {{
                body {{
                    padding: 10px;
                }}
                .container {{
                    padding: 15px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {html_content}
            <footer style="margin-top: 50px; text-align: center; color: #666;">
                <p>Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            </footer>
        </div>
    </body>
    </html>
    """
    
    # Write the HTML file
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    return html_file

def create_export_package(md_file, html_file, output_zip):
    """Create a zip file containing both MD and HTML versions"""
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add files to zip
        zipf.write(md_file, os.path.basename(md_file))
        zipf.write(html_file, os.path.basename(html_file))
        
        # Create a simple README
        readme_content = """Stack Overflow Python Questions Export

This package contains:
1. stackoverflow_top_python.md - Markdown version of the content
2. stackoverflow_python_questions.html - HTML version that can be opened in any web browser

To view:
- Open the .html file in your web browser for a formatted view
- Open the .md file in any text editor or Markdown viewer
"""
        zipf.writestr('README.txt', readme_content)

def main():
    md_file = 'stackoverflow_top_python.md'
    html_file = 'stackoverflow_python_questions.html'
    zip_file = 'stackoverflow_python_export.zip'
    
    if not os.path.exists(md_file):
        print(f"Error: {md_file} not found!")
        return
    
    # Convert MD to HTML
    print("Converting Markdown to HTML...")
    html_path = convert_md_to_html(md_file, html_file)
    
    # Create export package
    print("Creating export package...")
    create_export_package(md_file, html_file, zip_file)
    
    # Get the absolute paths
    abs_html_path = os.path.abspath(html_path)
    abs_zip_path = os.path.abspath(zip_file)
    
    # Open in default browser
    webbrowser.open('file://' + abs_html_path)
    
    print(f"\nExport complete!")
    print(f"Files created:")
    print(f"1. HTML version: {html_file}")
    print(f"2. Export package: {zip_file}")
    print(f"\nYou can share the {zip_file} file with others. It contains both Markdown and HTML versions.")

if __name__ == '__main__':
    main()
