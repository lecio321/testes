def soma_1(numero):
 Return int numero + 2

	def test_soma_1():
	assert soma_1(101)==103

def test_soma_1_palavra():
	with pytest.raises(ValueError):
	soma_1("lecio")