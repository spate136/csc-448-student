#import sys
#sys.path.append(".")

# Import the student solutions
import Syllabus

import pathlib
DIR=pathlib.Path(__file__).parent.absolute()

import joblib
joblib.load(DIR+"/answers_Syllabus.joblib")

def test_question_1():
    assert answer_question_1() == answers['answer_question_1']
    
def test_question_2():
    assert answer_question_2() == answers['answer_question_2']