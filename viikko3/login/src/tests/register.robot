*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set username  nalle
    Set Password  nalle123
    Click  button >> text=Register

Register With Too Short Username And Valid Password
    Set username  na
    Set Password  nalle123
    Click  button >> text=Register

Register With Valid Username And Too Short Password
    Set username  kalle
    Set Password  kalle1
    Click  button >> text=Register

Register With Username That Is Already In Use
    Set username  kalle
    Set Password  kalle123
    Click  button >> text=Register

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page