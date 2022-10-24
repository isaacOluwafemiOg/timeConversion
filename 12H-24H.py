def to24(s):
  spli=s.split(':')
  if spli[2][2]=='P' and int(spli[0])<12:
    spli[0]=str(int(spli[0])+12))
  elif spli[0]=='12' and spli[2][2]=='A':
    spli[0]=='00'
  spli[2]=spli[2].strip('PM').strip('AM')
  return ':'.join(spli)
