c=789
def foo():
	def bar():
		print(c)
	bar()
if __name__ == '__main__':
		foo()
		hanshu=foo
		hanshu()
		print(hanshu)
		print(locals())
		print(foo())#可以得到返回值为none
