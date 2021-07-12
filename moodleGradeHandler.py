import requests

MOODLE_URL = "https://moodle2.bgu.ac.il/moodle"
WEBSERVICE_URL = "webservice/rest/server.php?"

def parseCourseURL(url):
    try:
        course_module = url.split('id=')[1]
        return course_module
    except:
        raise ("Wrong Test URL Link.")


def getToken(username, password):
    try:
        response = requests.get(
            f'{MOODLE_URL}/login/token.php?username={username}&password={password}&service=moodle_mobile_app')
        token = response.json()['token']
        return token
    except:
        raise ("Invalid Username & Password")


def getQuizId(token, course_module):
    try:
        response = requests.get(
            f'{MOODLE_URL}/{WEBSERVICE_URL}wstoken={token}&moodlewsrestformat=json&wsfunction=mod_quiz_get_quizzes_by_courses')
        all_quiz = response.json()
        for quiz in all_quiz['quizzes']:
            if quiz['coursemodule'] == int(course_module):
                return quiz['id']
    except:
        raise ("Token Not Available")
    raise ("Invalid Exam URL")


def getUserId(token):
    try:
        response = requests.get(
            f'{MOODLE_URL}/{WEBSERVICE_URL}moodlewsrestformat=json&wsfunction=core_webservice_get_site_info&wstoken={token}')
        userid = response.json()['userid']
        return userid
    except:
        raise("Token Not Available")

def getExamResult(token,userid,quizid):
    try:
        response = requests.get(
            f'{MOODLE_URL}/{WEBSERVICE_URL}wstoken={token}&quizid={quizid}&userid={userid}&moodlewsrestformat=json&wsfunction=mod_quiz_get_user_best_grade')
        results = response.json()
        if results['hasgrade'] == False:
            return ("Exam results isn't avilable yet.")
        grade = results['grade']
        return (f"Your Grade is: {grade}")
    except:
        raise("Unable to get exam test, pleaes check if token is available ")
