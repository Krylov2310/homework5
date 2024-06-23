task = 'Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()
immutable_var = 1, 2, 'a', 'b'
print(immutable_var)
print(type(immutable_var))
# immutable_var[0] = 100
print('Изменить данные в Кортеже нельзя, так как он используется как хранилище какого нибудь списка, который '
      'должен быть сохранен в первоначальном состоянии с постоянными значениями и его нельзя было повредить')
print('Immutable tuple:', immutable_var)
mutable_list = [1, 2, 'a', 'b']
print('Mutable list: ', mutable_list)
mutable_list.append('Modified')
print('New Mutable List:', mutable_list)
