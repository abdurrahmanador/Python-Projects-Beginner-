import pyperclip, re

# Phone number regex pattern
phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))?       # Area code (optional)
    (\s|-|\.)?               # Separator (optional)
    (\d{3})                  # First 3 digits
    (\s|-|\.)                # Separator (required)
    (\d{4})                  # Last 4 digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # Extension (optional)
    )''', re.VERBOSE)

# Email regex pattern
email_re = re.compile(r'''(
  [a-zA-Z0-9._%+-]+        # Username
  @                        # @ symbol
  [a-zA-Z0-9.-]+           # Domain name
  (\.[a-zA-Z]{2,4})        # Dot-something
  )''', re.VERBOSE)

# Get text from clipboard
#text = str(pyperclip.paste())
text = """
Call me at 415-555-1234 ext 99 or (212) 555-0000.
You can also email me at test.email@gmail.com or example123@mail.co.uk.
"""


matches = []

# Find phone numbers in the text
for groups in phone_re.findall(text):
    phone_number = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phone_number += ' x' + groups[8]  # groups[8] is the extension number
    matches.append(phone_number)

# Find emails in the text
for groups in email_re.findall(text):
    matches.append(groups[0])  # groups[0] is the full email address

# Copy results to clipboard and print them
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
