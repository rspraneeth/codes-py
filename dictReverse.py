def groups_per_user(group_dictionary):
	"""given a dict of group: users, return a dict which has user: groups(list of groups the user is present in)"""
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		for user in users:
			if user not in user_groups:
				user_groups[user] = []
			user_groups[user].append(group)
	return user_groups

print(groups_per_user({
	"local": ["admin", "userA"],
	"public":  ["admin", "userB"],
	"administrator": ["admin"]}))
