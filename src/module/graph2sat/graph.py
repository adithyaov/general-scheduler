graph = {}

var01 = 'xtsgndp'
val11 = (1,2,3,4,5,6)
val12 = (1,2,4,4,5,6)

var02 = 'xtsgnd'
val21 = (1,2,3,4,5)
val22 = (1,2,4,4,5)

graph = {
	var01 : {
		val11 : [(var02,val21),('or',[(var01,val11),(var01,val12)])],
		val12 : [(var02,val11)]
	},
	var02 : {
		val21 : [(var02,val21),('and',[(var01,val11),(var01,val12)])],
		val22 : [(var01,val12)]
	}
}
