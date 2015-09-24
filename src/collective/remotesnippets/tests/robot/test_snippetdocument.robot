# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.remotesnippets -t test_snippetdocument.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.remotesnippets.testing.COLLECTIVE_REMOTESNIPPETS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_snippetdocument.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a SnippetDocument
  Given a logged-in site administrator
    and an add snippetdocument form
   When I type 'My SnippetDocument' into the title field
    and I submit the form
   Then a snippetdocument with the title 'My SnippetDocument' has been created

Scenario: As a site administrator I can view a SnippetDocument
  Given a logged-in site administrator
    and a snippetdocument 'My SnippetDocument'
   When I go to the snippetdocument view
   Then I can see the snippetdocument title 'My SnippetDocument'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add snippetdocument form
  Go To  ${PLONE_URL}/++add++SnippetDocument

a snippetdocument 'My SnippetDocument'
  Create content  type=SnippetDocument  id=my-snippetdocument  title=My SnippetDocument


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the snippetdocument view
  Go To  ${PLONE_URL}/my-snippetdocument
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a snippetdocument with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the snippetdocument title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
