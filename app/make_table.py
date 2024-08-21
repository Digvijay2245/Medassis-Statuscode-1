import re

def process_text_to_html(text):
    # Convert markdown-style bold (e.g., **text**) to HTML <strong> tags
    formatted_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    
    # Function to generate a table from headers and rows
    def create_table(headers, rows):
        headers_html = "".join([f"<th>{header}</th>" for header in headers])
        rows_html = "".join([
            "<tr>" + "".join([f"<td>{cell}</td>" for cell in row]) + "</tr>"
            for row in rows
        ])
        return f"<table border='1' style='width:100%; border-collapse: collapse;'><thead><tr>{headers_html}</tr></thead><tbody>{rows_html}</tbody></table>"

    # Define section headings
    headings = ['Meal', 'Dish', 'Quantity', 'Calories']
    content = []
    index = 0
    
    # Parsing each section
    while index < len(formatted_text):
        for heading in headings:
            if heading in formatted_text[index:]:
                # Find the start and end of the current section
                start = formatted_text.find(heading, index)
                end = len(formatted_text)
                
                # Find the next heading or end of the text
                next_heading_pos = min((formatted_text.find(h, start + len(heading)) for h in headings if formatted_text.find(h, start + len(heading)) > start), default=end)
                section_content = formatted_text[start:next_heading_pos].strip()
                
                # Extract headers and rows
                lines = section_content.split('\n')
                headers = lines[0].strip().split('|')
                rows = [line.split('|') for line in lines[1:] if line.strip()]
                
                # Create and append the table
                content.append(create_table(headers, rows))
                
                # Move the index to the end of the current section
                index = next_heading_pos
                break
        else:
            # If no heading found, just append the rest of the text
            content.append(formatted_text[index:])
            break

    # Join content with new lines
    return "<br>".join(content)
