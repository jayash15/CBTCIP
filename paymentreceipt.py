from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import datetime


tabledata = [
    ["S.No.", "Item", "Quantity", "Amount"],
    ["1", "Pencil", "5.0", "25.0"],
    ["2", "Notebook 240pg", "2.0", "120.0"],
    ["Sub Total", "", "", "125.0"],
    ["Discount", "", "", "5.0"],
    ["Total", "", "", "120.0"],
]


namepdf = SimpleDocTemplate("paymentreceipt.pdf", pagesize=A4)


styles = getSampleStyleSheet()


titlestyle = styles["Heading1"]
titlestyle.alignment = 1


title = Paragraph("Stationary Shop", titlestyle)


date = datetime.datetime.now().strftime("%Y-%m-%d")
gstno = "GSTIN: 123456789012"

datedisplay = Paragraph(date, styles["Normal"])
gstnodisplay = Paragraph(gstno, styles["Normal"])


spacer = Spacer(1, 0.25 * inch)


styling = TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (4, 4), 1, colors.black),
        ("BACKGROUND", (0, 0), (3, 0), colors.blue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.pink),
    ]
)


table = Table(tabledata, style=styling)


namepdf.build([title, Spacer(1, 0.1 * inch), gstnodisplay, datedisplay, Spacer(1, 0.2 * inch), table])
