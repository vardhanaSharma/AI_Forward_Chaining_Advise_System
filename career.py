from durable.lang import *

with ruleset('interests'):
	
	@when_all((m.interest == 'data science') & (m.cgpa >= 7) & (m.concept == 'tc') & (m.must == 'no'))
	def datascience(c):
		c.assert_fact('concept',{'cc':'theory'})
		c.assert_fact('must',{'ccc':'no'})	
		c.assert_fact('courses',{'field':'datascience'})
		
	@when_all((m.interest == 'sde') & (m.cgpa >= 6) & (m.concept == 'tc') & (m.must == 'no'))
	def sde(c):
		c.assert_fact('concept',{'cc':'theory'})
		c.assert_fact('must',{'ccc':'no'})		
		c.assert_fact('courses',{'field':'sde'})

	@when_all((m.interest == 'design') & (m.cgpa >= 7) & (m.concept == 'tc') & (m.must == 'no'))
	def design(c):
		c.assert_fact('concept',{'cc':'theory'})
		c.assert_fact('must',{'ccc':'no'})	
		c.assert_fact('courses',{'field':'design'})
	
	@when_all((m.interest == 'cybersecurity') & (m.cgpa >= 8) & (m.concept == 'tc') & (m.must == 'no'))
	def cybersecurity(c):
		c.assert_fact('concept',{'cc':'theory'})
		c.assert_fact('must',{'ccc':'no'})	
		c.assert_fact('courses',{'field':'cybersecurity'})

	@when_all((m.interest == 'biology') & (m.cgpa >= 6) & (m.concept == 'tc') & (m.must == 'no'))
	def biology(c):
		c.assert_fact('concept',{'cc':'theory'})
		c.assert_fact('must',{'ccc':'no'})	
		c.assert_fact('courses',{'field':'biology'})

	@when_all((m.interest == 'data science') & (m.cgpa >= 7) & (m.concept == 'pc') & (m.must == 'no'))
	def datascience(c):
		c.assert_fact('concept',{'cc' : 'project'})
		c.assert_fact('must',{'ccc':'no'})	
		c.assert_fact('courses',{'field':'datascience'})
		
	@when_all((m.interest == 'sde') & (m.cgpa >= 6) & (m.concept == 'pc') & (m.must == 'no'))
	def sde(c):
		c.assert_fact('concept',{'cc' : 'project'})	
		c.assert_fact('must',{'ccc':'no'})	
		c.assert_fact('courses',{'field':'sde'})

	@when_all((m.interest == 'design') & (m.cgpa >= 7) & (m.concept == 'pc') & (m.must == 'no'))
	def design(c):
		c.assert_fact('concept',{'cc' : 'project'})
		c.assert_fact('must',{'ccc':'no'})	
		c.assert_fact('courses',{'field':'design'})
	
	@when_all((m.interest == 'cybersecurity') & (m.cgpa >= 8) & (m.concept == 'pc') & (m.must == 'no'))
	def cybersecurity(c):
		c.assert_fact('concept',{'cc' : 'project'})
		c.assert_fact('must',{'ccc':'no'})	
		c.assert_fact('courses',{'field':'cybersecurity'})

	@when_all((m.interest == 'biology') & (m.cgpa >= 6) & (m.concept == 'pc') & (m.must == 'no'))
	def biology(c):
		c.assert_fact('concept',{'cc' : 'project'})
		c.assert_fact('must',{'ccc':'no'})	
		c.assert_fact('courses',{'field':'biology'})

	@when_all((m.interest == 'data science') & (m.cgpa >= 7) & (m.concept == 'tc') & (m.must == 'yes'))
	def datascience(c):
		c.assert_fact('domain_jobs',{'selected_area':'data_science'})	
		c.assert_fact('concept',{'cc':'theory'})
		c.assert_fact('must',{'ccc':'yes'})
		
	@when_all((m.interest == 'sde') & (m.cgpa >= 6) & (m.concept == 'tc') & (m.must == 'yes'))
	def sde(c):
		c.assert_fact('domain_jobs',{'selected_area':'sde'})	
		c.assert_fact('concept',{'cc':'theory'})
		c.assert_fact('must',{'ccc':'yes'})	

	@when_all((m.interest == 'design') & (m.cgpa >= 7) & (m.concept == 'tc') & (m.must == 'yes'))
	def design(c):
		c.assert_fact('domain_jobs',{'selected_area':'design'})	
		c.assert_fact('concept',{'cc':'theory'})
		c.assert_fact('must',{'ccc':'yes'})
	
	@when_all((m.interest == 'cybersecurity') & (m.cgpa >= 8) & (m.concept == 'tc') & (m.must == 'yes'))
	def cybersecurity(c):
		c.assert_fact('domain_jobs',{'selected_area':'cyber_security'})
		c.assert_fact('concept',{'cc':'theory'})
		c.assert_fact('must',{'ccc':'yes'})

	@when_all((m.interest == 'biology') & (m.cgpa >= 6) & (m.concept == 'tc') & (m.must == 'yes'))
	def biology(c):
		c.assert_fact('domain_jobs',{'selected_area':'biology'})
		c.assert_fact('concept',{'cc':'theory'})
		c.assert_fact('must',{'ccc':'yes'})

	@when_all((m.interest == 'data science') & (m.cgpa >= 7) & (m.concept == 'pc') & (m.must == 'yes'))
	def datascience(c):
		c.assert_fact('domain_jobs',{'selected_area':'data_science'})	
		c.assert_fact('concept',{'cc' : 'project'})
		c.assert_fact('must',{'ccc':'yes'})
		
	@when_all((m.interest == 'sde') & (m.cgpa >= 6) & (m.concept == 'pc') & (m.must == 'yes'))
	def sde(c):
		c.assert_fact('domain_jobs',{'selected_area':'sde'})	
		c.assert_fact('concept',{'cc' : 'project'})	
		c.assert_fact('must',{'ccc':'yes'})

	@when_all((m.interest == 'design') & (m.cgpa >= 7) & (m.concept == 'pc') & (m.must == 'yes'))
	def design(c):
		c.assert_fact('domain_jobs',{'selected_area':'design'})	
		c.assert_fact('concept',{'cc' : 'project'})
		c.assert_fact('must',{'ccc':'yes'})
	
	@when_all((m.interest == 'cybersecurity') & (m.cgpa >= 8) & (m.concept == 'pc') & (m.must == 'yes'))
	def cybersecurity(c):
		c.assert_fact('domain_jobs',{'selected_area':'cyber_security'})
		c.assert_fact('concept',{'cc' : 'project'})
		c.assert_fact('must',{'ccc':'yes'})

	@when_all((m.interest == 'biology') & (m.cgpa >= 6) & (m.concept == 'pc') & (m.must == 'yes'))
	def biology(c):
		c.assert_fact('domain_jobs',{'selected_area':'biology'})
		c.assert_fact('concept',{'cc' : 'project'})
		c.assert_fact('must',{'ccc':'yes'})
	
	@when_all(+m.selection)
	def output(c):
		print('{0}'.format(c.m.selection))

