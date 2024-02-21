#lib do playwright base
import pyperclip # lib para área de transferencia do windows
# from docx import Document # lib para interaçao comm word.docx
# from docx.shared import Inches # lib para interaçao comm word.docx 
# import pandas as pd # lib para tratamento de dados
# import re # lib regex
# from openpyxl import Workbook # lib para interaçao comm excel.xlsx
# import asyncio # lib para func asyn
# from tkinter import * # lib de interface
# from tkinter import ttk # lib de interface
# import json # lib para interaçao c/ Json
# import os # lib Sys func
# from typing import Generator # lib simulaçao de teclas
# import pytest # lib de testes do Playwright
# from playwright.sync_api import Playwright, APIRequestContext # lib para interação API do Playwright
# from bbrest import BbRest # lib python blackboard
from playwright.sync_api import Playwright, sync_playwright, expect

#python -m playwright codegen

# https://sereduc.blackboard.com/webapps/assessment/do/authoring/viewAssessmentManager?assessmentType=Pool&course_id=
# link root para criação de BQ só aceita ID interno

# https://sereduc.blackboard.com/learn/api/public/v3/courses/courseId:
# API to find internal ID course

#https://developer.blackboard.com/portal/displayApi
#link doc API black

#func sincrona
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # clipBoard = pyperclip.paste()
    pyperclip.copy("6848")
    page.goto("https://sereduc.blackboard.com/}")
    page.wait_for_load_state('domcontentloaded')
    page.get_by_role("button", name="OK").click()
    page.get_by_text("Nome de usuário").click()
    page.get_by_label("Nome de usuário").fill("rafael.dias")
    page.get_by_label("Nome de usuário").press("Tab")
    page.get_by_label("Senha").fill("123321!")
    page.get_by_label("Senha").press("Enter")
    page.wait_for_load_state('domcontentloaded')
    page.get_by_role("link", name="Administrador").click()
    page.wait_for_load_state('domcontentloaded')
    page.frame_locator("iframe[name=\"bb-base-admin-iframe\"]").get_by_role("link", name="Cursos").click()
    page.wait_for_load_state("domcontentloaded")
    page.frame_locator("iframe[name=\"bb-base-admin-iframe\"]").get_by_role("combobox", name="Atributo").select_option("CourseId")
    page.frame_locator("iframe[name=\"bb-base-admin-iframe\"]").get_by_role("combobox", name="Filtro").select_option("Equals")
    page.frame_locator("iframe[name=\"bb-base-admin-iframe\"]").get_by_label("Pesquisar:").click()
    page.frame_locator("iframe[name=\"bb-base-admin-iframe\"]").get_by_label("Pesquisar:").fill(pyperclip.paste())
    page.frame_locator("iframe[name=\"bb-base-admin-iframe\"]").get_by_label("Pesquisar:").press("Enter")
    page.wait_for_load_state('domcontentloaded') # wait page to fully load
    page.wait_for_timeout(5000)
    page.frame_locator("iframe[name=\"bb-base-admin-iframe\"]").get_by_role("button", name="Menu de opções: Código do Curso").hover()
    page.frame_locator("iframe[name=\"bb-base-admin-iframe\"]").get_by_role("menuitem", name="Copiar").click()
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_timeout(10000)

    # ---------------------
    context.close()
    browser.close()

#start da func
with sync_playwright() as playwright:
    run(playwright)
