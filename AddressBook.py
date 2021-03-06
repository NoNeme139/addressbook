import os
import pickle
#
v="1.1.1"
path='ab.data'
if os.access(path, os.F_OK) and os.path.getsize(path) > 0:
	file=open(path, 'rb')
	ls=pickle.load(file)
	file.close()
else:
	ls={}
logo=\
'''		  ┌┐      ┌┐
		  ├┤      ├<
		  ││ddress││ook
		  ┘└──────└┘──---'''
help='''
help		выводит это сообщение
exit		выход
list		список контактных данных
type		создание/редактирование контакта
find <имя>	поиск контакта
del  <имя>	удалить контакт
save		сохранить изменения
info		о программе
'''
E='Неверная команда.\n(для помощи, введите \"help\").\n'
#
def save():
	file=open(path, 'wb')
	pickle.dump(ls, file)
	file.close()
def line(n, a):
	print('	{}: {}'.format(n, a))
def find(n, action):
	if n in ls:
		return action
	else:
		print('Контакт "{}" не найден.'.format(n))
def delt(n):
	print('Контак удалён.')
	del ls[n]
#
print('\n\n'+logo+'\n\n')
while True:
	try:
		command=input('> ')
		w1=command[:4]
		if w1=='exit':
			opt=input(' При выходе все несохранённые изменения будут утеряны.\n Продолжить?\n yes/no: ')
			if opt=='yes':
				break
			else:
				del opt
		elif w1=='help':
			print(help)
		elif w1=='type':
			name=input('Имя контакта: ')
			address=input('Почта или номер телефона: ')
			ls[name]=address
		elif w1=='list':
			if len(ls)>0:
				for n, a in ls.items():
					line(n, a)
			else:
				print('Книга пуста.')
		elif w1=='info':
			print('{}\nAddressBook\nV {}\n(с) 2020 Terlyk Maksim.'.format(logo, v))
		elif w1=='find':		
			w2=command[5:]
			find(w2, (line(w2, ls[w2])))
		elif w1=='del ':
			w2=command[4:]
			find(w2, delt(w2))
		elif w1=='save':
			save()
			print('Сохранение прошло успешно.')
		else:
			print(E)
	except:
		print(E)

