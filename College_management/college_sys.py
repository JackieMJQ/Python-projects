import mysql.connector as mysql

hostname = "localhost"
user_name = "root"
pwd = "20010227"


db = mysql.connect(host=hostname, user = user_name, password = pwd, database = 'College_Management_sys')
command_handler = db.cursor(buffered = True)

def admin_session():
    print('Login sucess. Welcome admin system!')
    while 1:
        print()
        print('Admin Menu')
        print('1. Register new student')
        print('2. Register new teacher')
        print('3. Delete existing student')
        print('4. Delete existing teacher')
        print('5. Logout')
        
        user_option = input(str('Option:  '))
        if user_option == '1':
            print()
            print('Register new student')
            username = input(str('Student username:  '))
            password = input(str('Student password:  '))
            command_handler.execute(f"""INSERT INTO users (username, password, privilege) VALUES ("{username}", "{password}", 'student')""")
            db.commit()
            print()
            print(username + ' has been registered as a student.')
            
        elif user_option == '2':
            print()
            print('Register new teacher')
            username = input(str('Teacher username:  '))
            password = input(str('Teacher password:  '))
            command_handler.execute(f"""INSERT INTO users (username, password, privilege) VALUES ("{username}", "{password}", 'teacher')""")
            db.commit()
            print()
            print(username + ' has been registered as a teacher.')
            
        elif user_option == '3':
            print()
            print('Delete existing student account')
            username = input(str('Student username:  '))
            command_handler.execute(f"""DELETE from users where username = '{username}' AND privilege = 'student'""")
            db.commit()
            print()
            if command_handler.rowcount < 1:
                print('User not found')
            else:
                print(username + ' has been deleted.')
                
        elif user_option == '4':
            print()
            print('Delete existing teacher account')
            username = input(str('Teacher username:  '))
            command_handler.execute(f"""DELETE from users where username = '{username}' AND privilege = 'teacher'""")
            db.commit()
            print()
            if command_handler.rowcount < 1:
                print('User not found')
            else:
                print(username + ' has been deleted.')

        elif user_option == '5':
            break
        
        else:
            print('No valid option, please try again.')

def auth_admin():
    print()
    print('Admin Login')
    print()
    username = input(str('User Name:  '))
    password = input(str('Password:  '))
    
    if username == 'admin':
        if password == 'password':
            admin_session()
        else:
            print('Incorrect password!')
    else:
        print('Login details not recognized')
        
        
def main():
    while 1:
        print('Welcome to the college system')
        print()
        print('1. Login as student')
        print('2. Login as teacher')
        print('3. Login as admin')
        
        user_option = input(str('Option : '))
        if user_option == '1':
            print('Student Login')
        elif user_option == '2':
            print('Teacher Login')
        elif user_option == '3':
            auth_admin()
        else:
            print('No valid option was selected')
            

main()