def change( cash ):
# Your code goes her
	if cash <=1:
		return None

	else:

		sum=0

		find =False

		i_index , j_index , k_index =0,0,0

		sum_min =int( cash )

		for i in range(int( cash /2)+1):

			for j in range(int(cash /5)+1):

				for k in range(int( cash /10)+1):

					sum=2*i +5*j +10*k

					if sum==cash :

						find =True

						if sum_min > i + j + k :

							i_index , j_index , k_index = i , j , k

							sum_min = i_index + j_index + k_index

		if find ==True:

			return {

			'two': i_index ,

			'five': j_index ,

			'ten': k_index

			}

		else:
			return None

print(change(9007199254740991))