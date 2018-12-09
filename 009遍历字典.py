players = {'NBA':{'country':'USA','name':'Durant','honor':'2018 fmvp'},
          'World Cup':{'country':'France','name':'Pogba','honor':'2018 World Cup champion'},
          'UEFA':{'country':'Egypt','name':'Salah','honor':'2018 UEFA runner up'}
         }
for k,v in players.items():
    print('\n' + k)
    for ks,vs in v.items():
        print(ks + ' : ' + vs)
