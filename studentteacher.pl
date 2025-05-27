% student(StudentName).
student('Alice').
student('Bob').
student('Carol').

% teacher(TeacherName).
teacher('Dr. Smith').
teacher('Prof. Johnson').

% subject(SubjectCode, SubjectName).
subject(cs101, 'Computer Science').
subject(ma102, 'Mathematics').

% teaches(TeacherName, SubjectCode).
teaches('Dr. Smith', cs101).
teaches('Prof. Johnson', ma102).

% enrolled(StudentName, SubjectCode).
enrolled('Alice', cs101).
enrolled('Bob', cs101).
enrolled('Carol', ma102).
