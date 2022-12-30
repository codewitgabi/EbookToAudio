from django.shortcuts import render
import pyttsx3
import PyPDF2
from django.http import JsonResponse
import json
import os


def read_text_file(file):
    try:
        with open(file, "r") as f:
            content = f.read()
            eng = pyttsx3.init()
            eng.say(content)
            eng.runAndWait()

    except FileNotFoundError:
        pass


def read_PDF_file(file):
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
        pass

def index(request):
    return render(request, "main/index.html")


def read_file(request):
    data = json.loads(request.body)
    file = data.get("file")
    extension = file.split(".")[-1]

    if extension == "txt":
        read_text_file(file)
    elif extension == "pdf":
        read_PDF_file(file)

    return JsonResponse("Done", safe= False)


def save_txt_audio(file):
    try:
        with open(file, "r") as f:
            content = f.read()
            eng = pyttsx3.init()
            eng.save_to_file(content, f"{os.path.expanduser('~')}{os.path.sep}Downloads{os.path.sep}project.mp3")
            eng.runAndWait()

    except FileNotFoundError:
        pass

def save_pdf_audio(file):
    pass

def save_audio(request):
    data = json.loads(request.body)
    file = data.get("file")
    extension = file.split(".")[-1]

    if extension == "txt":
        save_txt_audio(file)
    elif extension == "pdf":
        save_pdf_audio(file)

    return JsonResponse("Download completed", safe= False)