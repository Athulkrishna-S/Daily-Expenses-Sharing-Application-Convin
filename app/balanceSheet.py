from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
import io

def generateBalanceSheet(users):
    overall_expenses = {}
    total_expense = 0

    for user in users:
        for purpose, amount in user.get("expenses", {}).items():
            overall_expenses[purpose] = overall_expenses.get(purpose, 0) + amount
            total_expense += amount

    # Create a BytesIO buffer for the PDF
    buffer = io.BytesIO()

    # Create a PDF document
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    header_style = styles['Heading2']
    sub_header_style = styles['Heading3']
    body_style = styles['BodyText']

    # Title
    elements.append(Paragraph("Balance Sheet", title_style))
    
    # Individual Expenses
    elements.append(Paragraph("Individual Expenses", header_style))
    
    for user in users:
        elements.append(Paragraph(f"{user['name']} ({user['email']})", sub_header_style))
        
        # Create a table for individual expenses
        data = [["Purpose", "Amount"]]
        for purpose, amount in user.get("expenses", {}).items():
            data.append([purpose, f"Rs {amount:.2f}"])

        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        
        elements.append(table)

    # Overall Expenses
    elements.append(Paragraph("Overall Expenses", header_style))
    
    overall_data = [["Purpose", "Amount"]]
    for purpose, amount in overall_expenses.items():
        overall_data.append([purpose, f"Rs {amount:.2f}"])
    
    overall_table = Table(overall_data)
    overall_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    elements.append(overall_table)

    # Total Expense
    total_data = [["Total", f"Rs {total_expense:.2f}"]]
    total_table = Table(total_data)
    total_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(total_table)

    # Build the PDF
    doc.build(elements)

    # Get the PDF data from the buffer
    pdf_data = buffer.getvalue()
    buffer.close()
    
    return pdf_data
