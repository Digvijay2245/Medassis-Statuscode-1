def format_response_as_table(raw_response):
    # Split the response by newlines
    lines = raw_response.split("\n")
    
    # Initialize HTML sections
    formatted_html = ''
    table_html = ''
    formatted_html += "<div style='padding-top: 10px;'>"
    in_table = False
    after_heading = False  # Flag to check if we are processing the first line after ##
    
    def bold_text(text):
        """Helper function to make text between ** ** bold."""
        formatted_line = ""
        parts = text.split()
        for i, part in enumerate(parts):
            if i % 2 == 1:  # Odd indices are between ** **
                formatted_line += f"<strong>{part}</strong>"
            else:
                formatted_line += part
        return formatted_line

    def escape_single_asterisk(text):
        """Helper function to escape single asterisks."""
        return text.replace("*", "&#42;")

    for line in lines:
        line = line.strip()
        
        # Check for the heading indicator
        if line.startswith("##"):
            after_heading = True
            continue  # Skip the current line, it's just the heading indicator
        
        if after_heading:
            # Wrap the first line after ## with <h3> tags
            formatted_html += f'<h3>{line}</h3>'
            after_heading = False  # Reset the flag after processing
            continue
        
        # Formatting the response text before the table
        if not line.startswith("|") and not in_table:
            # Make only the text between ** ** bold
            formatted_line = bold_text(line)
            formatted_html += f'<p>{formatted_line}</p>'
        
        # Start table section
        if line.startswith("|---"):
            in_table = True
            table_html += '<table style="width:100%; border-collapse: collapse;"><thead><tr>'
            continue
        
        # Table content handling
        if line.startswith("|") and in_table:
            if "Meal" in line and not "</th>" in table_html:
                headers = line.split("|")[1:-1]  # Split and ignore the leading and trailing pipes
                for header in headers:
                    table_html += f'<th style="border: 1px solid #ddd; padding: 8px; text-align: left; background-color: #f4f4f4;">{bold_text(header.strip())}</th>'
                table_html += '</tr></thead><tbody>'
            else:
                # Table rows
                columns = line.split("|")[1:-1]
                table_html += '<tr>'
                for column in columns:
                    formatted_column = bold_text(escape_single_asterisk(column.strip()))
                    table_html += f'<td style="border: 1px solid #ddd; padding: 8px;">{formatted_column}</td>'
                table_html += '</tr>'
        
        elif in_table and line == "":
            in_table = False
            table_html += '</tbody></table>'
            formatted_html += table_html
    
    if '</tbody></table>' not in table_html:
        table_html += '</tbody></table>'
        formatted_html += table_html
    formatted_html += "</div>"
    
    return format_response_as_table(raw_response)
    # Split the response by newlines
    lines = raw_response.split("\n")
    
    # Initialize HTML sections
    formatted_html = ''
    table_html = ''
    formatted_html += "<div style='padding-top: 10px;'>"
    in_table = False
    after_heading = False  # Flag to check if we are processing the first line after ##
    
    def bold_text(text):
        """Helper function to make text between ** ** bold."""
        formatted_line = ""
        parts = text.split("")
        for i, part in enumerate(parts):
            if i % 2 == 1:  # Odd indices are between ** **
                formatted_line += f"<strong>{part}</strong>"
            else:
                formatted_line += part
        return formatted_line

    def escape_single_asterisk(text):
        """Helper function to escape single asterisks."""
        return text.replace("*", "&#42;")

    for line in lines:
        line = line.strip()
        
        # Check for the heading indicator
        if line.startswith("##"):
            after_heading = True
            continue  # Skip the current line, it's just the heading indicator
        
        if after_heading:
            # Wrap the first line after ## with <h3> tags
            formatted_html += f'<h3>{line}</h3>'
            after_heading = False  # Reset the flag after processing
            continue
        
        # Formatting the response text before the table
        if not line.startswith("|") and not in_table:
            # Make only the text between ** ** bold
            formatted_line = bold_text(line)
            formatted_html += f'<p>{formatted_line}</p>'
        
        # Start table section
        if line.startswith("|---"):
            in_table = True
            table_html += '<table style="width:100%; border-collapse: collapse;"><thead><tr>'
            continue
        
        # Table content handling
        if line.startswith("|") and in_table:
            if "Meal" in line and not "</th>" in table_html:
                headers = line.split("|")[1:-1]  # Split and ignore the leading and trailing pipes
                for header in headers:
                    table_html += f'<th style="border: 1px solid #ddd; padding: 8px; text-align: left; background-color: #f4f4f4;">{bold_text(header.strip())}</th>'
                table_html += '</tr></thead><tbody>'
            else:
                # Table rows
                columns = line.split("|")[1:-1]
                table_html += '<tr>'
                for column in columns:
                    formatted_column = bold_text(escape_single_asterisk(column.strip()))
                    table_html += f'<td style="border: 1px solid #ddd; padding: 8px;">{formatted_column}</td>'
                table_html += '</tr>'
        
        elif in_table and line == "":
            in_table = False
            table_html += '</tbody></table>'
            formatted_html += table_html
    
    if '</tbody></table>' not in table_html:
        table_html += '</tbody></table>'
        formatted_html += table_html
    formatted_html += "</div>"
    
    return formatted_html