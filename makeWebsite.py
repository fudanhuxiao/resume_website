'''Author: Xiao Hu'''

'''first step, gathering information from my resume'''
def DetectName(resumeFile):
    firstline=resumeFile.readline()
    if not 'A'<=firstline[0]<='Z':
        raise ValueError, "Name has not been written properly!"
    return firstline

def DetectEmail(resumeFile):
    for line in resumeFile:
        if '@' in line:
            if '.com\n' in line:
                StringOrNot=line[line.find('@')+1:line.find('.com')] #the characters between '@' and the ending
                if 'a'<=StringOrNot[0]<='z' and type(StringOrNot)==str:
                    return line
            elif '.edu\n' in line:
                StringOrNot=line[line.find('@')+1:line.find('.edu')] #the characters between '@' and the ending
                if 'a'<=StringOrNot[0]<='z' and type(StringOrNot)==str:
                    return line

def DetectCourses(resumeFile): #return the string of the courses done
    for line in resumeFile:
        if 'Courses' in line:  
            i=7                
            while True:
                if ('a'<=line[i:]<='z' or 'A'<=line[i:]<='Z'):
                    return line[i:]
                else: i+=1     #Delete all punctuations after 'Courses' and before actual course name

def DetectProjects(resumeFile):
    proj=[]
    line=resumeFile.readline()
    while line:
        if 'Projects' in line: break
        line=resumeFile.readline()
    line=resumeFile.readline()
    while line:
        if line.count('----------')>=1: break
        if line.strip("\n")!="": proj.append(line)
        line=resumeFile.readline()
    
    return proj

def DetectEducation(resumeFile):
    edulist=[] #the list of lines that contains 'university' or 'University'
    edu=[]     #the list of lines that contains both university and degree information
    for line in resumeFile:
        if 'university' in line:
            edulist.append(line)
        elif 'University' in line:
            edulist.append(line)

    for ele in edulist:
        if 'Doctor' in ele:
            edu.append(ele)
        elif 'Master' in ele:
            edu.append(ele)
        elif 'Bachelor' in ele:
            edu.append(ele)
    
    return edu 
            
            
'''second step, writing HTML'''

def surround_block(tag,text):
    SurroundedLines=tag+text+tag[0]+'/'+tag[1:]
    return SurroundedLines

def IntroSection(name,email):
    BasicInfo=surround_block('<div>\n',(surround_block('<h1>\n',name)+surround_block('<p>\n',email)))
    return BasicInfo

def EduSection(education):
    DegreeInfo=""
    for i in range(0,len(education)):
        DegreeInfo+=surround_block('<li>\n',education[i])
    Degrees=surround_block('<u1>\n',DegreeInfo)
    EduInfo=surround_block('<div>\n',(surround_block('<h2>','Education')+Degrees))
    return EduInfo
    
def ProjSection(projects):
    ProjString=""
    for i in range(0,len(projects)):
        ProjString+=surround_block('<li>\n',surround_block('<p>\n',projects[i]))
    ProjInfo=surround_block('<div>\n',(surround_block('<h2>\n','Projects\n')+surround_block('<u1>\n',ProjString)))
    return ProjInfo

def CoursesSection(courses):
    CoursesInfo=surround_block('<div>\n',(surround_block('<h3>\n','Courses\n')+surround_block('<span>\n',courses)))
    return CoursesInfo

    
def main(): #read txt and write html
    resumeFile=open("myresume.txt",'rU')
    name=DetectName(resumeFile)
    resumeFile.seek(0)
    email='Email: '+DetectEmail(resumeFile)
    resumeFile.seek(0)
    courses=DetectCourses(resumeFile)
    resumeFile.seek(0)
    projects=DetectProjects(resumeFile)
    resumeFile.seek(0)
    education=DetectEducation(resumeFile)
    resumeFile.close()
    f=open('resume.html','r+')
    lines=f.readlines()
    f.seek(0)
    f.truncate()
    del lines[-1]
    del lines[-1]
    f.writelines(lines)  #delete the last two line to insert content
    f.write('<div id=\"page-wrap\">\n')
    f.write(IntroSection(name,email))
    f.write('<p>\n</p>\n')
    f.write(EduSection(education))
    f.write('<p>\n</p>\n')
    f.write(ProjSection(projects))
    f.write('<p>\n</p>\n')
    f.write(CoursesSection(courses))
    f.write('</div>\n</body>\n</html>\n')
    f.close()


if __name__ == '__main__':
    main()
    
