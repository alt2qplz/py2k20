# Список моделей, которые необходимо напечатать.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Цикл последовательно печатает каждую модель до конца списка.
# После печати каждая модель перемещается в список completed_models.
while unprinted_designs:
	current_design = unprinted_designs.pop(0)
	print(f"Printing model: {current_design}")
	completed_models.append(current_design)

# Вывод всех готовых моделей.
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)