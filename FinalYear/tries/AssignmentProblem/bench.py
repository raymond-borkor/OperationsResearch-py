from munkres import Munkres

m = Munkres()
def gen_cost_matrix():
	matrix = [[20, 16, 22, 18],
				[25, 28, 15, 21],
				[27, 20, 23, 26],
				[24, 20, 23, 26]]
	#Generate Cost Matrix
	def permute(a, results):
		if len(a) == 1:
			results.insert(len(results), a)
		else:
			for i in range(0, len(a)):
				element = a[i]
				a_copy = [a[j] for j in range(0, len(a)) if j != i]
				subresults = []
				permute(a_copy, subresults)
				for subresult in subresults:
					result = [element] + subresult
					results.insert(len(results), result)
def minimb