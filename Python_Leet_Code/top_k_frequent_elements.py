class Solution:
	def topKFrequent(self, nums: list[int], k: int) -> list[int]:
		# Declare hashmap 
		# element : count 

		# result list
		# sort the data and just send it 
		hash_map={}
		for i in nums:
			if i in hash_map:
				hash_map[i]+=1
			else:
				hash_map[i]=1


		items_dict=hash_map.items()
		sorted_list=sorted(items_dict,key=lambda x:x[1],reverse=True)
		temp_list=[]
		for i in sorted_list[:k]:
			temp_list.append(i[0])
		return temp_list

	
x=Solution()
print(x.topKFrequent([1,1,1,2,2,3],2))
