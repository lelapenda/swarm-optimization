import matplotlib.pyplot as plt


coordinates = [
[37,52],
[49,49],
[52,64],
[20,26],
[40,30],
[21,47],
[17,63],
[31,62],
[52,33],
[51,21],
[42,41],
[31,32],
[5,25],
[12,42],
[36,16],
[52,41],
[27,23],
[17,33],
[13,13],
[57,58],
[62,42],
[42,57],
[16,57],
[8,52],
[7,38],
[27,68],
[30,48],
[43,67],
[58,48],
[58,27],
[37,69],
[38,46],
[46,10],
[61,33],
[62,63],
[63,69],
[32,22],
[45,35],
[59,15],
[5,6],
[10,17],
[21,10],
[5,64],
[30,15],
[39,10],
[32,39],
[25,32],
[25,55],
[48,28],
[56,37],
[30,40]
]

salesman1=['1', '27', '51', '46', '32', '2', '22', '8', '48', '6', '14', '24', '23', '26', '31', '28', '3', '35', '36', '20', '29', '21', '50', '34', '30', '5', '12', '7', '43', '1']
salesman2=['1', '11', '16', '9', '38', '49', '47', '18', '25', '13', '41', '40', '19', '42', '4', '17', '44', '37', '15', '33', '45', '10', '39', '1']

initial_city=coordinates[int(salesman1[0])-1]
s1cities=[]
s2cities=[]

for city in salesman1:
	s1cities.append(coordinates[int(city)-1])

for city in salesman2:
	s2cities.append(coordinates[int(city)-1])

plt.plot([x[0] for x in s1cities], [x[1] for x in s1cities], 'xb-')
plt.plot([x[0] for x in s2cities], [x[1] for x in s2cities], 'xr-')
plt.plot([initial_city[0]], [initial_city[1]], 'xg')



plt.show()
