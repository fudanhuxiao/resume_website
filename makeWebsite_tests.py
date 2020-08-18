import unittest
from makeWebsite import *

class Test_makeWebsite(unittest.TestCase):
    fileName1 = ''
    fileName2 = ''
    fileName3 = ''
    fileName4 = ''
    fileName5 = ''
    fileName6 = ''
    
    def setUp(self):
        self.fileName1= 'testResume1.txt'
        self.f1=open(self.fileName1,'rU')
        self.fileName2= 'testResume2.txt'
        self.f2=open(self.fileName2,'rU')
        self.fileName3= 'testResume3.txt'
        self.f3=open(self.fileName3,'rU')
        self.fileName4= 'testResume4.txt'
        self.f4=open(self.fileName4,'rU')
        self.fileName5= 'testResume5.txt'
        self.f5=open(self.fileName5,'rU')
        self.fileName6= 'testResume6.txt'
        self.f6=open(self.fileName6,'rU')

    def test_DetectName(self):
        self.assertRaises(ValueError,DetectName,self.f1)
        self.assertEqual('Xiao Hu\n',DetectName(self.f2),'Detect name failed')

    def test_DetectEmail(self):
         self.assertNotEqual('huxiao@python.org\n',DetectEmail(self.f1),"Excludes non '.edu' or '.com' failed")
         self.assertNotEqual('huxiao@Seas.upenn.edu\n',DetectEmail(self.f2),"Excludes non-lowercase English character right after '@' failed")
         self.assertEqual('huxiao@gmail.com\n',DetectEmail(self.f3),"Detect email end with '.com' failed")
         self.assertEqual('huxiao@seas.upenn.edu\n',DetectEmail(self.f4),"Detect email end with '.edu' failed")
         self.assertNotEqual('huxiao@seas.upenn.EdU\n',DetectEmail(self.f5),"Excludes '.EdU' failed")
         self.assertNotEqual('huxiao@gmail.COM\n',DetectEmail(self.f5),"Excludes '.COM' failed")
         

    def test_DetectCourses(self):
         self.assertEqual('Engineering Economics, Probability\n',DetectCourses(self.f1),'Detect courses failed')

    def test_DetectProjects(self):
         self.assertEqual(['Roland Berger\n','Guotai Junan\n'],DetectProjects(self.f1),'Detect projects failed')

    def test_DetectEducation(self):
         self.assertEqual(['University of Pennsylvania: Master of Science\n', 'Fudan university: Bachelor of Science\n', 'Best university: Doctor of engineering\n'],DetectEducation(self.f1),'Detect education failed')

    def test_surround_block(self):
        self.assertEqual('<p>good</p>',surround_block('<p>','good'),'Surround block failed')

    def test_IntroSection(self):
        self.assertEqual('<div>\n<h1>\nElla</h1>\n<p>\nemail</p>\n</div>\n',IntroSection('Ella','email'),'write IntroSection failed')

    def test_EduSection(self):
        education=EduSection(['University of Pennsylvania: Master of Science','Fudan university: Bachelor of Science','Best university: Doctor of engineering'])
        self.assertEqual('<div>\n<h2>Education</h2><u1>\n<li>\nUniversity of Pennsylvania: Master of Science</li>\n<li>\nFudan university: Bachelor of Science</li>\n<li>\nBest university: Doctor of engineering</li>\n</u1>\n</div>\n',education,'write education failed')

    def test_ProjSection(self):
        proj=ProjSection(['Roland Berger','Guotai Junan'])
        self.assertEqual('<div>\n<h2>\nProjects\n</h2>\n<u1>\n<li>\n<p>\nRoland Berger</p>\n</li>\n<li>\n<p>\nGuotai Junan</p>\n</li>\n</u1>\n</div>\n',proj,'write projects failed')

    def test_CoursesSection(self):
        courses=CoursesSection("Engineering Economics, Probability")
        self.assertEqual('<div>\n<h3>\nCourses\n</h3>\n<span>\nEngineering Economics, Probability</span>\n</div>\n',courses,'write courses failed')



unittest.main()
