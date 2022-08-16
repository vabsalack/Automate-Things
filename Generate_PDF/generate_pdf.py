from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

report = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()

report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])


table_data = []
for key, value in fruit.items():
    table_data.append([key, value])


table_style = [("GRID", (0, 0), (-1, -1), 1, colors.blue)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

report_pie = Pie(width=3*5, height=3*5)
report_pie.data = []
report_pie.labels = []

for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

report_chart = Drawing()
report_chart.add(report_pie)

report.build([report_title, report_table, report_chart])





