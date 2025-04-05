# Automatic Registration Script

This is an automated registration script that can:
1. Automatically log in to Outlook email
2. Open a specified webpage and complete registration
3. Automatically retrieve and fill in verification codes

## Features

- Automatic Outlook login
- Automatic verification code retrieval
- Automatic form filling
- Support for custom registration pages
- Error handling mechanism

## Requirements

1. Python 3.7 or higher
2. Chrome browser
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Edit the `.env` file with your information:
   ```
   OUTLOOK_EMAIL=your_email@outlook.com
   OUTLOOK_PASSWORD=your_password
   IMAP_SERVER=outlook.office365.com
   REGISTRATION_URL=your_registration_url
   ```

2. Run the script:
   ```bash
   python auto_register.py
   ```

## Notes

- Ensure your Outlook account has IMAP access enabled
- CSS selectors in the script need to be adjusted according to the actual registration page
- Verification code retrieval logic may need to be adjusted based on the actual email format
- Manual intervention may be required if verification code recognition fails

## Security Tips

- Keep your account credentials secure
- Do not share the `.env` file containing real passwords
- Change passwords regularly

## Custom Configuration

To modify the registration page element selectors, edit the `register_account` function in `auto_register.py` and adjust the CSS selectors according to the actual page elements.