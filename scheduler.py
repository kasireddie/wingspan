import time
import pexpect   # 
import schedule  # Python schedule library

PORT = 5432
DBHOST = 'localhost'
DBNAME = 'wingspan'
DBUSER = 'wingspan'
PASSWORD = 'wingspanpass'

def backup_db():
    """ Backups the PostgreSQL database to a gzip file
    """
    with open('backup.sql', 'wb') as f:
        cmd = f'pg_dump -h {DBHOST} -U {DBUSER} {DBNAME}'
        child = pexpect.spawn(cmd)
        child.expect('Password:')
        child.sendline(PASSWORD)
        f.write(child.read())


if __name__=='__main__':
    # Every day at 12am or 00:00 time backup_db() is called.
    schedule.every().day.at('00:00').do(backup_db)

    while True:
        schedule.run_pending()
        time.sleep(1)