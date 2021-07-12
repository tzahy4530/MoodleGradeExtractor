import moodleGradeHandler as mgh

if __name__ == "__main__":
    username = input('Please Enter Username\n')
    password = input('Please Enter Password\n')
    course_url = input('Please Enter Exam URL\n'
                          'For Example: https://moodle2.bgu.ac.il/moodle/mod/quiz/view.php?id=1853627\n')
    course_module = mgh.parseCourseURL(course_url)
    token = mgh.getToken(username,password)
    quiz_id = mgh.getQuizId(token,course_module)
    userid = mgh.getUserId(token)
    exam_results = mgh.getExamResult(token,userid,quiz_id)
    print(exam_results)