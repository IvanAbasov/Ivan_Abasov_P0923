import requests
 
user_ids = []
 
id = 8712
for id in range(8712, 15000):
  print("---- A procurar no ID: ", id)
  resposta = requests.get(
      f'https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId={id}&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1747004400&end=1747609200&_=1747127413405'
  )
 
  if "Sessão como Formador" in resposta.text and ("Rogélio Manuel Nascimento Palma Rodrigues" in resposta.text):
    user_ids.append(id)
    break
  else:
    print("[x] O Rogélio não foi encontrado no horario do ID: ", id)

print("Filtered Events:")
for id in user_ids:
  print("ID's encontrados: ", id)  