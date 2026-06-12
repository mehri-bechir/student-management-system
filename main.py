from PyQt5.uic import loadUi
from PyQt5.QtWidgets import*
from pickle import*
student=dict(name=str,age=int,means=int)
student_modified=dict(name=str,age=int,means=int)
#
def fill_table_students():
    student_file=open("student.dat","rb")
    #line_number It is the last row number in the table.
    line_number=0
    end_file=False
    while end_file==False:
        try:
        
            student=load(student_file)
            w.table_students.insertRow(line_number)
            w.table_students.setItem(line_number,0,QTableWidgetItem(student["name"]))
            w.table_students.setItem(line_number,1,QTableWidgetItem(str(student["age"])))
            w.table_students.setItem(line_number,2,QTableWidgetItem(str(student["means"])+"%"))
            line_number=line_number+1
        except EOFError:
            end_file=True
    student_file.close()    

# then clicked the boutton "add"
def add():
    student={}
    name=w.name_student.text()
    age=w.age_student.text()
    means=w.means_student.text()
    if name=="" or age=="" or means=="":
        QMessageBox.critical(w,"errer","You must write in all the boxes")
    elif not(alpha_string(name) and name.find("  ")==-1):
        #alpha_string is fonction check if the name have alpha_string and space or not.
        QMessageBox.critical(w,"errer","The name should consist of a group of letters, and spaces if possible.")
    elif not(age.isdecimal() and 6<=int(age)<=20):
        QMessageBox.critical(w,"errer","The age must be between 6 and 20 years.")
    elif not(means.isdecimal()and 0<=int(means)<=100):
        QMessageBox.critical(w,"errer","The average must be a number between 0 and 100")
    else:
        student["name"]=name
        student["age"]=int(age)
        student["means"]=int(means)
        student_file=open("student.dat","ab")
        dump(student,student_file)
        student_file.close()
        #line_number It is the last row number in the table.
        line_number=w.table_students.rowCount()
        w.table_students.insertRow(line_number)
        w.table_students.setItem(line_number,0,QTableWidgetItem(name))
        w.table_students.setItem(line_number,1,QTableWidgetItem(str(age)))
        w.table_students.setItem(line_number,2,QTableWidgetItem(str(means)+"%"))
        w.name_student.clear()
        w.age_student.clear()
        w.means_student.clear()

def alpha_string(name):
    test=True
    # i it is the indic of name
    i=0
    while i<len(name) and test:
        if "A"<=name[i].upper()<="Z" or name[i]==" ":
            i=i+1
        else:
            test=False
    return test
## if clicked the boutton "modified"
def modified():
    if w.table_students.currentRow()!=-1:
        Selected_line=w.table_students.currentRow()
        #Selected_line the row clicked in the students table .
        
        name=w.name_student.text()
        age=w.age_student.text()
        means=w.means_student.text()
        name1=w.table_students.item(Selected_line,0).text()
        age1=int(w.table_students.item(Selected_line,1).text())
        means1=w.table_students.item(Selected_line,2).text()
        means1=int(means1[:len(means1)-1])
        if name=="" or age=="" or means=="":
            QMessageBox.critical(w,"errer","You must write in all the boxes")
        elif not(alpha_string(name) and name.find("  ")==-1):
            QMessageBox.critical(w,"errer","The name should consist of a group of letters, and spaces if possible.")
        elif not(age.isdecimal() and 6<=int(age)<=20):
            QMessageBox.critical(w,"errer","The age must be between 6 and 20 years.")
        elif not(means.isdecimal()and 0<=int(means)<=100):
            QMessageBox.critical(w,"errer","The average must be a number between 0 and 100")    
        else:
            student={}
            student["name"]=name1
            student["age"]=age1
            student["means"]=means1
            student_modified={}
            student_modified["name"]=name
            student_modified["age"]=int(age)
            student_modified["means"]=int(means)
            list_file=[]
            list_table=[]
            fill_list_file(list_file,student,student_modified)
            fill_list_table(list_table)
            list_table[Selected_line]=student_modified
            w.table_students.setRowCount(0)
            fill_table_students_modified(list_table)
            fill_file_student_modified(list_file)
            w.name_student.clear()
            w.age_student.clear()
            w.means_student.clear()
    else:
        QMessageBox.critical(w,"errer","You need to click on any cell in the table.")

