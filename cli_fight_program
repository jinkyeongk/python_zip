import time

print('Hello There! ')
print('Welcome to Digital World. ')
print('디지털 월드에 오신 것을 환영합니다.')



flag = False

class character :
  name =''
  level = 1
  blood = 100 # 체력
  power = 100  # 마나
  exp = 0     # 경험치
  skill = 0

  def print_info(self):
    print('')
    print('============ *', self.name, '의 정보 * ============ ')
    print('Level  : ', self.level)
    print('HP  : ', self.blood)
    print('MP  : ', self.power)
    print('EXP : ', self.exp)
    print('SKILL :', self.skill)
    print('=========================================== ')
    print('')

  def print_gage(self):
    print('')
    print('============ *', self.name, '의 HP & MP * ============ ')
    print('HP  : ', self.blood)
    print('MP  : ', self.power)
    print('=========================================== ')
    print('')

  def print_levelup(self):
    print('')
    print('============ *', self.name, '의 레벨이 올랐습니다. * ============ ')
    print('Level  : ', self.level)
    print('EXP : ', self.exp)
    print('=========================================== ')
    print('')
  
  def zero_blood(self):
    print('')
    print(self.name,'의 HP가 전부 소모되었습니다.')
    print('안타깝게도 게임을 종료합니다.')
    quit()
  

  def down(self,gage,num):
    if gage == 'HP':
      self.blood -= num
      if(self.blood < 0):
        self.blood = 0
    else :
      self.power -= num
      if(self.power < 0):
        self.power = 0
    print('(',self.name,'의 ',gage,'가 ', num, '감소하였습니다.)' )
    self.print_gage();
    if self.blood <= 0 :
      self.zero_blood()
      quit()
  def up(self, gage,num):
    if gage == 'HP' :
      self.blood += num
      if(self.blood >100):
        self.blood = 100
    elif gage == 'MP' :
      self.power += num
      if(self.power >100):
        self.power = 100
    else :
      self.exp += num
      if(self.exp >=100):
        self.level += (self.exp / 100)
        self.exp = (self.exp % 100)
        self.print_levelup()
    print('(',self.name,'의 ',gage,'가 ', num, '상승하였습니다.)' )
    self.print_gage();


avatar = character()

def input_name() :
  print('이름을 입력해주세요.')
  label = input()
  avatar.name = label
  print('캐릭터의 이름이 ',label,'가 맞습니까?')
  print('맞으면 Yes(y), 변경을 원하시면 No(n)를 입력해주세요.')
  ans = input()

  if(ans == 'N' or ans == 'No' or ans == 'n' or ans == 'no') :
    input_name()



input_name()

print('')
avatar.print_info()
print('')
print('')
print('당신은 디지털 세계에서 눈을 뜬 후, 알 수 없는 갈림 길에 서있습니다.')
print('왼쪽(l)은 숲이 너무도 울창해서 멀리 보이지 않는 칠흙같은 어둠의 숲길입니다.')
print('오른쪽(r) 갈림길은 경사가 가파른 자갈길입니다.')
print('어느길로 가시겠습니까 ?')
print('왼쪽(l) / 오른쪽(r)')

dir = input()

