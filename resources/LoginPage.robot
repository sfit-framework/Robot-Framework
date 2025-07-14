*** Settings ***
Library    ../keywords/LoginKeywords.py

*** Keywords ***
Login To Amazon
    LoginKeywords.Open Amazon Homepage
    Click Sign In
    Enter Email    er.ashwanikumar@gmail.com
    Enter Password And Login    India@123