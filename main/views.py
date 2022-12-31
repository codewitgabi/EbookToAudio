from django.shortcuts import render
import pyttsx3
import PyPDF2
from django.http import JsonResponse
import json
import os


def index(request):
    return render(request, "main/index.html")


def save_txt_audio(file):
    try:
        with open(file, "r") as f:
            content = f.read()
            eng = pyttsx3.init()
            #download_path = os.path.relpath(file).split(f"{os.path.sep}")[-1].split(".")[0]
            download_path = os.path.dirname(file)
            filename = file.split(".txt")[0].split(os.path.sep)[-1]
            eng.save(content, download_path + os.path.sep + filename + ".mp3")
            #eng.save_to_file(content, f"{os.path.expanduser('~')}{os.path.sep}Downloads{os.path.sep}{download_path}.mp3")
            eng.runAndWait()

    except FileNotFoundError:
        pass


def save_pdf_audio(file):
    try:
        with open(file, "rb") as pdfFile:
            pdfObj = PyPDF2.PdfReader(pdfFile)
            eng = pyttsx3.init()

            i = 0
            while i < len(pdfObj.pages):
                page = pdfObj.pages[i]
                eng.save_to_file(page.extract_text(), f"{os.path.expanduser('~')}{os.path.sep}Downloads{os.path.sep}page{i + 1}.mp3")
                eng.runAndWait()
                i += 1

    except UnicodeDecodeError:
        pass
    except FileNotFoundError:
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


# def read_text_file(file):
#     try:
#         with open(file, "r") as f:
#             content = f.read()
#             eng = pyttsx3.init()
#             eng.say(content)
#             eng.runAndWait()

#     except FileNotFoundError:
#         pass


# def read_PDF_file(file):
#     try:
#         with open(file, "rb") as pdfFile:
#             pdfObj = PyPDF2.PdfReader(pdfFile)
#             eng = pyttsx3.init()

#             i = 0
#             while i < len(pdfObj.pages):
#                 page = pdfObj.pages[i]

#                 eng.say(page.extract_text())
#                 eng.runAndWait()
#                 i += 1

#     except UnicodeDecodeError:
#         pass
#     except FileNotFoundError:
#         pass


# def read_file(request):
#     data = json.loads(request.body)
#     file = data.get("file")
#     extension = file.split(".")[-1]

#     if extension == "txt":
#         read_text_file(file)
#     elif extension == "pdf":
#         read_PDF_file(file)

#     return JsonResponse("Done", safe= False)
