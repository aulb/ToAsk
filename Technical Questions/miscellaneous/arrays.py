from collections import Counter
def count_distinct_window(array, window_size):
	# O(n) time
	# O(n) space
	if window_size < 1:
		return []

	# If window size is bigger...
	if window_size > len(array):
		return []

	# Assumed window size ...
	result = []
	counter = Counter()

	# initialization
	count_distinct = 0
	for i in range(window_size):
		current_number = array[i]
		current_count = counter.get(current_number, 0)
		if current_count == 0:
			count_distinct += 1
		counter[current_number] = current_count + 1
	result.append(count_distinct)

	# moving window
	for i in range(window_size, len(array)):
		current_number = array[i]
		previous_number = array[i - window_size] # beginning of array, not previous
		current_count = counter.get(current_number, 0)
		previous_count = counter.get(previous_number) # must be one from before
		# If its the last one that means its about to get "popped off" the hash
		if previous_count == 1:
			count_distinct -= 1
		# Incoming number is a distinct
		if current_count == 0:
			count_distinct += 1
		counter[current_number] = current_count + 1
		counter[previous_number] = previous_count - 1
		result.append(count_distinct)

	return result


		
def get_largest_sum(array):
	prev = maximum = array[0]
	for number in array:
		prev = number + (prev if prev > 0 else 0)
		if prev > maximum:
			maximum = prev
	return maximum

if __name__ == '__main__':
	unique_window1 = [1,1,1,2,1,3]
	result_window1 = [2,2,3]
	unique_window2 = [2,1,3,4,1,3,4]
	result_window2 = [4,3]

	assert count_distinct_window(unique_window1,4) == result_window1
	assert count_distinct_window(unique_window2,6) == result_window2
