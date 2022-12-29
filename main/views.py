from django.shortcuts import render
import pyttsx3
import PyPDF2
from django.contrib import messages


def read_text_file(request, file):
    try:
        with open(file, "r") as f:
            content = f.readlines()
            content = [line.strip() for line in content]
            eng = pyttsx3.init()

            for data in content:
                eng.say(data)
                eng.runAndWait()

    except FileNotFoundError:
        messages.error(request, f"{file} not found")


def read_PDF_file(request, file):
    try:
        with open(file, "rb") as pdfFile:
            pdfObj = PyPDF2.PdfReader(pdfFile)
            eng = pyttsx3.init()

            i = 0
            while i < len(pdfObj.pages):
                page = pdfObj.pages[i]

                eng.say(page.extract_text())
                eng.runAndWait()
                i += 1

    except UnicodeDecodeError:
        pass
    except FileNotFoundError:
        messages.error(request, f"{file} not found")


def index(request):
    if request.method == "POST":
        file = request.POST.get("filename")
        
        extension = file.split(".")[-1]

        if extension == "txt":
            read_text_file(request, file)
        elif extension == "pdf":
            read_PDF_file(request, file)
        else:
            messages.error(request, "File extension not supported")

    return render(request, "main/index.html")
