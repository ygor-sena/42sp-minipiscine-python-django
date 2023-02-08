import sys
import antigravity

def is_float(nbr):
	try:
		cast = float(nbr)
		return cast
	except ValueError as e:
		sys.exit(e)

def is_string(arg):
	try:
		cast = str(arg)
		return cast
	except ValueError as e:
		sys.exit(e)

def main():
	if len(sys.argv) != 4:
		sys.exit("Geohash takes 4 arguments: <latitude> <longitude> " +
			"<YYYY-mm-dd-dowopening>.\nRespectively: a float, a float and a string.")
	latitude = is_float(sys.argv[1])
	longitude = is_float(sys.argv[2])
	datedow = is_string(sys.argv[3])
	try:
		antigravity.geohash(latitude, longitude, datedow.encode())
	except TypeError:
		print("The 3 arguments must be float, float and string.")

#37.421542 -122.085589 2005-05-26-10458.68
if __name__ == '__main__':
	main()