#This function populates the file's list and adds or changes the student whose information has been altered.
def fill_list_file(list_file,student,student_modified):
    student_file=open("student.dat","rb")
    end_file=False
    while end_file==False:
        try:
            stud=load(student_file)
            if stud==student:
                list_file.append(student_modified)
                student["name"]=student["name"]+"*"
            else:
                
                
                
                list_file.append(stud)
                
        except EOFError:
            end_file=True
    student_file.close()
#This function adds the students currently in the table.in the list "list_table"
def fill_list_table(list_table):
    last_line=w.table_students.rowCount()
    row=0
    while row<=last_line:
        student={}
        name=w.table_students.item(row,0)
        age=w.table_students.item(row,1)
        means=w.table_students.item(row,2)
        if name and age and means:
            student["name"]=name.text()
            student["age"]=int(age.text())
            means=means.text()[:len(means.text())-1]
            student["means"]=int(means)
            list_table.append(student)
        row=row+1
#This function prints the students listed "list_table" onto the student table.
def fill_table_students_modified(list_table):
    line_number=0
    for student in list_table:
        w.table_students.insertRow(line_number)
        w.table_students.setItem(line_number,0,QTableWidgetItem(student["name"]))
        w.table_students.setItem(line_number,1,QTableWidgetItem(str(student["age"])))
        w.table_students.setItem(line_number,2,QTableWidgetItem(str(student["means"])+"%"))
        line_number=line_number+1
#This function updates the information in the file "student.dat" using the list "list_file".
def fill_file_student_modified(list_file):
    file_student=open("student.dat","wb")
    for student in list_file:
        dump(student,file_student)
    file_student.close()
#*****************************************************************************************************
#If you click on any cell in the student table, this function will display the student's name, age, and means average in the fields where they were entered.
def click():
    Selected_line=w.table_students.currentRow()
    name=w.table_students.item(Selected_line,0)
    age=w.table_students.item(Selected_line,1)
    means=w.table_students.item(Selected_line,2)
    if name is not None:

        w.name_student.setText(name.text())
        w.age_student.setText(age.text())
        means=means.text()[:len(means.text())-1]
        w.means_student.setText(means)
#*******************************************************************
#When you click on "delet", this function works.
def delete():
    if w.table_students.currentRow()!=-1:
        Selected_line=w.table_students.currentRow()
        #Selected_line the row clicked in the students table .
        student={}
        name=w.name_student.text()
        age=w.age_student.text()
        means=w.means_student.text()
        w.name_student.clear()
        w.age_student.clear()
        w.means_student.clear()
        student={}
        student["name"]=name
        student["age"]=int(age)
        student["means"]=int(means)
        list_file=[]
        fill_list_file_delete(list_file,student)
        fill_file_student_modified(list_file)
        w.table_students.removeRow(Selected_line)
         

    else:
        QMessageBox.critical(w,"errer","You need to click on any cell in the table.")
#This function sums the list of "list_file" students from the file "student.dat", excluding the student in question "student".
def fill_list_file_delete(list_file,student):
    student_file=open("student.dat","rb")
    end_file=False
    while end_file==False:
        try:
            stud=load(student_file)
            if not(stud==student):
                list_file.append(stud)  
            else:
                student["name"]=student["name"]+"*"

        except EOFError:
            end_file=True
    student_file.close()   

#When you press the search button, this function finds students who have the same name you entered to search for.
def search():
    name=w.name_student.text()
    if name=="":
        QMessageBox.critical(w,"errer","You must write in  boxes of name")
    elif not(alpha_string(name) and name.find("  ")==-1):
        QMessageBox.critical(w,"errer","The name should consist of a group of letters, and spaces if possible.")
    else:
        list_file_search=[]
        student_file=open("student.dat","rb")
        end_file=False
        while end_file==False:

            try:
                stud=load(student_file)
                if stud["name"]==name or stud["name"].find(name)!=-1:
                    list_file_search.append(stud)
            except EOFError:
                end_file=True
        student_file.close()
        w.table_students.setRowCount(0)
        fill_table_students_modified(list_file_search)
        w.name_student.clear()
        w.age_student.clear()
        w.means_student.clear()
def refresh():
    w.table_students.setRowCount(0)
    fill_table_students()
    w.name_student.clear()
    w.age_student.clear()
    w.means_student.clear()


app = QApplication([])
w = loadUi ("design.ui")
fill_table_students()
w.show()
w.button_add.clicked.connect (add)
w.button_modified.clicked.connect (modified)
w.button_delete.clicked.connect (delete)
w.button_search.clicked.connect (search)
w.table_students.cellClicked.connect(click)
w.button_refresh.clicked.connect (refresh)
app.exec()