with ruleset('concept'):
    @when_all((m.cc == 'theory'))
    def thesis(e):
        e.assert_fact({ 'selection': 'Can do research work'})
    @when_all((m.cc == 'project'))
    def project(e):
        e.assert_fact({ 'selection': 'Can work on good projects'})

    @when_all(+m.selection)
    def output(c):
        print('\n Concept based advice: {0}'.format(c.m.selection))

with ruleset('must'):
    @when_all((m.ccc == 'yes'))
    def yes(e):
        e.assert_fact({ 'selection': 'As you have done required courses then these are the jobs in your interest feild'})
    @when_all((m.ccc == 'no'))
    def no(e):
        e.assert_fact({ 'selection': 'You cannot go with these jobs as you have not done the requires courses \n You have to do specilization in the following otherwise choose another career option'})

    @when_all(+m.selection)
    def output(c):
        print('\n Final advice: {0}'.format(c.m.selection))

with ruleset('domain_jobs'):
	
	@when_all((m.selected_area == 'data_science'))
	def datascience(e):
		e.assert_fact({'selection':'Data Scientist','comma':' , '})
		e.assert_fact({'selection':'Data Analyst','comma':' , '})
		e.assert_fact({'selection':'Data Engineer','comma':' , '})
		e.assert_fact({'selection':'Machine Learning Scientist','comma':' , '})
		e.assert_fact({'selection':'Machine Learning Engineer','comma':' , '})

	@when_all((m.selected_area == 'sde'))
	def sde(e):
		e.assert_fact({'selection':'Software Development Engineer','comma':' , '})
		e.assert_fact({'selection':'Software Design Engineer','comma':' , '})
		e.assert_fact({'selection':'Software Testing Enginee','comma':' , '})
		e.assert_fact({'selection':'Software Support Enginee','comma':' , '})

	@when_all((m.selected_area == 'design'))
	def design(e):
        
		e.assert_fact({'selection':'Design Engineer','comma':' , '})
		e.assert_fact({'selection':'Graphic Designer','comma':' , '})
		e.assert_fact({'selection':'Game Designer','comma':' , '})
		e.assert_fact({'selection':'2D/3D Animation Designer','comma':' , '})
		e.assert_fact({'selection':'UI/UX Designer','comma':' , '})
	
	@when_all((m.selected_area == 'cyber_security'))
	def cybersecurity(e):
		e.assert_fact({'selection':'Information Security Analyst','comma':' , '})
		e.assert_fact({'selection':'Cyber Security Analyst','comma':' , '})
		e.assert_fact({'selection':'Security Engineer','comma':' , '})
		e.assert_fact({'selection':'Security Architect','comma':' , '})
		e.assert_fact({'selection':'Penetration Tester','comma':' , '})

	@when_all((m.selected_area == 'biology'))
	def biology(e):
		e.assert_fact({'selection':'Biochemist','comma':' , '})
		e.assert_fact({'selection':'Biomedical Engineer','comma':' , '})
		e.assert_fact({'selection':'Biological Technician','comma':' , '})
		e.assert_fact({'selection':'Biotechnology Entrepreneur','comma':' , '})

	@when_all(+m.selection)
	def output(e):
		print('Jobs in your domain: {0} {1}'.format(e.m.selection, e.m.comma))