print('')
#왼쪽 길로 간다
if dir == 'l' or dir == 'L' :
  print(' . . . . .')
  time.sleep(3)
  print('어둠 속에서 무언가 스쳤습니다!')
  print(' . . .!!')
  time.sleep(1)
  
  avatar.down('HP',20)
  print('')
  print('')
  print(avatar.name,': 어떡하지..? 지금이라도 돌아갈까?')
  print('돌아간다(y) / 가던 길을 간다 (n)')
  ans = input()
  # 되돌아가서 오른쪽 갈림길(가파른 자갈길)로 간다
  if(ans == 'y' or ans == 'Y'):
    print('온 길을 되돌아갑니다... ')
    print('갈림길에서 왼쪽인 자갈길로 갑니다... ')
    print(' . . . .')
    flag = True
    
  # 가던길인 왼쪽길(울창한 숲길)로 간다
  else:
    print(avatar.name,'은 어두운 곳에서 조심히 걷느라 많은 체력을 소모하였습니다.')
    avatar.down('HP',30)
    print('')
    print('!!!!!!!!!!!')
    time.sleep(1)
    print('어두운 숲의 끝에 저 멀리 빛이✨ 보이기 시작합니다.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    print(avatar.name,'은 보스 몬스터를 만났습니다.')
    time.sleep(1)
    print(avatar.name,' : 역시... 싸우는 수 밖에...')
    time.sleep(1)
    print('')
    print('싸우시겠습니까 ?')
    print('싸운다(f).... 다른 선택지는 없습니다.')
    ans = input()
    if(ans == 'f' or ans == 'F') :
      print('')
    else :
      print('다른 키를 누르셨지만 선택지는 싸움 뿐입니다.')
    print('전투를 시작합니다.')
    print('')
    time.sleep(2)
    print('🩸🩸🩸')
    time.sleep(1)
    print('!!!!!!!!!!!')
    time.sleep(1)
    avatar.down('HP',50)

else:
  flag = True
  
#오른쪽 길로 간다
if(flag ) : 
  time.sleep(1)
  print(avatar.name,'은 많은 체력을 소모하였습니다.')
  avatar.down('HP',50)

  print(avatar.name,'은 알 수 없는 몬스터를 만났습니다.')
  print('싸우시겠습니까 ?')
  print('싸운다(f)/도망간다(r)')
  print('')
  ans = input()

  # 싸운다
  if(ans == 'f' or ans == 'F') :
    print('')
    avatar.up('EXP',50)
    avatar.down('HP',30)
  else :
    print('')
    print('')
    print(avatar.name,'은 전력 질주하였습니다.')
    print(avatar.name,'은 체력을 소모하였습니다.')
    avatar.down('HP',20)

  print('')
  print(f'{avatar.name}은 알 수 없는 누군가를 만났습니다.')
  print(' 사람의 형태를 하고 있지만 사람이라고는 믿을 수 없습니다.')
  print('???? : 내 동료가 되겠나 ?')
  print('')
  print('동맹이 되시겠습니까 ?')
  print('알겠다고한다(y)/거절한다(n)')
  print('')
  
  ans = input()

  #동맹을 거절할 때
  if(ans == 'N' or ans == 'n') :
    print('??? : 감히 내 제안을 거절해 ? 진행시켜 !!')
    time.sleep(1)
    print('!!!!!!!!!!!')
    time.sleep(1)
    print('엄청난 무리의 몬스터들이 나타났습니다.')
    print('🩸🩸🩸')
    time.sleep(1)
    print('!!!!!!!!!!!')
    time.sleep(1)
    avatar.down('HP',100)

  # 동맹을 수락할 때
  else :
    
    print('알 수 없는 긍정적인 기운이 감돌기 시작했습니다.')
    time.sleep(1)
    avatar.up('HP',20)
    avatar.skill+=1
    avatar.print_info()
    print('Tokki : 내 이름은 Tokki라네, 이 곳을 수 백년간 지키고 있지.')
    time.sleep(1)
    print('Tokki : 오랜만에 보는 사람이구려 . . . 모습을 보아하니 온 지 얼마 안된것 같군..')
    print('Tokki : 가던 길이나 같이 가게나 ..')
    time.sleep(1)
    print(f'{avatar.name} : (좀 이상하지만..혼자보단 낫지..)')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    print(avatar.name,'은 중급 몬스터를 만났습니다.')
    print('싸우시겠습니까 ?')
    print('싸운다(f)/도망간다(r)')

    # 도망간다.
    if(ans == 'r' or ans == 'R') :
      time.sleep(1)
      print('!!!!!!!!!!!')
      time.sleep(1)
      print('전력질주하고 있지만 엄청난 그림자가 따라옵니다.')
      time.sleep(1)
      print('!!!!!!!!!!!')
      print('🩸🩸🩸')
      print('!!!!!!!!!!!')
      time.sleep(1)
      avatar.down('HP',100)
    # 싸운다.
    else : 
      print('')
      print('Tokki로 인해 알게된 스킬을 사용하시겠습니까 ? ')
      print(' 사용한다(y)/아직 잘 모르니 사용하지 않는다(n)')
      ans = input()
      if(ans == 'n' or ans == 'N') :
        print('Tokki : 알고 있는 스킬을 써 !!!!!!!!!!!!')
        print(f'{avatar.name} : 난 모르오.')
        print('Tokki : 써 !!!!!!!!!!!!')
        print(f'{avatar.name} : 난 모르...')
        time.sleep(1)
        print('🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸')
        avatar.down('HP',100)
      else:
        time.sleep(1)
        i = 1
        while i < 4:
          print('.')
          i+=1
          time.sleep(1)
        print('체력은 조금 감소하였지만, 경험치를 얻었습니다.')
        print('')
        avatar.up('EXP',30)
        print('')
        avatar.down('HP',10)
    
      print('')
      print(' 🌙 밤이 왔습니다.')
      print(' Tokki : 잠을 좀 자두게 .. 내일 다시 모험을 이어가려면 .....')
      print('잠을 잔다(y) / 불안하니 잠을 자지 않는다(n)')

      ans = input()

      if(ans == 'n' or ans == 'N') : 
        while avatar.blood <= 0 :
          print('....1 시간 후')
          avatar.down('HP',20)
          time.sleep(1)
        print(f'{avatar.name}은 과로하였습니다.')
      else :
        print(' 부스럭...')
        time.sleep(1)
        print(' 부스럭...부스럭')
        print('!!!!')
        time.sleep(1)
        print(f'{avatar.name}은 Tokki에게 죽임을 당했습니다.')
        print('🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸🩸')
        avatar.down('HP',100)


quit()


      
      
      





  
