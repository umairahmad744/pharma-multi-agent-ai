from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from datetime import datetime


def generate_pdf(report):
    filename = "report.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(
        Paragraph(
            "Pharma Manufacturing Intelligence Report",
            styles["Title"]
        )
    )
    story.append(Spacer(1, 20))

    # Query section
    story.append(
        Paragraph(
            "<b>Query:</b>",
            styles["Heading2"]
        )
    )
    story.append(
        Paragraph(
            report.get("query", "N/A"),
            styles["BodyText"]
        )
    )
    story.append(Spacer(1, 15))

    # Analysis section
    story.append(
        Paragraph(
            "<b>Analysis:</b>",
            styles["Heading2"]
        )
    )
    story.append(
        Paragraph(
            report.get("response", "No response available"),
            styles["BodyText"]
        )
    )
    story.append(Spacer(1, 15))

    # AI Route
    story.append(
        Paragraph(
            "<b>AI Route:</b>",
            styles["Heading2"]
        )
    )
    story.append(
        Paragraph(
            report.get("route", "N/A"),
            styles["BodyText"]
        )
    )
    story.append(Spacer(1, 20))

    # Footer
    story.append(
        Paragraph(
            f"<i>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}</i>",
            styles["Normal"]
        )
    )

    doc.build(story)
    return filename