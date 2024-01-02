*** Settings ***
Library    global_test.py

*** Test Cases ***
Test for TL namespace
    Log To Console    ${xyz}
    Evaluate    globals()
    Run Keyword And Ignore Error    Evaluate    globals()['xyz']
    ${tl}    global_test.get_new_details    ${xyz}
    Set Global Variable    ${xyz}
    Evaluate    globals()
    Log To Console    ${xyz}
    Run Keyword And Ignore Error    Evaluate    globals()['xyz']

Test TL second
    [Tags]    second
    Log To Console    ${xyz}
    Evaluate    globals()
    Run Keyword And Ignore Error    Evaluate    globals()['xyz']
    Log To Console    ${xyz}
    Run Keyword And Ignore Error    Evaluate    globals()['xyz']