with ruleset('courses'):
	
	@when_all((m.field == 'datascience'))
	def datascience(d):
		d.assert_fact({'selection':'NLP','comma':' , '})
		d.assert_fact({'selection':'AI','comma':' , '})
		d.assert_fact({'selection':'DL','comma':' , '})
		d.assert_fact({'selection':'ML','comma':' , '})
	
	@when_all((m.field == 'sde'))
	def sde(d):
		d.assert_fact({'selection':'Software Development','comma':' , '})
		d.assert_fact({'selection':'Data Structures and Algorithms','comma':' , '})
		d.assert_fact({'selection':'Software Engineering','comma':' , '})
		d.assert_fact({'selection':'Modern Algorithm Design','comma':' , '})
	
	@when_all((m.field == 'design'))
	def design(d):
		d.assert_fact({'selection':'Film Making and Radio Podcasting','comma':' , '})
		d.assert_fact({'selection':'Animations & Graphics','comma':' , '})
		d.assert_fact({'selection':'Introduction to 2D Animation','comma':' , '})
		d.assert_fact({'selection':'Introduction to 3D Production Design for Animation and Games','comma':' , '})
		d.assert_fact({'selection':'Game Design and Development','comma':' , '})
	
	@when_all((m.field == 'cyberSecurity'))
	def cybersecurity(d):
		d.assert_fact({'selection':'Neworks and System Security','comma':' , '})	
		d.assert_fact({'selection':'Privacy and Security in Online Social Media','comma':' , '})
		d.assert_fact({'selection':'Computer Network','comma':' , '})
		d.assert_fact({'selection':'Topics in Adaptive Cybersecurity','comma':' , '})

	@when_all((m.field == 'biology'))
	def biology(d):
		d.assert_fact({'selection':'Machine Learning for Biomedical Applications','comma':' , '})
		d.assert_fact({'selection':'Network Biology','comma':' , '})	
		d.assert_fact({'selection' :'Algorithms in Computational Biology','comma':' , '})
		d.assert_fact({'selection':'Computing for Medicine','comma':' , '})

	@when_all(+m.selection)
	def output(d):
		print('Specialization: {0} {1}'.format(d.m.selection, d.m.comma))

interest_dict = {1:'data science', 2:'sde', 3:'design', 4:'cybersecurity', 5:'biology' }
tp_dict = {1:'tc', 2:'pc'}
must_dict = {1:'yes', 2:'no'}
must_couse= {'data science':{'NLP','AI','DL', 'ML'}, 'sde':{'Software Development','Data Structures and Algorithms','OOPS','Software Engineering'}, 'design':{'Animations & Graphics','Introduction to 2D/3D design','Game Design and Development'}, 'cybersecurity':{'Networks and System Security','Algorithms','Computer Networks'}, 'biology':{'Computing for Medicine','Network Biology', 'Algorithms in Computational Biology'}}

#Starting the program
print('Welcome to Career Advise System!')
print()
while(True):
	cgpa = int(float(input('Enter your cgpa ')))
	if (cgpa >= 1 and cgpa <= 10) :
		break
	else:
		print('Wrong input!')

print('Choose your career interest:')
print()
print(' 1. Data Science \n 2. Software Development \n 3. Design \n 4. Cyber and Network Security \n 5. Computational Biology \n')
while(True):
	selected_area_interest = int(float(input('Enter career interest')))
	if(selected_area_interest >= 1 and selected_area_interest <= 14):
		interest_value = interest_dict[selected_area_interest]
		break
	else:
		print("Wrong input! ")
print()
print('Type of concepts you like')
print(' 1. Theoritical \n 2. Projects')
print()

while(True):
	selected_area_interest2 = int(input('Enter type of concept '))
	if(selected_area_interest2 >= 1 and selected_area_interest2 <= 2):
		interest_value2 = tp_dict[selected_area_interest2]
		break
	else:
		print("Wrong input! ")

print()	
print('List of importent courses related to your interest: ')
mustc = must_couse[interest_value]
# print(mustc)
for i in mustc:
    print(i)
print()
print(' 1. Yes \n 2. No')
print()

while(True):
	selected_area_interest3 = int(input('Have you done the must courses '))
	if(selected_area_interest3 >= 1 and selected_area_interest3 <= 2):
		interest_value3 = must_dict[selected_area_interest3]
		break
	else:
		print("Wrong input! ")
print()
print('Proceed with advise: ')
print(' 1. Yes \n 2. No')
print()
while(True):
	selected_area_interest_1 = int(input('Enter your choice: '))
	if(selected_area_interest_1 == 1):
		try:
			assert_fact('interests', {'interest':interest_value, 'cgpa':cgpa, 'concept':interest_value2, 'must':interest_value3})

		except BaseException as e:
			print('Your course interst is not appropriate according to your cgpa' )
		break
	
	else:
		print("Wrong input! ")
