*** Settings ***
Library    ../keywords/Login_ExtremeKeywords.py

*** Keywords ***
Login to Extreme
    Open Extreme Homepage
    Enter Email    ahqatest+2022-wireless8A@gmail.com
    Enter Password And Login    Aerohive123
    Click Sign In
    Click Log Out
