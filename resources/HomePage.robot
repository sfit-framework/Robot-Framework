*** Settings ***
Library    SeleniumLibrary
Library    ../keywords/HomeKeywords.py


*** Variables ***
${PRODUCT_NAME}    iPhone 13
${URL}        https://www.amazon.in
${EMAIL}      your_test_email@example.com
${PASSWORD}   your_test_password

*** Keywords ***
Open Amazon And Search Product
    HomeKeywords.open_amazon_homepage
    Search For Product    ${PRODUCT_NAME}
    get_list_option
