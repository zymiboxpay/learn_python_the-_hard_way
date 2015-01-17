# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

# print "how old are you?",
# age = raw_input()
# print "what\'s your name?",
# name = raw_input()

# print "your name is %s, and you are %s years old." % (name, age)

print 'the script is: ', script
print 'the file argv is: ',filename

txt = open(filename,'w+')

print 'the content is: ', txt.read()

txt.write('aaa')

print 'now the file is: ',txt.read()

txt.close()