import actions

def find_action(action):
	actions1 = actions.actions
	action_list = []
	percent_list = []
	root_action = actions1.get('data')
	for b in range(len(root_action)):
		name = root_action[b].get('item').get('name')
		percent = root_action[b].get('item').get('percent')
		if name in action_list:
			pass
		else:
			action_list.append(name)
			percent_list.append(percent)
		try:
			children = root_action[b].get('children')
			for c in range(len(children)):
				name = children[c].get('item').get('name')
				percent = children[c].get('item').get('percent')
				if name in action_list:
					pass
				else:
					action_list.append(name)
					percent_list.append(percent)
				try:
					children1 = children[c].get('children')
					for d in range(len(children1)):
						name = children1[d].get('item').get('name')
						percent = children1[d].get('item').get('percent')
						if name in action_list:
							pass
						else:
							action_list.append(name)
							percent_list.append(percent)
						try:
							children2 = children1[d].get('children')
							for e in range(len(children2)):
								name = children2[e].get('item').get('name')
								percent = children2[e].get('item').get('percent')
								if name in action_list:
									pass
								else:
									action_list.append(name)
									percent_list.append(percent)
								try:
									children3 = children2[e].get('children')
									for f in range(len(children3)):
										name = children3[f].get('item').get('name')
										percent = children3[f].get('item').get('percent')
										if name in action_list:
											pass
										else:
											action_list.append(name)
											percent_list.append(percent)
								except:
									pass
						except:
							pass
				except:
					pass
		except:
			pass

	item = action
	index = action_list.index(item)
	answer = str(percent_list[index]) + '%'

	return answer

def get_main_cats():
	actions2 = actions.actions
	root_action = actions2.get('data')
	main_cats = []
	for b in range(len(root_action)):
		name = root_action[b].get('item').get('name')
		main_cats.append(name)

	return main_cats

def get_children(mother):
	actions1 = actions.actions
	root_action = actions1.get('data')
	children_ = []
	root_id = []
	for b in range(len(root_action)):
		name = root_action[b].get('item').get('name')
		if name == mother:
			child1 = root_action[b].get('children')
			new_mother1 = root_action[b].get('item').get('parentId')
			root_id.append(new_mother1)
			for z1 in range(len(child1)):
				new_name1 = child1[z1].get('item').get('name')
				children_.append(new_name1)
		try:
			children = root_action[b].get('children')
			for c in range(len(children)):
				name = children[c].get('item').get('name')
				if name == mother:
					child2 = children[c].get('children')
					new_mother2 = children[c].get('item').get('parentId')
					root_id.append(new_mother2)
					for z2 in range(len(child2)):
						new_name2 = child2[z2].get('item').get('name')
						children_.append(new_name2)
				try:
					children1 = children[c].get('children')
					for d in range(len(children1)):
						name = children1[d].get('item').get('name')
						if name == mother:
							child3 = children1[d].get('children')
							new_mother3 = children1[d].get('item').get('parentId')
							root_id.append(new_mother3)
							for z3 in range(len(child3)):
								new_name3 = child3[z3].get('item').get('name')
								children_.append(new_name3)
						try:
							children2 = children1[d].get('children')
							for e in range(len(children2)):
								name = children2[e].get('item').get('name')
								if name == mother:
									child4 = children2[e].get('children')
									new_mother4 = children2[e].get('item').get('parentId')
									root_id.append(new_mother4)
									for z4 in range(len(child4)):
										new_name4 = child4[z4].get('item').get('name')
										children_.append(new_name4)
								try:
									children3 = children2[e].get('children')
									for f in range(len(children3)):
										name = children3[f].get('item').get('name')
										if name == mother:
											child5 = children3[f].get('children')
											new_mother5 = children3[f].get('item').get('parentId')
											root_id.append(new_mother5)
											for z5 in range(len(child5)):
												new_name5 = child5[z5].get('item').get('name')
												children_.append(new_name5)
								except:
									pass
						except:
							pass
				except:
					pass
		except:
			pass

	return children_, root_id[-1]
