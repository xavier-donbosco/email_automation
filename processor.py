# Databricks notebook source
# DBTITLE 1,Import Notebook
# MAGIC %run /Workspace/Users/xavier.donbosco@diggibyte.com/email_automation/utils

# COMMAND ----------

# DBTITLE 1,Get Parameters
dbutils.widgets.text("user_id","","user_id")
dbutils.widgets.text("password","","password")
dbutils.widgets.text("lst_recipient","","lst_recipient")

gmail_user     = dbutils.widgets.get("user_id")
gmail_password = dbutils.widgets.get("password")
to_emails      = eval(dbutils.widgets.get("lst_recipient"))

# COMMAND ----------

# DBTITLE 1,Send Mail
subject = 'Python Puzzles for the Everyday Coder'

msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = ', '.join(to_emails)
msg['Subject'] = subject

msg.attach(MIMEText(generate_html_body(random.choice(python_questions)), 'html'))

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)

    server.sendmail(gmail_user, to_emails, msg.as_string())
    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()
