import os, glob
from pdf2image import convert_from_path, convert_from_bytes



def main():
    pdf_list =[
        "./orgpdf/01.집합.pdf",
        "orgpdf/01.집합_해설.pdf",
        "orgpdf/02.명제.pdf",
        "orgpdf/02.명제_해설.pdf",
        "orgpdf/03.절대부등식.pdf",
        "orgpdf/03.절대부등식_해설.pdf",
        "orgpdf/04.함수유리함수무리함수.pdf",
        "orgpdf/04.함수유리함수무리함수_해설.pdf",
        "orgpdf/05.경우의수순열조합.pdf",
        "orgpdf/05.경우의수순열조합_해설.pdf",
        "orgpdf/고1-1기말범위.pdf",
        "orgpdf/고1-1기말범위_정답및해설.pdf",
        "orgpdf/고1-1중간범위.pdf",
        "orgpdf/고1-1중간범위_정답및해설.pdf" ]
    for pdf in pdf_list:
        images=convert_from_path(pdf)
        print("tests")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

