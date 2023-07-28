import io
import openpyxl

def import_txt(file_name):
    with io.open(file_name, "r", encoding="utf-8") as f:
        content = f.read()
    return content

def transform_to_excel(content):
    wb = openpyxl.Workbook()
    ws = wb.active
    for line in content.splitlines():
        row = line.split(",")
        ws.append(row)
    wb.save("output.xlsx")


if __name__ == "__main__":
    file_name = "input.txt"
    content = import_txt(file_name)
    transform_to_excel(content)
