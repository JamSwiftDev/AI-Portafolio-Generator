from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_pdf(nombre, profesion, resumen, experiencia, educacion, habilidades):
    c = canvas.Canvas("cv.pdf", pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, nombre)
    y -= 20
    c.setFont("Helvetica", 14)
    c.drawString(50, y, profesion)
    y -= 40

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Resumen Profesional:")
    y -= 20
    c.setFont("Helvetica", 11)
    for line in resumen.split(". "):
        c.drawString(60, y, line.strip())
        y -= 15

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Experiencia:")
    y -= 20
    c.setFont("Helvetica", 11)
    for line in experiencia.split("\n"):
        c.drawString(60, y, line)
        y -= 15

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Educación:")
    y -= 20
    c.setFont("Helvetica", 11)
    for line in educacion.split("\n"):
        c.drawString(60, y, line)
        y -= 15

    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Habilidades:")
    y -= 20
    c.setFont("Helvetica", 11)
    c.drawString(60, y, habilidades)

    c.save()
