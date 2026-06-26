import smtplib
import psycopg2
import logging
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import SMTP_PASSWORD,SMTP_USERNAME,SMTP_PORT,SMTP_SERVER 
from config import  db_connect_name,db_connect_host ,db_connect_password,db_connect_port,db_connect_user

def connection():
    try:
        conn = psycopg2.connect(
            host = db_connect_host,
            dbname = db_connect_name,
            user = db_connect_user,
            password = db_connect_password,
            port = db_connect_port,
        )

        print("Connection Successful")
        return conn
    
    except Exception as e:
        logging.error("SMTP login failed: Authentication unsuccessful due to invalid credentials or disabled SMTP AUTH.")
        print(f"connection unsucessful:{e}")
        return None
    
conn = connection()
cur = conn.cursor()

cur.execute("SELECT version();")


print(cur.fetchone())

# def setup_email_database():
#     try:
       
        # cur.execute("DROP TABLE IF EXISTS email CASCADE;")
        
        # cur.execute("""
        # CREATE TABLE email(
        #     email_id SERIAL PRIMARY KEY,
        #     email_to VARCHAR(50),
        #     contact_number BIGINT,
        #     notes_source VARCHAR(100),
        #     csr_projects VARCHAR(300),
        #     development_sectors VARCHAR(100),
        #     state VARCHAR(100),
        #     district VARCHAR(100),
        #     project_amount_outlay_cr VARCHAR(100),
        #     mode_of_implementation VARCHAR(100),
        #     company_name VARCHAR(100),
        #     financial_year VARCHAR(20),
        #     amount_spent_cr VARCHAR(100)
        # );
        # """)
        # print("Table 'email' created successfully.")

       
        # cur.execute("""
        # INSERT INTO email (
        #     email_to, contact_number, notes_source, csr_projects, 
        #     development_sectors, state, district, project_amount_outlay_cr, 
        #     mode_of_implementation, company_name, financial_year, amount_spent_cr
        # ) VALUES
        # ('prianshetty06@gmail.com', 8657226936, 'Head of CSR', 'Health Care', 'Andhra Pradesh', 'Nec/ Not Mentioned', '1.88', '1.88', 'Other Implementing agencies', 'Asian Paints Limited', 'FY 2020-21', '0.05'),
        # ('parandeindrayani7@gmail.com', 3256174628, 'Infosys Foundation', 'Safe Drinking Water', 'Andhra Pradesh', 'Nec/ Not Mentioned', '3.76', '3.76', 'Directly by Company', 'Asian Paints Limited', 'FY 2020-21', '0.01'),
        # ('riddhimanjrekar@gmail.com', 5654328699, 'ICICI Foundation', 'Education','Pan India', 'Nec/ Not Mentioned', '9.35', '9.35', 'Directly by Company', 'Asian Paints Limited', 'FY 2018-19', '0.01'),
        # ('vasudha.manjrekar16@gmail.com', 4587536896, 'Uses Bajaj Group CSR email', 'Health Care','Pan India', 'Nec/ Not Mentioned', '9.93', '9.93', 'Directly by Company', 'Asian Paints Limited', 'FY 2018-19', '0.2'),
        # ('oamb.work@gmail.com','2456743246');
        # """)
        
        
#         conn.commit()
#         print("Data insertion completed successfully.")

#     except Exception as e:
#         conn.rollback()
#         print(f"An error occurred: {e}")


# setup_email_database()

logging.basicConfig(
    filename = 'example_log.log',
    filemode = 'a',
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s' ,
    datefmt = '%Y-%m-%d %H:%M:%S' ,
    level = logging.DEBUG
)

def send_bulk_email():

    try:
        logging.info("Email attempt to send")
        cur.execute("""
            SELECT email_to, company_name, csr_projects
            FROM email;
                            
        """)
        recipients = cur.fetchall()

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls() 
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        for row in recipients:
            email_to = row[0]
            company_name = row[1]
            csr_projects = row[2]

            message = MIMEMultipart()
            message["To"] = email_to
            message["From"] = SMTP_USERNAME
            message["Subject"] = f"Inquiry Regarding CSR Initiatives at {company_name}"

            text_body = f"""Dear Team,

We are reaching out to discuss your ongoing CSR program: {csr_projects}. 
We hope to connect and discover potential collaboration opportunities.

Best regards,
Synergy Connect Team
"""
            html_body = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ margin: 0; padding: 0; background-color: #f4f4f7; font-family: Arial, sans-serif; }}
        table {{ border-spacing: 0; border-collapse: collapse; width: 100%; }}
        @media screen and (max-width: 600px) {{
            .wrapper {{ width: 100% !important; padding: 10px !important; }}
            .content {{ padding: 20px !important; }}
        }}
    </style>
</head>
<body>
    <table role="presentation" width="100%" bgcolor="#f4f4f7" cellspacing="0" cellpadding="0" border="0">
        <tr>
            <td align="center" style="padding: 20px 0;">
                <table class="wrapper" role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" style="background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                    
                    <!-- Header -->
                    <tr>
                        <td align="center" bgcolor="#4f46e5" style="padding: 25px 20px;">
                            <h1 style="margin: 0; color: #ffffff; font-size: 22px; font-weight: bold; letter-spacing: 1px;">
                                SYNERGY CONNECT
                            </h1>
                        </td>
                    </tr>

                    <!-- Body Content -->
                    <tr>
                        <td class="content" style="padding: 40px 30px; color: #333333; font-size: 16px; line-height: 1.6;">
                            <h2 style="margin-top: 0; color: #111111; font-size: 18px;">Dear Team,</h2>
                            
                            <p style="margin-bottom: 20px;">
                                We are reaching out to discuss your ongoing CSR program focused on <strong>{csr_projects}</strong> at <strong>{company_name}</strong>.
                            </p>
                            
                            <p style="margin-bottom: 30px;">
                                Our team tracks structural development sectors, and we hope to connect with you to discover potential collaboration opportunities that align with your strategic targets.
                            </p>

                            <!-- CTA Button -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center">
                                <tr>
                                    <td bgcolor="#4f46e5" style="border-radius: 4px; text-align: center;">
                                        <a href="https://example.com" target="_blank" style="background-color: #4f46e5; border: 1px solid #4f46e5; border-radius: 4px; color: #ffffff; display: inline-block; font-size: 15px; font-weight: bold; padding: 12px 24px; text-decoration: none;">
                                            Discuss Collaboration
                                        </a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td bgcolor="#f4f4f7" align="center" style="padding: 20px; color: #718096; font-size: 12px; border-top: 1px solid #e2e8f0;">
                            <p style="margin: 0 0 5px 0;">© 2026 Synergy Connect Team. All rights reserved.</p>
                            <p style="margin: 0;"><a href="#" style="color: #4f46e5; text-decoration: none;">Unsubscribe</a></p>
                        </td>
                    </tr>

                </table>
            </td>
        </tr>
    </table>
</body>
</html>"""

            message.attach(MIMEText(text_body, "plain"))
            message.attach(MIMEText(html_body, "html"))

            server.sendmail(SMTP_USERNAME, email_to, message.as_string())
            logging.info("Email sent successfully")

        server.quit()
        logging.info("Bulk Email sent successfully")

    except smtplib.SMTPAuthenticationError as auth_error:
        logging.error(f"SMTP authentication error(SMTP_SERVER error): {auth_error}")

    except smtplib.SMTPException as exc_err:
        logging.error(f"Exception error : {exc_err}")

send_bulk_email()
            