from pyDatalog import pyDatalog


pyDatalog.create_terms('A, B, C, X, Y, human, subject, classroom, stud, les, classr')

human['Alex'] = 'pupil'
human['Sara'] = 'pupil'
human['John'] = 'pupil'
human['Joe'] = 'pupil'

human['Mr. Harrison'] = 'teacher'
human['Mr. Smith'] = 'teacher'
human['Mrs. White'] = 'teacher'

stud['Alex'] = 'mathematics'
stud['John'] = 'physics'
stud['Joe'] = 'physics'
stud['Sara'] = 'chemistry'


+(subject['mathematics'] == 'Mr. Harrison')
+(subject['physics'] == 'Mr. Smith')
+(subject['chemistry'] == 'Mrs. White')

+(classroom['15'] == 'mathematics')
+(classroom['23'] == 'physics')
+(classroom['31'] == 'chemistry')



(les[A] == B) <= (subject[C] == B) & (stud[A] == C)

(classr[A] == B) <= (stud[A] == C) & (classroom[B] == C)



print('pupil     teacher')
print(les[A] == B)
print()
print('pupil     classroom')
print(classr[A] == B)

