
from openpyxl import load_workbook
import sys

# To install this package with conda run:
# conda install -c anaconda openpyxl

# Usage:
# python excel_to_text_file.py c:/folder/test.xlsx c:/folder/translation.txt


def main():
    if len(sys.argv) < 3:
        print("\nUsage error")
        print("\nex. excel_to_text.py test.xlsx translate.txt\n\n")
        sys.exit()

    directory = sys.argv[1]
    file = sys.argv[2]


    wb = load_workbook(directory)
    ws = wb.worksheets[0]

    txt_arry = []

    for a in range(14):
        for index, item in enumerate(ws):
            if index == 0:
                txt_arry.append('\n')
                txt_arry.append('language:' + str(item[a].value))
                print('language: ', item[a].value)
            else:
                txt_arry.append(item[a].value)
                print(item[a].value)
                
        txt_arry.append('\n')
        txt_arry.append('------------------------------------------')
        print('------------------------------------------')

    with open(file, 'w', encoding="utf-8") as outfile:
        for line in txt_arry:
            outfile.write("".join(line.strip()) + "\n")

    print('\n\nConversion finished!\n\n')

if __name__ == "__main__":
    main()

