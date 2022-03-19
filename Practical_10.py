# NAME : ANKIT GANATRA
# ID : 20CE030
# Generate PDF file of your 3rd Semester Mark-sheet

# importing canvas
from reportlab.pdfgen.canvas import Canvas

file = Canvas("Marksheet_20CE030.pdf")
file.drawString(50, 830, "This is the marksheet of 20CE030 of 3rd Semester")
file.drawString(50, 800, "CE251 JAVA PROGRAMMING PRACTICAL: AA")
file.drawString(50, 780, "CE251 JAVA PROGRAMMING THEORY: AA")
file.drawString(50, 760, "CE252 DIGITAL ELECTRONICS PRACTICAL: BB")
file.drawString(50, 740, "CE252 DIGITAL ELECTRONICS THEORY: AB")
file.drawString(50, 720, "CE257 DATA COMMUNICATION & NETWORKING PRACTICAL: AA")
file.drawString(50, 700, "CE257 DATA COMMUNICATION & NETWORKING THEORY: AB")
file.drawString(50, 680, "HS123.02 A CREATIVITY, PROBLEM SOLVING AND INNOVATION PRACTICAL: AA")
file.drawString(50, 660, "MA253 DISTINCT MATHEMATICS AND ALGEBRA THEORY: AA")
file.drawString(50, 640, "CE244 SOFTWARE GROUP PROJECT-1  PRACTICAL: AA")
file.drawString(50, 620, "PD261 ASTROPHYSICS, SPACE AND COSMOS-1  PRACTICAL: AA")
file.drawString(50, 590, "CGPA : 9.11")
file.drawString(50, 570, "SGPA : 9.02")
file.save()

# Setting the Page Size

from reportlab.lib.units import inch, cm  # noqa

print(cm)
print(inch)

file = Canvas("Marksheet_20CE030.pdf", pagesize=(8.5 * inch, 11 * inch))

from reportlab.lib.pagesizes import LETTER  # noqa

file = Canvas("Marksheet_20CE030.pdf", pagesize=LETTER)
print(LETTER)

# Setting Font Properties

file = Canvas("font-example.pdf", pagesize=LETTER)
file.setFont("Times-Roman", 18)
file.drawString(1 * inch, 10 * inch, "Times New Roman (20 pt)")
file.save()

# The code below creates a PDF with blue text
from reportlab.lib.colors import blue 
from reportlab.lib.pagesizes import LETTER 
from reportlab.lib.units import inch 
from reportlab.pdfgen.canvas import Canvas  

file = Canvas("font-colors.pdf", pagesize=LETTER)

# Set font to Times New Roman with 12-point size
file.setFont("Times-Roman", 12)

# Draw blue text one inch from the left and ten
# inches from the bottom
file.setFillColor(blue)
file.drawString(1 * inch, 10 * inch, "Blue text")

# Save the PDF file
file.save()


# GITHUB REPO LINK : https://github.com/Ankit-34/Collage-Assignments