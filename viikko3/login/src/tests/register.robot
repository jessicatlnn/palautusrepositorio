*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set username  nalle
    Set Password  nalle123
    Set Password Confirmation  nalle123
    Click  button >> text=Register
    Get Title  ==  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set username  na
    Set Password  nalle123
    Set Password Confirmation  nalle123
    Click  button >> text=Register

Register With Valid Username And Too Short Password
    Set username  kalle
    Set Password  kalle1
    Set Password Confirmation  kalle1
    Click  button >> text=Register

Register With Username That Is Already In Use
    Set username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register

Register With Password That Contains Only Lowercase Letters
    Set username  nalle
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Page Should Be Open
    Get Text  body  *=  Salasanan täytyy sisältää vähintään yksi numero tai erikoismerkki.

Register With Password That Contains Only Uppercase Letters
    Set username  nalle
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Page Should Be Open
    Get Text  body  *=  Salasanan täytyy sisältää vähintään yksi numero tai erikoismerkki.

Register With Password That Contains Letters And Numbers
    Set username  nalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Get Title  ==  Welcome to Ohtu Application!

Register With Password That Contains Letters And Special Characters
    Set username  nalle
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Get Title  ==  Welcome to Ohtu Application!

Register With Matching Password Confirmation
    Set username  nalle
    Set Password  nalle123
    Set Password Confirmation  nalle123
    Click  button >> text=Register
    Get Title  ==  Welcome to Ohtu Application!

Register With Nonmatching Password Confirmation
    Set username  nalle
    Set Password  nalle123
    Set Password Confirmation  nalle456
    Click  button >> text=Register
    Register Page Should Be Open
    Get Text  body  *=  Salasanan ja sen vahvistuksen täytyy olla samat.

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Fill Secret  id=password_confirmation  $password_confirmation