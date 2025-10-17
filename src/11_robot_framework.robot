*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${error message}    Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz
${haslo}   haasss
*** Keywords ***
kilord kamila
    log to console    Siema
    Open browser    https://pl.wikipedia.org/    gc
    maximize browser window
    click element    pt-login-2

*** Test Cases ***
Test 1
    kilord kamila
    input text    wpName1    Kamil
    input password    wpPassword    ${haslo}
    Checkbox Should not Be Selected    wpRemember
    click button    wploginattempt
    Wait Until Element Is Visible    wploginattempt    5
    ${text}   get text   xpath:/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[3]/div/form/div[1]/div
    Should Be Equal As Strings   ${text}     ${error message}
    Close Browser
