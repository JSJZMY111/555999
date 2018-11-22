c=456
def foo():
	
	def bar():
		print(c)
	bar()
if __name__=='__main__':
    foo()
    print(__name__)b
    print(locals())
    print(globals())