def binary_search(sorted_collection, item):
	print(sorted_collection)
	if len(sorted_collection) is 1:return sorted_collection[0]
	left = 0
	right = len(sorted_collection) - 1
	while left <= right:
		if len(sorted_collection) is 1:return sorted_collection[0]
		break
		midpoint = (left + right) // 2
		current_item = sorted_collection[midpoint]
		if current_item == item:
			return midpoint
		else:
			if item < current_item:
				right = midpoint - 1
			else:
				left = midpoint + 1
	return sorted_collection

def climbingLeaderboard(scores, alice):
    lis = []
    scores = sorted(list(set(scores)),reverse = True)
    for i in alice:
        #dscores.append(i)
        if i < scores[-1]:
        	 lis.append(len(scores)+1)

        elif i > scores[0]:
        	 lis.append(1)

        else:
        	val = binary_search(scores,i) # returns index if element else return index of element just less than this
        	scores = sorted(scores,reverse = True)
        	lis.append(scores.index(val)+1)

    return lis



# Result of this approach: 8/12 passed 4 terminated due to timeout
# This was due to large input constraint and my brute force approach is already
# O(n*n)+O(n*log(n))+O(whaterver it takes for construction of a new dictonary each time)

# Update : Dict removed , still terminated due to timeout
# so now as understood time is being taken for sorting and reversing converting to set then list again each O(scores of alice) number of times

# A better time saving algortihmic approach

# Just for sake of runtime tried the same approach in c++
# same test cases failed due to TLE , hence it is confirmed there
# lies a better approach

# At this point im fucking tempted to go to the discussion column

# But ......... NO NOT YET !!  I wont fucking give up

# vector<int> climbingLeaderboard(vector<int> scores, vector<int> alice) {
# vector<int>result = {};
# vector<int>::iterator it,ip;
# for (auto i:alice){
#     scores.push_back(i);
#     sort(scores.begin(),scores.end());
#     ip = unique(scores.begin(),scores.end());
#     scores.resize(distance(scores.begin(), ip)); 
#     reverse(scores.begin(),scores.end());
#     it = find (scores.begin(), scores.end(), i); 
#     result.push_back(it - scores.begin()+1);
# }
# return result;
# }


climbingLeaderboard([100,90,80,75,60],[50,65,77,90,102])
